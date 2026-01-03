from multiprocessing import Process, freeze_support, Queue, Pool, cpu_count
import time
from functools import partial

def check_value_in_list(x, i, number_of_processes, queue):
    max_number_to_check_to = 10**8
    lower = int(i * max_number_to_check_to / number_of_processes)
    upper = int((i + 1) * max_number_to_check_to / number_of_processes)
    number_of_hits = 0
    for i in range(lower, upper):
        if i in x:
            number_of_hits += 1
    queue.put((lower, upper, number_of_hits))

def square(y, additional, x):
    return x ** y + additional

def square(x, y):
    return x ** y

def check_number_of_values_in_range(comp_list, lower, upper):
    number_of_hits = 0
    for i in range(lower, upper):
        if i in comp_list:
            number_of_hits += 1
    return number_of_hits

def main():
    num_processes = 4
    comparison_list = [1, 2, 3]
    power_list = [4, 5, 6]
    start_time = time.time()
    num_cpu_available = max(1, cpu_count()-1)
    lower_and_upper_bounds = [(0, 25*10**6), (25*10**6, 50*10**6), 
                              (50*10**6, 75*10**6), (75*10**6, 10**8)]
    print("Number of CPUs available:", num_cpu_available)
    """
    # power = 3
    # additional = 10
    # partial_function = partial(square, power, additional)   # Fix y and additional, vary x
    # with Pool(2) as mp_pool:
    #     results = mp_pool.map(partial_function, comparison_list)
        # cannot pass more than one argument with map, hence using partial
    """
    # with Pool(2) as mp_pool:
    #     results = mp_pool.starmap(square, zip(comparison_list, power_list))

    """
    # processes = []
    # queue = Queue()
    # for i in range(num_processes):
    #     t = Process(target=check_value_in_list, args=(comparison_list, i, num_processes, queue))
    #     processes.append(t)

    # for t in processes:
    #     t.start()

    # for t in processes:
    #     t.join()

    # queue.put('DONE')
    # while True:
    #     val = queue.get()
    #     if val == 'DONE':
    #         break
    #     lower, upper, hits = val
    #     print(f"Checked range {lower} to {upper}, found {hits} hits.")"""
    
    prepared_list = []
    for i in range(len(lower_and_upper_bounds)):
        prepared_list.append((comparison_list, *lower_and_upper_bounds[i]))
    
    with Pool(num_cpu_available) as mp_pool:
        results = mp_pool.starmap(check_number_of_values_in_range, prepared_list)

    print("Result:", results)
    print("Total time taken:", time.time() - start_time, "seconds")

    # print(partial_function(5))  # Testing partial function separately

if __name__ == "__main__":
    freeze_support()
    main()