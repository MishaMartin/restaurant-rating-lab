import random

scores = open("scores.txt", "r")
scores = scores.readlines()
scores.sort()

user_input = ""

dictionary = {}

for i in scores:
    i = i.rstrip().split(":")
    dictionary[F"{i[0]}"] = F"{i[1]}"

def view():
    for i in dictionary:
        print(i,"is rated at", dictionary[i])
    
def add():
    print("We would love for you to rate a new restaurant for our list!")
    new_restaurant = str(input("Restarant Name\n")).capitalize()

    new_rating = 0

    while new_rating < 1 or new_rating > 5: 
        new_rating = int(input("Restaurant Rating\n"))
        if new_rating < 1 or new_rating > 5:
            print("Please use a number from 1 to 5")
    # print(dictionary)
    dictionary[new_restaurant] = new_rating

    sorted_dictionary = {}
    for i in sorted(dictionary):
        sorted_dictionary[i] = dictionary[i]

    for i in sorted_dictionary:
        print(i,"is rated at", sorted_dictionary[i])

def update():
    num = random.randrange(0,len(dictionary))
    new_value = list(dictionary.items())
    rating = new_value[num]
    new_rating = int(input("Please input new restaurant rating.\n"))
    #still working on this section to be able to update the rating.

def cancel():
    exit()
    
while user_input != "quit":
    user_input = input("Please type the response of what you would like to do:\nSee restaurants and ratings: see\n"
        "Add a restauarant and rating: add\n"
        "Update a random restaurant rating: update\n"
        "Quit: quit\n"
        "What would you like to do?\n")
    
    if user_input == "see":
        view()
    if user_input == "add":
        add()
    if user_input == "update":
        update()
    if user_input == "quit":
        cancel()
