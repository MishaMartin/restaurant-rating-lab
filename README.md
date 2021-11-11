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

##Further Study

###Validate New Score
Modify the script so that it validates the score users provide when they add a new restaurant and rating. The rating must be an integer between 1 and 5 (inclusive). If they enter something invalid, the script should prompt them again.

###Give the User Choices
Modify your script so that once it’s loaded the data from scores.txt, it gives users the choice of:

Seeing all the ratings (in alphabetical order)

Adding a new restaurant (and rating it)

Quitting

After performing the user’s chosen action, the script should prompt the user again for what they want to do and continue to do so until the user quits.

###Update a Random Restaurant’s Rating
Modify your script so it gives users another option: updating a (random) restaurant rating. If they choose this option:

Choose a random restaurant from the list in the file. (Hint: the choice() function in the random module will be helpful here.)

Tell the user the chosen restaurant and its rating.

Ask the user what the new rating should be.

Update the rating.

As before, once the rating has been updated, again give the user the choice of seeing, adding, updating, or quitting.

###Update a Chosen Restaurant’s Rating
Modify your script to give users the option to update the rating of a restaurant they choose, rather than a random one.

###To Restaurants and Beyond!
Modify your script so that it displays a list of text files in current directory and allows the users to upload other files. Now we can keep the ratings for different types of restaurants. Allow the user to leave one list and open another.

Hint: You may want to look up the following methods.
os.listdir

os.path.isfile

sys.exit