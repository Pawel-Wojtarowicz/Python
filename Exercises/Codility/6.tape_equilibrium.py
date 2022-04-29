# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

lista = [3, 1, 2, 4, 3]


def solution(A):
    result = []
    for i in range(1, len(lista)+1):
        part1 = lista[:i]
        part2 = lista[i:]
        result.append(abs(sum(part1)-sum(part2)))
    return min(result)


def solution2(A):
    res = []
    left_sum = 0
    right_sum = sum(A)
    for i in range(0, len(A)-1):
        left_sum += A[i]
        right_sum = right_sum - A[i]
        res.append(abs(right_sum-left_sum))
    return min(res)


print(solution(lista))
print(solution2(lista))
