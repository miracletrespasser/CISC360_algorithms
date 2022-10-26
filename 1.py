# Recursive function to find a bottom in the list
def findBottomElement(A, left, right):
    #start in the middle
    mid = (left + right) // 2
 
    # return the element if it is lower or equal than its neighbors
        #if the element is the left most
    if ((mid == 0 or A[mid - 1] >= A[mid]) and
            #if the element is the right most 
            (mid == len(A) - 1 or A[mid + 1] >= A[mid])):
        return mid
 
    # If the left neighbor is lower
    if mid - 1 >= 0 and A[mid - 1] < A[mid]:
        result= findBottomElement(A, left, mid - 1)
    if result == -1:
        # If the right neighbor of `mid` is lower
        if mid + 1 <= len(A) - 1 and A[mid + 1] < A[mid]:
            return findBottomElement(A, mid + 1, right)
    else
        return result
    #if there is no match, return -1
    return -1
    