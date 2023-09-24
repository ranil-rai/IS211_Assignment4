
import time
import random

def generate_random_list(size):
    return [random.randint(1, size * 10) for _ in range(size)]

def sequential_search(arr, item):
    start_time = time.time()
    pos = 0
    found = False
    while pos < len(arr) and not found:
        if arr[pos] == item:
            found = True
        else:
            pos += 1
    return found, time.time() - start_time

def ordered_sequential_search(arr, item):
    start_time = time.time()
    arr.sort()
    pos = 0
    found = False
    stop = False
    while pos < len(arr) and not found and not stop:
        if arr[pos] == item:
            found = True
        else:
            if arr[pos] > item:
                stop = True
            else:
                pos += 1
    return found, time.time() - start_time

def binary_search_iterative(arr, item):
    start_time = time.time()
    arr.sort()
    first = 0
    last = len(arr) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if arr[midpoint] == item:
            found = True
        else:
            if item < arr[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found, time.time() - start_time

def binary_search_recursive(arr, item):
    start_time = time.time()
    arr.sort()
    def recursive_search(arr, item, first, last):
        if last < first:
            return False
        midpoint = (first + last) // 2
        if arr[midpoint] == item:
            return True
        else:
            if item < arr[midpoint]:
                return recursive_search(arr, item, first, midpoint - 1)
            else:
                return recursive_search(arr, item, midpoint + 1, last)
    found = recursive_search(arr, item, 0, len(arr) - 1)
    return found, time.time() - start_time

def main():
    list_sizes = [500, 1000, 10000]
    search_functions = [
        sequential_search,
        ordered_sequential_search,
        binary_search_iterative,
        binary_search_recursive
    ]
    for size in list_sizes:
        print(f"\nList Size: {size}")
        total_times = {func.__name__: 0 for func in search_functions}
        for _ in range(100):
            arr = generate_random_list(size)
            for func in search_functions:
                _, elapsed_time = func(arr[:], -1)  # Searching for -1, which is not in the list
                total_times[func.__name__] += elapsed_time
        for func in search_functions:
            print(f"{func.__name__} took %10.7f seconds to run, on average" % (total_times[func.__name__] / 100))

if __name__ == "__main__":
    main()
