#Define the menu of restaurant.
menu = {
    'Burger':5.99,
    'BB.Q':7.99,
    'Coffee':8.99,
    'Pasta':6.99,
    'Pizza':7.99,
    'Salad':4.99,
    'Fries':2.99,
    'Soda':1.99,
    'Steak':9.99,
    'Water':0.50,
}

#Greet!
print("Welcome to our restaurant!")
print("Here is our menu:")
print("Burger: 5.99$\nBB.Q: 7.99$\nCoffee: 8.99$\nPasta: 6.99$\nPizza: 7.99$\nSalad: 4.99$\nFries: 2.99$\nSode: 1.99$\nSteak: 9.99$\nWater: 0.50$")

orderTotal = 0

#Ask the user to order.
item1 = input("Enter the name of the item you want to order = ")
if item1 in menu:
    orderTotal += menu[item1]
    print(f"Your {item1} has been added to your order.")
else:
    print(f"Sorry, we do not have {item1} on our menu.")

#Ask if they want to have anything else?
another_order = input("Would you like to have anything else? (Yes/No) ")
if another_order == "Yes":
    item2 = input("Enter the name of the item you want to order = ")
    if item2 in menu:
        orderTotal += menu[item2]
        print(f"Your {item2} has been added to your order.")
    else:
        print(f"Sorry, we do not have {item2} on our menu.")

print(f"The total amount of your order is {orderTotal}$")
