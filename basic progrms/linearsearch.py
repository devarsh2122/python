# Python program for linear search

def linearSearch(arr, key):  #user-defined function
    for i in range(len(arr)): 
        if (arr[i] == key): 
            return i 
    return -1

arr = []
for x in range(5):
    y= input('enter a number')
    arr.append(int(y))
#arr = [50, 90, 30, 70, 60]  #array

key = input('enter a number to search in')
#key = 70  #search key

index = linearSearch(arr, int(key)) #calling function

# display result
if (index == -1):
    print(key, 'not Found.')
else:
    print(key, 'Found at Index', index)