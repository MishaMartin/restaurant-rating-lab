"""Restaurant rating lister."""
scores = open("scores.txt", "r")
scores = scores.readlines()
scores.sort()

user_input = input("Please type the response of what you would like to do:\nSee restaurants and ratings: Type (a)\nAdd a restauarant and rating: Type(b)\nQuit: Type (x)\nWhat would like to do?\n")

dictionary = {}

for i in scores:
    i = i.rstrip().split(":")
    dictionary[F"{i[0]}"] = F"{i[1]}"

def view():
    for i in dictionary:
        print(i,"is rated at", dictionary[i])
    
def add():
    print("We would love for you to rate a new restaurant for our list!")
    new_restaurant = str(input("Restarant Name\n"))

    new_rating = 0

    while new_rating < 1 or new_rating > 5: 
        new_rating = int(input("Restaurant Rating\n"))
        if new_rating < 1 or new_rating > 5:
            print("Please use a number from 1 to 5")
    print(dictionary)
    dictionary[new_restaurant] = new_rating

    sorted_dictionary = {}
    for i in sorted(dictionary):
        sorted_dictionary[i] = dictionary[i]

    for i in sorted_dictionary:
        print(i,"is rated at", sorted_dictionary[i])

def cancel():
    exit()
    

if user_input == "a":
    view()
if user_input == "b":
    add()
if user_input == "x":
    cancel()
