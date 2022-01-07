
def merge_sort(arr):
    n = len(arr)

    if n > 1:
        mid = n//2
        left = arr[0:mid]
        right = arr[mid:n]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, arr)

def merge(left, right, arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1
    
    if i == len(left):   
        t = right[j:]
        for value in t:
            arr[k] = value
            k += 1
    else:
        t = left[i:]
        for value in t:
            arr[k] = value
            k += 1
