"""
A leader in an array is an element which is greater than all the elements on its right side in the array.

For example, take an array {2,5,8,7,3,6}. Here 6,7,8 are leaders. Let's take a look at them one by one.
    6 - It is a leader by default because it is the last element of the array.
    7 - It is a leader because it is greater than the elements on its right, i.e., 3,6.
    8 - It is also a leader because it is greater than all the elements on its right, i.e., 7,3,6.
"""


# function for finding leaders
def find_leader_1(arr, n):
    """
    - Time complexity is O(N x N).

    for i=0 to n-1
        for j = i to n-1
            if array[i] < array[j]
                break
            if j == n-1
                print array[i]
    """
    result = []
    for i in range(0, n):
        for j in range(i, n):
            if arr[i] < arr[j]:
                break
            if j == n - 1:
                result.append(arr[i])
    return result

def find_leader_2(arr, n):
    """
    - Time complexity is O(N).
    L = last element
    print L
    for i = n-2 to 0
        if array[i] > L
            L = array[i]
            print L
    """
    result = []
    current = arr[n - 1]
    result.append(current)
    for i in range(n - 2, -1, -1):
        if arr[i] > current:
            current = arr[i]
            result.append(current)
    return result

arr = [ 7, 6, 4, 5, 0, 1 ]
result_1 = sorted(find_leader_1(arr, len(arr)))
result_2 = sorted(find_leader_2(arr, len(arr)))
expected = [1, 5, 6, 7]
assert result_1 == expected
assert result_2 == expected

