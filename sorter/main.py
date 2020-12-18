import numpy as np


def sorted_builtin(ar):
    ar.sort()
    return ar


def custom_sort(ar):
    original_array = ar.copy()
    print("Original array:")
    print(ar)
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
                print(f"Swapping {ar[left]} with {ar[right]}:")
                temp_right = ar[left]
                ar[left] = ar[right]
                ar[right] = temp_right
                swaps += 1
            else:
                # don't swap
                print(f"Not swapping {ar[left]} with {ar[right]}:")
                streak += 1

            # print array thus far
            print(ar)

            left += 1
            right += 1

        if streak == len(ar) - 1:
            # done
            done = True
            print("Done!")
            print(f"Original array: {original_array}")
            print(f"Sorted array: {ar}")
            print(f"Scans: {scans}")
            print(f"Swaps: {swaps}")

        streak = 0
        left = 0
        right = 1


x = np.array([0, -3, 20, 14, -209])

custom_sort(x)
