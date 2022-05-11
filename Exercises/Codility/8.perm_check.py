# https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/

A = [1, 2, 4]


def solution(A):
    if len(A) == 0:
        return []
    if len(A) == 1:
        return [A]

    lst = []
    for i in range(len(A)):
        m = A[i]
        remLst = A[:i] + A[i+1:]
        for p in solution(remLst):
            lst.append([m] + p)

    return lst


def solution2(A):
    A = sorted(A)
    if A == range(1, len(A)+1):
        return 1
    else:
        return 0


print(solution(A))
print(solution2(A))
