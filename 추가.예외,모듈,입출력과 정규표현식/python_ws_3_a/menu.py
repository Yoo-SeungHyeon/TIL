coffee_menu = []

def add_coffee(coffee_name):
    coffee_menu.append(coffee_name)

def show_menu():
    print("현재 커피 메뉴:")
    for coffee in coffee_menu:
        print(coffee)

