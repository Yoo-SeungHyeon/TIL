
inventory = []

def add_stock(coffee_name, count):
    inventory.append((coffee_name, count))

def show_inventory():
    print("재고:")
    for inven in inventory:
        print(f'{inven[0]}: {inven[1]}개')