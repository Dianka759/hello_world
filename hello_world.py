# 1. TASK: print "Hello World"
print("Hello World")

# 2. print "Hello Noelle!" with the name in a variable
name = "Diana"
print("Hello", name, "!")  # with a comma
print("Hello " + name + "!")  # with a +

# 3. print "Hello 42!" with the number in a variable
name = 7
print("Hello", name, "!")  # with a comma
print("Hello " + str(name) + "!")  # with a +	-- this one should give us an error!

# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "crab rangoons"
fave_food2 = "gummy bears"
print("I love to eat {} and {}.".format(fave_food1, fave_food2))  # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.")  # with an f string

#  practice
name = "Diana"
print (len(name))
print (name.upper())
print (name.lower())

my_friends = ["Andrew", "Angelika","Franek"]
print ("I have " + str(len(my_friends)) + " friends.")
my_friends.append("Winter")
print(my_friends)
print("Now I have " + str(len(my_friends)) + " friends.")