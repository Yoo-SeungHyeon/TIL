menus = []

def add_item(coffee_name, price):
    menus.append((coffee_name, price))


def show_menu():
    print("메뉴:")
    for menu in menus:
        print(f'{menu[0]}: {menu[1]}원')


