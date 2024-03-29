__author__ = 'Kalyan'

notes = '''
Implement a left binary search and write exhaustive tests for the same. Left binary search returns the index of left most
element when a search key repeats. For e.g if input is [1,2,3,3,4,4,5] and I search 3, it should return 2 as index 2 is
the left most occurance of 3.

In [1,1,1,1,1,1,1,1], I search for 1, you should return 0.

Note that we are looking for a binary search => we want not more than log(N) lookups, so a solution that involves finding
a random 1 and then doing a linear scan to the left is not a solution :).

- input is an indexable, value is any object.
- return -1 if not found or index of 1st occurance if found.
'''


def left_binary_search(input, value):
    if input == None:
        return -1
    low, high = 0, len(input) - 1

    while low <= high:
        mid = int((low + high) / 2)
        if input[mid] == value:
            temp = my_bin_search(input, value, 0, mid - 1)
            while temp!=-1:
                mid=temp
                temp=my_bin_search(input,value,0,temp-1)
            return mid
        elif input[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def my_bin_search(input,value,start,end):
    if input == None:
        return -1
    low, high = start, end

    while low <= high:
        mid = int((low + high) / 2)
        if input[mid] == value:
                return mid
        elif input[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# write your own exhaustive tests :)
def test_left_binary_search_student():
    assert  0==left_binary_search([1,1,1,1,1,1,1,1],1)
    assert 2 == left_binary_search([1,2,3,3,4,4,5], 3)
    assert -1==left_binary_search(None,None)
    assert -1==left_binary_search([1,2,3,3,4,4,5],6)
    assert  4==left_binary_search([1,2,3,3,4,4,5],4)




# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_left_binary_search_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_left_binary_search(left_binary_search)
