import time

username = "bazif"
password = "secretpassword"

username_input = input("Username: ")
password_input = input("Password: ")

if username_input == username and password_input == password:
    print("Login successful!")
    print("Please wait! Loading...")
    time.sleep(3)
    print("Loading...")
    time.sleep(1)
    print("...")
    print("You have been successfully logged.")

elif username_input != username and password_input == password:
    print("Please wait...")
    time.sleep(3)
    print("Username incorrect. Please try again.")

elif username_input == username and password_input != password:
    print("Please wait...")
    time.sleep(3)
    print("Password incorrect. Please try again.")

else:
    print("Please wait...")
    time.sleep(3)
    print("Username and password incorrect. Please check try again.")