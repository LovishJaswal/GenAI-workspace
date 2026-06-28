print("\nHi, Welcome to xyz Food and Beverages\n")
data = {
    "Rice": {"price": 80, "quantity": 10},
    "Milk": {"price": 60, "quantity": 25},
    "Paneer": {"price": 120, "quantity": 8},
    "Eggs": {"price": 70, "quantity": 50},
    "Chicken": {"price": 250, "quantity": 5},
    "Apples": {"price": 90, "quantity": 20},
    "Cooking Oil": {"price": 180, "quantity": 12},
    "Bread": {"price": 55, "quantity": 15},
    "Cheese": {"price": 150, "quantity": 7},
    "Bananas": {"price": 65, "quantity": 30},
    "Curd": {"price": 75, "quantity": 18},
    "Butter": {"price": 110, "quantity": 10},
    "Jam": {"price": 85, "quantity": 9},
    "Coffee": {"price": 200, "quantity": 6},
    "Tea Powder": {"price": 95, "quantity": 14},
    "Almonds": {"price": 300, "quantity": 4},
    "Cashews": {"price": 350, "quantity": 3},
    "Honey": {"price": 160, "quantity": 8},
    "Cornflakes": {"price": 140, "quantity": 11},
    "Orange Juice": {"price": 130, "quantity": 13}
}

#Inventory system

def admin_block():
    while True:
        option = input("\nEnter the corresponding number of your choice-\n" \
        "1 - Add a new item\n" \
        "2 - Remove item\n" \
        "3 - Update the quantity\n" \
        "4 - Search for an item\n" \
        "5 - Print all items sorted by quantity\n" \
        "\n Type 'exit' to exit\n" \
        " Enter your choice here: ").strip()
        try:
            option = int(option)
        except:
            pass
        if option == 1:
            new_item_name = input("\nEnter the item's name: ")
            if new_item_name in data:
                print("Item already exists")
                continue
            new_item_price = int(input("Enter the item's price: "))
            new_item_quantity = int(input("Enter the item's quantity: "))
            data[new_item_name] = {"price": new_item_price, "quantity": new_item_quantity}
            print(data)
        elif option == 2:
            remove_item = input("\nEnter the item's name: ")
            if remove_item in data:
                data.pop(remove_item)
                print("Operation successful")
            else:
                print("Item not found")
        elif option == 3:
            update_qu_name = input("\nEnter the item's name: ")
            print(f"Available Quantity: {data[update_qu_name]['quantity']}")
            qnt = int(input("\nEnter the new quantity: "))
            data[update_qu_name]["quantity"] = qnt
            print("Operation successful")
        elif option == 4:
            search_item_name = input("\nEnter the item's name: ")
            if search_item_name in data:
                print(data[search_item_name])
            else:
                print("value not found!")
        elif option == 5:
            print("\nAvailable data: ")
            print(sorted(data.items(), key=lambda item: item[1]["quantity"]))
        elif option == 'exit':
            break
        else:
            print("\nError! Enter a valid choice")
            continue
        

user_data = []
item = None
while True:
    item = input("Kindly enter your item's name or press 'exit' to exit: ").strip()
    if item == 'exit':
        break
    if item == "admin@123":
        admin_block()
        break
    if item not in data:
        print("Sorry! Item is not available at the moment")
        continue
    quantity_by_user = int(input("Kindly enter your item's quantity: "))
    price = data[item]['price']
    if quantity_by_user > data[item]["quantity"]:
        print("Not enough stock available")
        continue
    user_data.append((item, price, quantity_by_user))
    data[item]["quantity"] -= quantity_by_user


def add_price():
    tot_price = 0
    for i in user_data:
        tot_price+=(i[1])*(i[2])
    return tot_price


total_price = add_price()
after_discount_price = 0
if total_price > 1000:
    after_discount_price = (95/100)*total_price

print("\nHere's your receipt: \n\n")
print("Item, Price(per item), Quantity\n")
for x in user_data:
    print(f"{x[0]}, {x[1]}, {x[2]}")


print(f"\nTotal price: {total_price}")
if after_discount_price != 0:
    print("Discount applied: 5%")
    print(f"Grand Total: {after_discount_price}")


