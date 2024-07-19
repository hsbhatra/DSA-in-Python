# LAST OCCURRENCE OF AN ELEMENT IN AN ARRAY

def lastOccurenceInAnArray (arr, number, size, i=-1):
    lastIndex = None
    if i == int("-"+str(size)) and lastIndex == None:
        return "No matching element found!"
    elif i == int("-"+str(size)) and lastIndex != None:
        return f"The last index of the element is {lastIndex}."
    
    if arr[i] == number:
        lastIndex = i
        return size + lastIndex
    return lastOccurenceInAnArray(arr, number, size, i-1)
    
arr_1 = [3,5,7,2,4,7,5]
print(lastOccurenceInAnArray(arr_1, 7, len(arr_1)))