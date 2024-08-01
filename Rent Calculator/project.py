#Rent Distributor.

rent = int(input("Enter the house/hostel rent : "))
grocery = int(input("Enter the grocery expense : "))
internet = int(input("Enter the amount of internet bill : "))
electricity = int(input("Enter the amount of electricity bill : "))
water = int(input("Enter the amount of water bill : "))
other = int(input("Enter other expenses : "))
people = int(input("Enter the number of people living in the house/hostel : "))

output = (rent + grocery + internet + electricity + water + other) // people

print(f"Each person will pay = {output}$")
