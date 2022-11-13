## Section 1 - variables and functions: 

# Question 1: Create two variables. One should be a string data type, and the other should be of type int.

my_text = "Supertext"
my_int= 90909

# Use a single print statement to print both variables:
print(my_text, my_int)


# Question 2: Create a Python function that prints a greeting with a name as the parameter.
def greet(name):
  print(f"Welcome to the class {name}")

# Invoke the function with a name argument of your choosing:
  greet("Scott")



## Section 2 - lists:

# Question 3: Create a list of your favorite movies with  at least 4 elements:
fav_movies = ["Akira", "Howl's Moving Castle","Bleach","Pale Rider"]


# Question 4: Use a print statement to print the list item at the index of 1:
print(fav_movies[1])

# Question 5: Append a movie to the end of your list:
fav_movies.append("Pulp Fiction")

# Use a print statement to print this ammended list:
print(fav_movies)


## Section 3 - dictionaries:

# Question 6: Create a dictionary named 'cellphone' with 2 key:value pairs that are the properties of your cellphone.
#The keys should be: "color" and "number".
#Fill out the values on your own:
cell_phone={"color":"red", "number": "16505534385"}

# Question 7: Access a value from inside the dictionary (Try to print the value of the 'color' property).
color = cell_phone["color"]
print(f"My cell is {color}")



## Section 4 - strings:

# Question 8: Create a variable and store a string with multiple words in it:

my_strings="This is my string.  There are many like it but this one is mine."

# Question 9: Utilize the method that capitalizes the first letter of each word in your string - store this new string in a new variable:
title = my_strings.title()

# Use a print statement to print the new string:
print(title, my_strings)



#Bonus:

# Question 10: Uncomment and look into this nested dictionary - try to relate your knowledge of objects and arrays in JavaScript.

students_in_order = {
   1: {'name': 'Esteban', 'age': '27', 'eye color': 'blue'},
   2: {'name': 'Jackson', 'age': '22', 'eye color': 'brown'},
   3: {'name': 'Zayn', 'age': '26', 'eye color': 'green'}
 }

# Question 10 A: Write a print function that outputs the second student in the dictionary
def get_second_student(index):
  return students_in_order[index]

print(get_second_student(2))
# Question 10 B: Write a print statement that outputs the name "Zayn" using the dictionary
print(get_second_student(3)["name"])
# Question 10 C: Write a print statment that outputs the age of Esteban from the dictionary
print(get_second_student(1)["age"])