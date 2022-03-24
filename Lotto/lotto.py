import random
from random import sample
      
def player_numbers():
    while True:
        try:
            numbers = list(map(int,input("Podaj 6 liczb po przecinku (od 1 do 49): ").strip().split(',')))[:6]     
            if len(numbers) == 6 and len(numbers) == len(set(numbers)) and all(i >= 1 and i < 50 for i in numbers):
                break
            else:
                pass
        except Exception as e: print("Podałeś złe liczby, spróbuj jeszcze raz. Wybierz 6 z zakresu 1-49")  
        continue
    return set(numbers)


def random_num():
    return set(random.sample(range(1, 50), 6))


counter = 0
how_many_years = 0
how_many_4 = 0
how_many_5 = 0
numbers = player_numbers()

while True:
    random_numbers = random_num()
    
    if random_numbers == numbers:
        print("Moje liczby: ", numbers)
        print("Koniec gry, brawo")
        print(f"Czwórek było {how_many_4} a piątek {how_many_5}.")
        counter = counter/3
        how_many_years = counter/52
        print(f"Zanim wygrałeś mineło, {counter:,.2f} tygodni(a), co daje, {how_many_years:.2f} lat.")
        break
    else: 
        how_many_4or5 = random_numbers.intersection(numbers)
        if len(how_many_4or5) == 4:
            how_many_4 += 1
        if len(how_many_4or5) == 5:
            how_many_5 += 1
        counter +=1
        continue

