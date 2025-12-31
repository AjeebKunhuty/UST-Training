import importlib
import threading
import time

import yaml
from multiprocessing import Queue

class YamlPipelineExecutor(threading.Thread):
    def __init__(self, filename):
        super(YamlPipelineExecutor, self).__init__()
        self._pipeline_location = filename
        self._queues = {}
        self._workers = {}
        self._queue_consumers = {}
        self._downstream_queues = {}

    def _load_pipeline(self):
        with open(self._pipeline_location, 'r') as file:
            self._yaml_data = yaml.safe_load(file)

    def _initialize_queues(self):
        for queue in self._yaml_data.get('queues', []):
            queue_name = queue['name']
            self._queues[queue_name] = Queue()

    def _initialize_workers(self):
        for worker in self._yaml_data['workers']:
            WorkerClass = getattr(importlib.import_module(worker['location']), worker['class'])
            input_queue = worker.get('input_queue')
            output_queues = worker.get('output_queues')
            workerName = worker['name']
            num_instances = worker.get('instances', 1)
            input_values = worker.get('input_values')

            self._downstream_queues[workerName] = output_queues
            if input_queue:
                self._queue_consumers[input_queue] = num_instances

            init_params = {
                'input_queue': self._queues[input_queue] if input_queue else None,
                'output_queue': [self._queues[q] for q in output_queues] \
                      if output_queues else None
            }

            if input_values:
                init_params['input_values'] = input_values

            self._workers[workerName] = []
            for i in range(num_instances):
                self._workers[workerName].append(WorkerClass(**init_params))

    def _join_workers(self):
        for worker_name in self._workers:
            for worker_thread in self._workers[worker_name]:
                worker_thread.join()

    def process_pipeline(self):
        self._load_pipeline()
        self._initialize_queues()
        self._initialize_workers()
        # self._join_workers()

    def run(self):
        self.process_pipeline()
        while True:
            total_worker_alive = 0
            worker_stats = []
            to_del = []
            for worker_name in self._workers:
                total_worker_threads_alive = \
                    sum(1 for t in self._workers[worker_name] if t.is_alive())
                total_worker_alive += total_worker_threads_alive
                if total_worker_threads_alive == 0:
                    if self._downstream_queues[worker_name]:
                        for output_queue in self._downstream_queues[worker_name]:
                            for i in range(self._queue_consumers.get(output_queue, 0)):
                                self._queues[output_queue].put('DONE')
                    to_del.append(worker_name)
                worker_stats.append([worker_name, total_worker_threads_alive])
            print(worker_stats)

            if total_worker_alive == 0:
                break

            for queue in self._queues:
                print(f"Queue {queue} size: {self._queues[queue].qsize()}")

            for worker_name in to_del:
                del self._workers[worker_name]

            time.sleep(5)