import os
import time
import threading

from workers.WikiWorker import WikiWorker
from workers.YahooFinanceWorkers import YahooFinancePriceScheduler, YahooFinanceWorker
from multiprocessing import Queue
from workers.PostgresWorker import PostgresMasterScheduler
from yaml_reader import YamlPipelineExecutor

def main():
    # print("PG_USER =", repr(os.environ.get("PG_USER")))
    # print("PG_PASSWORD =", repr(os.environ.get("PG_PASSWORD")))
    # print("PG_PORT =", repr(os.environ.get("PG_PORT")))
    # print("PG_DB =", repr(os.environ.get("PG_DB")))

    # raise SystemExit("STOP HERE")
    startTime = time.time()
    pipeline_location = os.environ.get("PIPELINE_LOCATION") or 'pipelines/wiki_yahoo_scrapper_pipeline.yaml'
    # if pipeline_location is None:
    #     print("Pipeline not set")
    #     exit()
    yamlPipelineExecutor = YamlPipelineExecutor(filename=pipeline_location)
    #yamlPipelineExecutor.process_pipeline()
    yamlPipelineExecutor.start()
    
    # wiki_worker = WikiWorker()

    # symbols = list(wiki_worker.get_sp_500_companies())
    # # print(symbols[:10])  # Print first 10 symbols for verification
    # for symbol in symbols[:]:
    #     yamlPipelineExecutor._queues['SymbolQueue'].put(symbol)
    # yamlPipelineExecutor._queues['SymbolQueue'].put('DONE')  # Signal the scheduler to stop after processing all symbols

    # for i in range(200):
    #     yamlPipelineExecutor._queues['SymbolQueue'].put('DONE')
    
    # yamlPipelineExecutor._join_workers()
    
    endTime = time.time()
    print(f"Total time taken: {round(endTime - startTime,1)} seconds")
    
    """ Old code for reference, now replaced by YAML pipeline executor
    # symbol_queue = Queue()
    # postgres_queue = Queue()

    # yahooFinanceThreads = []    # List to keep track of threads
    # numYahooFinanceWorkers = 100
    # for i in range(numYahooFinanceWorkers):
    #     yahooFinancePriceScheduler = YahooFinancePriceScheduler(input_queue=symbol_queue, output_queue=[postgres_queue])
    #     yahooFinanceThreads.append(yahooFinancePriceScheduler)

    # postgresThreads = []     # List to keep track of threads
    # numPostgresWorkers = 100
    # for i in range(numPostgresWorkers):
    #     postgresMasterScheduler = PostgresMasterScheduler(input_queue=postgres_queue)
    #     postgresThreads.append(postgresMasterScheduler)

    # for t in yahooFinanceThreads:
    #     t.join()


    # for i in range(len(postgresThreads)):
    #     yamlPipelineExecutor._queues['PostgresUploading'].put('DONE')
    
    # # for t in postgresThreads:
    #     t.join()
    
    # print(symbol_queue)
    # print(symbol_queue.get())

    # current_threads = []
    # startTime = time.time()
    # for i in range(1, 6):
    #     t2 = threading.Thread(target=sleep_a_little, args=(i,))
    #     t2.start()
    #     current_threads.append(t2)
    
    # for t in current_threads:
    #     t.join()
    
    # endTime = time.time()
    # print(f"Total time taken for sleep: {round(endTime - startTime,1)} seconds")"""

if __name__ == "__main__":
    main()