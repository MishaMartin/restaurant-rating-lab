"""Restaurant rating lister."""
scores = open("scores.txt", "r")
scores = scores.readlines()
scores.sort()

dictionary = {}

for i in scores:
    i = i.rstrip().split(":")
    dictionary[F"{i[0]}"] = F"{i[1]}"
print(dictionary)

for i in dictionary:
    print(i,"is rated at", dictionary[i])

print("We would love for you to rate a new restaurant for our list!")
new_restaurant = str(input("Restarant Name\n"))
new_rating = str(input("Restaurant Rating\n"))

dictionary[new_restaurant] = new_rating

sorted_dictionary = {}
for i in sorted(dictionary):
    sorted_dictionary[i] = dictionary[i]

for i in sorted_dictionary:
    print(i,"is rated at", sorted_dictionary[i])
