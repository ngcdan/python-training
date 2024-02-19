"""
Insertion sort is a simple algorithm that works similarly to the way we sort playing cards using both hands.
We traverse one by one through all the cards and compare them with each other.
The sorted cards would appear on the left of our hand while the unsorted cards would appear on the right.
It is also useful when the input array is almost sorted, and only a few elements are misplaced in the whole array.

- How we implemented
1. If it is the first ele, then place it in the sorted sub-array.
2. Pick the next ele.
3. Compare the picked ele with all the elements in sorted sub-array.
4. Shift all the elements in sorted sub-array that are greater than the picked element to be sorted.
5. Insert the element at the desired place.
6. Repeat the above steps until the array is completely sorted.

- Time and space complexity
The worst case time complexity is O(n^2) and the worst case space complexity is O(1).
The best case time complexity is O(n) and the best case space complexity is O(1).

- Reference: https://www.scaler.com/topics/insertion-sort-in-python/

"""

def InsertionSort(array):
    # Traversing the array from 1 to length of the array(a)
    for i in range(1, len(array)):
        temp = array[i]
        # Shift elements of array[0 to i -1] that are greater than temp to one position ahead of their current position
        j = i - 1
        while j >= 0 and temp < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = temp

def InsertionSortDesc(array):
    # Traversing the array from 1 to length of the array.
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while j >= 0 and temp > array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp
'''
loop 1:
    temp = 4
    sorted array = [1]
    compare 4 with 1 ->   4 > 1 -> [4, 1]
    array[0] = temp(1)
loop 2:
    temp = 16
    sorted array = [4, 1]
    compare 16 with 4 ->   16 > 4 -> [16, 4, 1]
    array[1] = temp (4)

'''

input = [9, 4, 16, 1, 5]

print('Original array is:')
print(input)

InsertionSort(input)
print('Sorted array is:')
print(input)

InsertionSortDesc(input)
print('Sorted Desc array is:')
print(input)








