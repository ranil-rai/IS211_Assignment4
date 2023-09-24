
import time
import random

def generate_random_list(size):
    return [random.randint(1, size * 10) for _ in range(size)]

def insertion_sort(arr):
    start_time = time.time()
    for index in range(1, len(arr)):
        current_value = arr[index]
        position = index
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position = position - 1
        arr[position] = current_value
    return arr, time.time() - start_time

def shell_sort(arr):
    start_time = time.time()
    sublist_count = len(arr) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(arr, start_position, sublist_count)
        sublist_count = sublist_count // 2
    return arr, time.time() - start_time

def gap_insertion_sort(arr, start, gap):
    for i in range(start + gap, len(arr), gap):
        current_value = arr[i]
        position = i
        while position >= gap and arr[position - gap] > current_value:
            arr[position] = arr[position - gap]
            position = position - gap
        arr[position] = current_value

def python_sort(arr):
    start_time = time.time()
    arr.sort()
    return arr, time.time() - start_time

def main():
    list_sizes = [500, 1000, 10000]
    sort_functions = [
        insertion_sort,
        shell_sort,
        python_sort
    ]
    for size in list_sizes:
        print(f"\nList Size: {size}")
        total_times = {func.__name__: 0 for func in sort_functions}
        for _ in range(100):
            arr = generate_random_list(size)
            for func in sort_functions:
                _, elapsed_time = func(arr[:])
                total_times[func.__name__] += elapsed_time
        for func in sort_functions:
            print(f"{func.__name__} took %10.7f seconds to run, on average" % (total_times[func.__name__] / 100))

if __name__ == "__main__":
    main()
