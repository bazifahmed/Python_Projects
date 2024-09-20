import random

print(
    "Alex",
    "Sam",
    "Tom",
    "John",
    "Peter",
    "Nadiya",
    "Carmelia",
    "Noah",
    "Bazif",
    "Jeff",
)

print("Who should I invite for Netflix and Chill?")

friends = [
    "Alex",
    "Sam",
    "Tom",
    "John",
    "Peter",
    "Nadiya",
    "Carmelia",
    "Noah",
    "Bazif",
    "Jeff",
]

# random.choice(array) --> random item in this array

selected = random.choice(friends) # randomly chooses a friend

print(selected)