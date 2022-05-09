# https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/

A = [1, 3, 4, 5, 6, 8, 2, 2, 2, 7, 2, 3]


def solution(X, A):
    if X > len(A) or X not in A:
        return -1
    else:
        temp = {}
        for i, leaf in enumerate(A):
            temp[leaf] = i
            # print("Temp:",temp)
            # print("len",len(temp))
            if len(temp) == X:
                return i
    return -1


print("Result:", solution(8, A))
