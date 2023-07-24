arr = [1, 5, 12, 18, 16, 39 , 42, 57 ]
target = 39

def binarySearch(arr,target):
    left = 0
    right = len(arr) - 1

    while(left <= right):
        middle = (left + right) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return - 1

result = binarySearch(arr, target)
print (f"taget is located at index: {result}")