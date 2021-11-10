# restaurant-rating-lab

Dictionaries: Restaurant Ratings¶
Introduction
As you may recall, dictionaries are sets of key-value pairs where every key is unique. In this exercise you will get some more practice working with dictionaries.

Setup
Download the materials for this exercise by clicking here.

Reading Ratings in from a File
In this directory, you will find a text file, scores.txt, containing a series of local restaurant ratings. Each line looks like this:

RestaurantName:Rating
Your job is to write a program named ratings.py that:

Reads the ratings in from the file

Stores them in a dictionary

And finally, spits out the ratings in alphabetical order by restaurant

Hint 1: Using .items() to get a list of your dictionary entries will help with sorting.

Hint 2: Refer to the Python docs on the sorted() function if you need a reminder of how to sort.

Sample output:

$ python3 restaurant-ratings.py
Big Bean Shack is rated at 3.
Chip Shop is rated at 3.
Diagon Alley cafe is rated at 2.
Eternelle's Elixir of Refreshment is rated at 5.
Florean Fortescue's Ice Cream Parlour is rated at 4.
Jellied Eel Shop is rated at 3.
Luchino Caffe is rated at 1.
Ministry Munchies is rated at 1.
The Bear & Staff is rated at 2.
The Club is rated at 2.
The Porcupine is rated at 5.
The Tavern is rated at 3.
Allowing the User to Add Ratings
Modify your script so that after it reads the scores file from disk, it prompts the user for a new restaurant and rating.
($ For ease of reading with colors)

The program should:

Prompt the user for a restaurant name

Prompt the user for a restaurant score

Store the new restaurant/rating in the dictionary

Print all of the ratings in alphabetical order (including the new one, of course)