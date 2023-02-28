def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start +=1
        end -= 1

array = [1,2,3,4,5,6]
print("The array is", array)
reverseList(array, 0, 5)
print("The reverse array is:")
print(array)
