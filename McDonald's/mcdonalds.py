import csv

MAX_CALORIES = 2000

def read_menu():
    with open('d:\python\mcdonalds\menu.csv', 'r') as file:
        reader = csv.reader(file, delimiter = '\t')
        menu = {index: dish for index, dish in enumerate(reader, start=1)}

    return menu
    

def print_menu(menu):
    for index, dish in menu.items():
        print(f'{index} -> {dish[0]} - {dish[1]} kcal')


def make_order(menu):
    your_choice = None
    order = []

    while your_choice != 0:
        if (your_choice := int(input("what do you want to eat, 0 to order: "))) != 0:
            order.append(menu[your_choice])

    return order


def count_calories(order):
    calories = 0
    for dish in order:
        calories += int(dish[1])

    print(f'you ate {calories} calories')
    print(f'and you will be fat :)') if calories > MAX_CALORIES else print('good job')

if __name__ == '__main__':

    menu = read_menu()
    print_menu(menu)
    order = make_order(menu)
    count_calories(order)
