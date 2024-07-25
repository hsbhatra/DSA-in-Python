# 1. Arrays
# # Sub-Topics:
    # Basic operations (traversal, insertion, deletion)        
    # Two-pointer technique
    # Sliding window technique      *
    # Prefix sums                   *

# # Practice Questions:
    # Easy:
        # 1. Find the maximum and minimum elements in an array.
        # 2. Reverse an array.

    # Medium:
        # 3. Find the subarray with the maximum sum (Kadane's algorithm).
        # 4. Move all zeroes to the end of an array.

    # Hard:
        # 5. Find the longest subarray with a given sum.
        # 6. Median of two sorted arrays.


##############################################################################################################

# # Traversal:
    # Traversal refers to accessing each element of the array at least once to perform some operation (e.g., printing elements, summing elements).
def traverseArray(arr):
    for element in arr:
        print(element, end=" ")
    print()

a = [1, 2, 3, 4, 5]
traverseArray(a)    # Traverse and prints the items in array.
        

# # Insertion:
    # Insertion involves adding an element to a specific position in the array. In a fixed-size array, you may need to shift elements to make space.
def InsertElement(arr, element, position):
    index = position-1
    arr.insert(index, element)
    return arr

b = a       # Here b is storing address/reference of a, not a copy of a.
b = InsertElement(b, 6, 6)      # So if we insert any item/element to array 'b', it will be eventually updated in the array 'a'.
traverseArray(b)    # Traverse and prints the items in array.


# # Deletion:
    # Deletion involves removing an element from a specific position in the array.
def deleteElement(arr, position):
    arr.pop(position-1)
    return arr

c = a       # Here c is storing address/reference of a, not a copy of a.
c = deleteElement(c, 6)         # So if we delete any item/element to array 'c', it will be eventually updated in the array 'a'.
traverseArray(c)

##############################################################################################################

# # Two-pointer Technique
# The two-pointer technique involves using two pointers to iterate through the array, which can help solve problems involving pairs or subarrays.

# # Example: Find two numbers in a 'sorted' array that add up to a target sum. (Using Two-pointer technique).
def twoSum(arr, targetSum):
    left, right = 0, len(arr)-1
    while left<right:
        currentSum = arr[left]+arr[right]
        if currentSum == targetSum:
            return arr[left], arr[right]
        elif currentSum < targetSum:
            left+=1
        else:
            right-=1
    return None

print(twoSum(c, 5))

##############################################################################################################

# # Sliding Window Technique
# The sliding window technique is useful for finding subarrays or substrings that satisfy certain conditions. 
# It involves moving a "contiguous window/block" of elements across the array.
# The size of the window can be fixed or variable depending on the problem.
# Initial Window: 
    # Start with an initial window of a given size at the beginning of the array.
# Sliding the Window:
    # Move the window across the array by shifting its starting and ending positions.
    # Update the necessary variables as the window slides.
# Optimal Substructure:
    # It means that the solution for a current window can be derived or optimized using the solution of the previous window. 
    # This allows us to avoid recalculating from scratch for each new window, thereby improving efficiency.

# # Example: Find the maximum sum of a subarray of size k.

# Input Format:
# arr: List of integers (e.g., [1, 2, 3, 4, 5])
# k: Integer representing the size of the subarray (e.g., 3)

# Output Format:
# Integer representing the maximum sum of a subarray of size k

# Constraints:
# 1 <= len(arr) <= 10^5 (Length of the array)
# 1 <= k <= len(arr) (Size of the subarray must be at least 1 and at most the length of the array)
# -10^4 <= arr[i] <= 10^4 (Element values)

def maxSubArray(arr, k):
    n = len(arr)
    if n<k:
        return 0
    
    # Step 1: Compute the sum of the first k elements
    currentSum = sum(arr[0:k])
    maxSum = currentSum

    # Step 2: Sliding Window
    for i in range(k, n-1):
        # Initializing sliding window.
        currentSum = currentSum - arr[i-k] + arr[i]
        maxSum = max(currentSum, maxSum)

    return maxSum

print(f"Max Sub-Array (Sliding Window Technique)- {maxSubArray(a, 3)}")

##############################################################################################################

# # Prefix Sums
    # Prefix sums are useful for quickly calculating the sum of elements in a subarray. 
    # The "prefix sum array" stores the 'cumulative sum of elements from the start of the array up to each index'.

# # Example: Calculate the sum of elements between indices i and j (both inclusive).

# Input Format:
# arr: List of integers (e.g., [1, 2, 3, 4, 5])
# i: Integer representing the starting index of the subarray (e.g., 1)
# j: Integer representing the ending index of the subarray (e.g., 3)

# Output Format:
# Integer representing the sum of elements between indices i and j (inclusive)

# Constraints:
# 1 <= len(arr) <= 10^5 (Length of the array)
# 0 <= i <= j < len(arr) (Indices must be within the bounds of the array)
# -10^4 <= arr[i] <= 10^4 (Element values)

def prefixSum(arr):
    prefixSumArray = [0]

    for i in range(1, len(arr)+1):
        prefixSumArray.append(prefixSumArray[i-1] + arr[i-1])

    return prefixSumArray

def rangeSum(arr, start, end):
    prefix = prefixSum(arr)
    print("Prefix Array for [1,2,3,4,5]-", prefix)
    return prefix[end+1] - prefix[start]

def sumElementsBetweenIndices(arr, start, end):
    print(f"Sum of elements between {start} and {end} indices is {rangeSum(arr, start, end)}")

sumElementsBetweenIndices([1,2,3,4,5], 1, 3)


##############################################################################################################

# # Kadane's Algorithm (pseudo code):-

# function kadane_algorithm(arr):
    # Initialize current_max and global_max with the first element of the array
    # current_max = arr[0]
    # global_max = arr[0]

    # # Iterate through the array starting from the second element
    # for i from 1 to length(arr) - 1:
        # # Update current_max to the maximum of current element and current_max + current element
    #     current_max = max(arr[i], current_max + arr[i])
        
    #     # Update global_max if current_max is greater
    #     if current_max > global_max:
    #         global_max = current_max

    # return global_max

