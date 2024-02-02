# Street Foods Online Delivery System
# Created by Christiane Rhely Joselle A. Bacani
orders = []

def print_menu():
    print("\t\t\tMENU!")
    print("1.) Fishball\t\tP 1\n2.) Eggball\t\t\tP 5\n3.) Kikiam\t\t\tP 2\n4.) Isaw\t\t\tP 5\n5.) Atay\t\t\tP 5\n6.) Barbecue\t\tP 5")

def buy():
    userOrder = int(input("Enter your order here: "))
    price_list = {1: 1, 2: 5, 3: 2, 4: 5, 5: 5, 6: 5}

    price = price_list.get(userOrder, 0)
    if price == 0:
        print("INVALID ORDER!")
        return  

    quantity = int(input("Enter quantity here: "))
    orders.append({"item": userOrder, "quantity": quantity, "price": price})

def print_order_summary():
    total_price = sum(order["quantity"] * order["price"] for order in orders)
    print("Total Price : P", total_price)
    for order in orders:
        print(f"Item: {order['item']}, Quantity: {order['quantity']}, Price: P {order['quantity'] * order['price']}")

print("Welcome to Street Foods Online Delivery System!")
input("Press enter to start: ")

while True:
    print("1.) Order Food\n2.) About\n3.) Exit")
    userChoose = int(input("Enter your choice here: "))

    if userChoose == 1:
        print_menu()
        buy()
        orderAgain = input("Do you want to order more (y/n)?: ")
        if orderAgain.lower() != "y":
            print_order_summary()
            break

    elif userChoose == 2:
        print("\nAbout Street Foods Online Delivery System\n")
        print("At Street Foods Online, we bring the delectable world of street food right to your doorstep.")
        print("Our mission is to provide a convenient and enjoyable way for you to savor the flavors of")
        print("your favorite street foods without leaving the comfort of your home.")
        print("Whether you're craving crispy fishballs, savory kikiam, or mouth-watering barbecue,")
        print("we've got you covered with a diverse menu of delicious street food options.")
        print("\nWhy choose Street Foods Online Delivery System?\n")
        print("1. Wide Variety: Explore a diverse menu featuring popular street food items.")
        print("2. Easy Ordering: Our user-friendly system makes ordering your favorite snacks a breeze.")
        print("3. Quick Delivery: Experience prompt and reliable delivery services to satisfy your cravings.")
        print("4. Quality Assurance: We prioritize the quality and freshness of our street food offerings.")
        print("\nThank you for choosing Street Foods Online Delivery System! Enjoy your delightful street food experience.")

    elif userChoose == 3:
        break 












