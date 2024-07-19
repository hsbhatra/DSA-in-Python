# PRINTING ARRAY USING RECURSION

def printingArrayRecursively(arr, size, i=0):
    if i == size:
        return
    print(arr[i], end=" ")
    return printingArrayRecursively(arr, size, i+1)

arr_1 = [3,5,7,2,4,7,5]
printingArrayRecursively(arr_1, len(arr_1))

print()

# FINDING FIRST OCCURRENCE OF AN ELEMENT IN AN ARRAY (use the above logic here).

def firstOccurrenceInAnArray(arr, number, size, i=0):
    if i == size:
        return "No element/value in the array matches the number."
    
    if arr[i] == number:
        return f"The first occurrence of {number} in the array is at {i+1} position ({i} index)."
    else:
        return firstOccurrenceInAnArray(arr, number, size, i+1)


arr_2 = [3,5,7,2,4,7,5]
print(firstOccurrenceInAnArray(arr_2, 7, len(arr_2)))
