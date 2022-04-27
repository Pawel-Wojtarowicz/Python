#https://app.codility.com/programmers/lessons/1-iterations/binary_gap/


def solution(N):
    return len(max(format(N, 'b').strip('0').split('1')))  


print(solution(9999))

