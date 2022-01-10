from quick_sort import quick_sort

def test_quick_sort1():
    arr = [8,4,23,42,16,15]
    quick_sort(arr, 0, 5)
    expected = [4, 8, 15, 16, 23, 42]
    assert arr == expected

def test_quick_sort2():
    arr = [20,18,12,8,5,-2]
    quick_sort(arr, 0, 5)
    expected = [-2, 5, 8, 12, 18, 20]
    assert arr == expected

def test_quick_sort3():
    arr = [5,12,7,5,5,7]
    quick_sort(arr, 0, 5)
    expected = [5, 5, 5, 7, 7, 12]
    assert arr == expected

def test_quick_sort4():
    arr = [2,3,5,7,13,11]
    quick_sort(arr, 0, 5)
    expected = [2, 3, 5, 7, 11, 13]
    assert arr == expected