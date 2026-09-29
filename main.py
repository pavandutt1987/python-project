# Welcome to Python Guruji! Press Run ▶ (or Ctrl+Enter)
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


print(bubble_sort([1,6,8,5,4,3,2,0]))