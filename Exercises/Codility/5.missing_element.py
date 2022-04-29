#https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

A = []

def solution(A):
    if (len(A) == 0):
        return 1
    else:
        maximumNumber = len(A)+1
        totalSum = (maximumNumber*(maximumNumber + 1))/2
        partialSum = 0
    
        for i in range(len(A)):
            partialSum += A[i]
            result = totalSum - partialSum
        return int(result)

print(solution(A))
