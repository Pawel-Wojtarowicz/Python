import json
import random

used_questions = []
points = 0
category = {"1":"Film", "2":"IT", "3":"Geogriafia"}

def show_questions(question):
    global points

    print()
    print(question["pytanie"])
    print("a:", question["a"])
    print("b:", question["b"])
    print("c:", question["c"])
    print("d:", question["d"])
    print()

    answer = input("Która odpowiedź wybierasz? ")
    answer = answer.lower()
    while not answer in ("a", "b", "c", "d"):
        print("Nie ma takiej opcji. Wybierz 'a', 'b', 'c' lub 'd'")
        answer = input("Która odpowiedź wybierasz? ")
        answer = answer.lower()
        
    if answer == question["prawidlowa_odpowiedz"]:
        points += 1
        print("Brawo! To prawidłowa odpowiedź. Masz juz", points, "punktów.")
    else:
        print("Niestety to zła odpowiedź, prawidłowa odpowiedź to " + question["prawidlowa_odpowiedz"] + ".")

while True:
    with open("d:\python\git\json\quiz2.json", encoding="utf-8") as json_file:
        questions = json.load(json_file)
        random.shuffle(questions)
        user_choice = input("Wybiesz Kategorie\n1. Film\n2. IT\n3. Geografia\n:")

        for i in range(0, len(questions)):
            if points == 2: 
                break
            elif questions[i]["id"] in used_questions:
                continue
            else:
                if questions[i]["kategoria"] == category[str(user_choice)]: 
                    show_questions(questions[i])
                    used_questions.append(questions[i]["id"])

    if input("Chcesz zagrac jeszcze raz? T/N: ").upper() == 'T':
        points = 0
        continue
    else:
        break

print("Koniec gry. Zdobyłes punktów " + str(points) + ".")

