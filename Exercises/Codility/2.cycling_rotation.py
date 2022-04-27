#https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

A = [3, 8, 9, 7, 6]


def solution(A, K):
    A = A[::-1]
    for x in range(K):
        A.append(A.pop(0))
    return A[::-1]


print(solution(A, 3))