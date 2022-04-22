def BinarySearch(arr, key):  #user-defined function
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1

arr = [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 ]  #array
key = int(input('Enter search key: '))  #search key

# calling function
result = BinarySearch(arr, key)

# display result
if result != -1:
    print(key, "Found at index", str(result))
else:
    print(key, "not Found")