# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below

# IF the first number is greater , swap
#  else, if continue to the next index
# els, if
# and while loop
# LOok up flag
# ##
def bubble_sort(arr):
    swap = True
    while swap:
        swap = False  s
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:  # compare if current element is greater than its neighbor in right
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap if  yes
                swap = True
    return arr

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
