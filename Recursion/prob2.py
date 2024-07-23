# Write a function that reverses a string. The input string is given as an array of characters 's'.
# You must do this by modifying the input array in-place with O(1) extra memory.

# Ex:-
# input: ['h', 'e', 'l', 'l', 'o']
# output: ['o', 'l', 'l', 'e','h']

def printingArrayRecursively(arr, size, i=0):
    if i == size:
        return
    print(arr[i], end=" ")
    return printingArrayRecursively(arr, size, i+1)

# arr_1 = [3,5,7,2,4,7,5]
# printingArrayRecursively(arr_1, len(arr_1))

# print()

# printingArrayRecursively(arr_2, len(arr_2))

def reverseArrayRecursively(arr, size, i=0, j=-1):
    if i>=j:
        return 
    
    arr[i], arr[j] = arr[j], arr[i]
    i+=1
    j-=1
    reverseArrayRecursively(arr, size, i, j)

arr_2 = ['h', 'e', 'l', 'l', 'o']
size = len(arr_2)
reverseArrayRecursively(arr_2, size,0,len(arr_2)-1)
# printingArrayRecursively(arr_2, size)
print(arr_2)