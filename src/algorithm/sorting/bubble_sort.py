"""
Bubble Sort Algorithm

Bubble Sort is the simplest sorting algorithm that works by 
repeatedly swapping the adjacent elements if they are in the wrong order. 
This algorithm is not suitable for large data sets as its average and worst-case time 
complexity is quite high.

Time Complexity: O(n^2)
Space COmplexity: O(1)

"""

arr = [5, 1, 4, 2, 8]

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]

print(arr)
bubble_sort(arr)
print(arr)