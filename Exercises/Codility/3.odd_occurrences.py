# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/


mylist = [1, 7, 7, 7, 3, 9, 9, 9, 7, 9, 10, 0, 0]
mylist1 = [9, 7, 9, 7, 5, 3, 3, 1, 1, 9, 7]
print(sorted(set([i for i in mylist if mylist.count(i) < 2])))
print(sorted(set([i for i in mylist1 if mylist1.count(i) < 2])))


def solution(mylist1):
    return [i for i in mylist1 if mylist1.count(i) < 2][0]


print("#####")
for i in mylist:
    if mylist.count(i) < 2:
        print(i)


for i in mylist1:
    if mylist1.count(i) < 2:
        print(i)


solution(mylist1)
