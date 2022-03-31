import csv


class Dish:
    def __init__(self, name, calories, proteins, fats, carbs):
        self.name = name
        self.calories = calories
        self.proteins = proteins
        self.fats = fats
        self.carbs = carbs

    def __repr__(self):
        return self.name


class Menu:
    def __init__(self):
        self.dishes = {}

    def add_dish(self, index, dish):
        self.dishes[index] = dish

    def show(self):
        items = []
        for index, dish in self.dishes.items():
            items.append(f'{index}. {dish}')
        return '\n'.join(items)


class Order:
    def __init__(self, menu):
        self.menu = menu
        self.ordered_dishes = []

    def add_dish_to_order(self, dish):
        self.ordered_dishes.append(dish)

    def count_calories(self):
        return sum([dish.calories for dish in self.ordered_dishes])


if __name__ == '__main__':

    def parseNumber(string):
        return float(string.strip().replace(',', '.'))
    menu = Menu()
    order = Order(menu)
    your_choice = None

    with open('d:\python\mcdonalds\menu.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for index, row in enumerate(reader, start=1):
            name = row.pop(0)
            values = [parseNumber(element) for element in row]
            dish_item = Dish(name, *values)
            menu.add_dish(index, dish_item)

    print(menu.show())

    while your_choice != 0:
        if (your_choice := int(input("What do you want to eat, 0 to order: "))) != 0:
            order.add_dish_to_order(menu.dishes[your_choice])

    print("You ate", order.count_calories(), "calories.")
