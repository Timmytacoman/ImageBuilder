import numpy as np
import time
import random


def time_custom(x):
    start_time = time.time()
    custom_sort(x)
    end_time = time.time()
    return end_time - start_time


def time_builtin(x):
    start_time = time.time()
    sorted_builtin(x)
    end_time = time.time()
    return end_time - start_time


def sorted_builtin(ar):
    print("--------------------------------------")
    print("Using builtin sort:")
    print(f"Original array: {ar}")
    ar.sort()
    print(f"Sorted array: {ar}")
    print("--------------------------------------")
    return ar


def custom_sort(ar):
    original_array = ar.copy()
    print("--------------------------------------")
    print("Using custom sort:")

    # print("Original array:")
    # print(ar)
    # select left and right
    left = 0
    right = 1

    scans = 0
    swaps = 0
    streak = 0
    done = False

    while not done:

        scans += 1
        # scan through all elements
        while right != len(ar):
            # compare nums
            if ar[left] > ar[right]:
                # swap
                # print(f"Swapping {ar[left]} with {ar[right]}:")
                temp_right = ar[left]
                ar[left] = ar[right]
                ar[right] = temp_right
                swaps += 1
            else:
                # don't swap
                # print(f"Not swapping {ar[left]} with {ar[right]}:")
                streak += 1

            # print array thus far
            # print(ar)

            left += 1
            right += 1

        if streak == len(ar) - 1:
            # done
            done = True
            # print("Done!")
            print(f"Original array: {original_array}")
            print(f"Sorted array: {ar}")

            # print(f"Scans: {scans}")
            # print(f"Swaps: {swaps}")

        streak = 0
        left = 0
        right = 1


rnd_list = []
for i in range(500):
    rnd_list.append(random.randint(0, 100))

x = np.array(rnd_list)
y = np.copy(x)
print(time_custom(x))
print(time_builtin(y))
