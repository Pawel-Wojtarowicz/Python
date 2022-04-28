#https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/


def solution(X, Y, D):
    i = 0
    while (X < Y):
        i += 1
        X = X + D
        if (X >= Y):
            return i
        else: 
            continue
    else:
        return i

print("Wynik: ",solution(0, 95, 30))


    