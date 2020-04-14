# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    # ArrA and ArrB is sorted
    # compare the first index when merging
    a = 0
    b = 0

    for i in range(0, elements):
        if a >= len(arrA):  # ArrA elements are merged
            merged_arr[i] = arrB[b]
            b += 1

        elif b >= len(arrB):
            merged_arr[i] = arrA[a]  # ArrB Elements are merged
            a += 1

        elif ArraA[a] < ArraB[b]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]  # Merged index of i into arrA[a]
            a += 1

        else:
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
