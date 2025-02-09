coffee_menu = []

def record_sale(coffee, count):
    with open("sales.txt", 'a') as f:
        f.write(f"{coffee}, {count}\n")
