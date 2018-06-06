#~~Learn to program 1
# Programming involves listing all the things that must happen to solve a problem
# When writing a program first determine step-by-step what needs to happen
# Then convert those steps into the language being Python in this situation

# Every language has the following
# 1. The ability to accept input and store it in many ways
# 2. The ability to output information to the screen, files, etc.
# 3. The ability to conditionally do one thing or another thing
# 4. The ability to do something multiple times
# 5. The ability to make mathematical calculations
# 6. The ability to change data
# 7. (Object Oriented Programming) Model real world objects using code

# ---------- Hello World ----------

# Ask the user to input their name and assign it to the name variable
# Variable names start with a letter or _ and then can contain numbers
# Names are case sensitive so name is not the same as Name
name = input('What is your name ')

# Print out Hello followed by the name they entered
print('Hello ', name)

# You can't use the following for variable names
# and, del, from, not, while, as, elif, global,
# or, with, assert, else, if, pass, yield, break,
# except, import, print, class, exec, in, raise,
# continue, finally, is, return, def, for, lambda,
# try

# Single line comments are ignored by the interpreter
'''
So are multiline comments
'''

# ---------- MATH ON 2 VALUES ----------

# Ask the user to input 2 values and store them in variables num1 and num2
# split() splits input using whitespace
num1, num2 = input('Enter 2 numbers : ').split()

# Convert strings into regular numbers (integers)
num1 = int(num1)
num2 = int(num2)

# Add the values entered and store in sum
sum = num1 + num2

# Subtract the values and store in difference
difference = num1 - num2

# Multiply the values and store in product
product = num1 * num2

# Divide the values and store in quotient
quotient = num1 / num2

# Use modulus on the values to find the remainder
remainder = num1 % num2

# Print your results
# format() loads the variable values in order into the {} placeholders
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))

# ---------- PROBLEM : MILES TO KILOMETERS ----------
# Sample knowing that kilometers = miles * 1.60934
# Enter Miles 5
# 5 miles equals 8.0467 kilometers

# Ask the user to input miles and assign it to the miles variable
miles = input('Enter Miles ')

# Convert from string to integer
miles = int(miles)

# Perform calculation by multiplying 1.60934 times miles
kilometers = miles * 1.60934

# Print results using format()
print("{} miles equals {} kilometers".format(miles, kilometers))

# ---------- CALCULATOR ----------
# Receive 2 numbers separated by an operator and show a result
# Sample
# Enter Calculation: 5 * 6
# 5 * 6 = 30

# Store the user input of 2 numbers and an operator
num1, operator, num2 = input('Enter Calculation: ').split()

# Convert strings into integers
num1 = int(num1)
num2 = int(num2)

# If, else if (elif) and else execute different code depending on a condition
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1+num2))

# If the 1st condition wasn't true check if this one is
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))

# If none of the above conditions were true then execute this by default
else:
    print("Use either + - * or / next time")

# Other conditional operators
# > : Greater than
# < : Less than
# >= : Greater than or equal to
# <= : Less than or equal to
# != : Not equal to

# ---------- IS BIRTHDAY IMPORTANT ----------
# We'll provide different output based on age
# 1 - 18 -> Important
# 21, 50, > 65 -> Important
# All others -> Not Important

# eval() converts a string into an integer if it meets the guidelines
age = eval(input("Enter age: "))

# Logical operators can be used to combine conditions
# and : If both are true it returns true
# or : If either are true it returns true
# not : Converts true into false and vice versa

# If age is both greater than or equal to 1 and less than or equal to 18 it is true
if (age >= 1) and (age <= 18):
    print("Important Birthday")

# If age is either 21 or 50 then it is true
elif (age == 21) or (age == 50):
    print("Important Birthday")

# We check if age is less than 65 and then convert true to false or vice versa
# This is the same as if we put age > 65
elif not(age < 65):
    print("Important Birthday")
else:
    print("Sorry Not Important")

# ---------- PROBLEM : DETERMINE GRADE ----------
# If age 5 go to kindergarten
# Ages 6 through 17 goes to grades 1 through 12
# If age is greater then 17 then say go to college
# Try to complete with 10 or less lines

# Ask for the age
age = eval(input("Enter age: "))

# Handle if age < 5
if age < 5:
    print("Too Young for School")

# Special output just for age 5
elif age == 5:
    print("Go to Kindergarten")

# Since a number is the result for ages 6 - 17 we can check them all
# with 1 condition
# Use calculation to limit the conditions checked
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to {} grade".format(grade))

# Handle everyone else
else:
    print("Go to College")


#~~Learn to program 2
# Every program has the ability to perform actions on a list of
# values. The for loop can be used to do this.

# Each time we go through the loop variable i's value will be
# assigned the next value in our list

for i in [2,4,6,8,10]:
    print("i = ", i)

# We can also have range define our list for us. range(10) will
# create a list starting at 0 and go up to but not include
# the value passed to it.

for i in range(10):
    print("i = ", i)

# We can define the starting and ending value for range
for i in range(2, 10):
    print("i = ", i)

# You can use modulus to see if a number is odd or even
# If we divide an even by 2 there will be no remainder
# so if i % 2 == 0 we know it is true
i = 2
print((i % 2) == 0)

# ---------- PROBLEM : PRINT ODDS FROM 1 to 20 ----------
# Use a for loop, range, if and modulus to print out the odds

# Use for to loop through the list from 1 to 21

for i in range(1, 21):

# Use modulus to check that the result is NOT EQUAL to 0
# Print the odds

    if ((i % 2) != 0):
        print("i = ", i)

# ---------- WORKING WITH FLOATS ----------
# Floating point numbers are numbers with decimal values

your_float = input("Enter a float: ")

# We can convert a string into a float like this

your_float = float(your_float)

# We can define how many decimals are printed being 2
# here by putting :.2 before f
print("Rounded to 2 decimals : {:.2f}".format(your_float))

# ---------- PROBLEM : COMPOUNDING INTEREST ----------
# Have the user enter their investment amount and expected interest
# Each year their investment will increase by their investment +
# their investment * the interest rate
# Print out their earnings after a 10 year period

# Ask for money invested + the interest rate
money = input("How much to invest: ")
interest_rate = input("Interest Rate: ")

# Convert value to a float
money = float(money)

# Convert value to a float and round the percentage rate by 2 digits
interest_rate = float(interest_rate) * .01

# Cycle through 10 years using for and range from 0 to 9
for i in range(10):

    # Add the current money in the account + interest earned that year
    money = money + (money * interest_rate)

# Output the results
print("Investment after 10 years: {:.2f}".format(money))

# ---------- WORKING WITH FLOATS ----------
# When working with floats understand that they are not precise

# This should print 0 but it doesn't
i = 0.1 + 0.1 + 0.1 - 0.3
print(i)

# Floats will print nonsense beyond 16 digits of precision
i = .11111111111111111111111111111111
j = .00000000000000010000000000000001

print("Answer : {:.32}".format(i + j))

# ---------- ORDER OF OPERATIONS ----------
# When making calculations unless you use parentheses * and /
# will supersede + and -

print("3 + 4 * 5 = {}".format(3 + 4 * 5))

print("(3 + 4) * 5 = {}".format((3 + 4) * 5))

# ---------- THE WHILE LOOP ----------
# We can also continue looping as long as a condition is true
# with a while loop

# While loops are used when you don't know how many times
# you will have to loop

# We can use the random module to generate random numbers
import random

# Generate a random integer between 1 and 50
rand_num = random.randrange(1, 51)

# The value we increment in the while loop is defined before the loop
i = 1

# Define the condition that while true we will continue looping
while (i != rand_num):

    # You must increment your iterator inside the while loop
    i += 1

# Outside of the while loop when we stop adding whitespace
print("The random value is : ", rand_num)

# ---------- BREAK AND CONTINUE ----------
# Continue stops executing the code that remains in the loop and
# jumps back to the top

# Break jumps completely out of the loop

i = 1

while i <= 20:

    # If a number is even don't print it
    if (i % 2) == 0:
        i += 1
        continue

    # If i equals 15 stop looping
    if i == 15:
        break

    # Print the odds
    print("Odd : ", i)

    # Increment i
    i += 1

# ---------- PROBLEM : DRAW A PINE TREE ----------
# For this problem I want you to draw a pine tree after asking the user
# for the number of rows. Here is the sample program

'''
How tall is the tree : 5
    #
   ###
  #####
 #######
#########
    #
'''

# You should use a while loop and 3 for loops

# I know that this is the number of spaces and hashes for the tree
# 4 - 1
# 3 - 3
# 2 - 5
# 1 - 7
# 0 - 9
# Spaces before stump = Spaces before top

# So I need to
# 1. Decrement spaces by one each time through the loop
# 2. Increment the hashes by 2 each time through the loop
# 3. Save spaces to the stump by calculating tree height - 1
# 4. Decrement from tree height until it equals 0
# 5. Print spaces and then hashes for each row
# 6. Print stump spaces and then 1 hash

# Get the number of rows for the tree
tree_height = input("How tall is the tree : ")

# Convert into an integer
tree_height = int(tree_height)

# Get the starting spaces for the top of the tree
spaces = tree_height - 1

# There is one hash to start that will be incremented
hashes = 1

# Save stump spaces til later
stump_spaces = tree_height - 1

# Makes sure the right number of rows are printed
while tree_height != 0:

    # Print the spaces
    # end="" means a newline won't be added
    for i in range(spaces):
        print(' ', end="")

    # Print the hashes
    for i in range(hashes):
        print('#', end="")

    # Newline after each row is printed
    print()

    # I know from research that spaces is decremented by 1 each time
    spaces -= 1

    # I know from research that hashes is incremented by 2 each time
    hashes += 2

    # Decrement tree height each time to jump out of loop
    tree_height -= 1

# Print the spaces before the stump and then a hash
for i in range(stump_spaces):
    print(' ', end="")

print("#")


#~~Learn to Program 3
# ---------- FORCE USER TO ENTER A NUMBER ----------
# By giving the while a value of True it will cycle until a break is reached
while True:

    # If we expect an error can occur surround potential error with try
    try:
        number = int(input("Please enter a number : "))
        break

    # The code in the except block provides an error message to set things right
    # We can either target a specific error like ValueError
    except ValueError:
        print("You didn't enter a number")

    # We can target all other errors with a default
    except:
        print("An unknown error occurred")

print("Thank you for entering a number")

# ---------- Problem : Implement a Do While Loop ----------
# Now I want you to implement a Do While loop in Python
# They always execute all of the code at least once and at
# the end check if a condition is true that would warrant
# running the code again. They have this format
# do {
#   ... Bunch of code ...
# } while(condition)

# I'll create a guessing game in which the user must chose
# a number between 1 and 10 of the following format
'''
Guess a number between 1 and 10 : 1
Guess a number between 1 and 10 : 3
Guess a number between 1 and 10 : 5
Guess a number between 1 and 10 : 7
You guessed it
'''

# Hint : You'll need a while and break

secret_number = 7

while True:
    guess = int(input("Guess a number between 1 and 10 : "))

    if guess == secret_number:
        print("You guessed it")
        break

# ---------- MATH MODULE ----------
# Python provides many functions with its Math module
import math

# Because you used import you access methods by referencing the module
print("ceil(4.4) = ", math.ceil(4.4))
print("floor(4.4) = ", math.floor(4.4))
print("fabs(-4.4) = ", math.fabs(-4.4))

# Factorial = 1 * 2 * 3 * 4
print("factorial(4) = ", math.factorial(4))

# Return remainder of division
print("fmod(5,4) = ", math.fmod(5,4))

# Receive a float and return an int
print("trunc(4.2) = ", math.trunc(4.2))

# Return x^y
print("pow(2,2) = ", math.pow(2,2))

# Return the square root
print("sqrt(4) = ", math.sqrt(4))

# Special values
print("math.e = ", math.e)
print("math.pi = ", math.pi)

# Return e^x
print("exp(4) = ", math.factorial(4))

# Return the natural logarithm e * e * e ~= 20 so log(20) tells
# you that e^3 ~= 20
print("log(20) = ", math.log(20))

# You can define the base and 10^3 = 1000
print("log(1000,10) = ", math.log(1000,10))

# You can also use base 10 like this
print("log10(1000) = ", math.log10(1000))

# We have the following trig functions
# sin, cos, tan, asin, acos, atan, atan2, asinh, acosh,
# atanh, sinh, cosh, tanh

# Convert radians to degrees and vice versa
print("degrees(1.5708) = ", math.degrees(1.5708))
print("radians(90) = ", math.radians(90))

# ---------- ACCURATE FLOATING POINT CALCULATIONS ----------

# The decimal module provides for more accurate floating point calculations
# With from you can reference methods without the need to reference the module
# like we had to do with math above
# We create an alias being D here to avoid conflicts with methods with
# the same name
from decimal import Decimal as D

sum = D(0)
sum += D("0.01")
sum += D("0.01")
sum += D("0.01")
sum -= D("0.03")

print("Sum = ", sum)

# ---------- STRINGS ----------
# Text is stored using the string data type
# You can use type to see the data type of a value
print(type(3))
print(type(3.14))

# Single quotes or double are both used for strings
print(type("3"))
print(type('3'))

samp_string = "This is a very important string"

# Each character is stored in a series of boxes labeled with index numbers
# You can get a character by referencing an index
print(samp_string[0])

# Get the last character
print(samp_string[-1])

# Get the last character
print(samp_string[3+5])

# Get the string length
print("Length :", len(samp_string))

# Get a slice by saying where to start and end
# The 4th index isn't returned
print(samp_string[0:4])

# Get everything starting at an index
print(samp_string[8:])

# Join or concatenate strings with +
print("Green " + "Eggs")

# Repeat strings with *
print("Hello " * 5)

# Convert an int into a string
num_string = str(4)

# Cycle through each character with for
for char in samp_string:
    print(char)

# Cycle through characters in pairs
# Subtract 1 from the length because length is 1 more then the highest index
# because strings are 0 indexed
# Use range starting at index 0 through string length and increment by
# 2 each time through
for i in range(0, len(samp_string)-1, 2):
    print(samp_string[i] + samp_string[i+1])

# Computers assign characters with a number known as a Unicode
# A-Z have the numbers 65-90 and a-z 97-122

# You can get the Unicode code with ord()
print("A =", ord("A"))

# You can convert from Unicode with chr
print("65 =", chr(65))

# ---------- PROBLEM : SECRET STRING ----------
# Receive a uppercase string and then hide its meaning by turning
# it into a string of unicodes
# Then translate it from unicode back into its original meaning

norm_string = input("Enter a string to hide in uppercase: ")

secret_string = ""

# Cycle through each character in the string
for char in norm_string:

    # Store each character code in a new string
    secret_string += str(ord(char))

print("Secret Message :", secret_string)

norm_string = ""

# Cycle through each character code 2 at a time by incrementing by
# 2 each time through since unicodes go from 65 to 90
for i in range(0, len(secret_string)-1, 2):

    # Get the 1st and 2nd for the 2 digit number
    char_code = secret_string[i] + secret_string[i+1]

    # Convert the codes into characters and add them to the new string
    norm_string += chr(int(char_code))

print("Original Message :", norm_string)

# ---------- SUPER AWESOME MIND SCRAMBLING PROBLEM ----------
# Make the above work with upper and lowercase with 1 addition and
# 1 subtraction

# Add these 2 changes

# secret_string += str(ord(char) - 23)

# norm_string += chr(int(char_code) + 23)




#~~Learn to program 4
# ---------- STRING METHODS ----------

# Strings have many methods we can use beyond what I covered last time
rand_string = "   this is an important string   "

# Delete whitespace on left
rand_string = rand_string.lstrip()

# Delete whitespace on right
rand_string = rand_string.rstrip()

# Delete whitespace on right and left
rand_string = rand_string.strip()

# Capitalize the 1st letter
print(rand_string.capitalize())

# Capitalize every letter
print(rand_string.upper())

# lowercase all letters
print(rand_string.lower())

# Turn a list into a string and separate items with the defined
# separator
a_list = ["Bunch", "of", "random", "words"]
print(" ".join(a_list))

# Convert a string into a list
a_list_2 = rand_string.split()

for i in a_list_2:
    print(i)

# Count how many times a string occurs in a string
print("How many is :", rand_string.count("is"))

# Get index of matching string
print("Where is string :", rand_string.find("string"))

# Replace a substring
print(rand_string.replace("an ", "a kind of "))

# ---------- PROBLEM : ACRONYM GENERATOR ----------
# You will enter a string and then convert it to an acronym
# with uppercase letters like this
'''
Convert to Acronym : Random Access Memory
RAM
'''

# Ask for a string
orig_string = input("Convert to Acronym : ")

# Convert the string to all uppercase
orig_string = orig_string.upper()

# Convert the string into a list
list_of_words = orig_string.split()

# Cycle through the list
for word in list_of_words:

    # Get the 1st letter of the word and eliminate the newline
    print(word[0], end="")

print()

# ---------- MORE STRING METHODS ----------
# For our next problem some additional string methods are going to be
# very useful

letter_z = "z"
num_3 = "3"
a_space = " "

# Returns True if characters are letters or numbers
# Whitespace is false
print("Is z a letter or number :", letter_z.isalnum())

# Returns True if characters are letters
print("Is z a letter :", letter_z.isalpha())

# Returns True if characters are numbers (Floats are False)
print("Is 3 a number :", num_3.isdigit())

# Returns True if all are lowercase
print("Is z a lowercase :", letter_z.islower())

# Returns True if all are uppercase
print("Is z a uppercase :", letter_z.isupper())

# Returns True if all are spaces
print("Is space a space :", a_space.isspace())

# ---------- MAKE A isfloat FUNCTION ----------
# There is no way to check if a string contains a float
# so let's make one by defining our own function

# Functions allow use to avoid repeating code
# They can receive values (attributes / parameters)
# They can return values

# You define your function name and the names for the values
# it receives like this

def isfloat(str_val):
    try:

        # If the string isn't a float float() will throw a
        # ValueError
        float(str_val)

        # If there is a value you want to return use return
        return True
    except ValueError:
        return False

pi = 3.14

# We call our functions by name and pass in a value between
# the parentheses
print("Is Pi a Float :", isfloat(pi))

# ---------- PROBLEM : CAESAR'S CIPHER ----------
# Receive a message and then encrypt it by shifting the
# characters by a requested amount to the right
# A becomes D, B becomes E for example
# Also decrypt the message back again

# A-Z have the numbers 65-90 in unicode
# a-z have the numbers 97-122
# You get the unicode of a character with ord(yourLetter)
# You convert from unicode to character with chr(yourNumber)

# You should check if a character is a letter and if not
# leave it as its default

# Hints
# Use isupper() to decided which unicodes to work with
# Add the key (number of characters to shift) and if
# bigger or smaller then the unicode for A, Z, a, or z
# increase or decrease by 26

# Receive the message to encrypt and the number of characters to shift
message = input("Enter your message : ")
key = int(input("How many characters should we shift (1 - 26)"))

# Prepare your secret message
secret_message = ""

# Cycle through each character in the message
for char in message:

    # If it isn't a letter then keep it as it is in the else below
    if char.isalpha():

        # Get the character code and add the shift amount
        char_code = ord(char)
        char_code += key

        # If uppercase then compare to uppercase unicodes
        if char.isupper():

            # If bigger than Z subtract 26
            if char_code > ord('Z'):
                char_code -= 26

            # If smaller than A add 26
            elif char_code < ord('A'):
                char_code += 26

        # Do the same for lowercase characters
        else:
            if char_code > ord('z'):
                char_code -= 26
            elif char_code < ord('a'):
                char_code += 26

        # Convert from code to letter and add to message
        secret_message += chr(char_code)

    # If not a letter leave the character as is
    else:
        secret_message += char

print("Encrypted :", secret_message)

# To decrypt the only thing that changes is the sign of the key
key = -key

orig_message = ""

for char in secret_message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key

        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
            elif char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('z'):
                char_code -= 26
            elif char_code < ord('a'):
                char_code += 26

        orig_message += chr(char_code)

    else:
        orig_message += char

print("Decrypted :", orig_message)

# ---------- EXTRA HOMEWORK ----------
# For homework put the duplicate code above in a function











#~~Learn to program 5


# ---------- FUNCTION BASICS ----------

# Functions allow use to reuse code and make the code easier
# to understand

# To create a function type def (define) the function name
# and then in parentheses a comma separated list of values
# to pass if needed

def add_numbers(num_1, num2):

    # Return returns a value if needed
    return num_1 + num2

# You call the function by name followed by passing comma
# separated values if needed and a value may or may not be
# returned

print("5 + 4 =", add_numbers(5, 4))

# ---------- FUNCTION LOCAL VARIABLES ----------
# Any variable defined inside of a function is available only
# in that function

# ---------- EXAMPLE 1 ----------
# Variables created in a function can't be accessed outside
# of it

def assign_name():
    name = "Doug"

assign_name()

# Throws a NameError
# print(name)

# ---------- EXAMPLE 2 ----------

# You can't change a global variable even if it is passed
# into a function
def change_name(name):

    # Trying to change the global
    name = "Mark"

# A variable defined outside of a function can't be changed
# in the function using the above way
name = "Tom"

# Try to change the value
change_name(name)

# Prints Tom even though the function tries to change it
print(name)

# ---------- EXAMPLE 3 ----------

# If you want to change the value pass it back
def change_name_2():
    return "Mark"

name = change_name_2()

print(name)

# ---------- EXAMPLE 4 ----------
# You can also use the global statement to change it

gbl_name = "Sally"

def change_name_3():
    global gbl_name
    gbl_name = "Sammy"

change_name_3()

print(gbl_name)

# ---------- RETURNING NONE ----------
# If you don't return a value a function will return None

def get_sum(num1, num2):
    sum = num1 + num2

print(get_sum(5, 4))

# ---------- PROBLEM : SOLVE FOR X ----------
# Make a function that receives an algebraic equation like
# x + 4 = 9 and solve for x
# x will always be the 1st value received and you only
# will deal with addition

# Receive the string and split the string into variables
def solve_eq(equation):
    x, add, num1, equal, num2 = equation.split()

    # Convert the strings into ints
    num1, num2 = int(num1), int(num2)

    # Convert the result into a string and join (concatenate)
    # it to the string "x = "
    return "x = " + str(num2 - num1)

print(solve_eq("x + 4 = 9"))

# ---------- RETURN MULTIPLE VALUES ----------
# You can return multiple values with the return statement

def mult_divide(num1, num2):
    return (num1 * num2), (num1 / num2)

mult, divide = mult_divide(5, 4)

print("5 * 4 =", mult)
print("5 / 4 =", divide)

# ---------- RETURN A LIST OF PRIMES ----------
# A prime can only be divided by 1 and itself
# 5 is prime because 1 and 5 are its only positive factors
# 6 is a composite because it is divisible by 1, 2, 3 and 6

# We'll receive a request for primes up to the input value
# We'll then use a for loop and check if modulus == 0 for
# every value up to the number to check
# If modulus == 0 that means the number isn't prime

def isprime(num):
    # This for loop cycles through primes from 2 to
    # the value to check
    for i in range(2, num):

        # If any division has no remainder we know it
        # isn't a prime number
        if (num % i) == 0:
            return False
    return True


def getPrimes(max_number):

    # Create a list to hold primes
    list_of_primes = []

    # This for loop cycles through primes from 2 to
    # the maximum value requested
    for num1 in range(2, max_number):

        if isprime(num1):
            list_of_primes.append(num1)

    return list_of_primes

max_num_to_check = int(input("Search for Primes up to : "))

list_of_primes = getPrimes(max_num_to_check)

for prime in list_of_primes:
    print(prime)

# ---------- UNKNOWN NUMBER OF ARGUMENTS ----------
# We can receive an unknown number of arguments using
# the splat (*) operator

def sumAll(*args):

    sum = 0

    for i in args:
        sum += i

    return sum

print("Sum :", sumAll(1,2,3,4))

# ---------- pythontut2.py ----------

# We need this module for our program
import math

# Functions allow us to avoid duplicate code in our programs

# Aside from having to type code twice duplicate code is bad
# because it requires us to change multiple blocks of code
# if we need to make a change

# ---------- OUR FUNCTIONS ----------

# This routes to the correct area function
# The name of the value passed doesn't have to match
def get_area(shape):

    # Switch to lowercase for easy comparison
    shape = shape.lower()

    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Please enter rectangle or circle")

# Create function that calculates the rectangle area
def rectangle_area():
    length = float(input("Enter the length : "))
    width = float(input("Enter the width : "))

    area = length * width

    print("The area of the rectangle is", area)


# Create function that calculates the circle area
def circle_area():
    radius = float(input("Enter the radius : "))

    area = math.pi * (math.pow(radius, 2))

    # Format the output to 2 decimal places
    print("The area of the circle is {:.2f}".format(area))


# ---------- END OF OUR FUNCTIONS ----------

# We often place our main programming logic in a function called main
# We create it this way

def main():

    # Our program will calculate the area for rectangles or circles

    # Without functions we'd have to create a giant list of ifs, elifs

    # Ask the user what shape they have
    shape_type = input("Get area for what shape : ")

    # Call a function that will route to the correct function
    get_area(shape_type)

    # Because of functions it is very easy to see what is happening
    # For more detail just refer to the very short specific functions

# All of the function definitions are ignored and this calls for main()
# to execute when the program starts

main()

# ---------- HOMEWORK ----------
# Add the ability to calculate the area for parallelograms,
# rhombus, triangles, and trapezoids















#~~Learn to program 6


# ---------- LEARN TO PROGRAM 6 ----------

import random
import math

# With lists we can refer to groups of data with 1 name

# Each item in the list corresponds to a number (index)
# just like how people have identification numbers.
# By default the 1st item in a list has the index 0

# [0 : "string"] [1 : 1.234] [2 : 28] [3 : "c"]

# Python lists can grow in size and can contain data
# of any type

randList = ["string", 1.234, 28]

# Create a list with range
oneToTen = list(range(10))

# An awesome thing about lists is that you can use many
# of the same functions with them that you used with strings

# Combine lists
randList = randList + oneToTen

# Get the 1st item with an index
print(randList[0])

# Get the length
print("List Length :", len(randList))

# Slice a list to get 1st 3 items
first3 = randList[0:3]

# Cycle through the list and print the index
for i in first3:
    print("{} : {}".format(first3.index(i), i))

# You can repeat a list item with *
print(first3[0] * 3)

# You can see if a list contains an item
print("string" in first3)

# You can get the index of a matching item
print("Index of string :", first3.index("string"))

# Find out how many times an item is in the list
print("How many strings :", first3.count("string"))

# You can change a list item
first3[0] = "New String"

for i in first3:
    print("{} : {}".format(first3.index(i), i))

# Append a value to the end of a list
first3.append("Another")

# ---------- PROBLEM : CREATE A RANDOM LIST ----------
# Generate a random list of 5 values between 1 and 9
numList = []
for i in range(5):
    numList.append(random.randrange(1, 9))

# ---------- SORT A LIST : BUBBLE SORT ----------
# The Bubble sort is a way to sort a list
# It works this way
# 1. An outer loop decreases in size each time
# 2. The goal is to have the largest number at the end of
#    the list when the outer loop completes 1 cycle
# 3. The inner loop starts comparing indexes at the beginning
#    of the loop
# 4. Check if list[Index] > list[Index + 1]
# 5. If so swap the index values
# 6. When the inner loop completes the largest number is at
#    the end of the list
# 7. Decrement the outer loop by 1

# Create the value that will decrement for the outer loop
# Its value is the last index in the list
i = len(numList) - 1

while i > 1:

    j = 0

    while j < i:

        # Tracks the comparison of index values
        print("\nIs {} > {}".format(numList[j], numList[j+1]))
        print()

        # If the value on the left is bigger switch values
        if numList[j] > numList[j+1]:

            print("Switch")

            temp = numList[j]
            numList[j] = numList[j + 1]
            numList[j + 1] = temp

        else:
            print("Don't Switch")

        j += 1

        # Track changes to the list
        for k in numList:
            print(k, end=", ")
        print()

    print("END OF ROUND")

    i -= 1

for k in numList:
    print(k, end=", ")
print()

# ---------- MORE LIST FUNCTIONS ----------
numList = []
for i in range(5):
    numList.append(random.randrange(1, 9))

# Sort a list
numList.sort()

# Reverse a list
numList.reverse()

for k in numList:
    print(k, end=", ")
print()

# Insert value at index insert(index, value)
numList.insert(5, 10)

# Delete first occurrence of value
numList.remove(10)

for k in numList:
    print(k, end=", ")
print()

# Remove item at index
numList.pop(2)

for k in numList:
    print(k, end=", ")
print()

# ---------- LIST COMPREHENSIONS ----------
# You can construct lists in interesting ways using
# list comprehensions

# Perform an operation on each item in the list

# Create a list of even values
evenList = [i*2 for i in range(10)]

for k in evenList:
    print(k, end=", ")
print()

# List of lists containing values to the power of
# 2, 3, 4
numList = [1,2,3,4,5]

listOfValues = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)]
                for m in numList]

for k in listOfValues:
    print(k)
print()

# Create a 10 x 10 list
multiDList = [[0] * 10 for i in range(10)]

# Change a value in the multidimensional list
multiDList[0][1] = 10

# Get the 2nd item in the 1st list
# It may help to think of it as the 2nd item in the 1st row
print(multiDList[0][1])

# Get the 2nd item in the 2nd list
print(multiDList[1][1])

# ---------- MULTIDIMENSIONAL LIST ----------

# Show how indexes work with a multidimensional list
listTable = [[0] * 10 for i in range(10)]

for i in range(10):

    for j in range(10):
        listTable[i][j] = "{} : {}".format(i, j)

for i in range(10):

    for j in range(10):
        print(listTable[i][j], end=" || ")
    print()

# ---------- PROBLEM : CREATE MULTIPLICATION TABLE ----------
# With 2 for loops fill the cells in a multidimensional
# list with a multiplication table using values 1 - 9
'''
1, 2, 3, 4, 5, 6, 7, 8, 9,
2, 4, 6, 8, 10, 12, 14, 16, 18,
3, 6, 9, 12, 15, 18, 21, 24, 27,
4, 8, 12, 16, 20, 24, 28, 32, 36,
5, 10, 15, 20, 25, 30, 35, 40, 45,
6, 12, 18, 24, 30, 36, 42, 48, 54,
7, 14, 21, 28, 35, 42, 49, 56, 63,
8, 16, 24, 32, 40, 48, 56, 64, 72,
9, 18, 27, 36, 45, 54, 63, 72, 81
'''

# Create the multidimensional list
multTable = [[0] * 10 for i in range(10)]

# This will increment for each row
for i in range(1, 10):

    # This will increment for each item in the row
    for j in range(1, 10):

        # Assign the value to the cell
        multTable[i][j] = i * j

# Output the data in the same way you assigned it
for i in range(1, 10):

    for j in range(1, 10):
        print(multTable[i][j], end=", ")

    print()
















#~~Learn to program 7


# ---------- LEARN TO PROGRAM 7 ----------

# ---------- DICTIONARIES ----------

# While lists organize data based on sequential indexes
# Dictionaries instead use key / value pairs.

# A key / value pair could be
# fName : "Derek" where fName is the key and "Derek" is
# the value

# Create a Dictionary about me
derekDict = {"fName": "Derek", "lName": "Banas", "address": "123 Main St"}

# Get a value with the key
print("May name :", derekDict["fName"])

# Change a value with the key
derekDict["address"] = "215 North St"

# Dictionaries may not print out in the order created
# since they are unordered
print(derekDict)

# Add a new key value
derekDict['city'] = 'Pittsburgh'

# Check if a key exists
print("Is there a city :", "city" in derekDict)

# Get the list of values
print(derekDict.values())

# Get the list of keys
print(derekDict.keys())

# Get the key and value with items()
for k, v in derekDict.items():
    print(k, v)

# Get gets a value associated with a key or the default
print(derekDict.get("mName", "Not Here"))

# Delete a key value
del derekDict["fName"]

# Loop through the dictionary keys
for i in derekDict:
    print(i)

# Delete all entries
derekDict.clear()

# List for holding Dictionaries
employees = []

# Input employee data
fName, lName = input("Enter Employee Name : ").split()

employees.append({'fName': fName, 'lName': lName})

print(employees)


# ---------- PROBLEM : CREATE A CUSTOMER LIST ----------
# Create an array of customer dictionaries
# Output should look like this
'''
Enter Customer (Yes/No) : y
Enter Customer Name : Derek Banas
Enter Customer (Yes/No) : y
Enter Customer Name : Sally Smith
Enter Customer (Yes/No) : n
Derek Banas
Sally Smith
'''

# Create customer array outside the for so it isn't local
# to the while loop
customers = []

while True:

    # Cut off the 1st letter to cover if the user
    # types a n or y
    createEntry = input("Enter Customer (Yes/No) : ")
    createEntry = createEntry[0].lower()

    if createEntry == "n":

        # Leave the while loop when n is entered
        break
    else:

        # Get the customer name by splitting at the space
        fName, lName = input("Enter Customer Name : ").split()

        # Add the dictionary to the array
        customers.append({'fName': fName, 'lName': lName})

# Print out customer list
for cust in customers:
    print(cust['fName'], cust['lName'])

# ---------- RECURSIVE FUNCTIONS ----------
# A function that refers to itself is a recursive function

# Calculating factorials is commonly done with a recursive
# function 3! = 3 * 2 * 1

def factorial(num):

    # Every recursive function must contain a condition
    # when it ceases to call itself
    if num <= 1:
        return 1
    else:

        result = num * factorial(num - 1)
        return result

print(factorial(4))

# 1st : result = 4 * factorial(3) = 4 * 6 = 24
# 2nd : result = 3 * factorial(2) = 3 * 2 = 6
# 3rd : result = 2 * factorial(1) = 2 * 1 = 2

# ---------- PROBLEM : CALCULATE FIBONACCI NUMBERS ----------
# To calculate Fibonacci numbers we sum the 2 previous
# values to calculate the next item in the list like this
# 1, 1, 2, 3, 5, 8 ...

# The Fibonacci sequence is defined by:
# Fn = Fn-1 + Fn-2
# Where F0 = 0 and F1 = 1

'''
Sample Run Though to Help
print(fib(3))

# 1st : result = fib(2) + fib(1) : 2 + 1
# 2nd : result = (fib(1) + fib(0)) + (fib(0)) : 1 + 0
# 3rd : result = fib(2) + fib(1)

print(fib(4))

# 1st : result = fib(3) + fib(2) : 3 + 2
# 2nd : result = (fib(2) + fib(1)) + (fib(1) + fib(0)) : 2 + 1
# 3rd : result = (fib(1) + fib(0)) + fib(0) : 1 + 0
'''

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:

        result = fib(n-1) + fib(n-2)
        return result

print(fib(3))

print(fib(4))























#~~Learn to program 8



# ---------- READING & WRITING TEXT ----------

# The os module provides methods for file processing
import os

# We are able to store data for later use in files

# You can create or use an already created file with open

# If you use w (write) for mode then the file is
# overwritten.
# If you use a (append) you add to the end of the file

# Text is stored using unicode where numbers represent
# all possible characters

# We start the code with with which guarantees the file
# will be closed if the program crashes
with open("mydata.txt", mode="w", encoding="utf-8") as myFile:

    # You can write to the file with write
    # It doesn't add a newline
    myFile.write("Some random text\nMore random text\nAnd some more")


# Open the file for reading
# You don't have to provide a mode because it is
# read by default
with open("mydata.txt", encoding="utf-8") as myFile:

    # We can read data in a few ways
    # 1. read() reads everything into 1 string
    # 2. readline() reads everything including the first newline
    # 3. readlines() returns a list of every line which includes
    # each newline

    # Use read() to get everything at once
    print(myFile.read())

# Find out if the file is closed
print(myFile.closed)

# Get the file name
print(myFile.name)

# Get the access mode of the file
print(myFile.mode)

# Rename our file
os.rename("mydata.txt", "mydata2.txt")

# Delete a file
# os.remove("mydata.dat")

# Create a directory
# os.mkdir("mydir")

# Change directories
# os.chdir("mydir")

# Display current directory
print("Current Directory :", os.getcwd())

# Remove a directory, but 1st move back 1 directory
# os.chdir("..")
# os.rmdir("mydir")

# ---------- PROBLEM : Fibonacci sequence ----------
# Previously we generated 1 number in the
# Fibonacci sequence. This time ask the user to define
# how many numbers they want and display them
# The formula for calculating the Fibonacci sequence is
# Fn = Fn-1 + Fn-2
# Where F0 = 0 and F1 = 1

# Sample Output
'''
How many Fibonacci values should be found : 30
1
1
2
3
5
All Done
'''

def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        result = fib(num - 1) + fib(num - 2)
        return result

numFibValues = int(input("How many Fibonacci values should be found : "))

i = 1

# While i is less then the number of values requested
# continue to find more
while i < numFibValues:

    # Call the fib()
    fibValue = fib(i)

    print(fibValue)

    i += 1

print("All Done")


# ---------- READ ONE LINE AT A TIME ----------
# You can read 1 line at a time with readline()

# Open the file
with open("mydata2.txt", encoding="utf-8") as myFile:

    lineNum = 1

    # We'll use a while loop that loops until the data
    # read is empty
    while True:
        line = myFile.readline()

        # line is empty so exit
        if not line:
            break

        print("Line", lineNum, " :", line, end="")

        lineNum += 1

# ---------- PROBLEM : ANALYZE THE FILE ----------
# As you cycle through each line output the number of
# words and average word length
'''
Line 1
Number of Words : 3
Avg Word Length : 4.7
Line 2
Number of Words : 3
Avg Word Length : 4.7
'''

with open("mydata2.txt", encoding="utf-8") as myFile:

    lineNum = 1

    while True:
        line = myFile.readline()

        # line is empty so exit
        if not line:
            break

        print("Line", lineNum)

        # Put the words in a list using the space as
        # the boundary between words
        wordList = line.split()

        # Get the number of words with len()
        print("Number of Words :", len(wordList))

        # Incremented for each character
        charCount = 0

        for word in wordList:
            for char in word:
                charCount += 1

        # Divide to find the answer
        avgNumChars = charCount/len(wordList)

        # Use format to limit to 2 decimals
        print("Avg Word Length : {:.2}".format(avgNumChars))

        lineNum += 1

# ---------- TUPLES ----------
# A Tuple is like a list, but their values can't be changed
# Tuples are surrounded with parentheses instead of
# square brackets

myTuple = (1, 2, 3, 5, 8)

# Get a value with an index
print("1st Value :", myTuple[0])

# Get a slice from the 1st index up to but not including
# the 3rd
print(myTuple[0:3])

# Get the number of items in a Tuple
print("Tuple Length :", len(myTuple))

# Join or concatenate tuples
moreFibs = myTuple + (13, 21, 34)

# Check if a value is in a Tuple
print("34 in Tuple :", 34 in moreFibs)

# Iterate through a tuple
for i in moreFibs:
    print(i)

# Convert a List into a Tuple
aList = [55, 89, 144]
aTuple = tuple(aList)

# Convert a Tuple into a List
aList = list(aTuple)

# Get max and minimum value
print("Min :", min(aTuple))
print("Max :", max(aTuple))





















#~~Learn to program 9


# ---------- LEARN TO PROGRAM 9 ----------

# Real world objects have attributes and capabilities

# A dog for example has the attributes of height, weight
# favorite food, etc.

# It has the capability to run, bark, scratch, etc.

# In object oriented programming we model real world objects
# be defining the attributes (fields) and capabilities (methods)
# that they have.

# A class is the template used to model these objects
# Here we will model a Dog object

class Dog:

    # The init method is called to create an object
    # We give default values for the fields if none
    # are provided
    def __init__(self, name="", height=0, weight=0):

        # self allows an object to refer to itself
        # It is like how you refer to yourself with my

        # We will take the values passed in and assign
        # them to the new Dog objects fields (attributes)
        self.name = name
        self.height = height
        self.weight = weight

        # Define what happens when the Dog is asked to
        # demonstrate its capabilities

    def run(self):
        print("{} the dog runs".format(self.name))

    def eat(self):
        print("{} the dog eats".format(self.name))

    def bark(self):
        print("{} the dog barks".format(self.name))


def main():

    # Create a new Dog object
    spot = Dog("Spot", 66, 26)

    spot.bark()

    bowser = Dog()

main()


# ---------- GETTERS & SETTERS ----------
# Getters and Setters are used to protect our objects
# from assigning bad fields or for providing improved
# output

class Square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    # This is the getter
    @property
    def height(self):
        print("Retrieving the height")

        # Put a __ before this private field
        return self.__height

    # This is the setter
    @height.setter
    def height(self, value):

        # We protect the height from receiving a bad value
        if value.isdigit():

            # Put a __ before this private field
            self.__height = value
        else:
            print("Please only enter numbers for height")

    # This is the getter
    @property
    def width(self):
        print("Retrieving the width")
        return self.__width

    # This is the setter
    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for width")

    def getArea(self):
        return int(self.__width) * int(self.__height)


def main():
    aSquare = Square()

    height = input("Enter height : ")
    width = input("Enter width : ")

    aSquare.height = height
    aSquare.width = width

    print("Height :", aSquare.height)
    print("Width :", aSquare.width)

    print("The Area is :", aSquare.getArea())


main()

# ---------- WARRIORS BATTLE ----------
# We will create a game with this sample output
'''
Sam attacks Paul and deals 9 damage
Paul is down to 10 health
Paul attacks Sam and deals 7 damage
Sam is down to 7 health
Sam attacks Paul and deals 19 damage
Paul is down to -9 health
Paul has Died and Sam is Victorious
Game Over
'''

# We will create a Warrior & Battle class

import random
import math

# Warriors will have names, health, and attack and block maximums
# They will have the capabilities to attack and block random amounts
class Warrior:
    def __init__(self, name="warrior", health=0, attkMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax

    def attack(self):
        # Randomly calculate the attack amount
        # random() returns a value from 0.0 to 1.0
        attkAmt = self.attkMax * (random.random() + .5)

        return attkAmt

    def block(self):

        # Randomly calculate how much of the attack was blocked
        blockAmt = self.blockMax * (random.random() + .5)

        return blockAmt

# The Battle class will have the capability to loop until 1 Warrior dies
# The Warriors will each get a turn to attack each turn

class Battle:

    def startFight(self, warrior1, warrior2):

        # Continue looping until a Warrior dies switching back and
        # forth as the Warriors attack each other
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break

            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break

    # A function will receive each Warrior that will attack the other
    # Have the attack and block amounts be integers to make the results clean
    # Output the results of the fight as it goes
    # If a Warrior dies return that result to end the looping in the
    # above function

    # Make this method static because we don't need to use self
    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorAAttkAmt = warriorA.attack()

        warriorBBlockAmt = warriorB.block()

        damage2WarriorB = math.ceil(warriorAAttkAmt - warriorBBlockAmt)

        warriorB.health = warriorB.health - damage2WarriorB

        print("{} attacks {} and deals {} damage".format(warriorA.name,
                                                         warriorB.name, damage2WarriorB))

        print("{} is down to {} health".format(warriorB.name,
                                               warriorB.health))

        if warriorB.health <= 0:
            print("{} has Died and {} is Victorious".format(warriorB.name,
                                                            warriorA.name))

            return "Game Over"
        else:
            return "Fight Again"


def main():

    # Create 2 Warriors
    paul = Warrior("Paul", 50, 20, 10)
    sam = Warrior("Sam", 50, 20, 10)

    # Create Battle object
    battle = Battle()

    # Initiate Battle
    battle.startFight(paul, sam)

main()





















#~~Learn to program 10

# When we create a class we can inherit all of the fields and methods
# from another class. This is called inheritance.

# The class that inherits is called the subclass and the class we
# inherit from is the super class

# This will be our super class
class Animal:

    def __init__(self, birthType="Unknown",
                 appearance="Unknown",
                 blooded="Unknown"):
        self.__birthType = birthType
        self.__appearance = appearance
        self.__blooded = blooded

    # The getter method
    @property
    def birthType(self):

        # When using getters and setters don't forget the __
        return self.__birthType

    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    # Can be used to cast our object as a string
    # type(self).__name__ returns the class name
    def __str__(self):
        return "A {} is {} it is {} it is " \
                "{}".format(type(self).__name__,
                                              self.birthType,
                                              self.appearance,
                                              self.blooded)

# Create a Mammal class that inherits from Animal
# You can inherit from multiple classes by separating
# the classes with a comma in the parentheses
class Mammal(Animal):
    def __init__(self, birthType="born alive",
                 appearance="hair or fur",
                 blooded="warm blooded",
                 nurseYoung=True):

        # Call for the super class to initialize fields
        Animal.__init__(self, birthType,
                        appearance,
                        blooded)

        self.__nurseYoung = nurseYoung

    # We can extend the subclasses
    @property
    def nurseYoung(self):
        return self.__nurseYoung

    @nurseYoung.setter
    def appearance(self, nurseYoung):
        self.__nurseYoung = nurseYoung

    # Overwrite __str__
    # You can use super() to refer to the superclass
    def __str__(self):
        return super().__str__() + " and it is {} they nurse " \
            "their young".format(self.nurseYoung)


class Reptile(Animal):
    def __init__(self, birthType="born in an egg or born alive",
                 appearance="dry scales",
                 blooded="cold blooded"):

        # Call for the super class to initialize fields
        Animal.__init__(self, birthType,
                    appearance,
                    blooded)

    # Operator overloading isn't necessary in Python because
    # Python allows you to enter unknown numbers of values
    # Always make sure self is the first attribute in your
    # class methods
    def sumAll(self, *args):
        sum = 0

        for i in args:

            sum += i

        return sum


def main():
    animal1 = Animal("born alive")

    print(animal1.birthType)

    # Call __str__()
    print(animal1)
    print()

    mammal1 = Mammal()

    print(mammal1)

    print(mammal1.birthType)
    print(mammal1.appearance)
    print(mammal1.blooded)
    print(mammal1.nurseYoung)
    print()

    reptile1 = Reptile()

    print(reptile1.birthType)
    print(reptile1.appearance)
    print(reptile1.blooded)
    print()

    # Operator overloading in Python
    print("Sum : {}".format(reptile1.sumAll(1,2,3,4,5)))

    # Polymorphism in Python works differently from other
    # languages in that functions accept any object
    # and expect that object to provide the needed method

    # This isn't something to dwell on. Just know that
    # if you call on a method for an object that the
    # method just needs to exist for that object to work.
    # Polymorphism is a big deal in other languages that
    # are statically typed (type is defined at declaration)
    # but because Python is dynamically typed (type defined
    # when a value is assigned) it doesn't matter as much.

    def getBirthType(theObject):
        print("The {} is {}".format(type(theObject).__name__,
                                theObject.birthType))

    getBirthType(mammal1)
    getBirthType(reptile1)



main()

# ---------- MAGIC METHODS ----------
# Magic methods are surrounded by double underscores
# We can use magic methods to define how operators
# like +, -, *, /, ==, >, <, etc. will work with our
# custom objects

# Magic methods are used for operator overloading
# in Python

# __eq__ : Equal
# __ne__ : Not Equal
# __lt__ : Less Than
# __gt__ : Greater Than
# __le__ : Less Than or Equal
# __ge__ : Greater Than or Equal
# __add__ : Addition
# __sub__ : Subtraction
# __mul__ : Multiplication
# __div__ : Division
# __mod__ : Modulus

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    # Magic method that defines the string format of the object
    def __str__(self):

        # :02d adds a leading zero to have a minimum of 2 digits
        return "{}:{:02d}:{:02d}".format(self.hour,self.minute, self.second)

    def __add__(self, other_time):

        new_time = Time()

        # ---------- PROBLEM ----------
        # How would you go about adding 2 times together?

        # Add the seconds and correct if sum is >= 60
        if (self.second + other_time.second) >= 60:
            self.minute += 1
            new_time.second = (self.second + other_time.second) - 60
        else:
            new_time.second = self.second + other_time.second

        # Add the minutes and correct if sum is >= 60
        if (self.minute + other_time.minute) >= 60:
            self.hour += 1
            new_time.minute = (self.minute + other_time.minute) - 60
        else:
            new_time.minute = self.minute + other_time.minute

        # Add the minutes and correct if sum is > 60

        if (self.hour + other_time.hour) > 24:
            new_time.hour = (self.hour + other_time.hour) - 24
        else:
            new_time.hour = self.hour + other_time.hour

        return new_time


def main():
    time1 = Time(1, 20, 30)

    print(time1)

    time2 = Time(24, 41, 30)

    print(time1 + time2)

    # For homework get the Time objects to work for the other
    # mathematical and comparison operators



main()



















#~~Learn to program 11


# ---------- STATIC METHODS ----------

# Static methods allow access without the need to initialize
# a class. They should be used as utility methods, or when
# a method is needed, but it doesn't make sense for the real
# world object to be able to perform a task

class Sum:

    # You use the static method decorator to define that a
    # method is static
    @staticmethod
    def getSum(*args):

        sum = 0

        for i in args:
            sum += i

        return sum

def main():

    # Call a static method by proceeding it with its class
    # name
    print("Sum :", Sum.getSum(1,2,3,4,5))


main()


# ---------- STATIC VARIABLES ----------
# Fields declared in a class, but outside of any method
# are static variables. There value is shared by every
# object of that class

class Dog:

    # This is a static variable
    num_of_dogs = 0

    def __init__(self, name="Unknown"):
        self.name = name

        # You reference the static variable by proceeding
        # it with the class name
        Dog.num_of_dogs += 1

    @staticmethod
    def getNumOfDogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))

def main():

    spot = Dog("Spot")

    doug = Dog("Doug")

    spot.getNumOfDogs()


main()

# ---------- MODULES ----------
# Your Python programs will contain a main program that
# includes your main function. Then you will create many
# modules in separate files. Modules also end with .py
# just like any other Python file

# ————— sum.py —————
def getSum(*args):
    sum = 0

    for i in args:
        sum += i

    return sum

# ————— End of sum.py —————

# You can import by listing the file name minus the py
import sum

# Get access to functions by proceeding with the file
# name and then the function you want
print("Sum :", sum.getSum(1,2,3,4,5))

# ---------- FROM ----------

# You can use from to copy specific functions from a module
# You can use from sum import * to import all functions
# You can import multiple functions by listing them after
# import separated by commas
from sum import getSum

# You don't have to reference the module name now
print("Sum :", getSum(1,2,3,4,5))


# ---------- EXCEPTION HANDLING ----------
# Exceptions are triggered either when an error occurs
# or when you want them to.

# We use exceptions are used to handle errors, execute
# specific code when code generates something out of
# the ordinary, to always execute code when something
# happens (close a file that was opened),

# When an error occurs you stop executing code and jump
# to execute other code that responds to that error

# Let's handle an IndexError exception that is
# triggered when you try to access an index in a list
# that doesn't exist

# Surround a potential exception with try
try:
    aList = [1,2,3]

    print(aList[3])

# Catch the exception with except followed by the
# exception you want to catch

# You can catch multiple exceptions by separating them
# with commas inside parentheses
# except (IndexError, NameError):
except IndexError:
    print("Sorry that index doesn't exist")

# If the exception wasn't caught above this will
# catch all others
except:
    print("An unknown error occurred")

# ---------- CUSTOM EXCEPTIONS ----------

# Lets trigger an exception if the user enters a
# name that contains a number

# Although you won't commonly create your own exceptions
# this is how you do it

# Create a class that inherits from Exception
class DogNameError(Exception):

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

try:
    dogName = input("What is your dogs name : ")

    if any(char.isdigit() for char in dogName):

        # Raise your own exception
        # You can raise the built in exceptions as well
        raise DogNameError

except DogNameError:
    print("Your dogs name can't contain a number")

# ---------- FINALLY & ELSE ----------
# finally is used when you always want certain code to
# execute whether an exception is raised or not

num1, num2 = input("Enter to values to divide : ").split()

try:
    quotient = int(num1) / int(num2)
    print("{} / {} = {}".format(num1, num2, quotient))

except ZeroDivisionError:
    print("You can't divide by zero")

# else is only executed if no exception was raised
else:
    print("You didn't raise an exception")

finally:
    print("I execute no matter what")

# ---------- PROBLEM EXCEPTIONS & FILES ----------
# 1. Create a file named mydata2.txt and put data in it
# 2. Using what you learned in part 8 and Google to find
# out how to open a file without with try to open the
# file in a try block
# 3. Catch the FileNotFoundError exception
# 4. In else print the file contents
# 5. In finally close the file
# 6. Try to open the nonexistent file mydata3.txt and
# test to see if you caught the exception

try:
    myFile = open("mydata2.txt", encoding="utf-8")

# We can use as to access data and methods in the
# exception class
except FileNotFoundError as ex:
    print("That file was not found")

    # Print out further data on the exception
    print(ex.args)

else:
    print("File :", myFile.read())
    myFile.close()

finally:
    print("Finished Working with File")































#~~Learn to program 12


# ---------- ADVANCED FUNCTIONS ----------

# ---------- FUNCTIONS AS OBJECTS ----------

def mult_by_2(num):
    return num * 2

# A function can be
# 1. Assigned to another name

times_two = mult_by_2

print("4 * 2 =", times_two(4))

# 2. Passed into other functions

def do_math(func, num):

    return func(num)

print("8 * 2 =", do_math(mult_by_2, 8))

# 3. Returned from a function

def get_func_mult_by_num(num):

    # Create a dynamic function that will receive a value
    # and then return that value times the value passed
    # into getFuncMultByNum()
    def mult_by(value):
        return num * value

    return mult_by

generated_func = get_func_mult_by_num(5)

print("5 * 10 =", generated_func(10))

# 4. Embedded in a data structure

listOfFuncs = [times_two, generated_func]

print("5 * 9 =", listOfFuncs[1](9))

# ---------- PROBLEM ----------
# Create a function that receives a list and a function
# The function passed will return True or False if a list
# value is odd.
# The surrounding function will return a list of odd
# numbers

def is_it_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def change_list(list, func):

    oddList = []

    for i in list:
        if func(i):
            oddList.append(i)

    return oddList

aList = range(1, 21)

print(change_list(aList, is_it_odd))


# ---------- FUNCTION ANNOTATIONS ----------
# It is possible to define the data types of attributes
# and the returned value with annotations, but they have
# no impact on how the function operates, but instead
# are for documentation

def random_func(name: str, age: int, weight: float) -> str:
    print("Name :", name)
    print("Age :", age)
    print("Weight :", weight)

    return "{} is {} years old and weighs {}".format(name, age, weight)

print(random_func("Derek", 41, 165.5))

# You don't get an error if you pass bad data
print(random_func(89, "Derek", "Turtle"))

# You can print the annotations
print(random_func.__annotations__)

# ---------- ANONYMOUS FUNCTIONS : LAMBDA ----------
# lambda is like def, but rather then assign the function
# to a name it just returns it. Because there is no name
# that is why they are called anonymous functions. You
# can however assign a lambda function to a name.

# This is their format
# lambda arg1, arg2,... : expression using the args

# lambdas are used when you need a small function, but
# don't want to junk up your code with temporary
# function names that may cause conflicts

# Add values
sum = lambda x, y : x + y

print("Sum :", sum(4, 5))

# Use a ternary operator to see if someone can vote
can_vote = lambda age: True if age >= 18 else False

print("Can Vote :", can_vote(16))

# Create a list of functions
powerList = [lambda x: x ** 2,
             lambda x: x ** 3,
             lambda x: x ** 4]

# Run each function on a value
for func in powerList:
    print(func(4))


# You can also store lambdas in dictionaires

attack = {'quick': (lambda: print("Quick Attack")),
           'power': (lambda: print("Power Attack")),
           'miss': (lambda: print("The Attack Missed"))}

attack['quick']()

# You could get a random dictionary as well for say our
# previous warrior objects
import random

# keys() returns an iterable so we convert it into a list
# choice() picks a random value from that list
attackKey = random.choice(list(attack.keys()))

attack[attackKey]()

# ---------- PROBLEM ----------
# Create a random list filled with the characters H and T
# for heads and tails. Output the number of Hs and Ts
# Example Output
# Heads :  46
# Tails :  54

# Create the list
flipList = []

# Populate the list with 100 Hs and Ts
# Trick : random.choice() returns a random value from the list
for i in range(1, 101):
    flipList += random.choice(['H', 'T'])

# Output results
print("Heads : ", flipList.count('H'))
print("Tails : ", flipList.count('T'))


# ---------- MAP ----------
# Map allows us to execute a function on each item in a list

# Generate a list from 1 to 10
oneTo10 = range(1, 11)

# The function to pass into map
def dbl_num(num):
    return num * 2

# Pass in the function and the list to generate a new list
print(list(map(dbl_num, oneTo10)))

# You could do the same thing with a lambda
print(list(map((lambda x: x * 3), oneTo10)))

# You can perform calculations against multiple lists
aList = list(map((lambda x, y: x + y), [1, 2, 3], [1, 2, 3]))
print(aList)

# ---------- FILTER ----------
# Filter selects items from a list based on a function

# Print out the even values from a list
print(list(filter((lambda x: x % 2 == 0), range(1, 11))))

# ---------- PROBLEM ----------
# Find the multiples of 9 from a random 100 value list with
# values between 1 and 1000

# Generate a random list with randint between 1 and 1000
# Use range to generate 100 values
randList = list(random.randint(1, 1001) for i in range(100))

# Use modulus to find multiples of 9 by passing the random
# list to filter
print(list(filter((lambda x: x % 9 == 0), randList)))


# ---------- REDUCE ----------
# Reduce receives a list and returns a single result

# You must import reduce
from functools import reduce

# Add up the values in a list
print(reduce((lambda x, y: x + y), range(1, 6)))


























#~~Learn to program 13


# ---------- ITERABLES ----------
# An iterable is a stored sequence of values (list) or,
# as we will see when we cover generators, an
# object that produces one value at a time

# Iterables differ from iterators in that an iterable
# is an object with an __iter__ method which returns
# an iterator. An iterator is an object with a
# __next__ method which retrieves the next value from
# sequence of values

# Define a string and convert it into an iterator
sampStr = iter("Sample")

print("Char :", next(sampStr))
print("Char :", next(sampStr))

# You can add iterator behavior to your classes
class Alphabet:

    def __init__(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.letters) - 1:
            raise StopIteration
        self.index += 1
        return self.letters[self.index]

alpha = Alphabet()

for letter in alpha:
    print(letter)

# Iterate through a dictionary because it is an iterable
derek = {"fName": "Derek", "lName": "Banas"}

for key in derek:
    print(key, derek[key])

# ---------- PROBLEM ----------
# Create a class that returns values from the Fibonacci
# sequence each time next is called
# Sample Output
# Fib : 1
# Fib : 2
# Fib : 3
# Fib : 5

class FibGenerator:

    def __init__(self):
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        fibNum = self.first + self.second
        self.first = self.second
        self.second = fibNum
        return fibNum

fibSeq = FibGenerator()

for i in range(10):
    print("Fib :", next(fibSeq))

# ---------- LIST COMPREHENSIONS ----------
# A list comprehension executes an expression against an iterable

# Note: While they are super powerful, try not to make list
# comprehensions that are hard to figure out for others

# To multiply 2 times every value with a map we'd do
print(list(map((lambda x: x * 2), range(1, 11))))

# With a list comprehension we'd do
# Note that a list comprehension is surrounded by []
# because it returns a list
print([2 * x for x in range(1, 11)])

# To construct a list of odds using filter we'd
print(list(filter((lambda x: x % 2 != 0), range(1, 11))))

# To do the same with a list comprehension
print([x for x in range(1, 11) if x % 2 != 0])

# A list comprehension can act as map and filter
# on one line
# Generate a list of 50 values and take them to the power
# of 2 and return all that are multiples of 8

print([i ** 2 for i in range(50) if i % 8 == 0])

# You can have multiple for loops as well
# Multiply all values in one list times all values in
# another
print([x * y for x in range(1, 3) for y in range(11, 16)])

# You can put list comprehensions in list comprehensions
# Generate a list of 10 values, multiply them by 2 and
# return multiples of 8
print([x for x in [i * 2 for i in range(10)] if x % 8 == 0])

# ---------- PROBLEM ----------
# Generate a list of 50 random values between 1 and 1000
# and return those that are multiples of 9
# You'll have to use a list comprehension in a list comprehension
# This is a hard one!

import random

print([x for x in [random.randint(1, 1001) for i in range(50)] if x % 9 == 0])

# List comprehensions also make it easy to work with
# multidimensional lists

multiList = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

print([col[1] for col in multiList])

# Get the diagonal by incrementing 0, 0 -> 1, 1 -> 2, 2
print([multiList[i][i] for i in range(len(multiList))])

# ---------- GENERATOR FUNCTIONS ----------
# A generator function returns a result generator when called
# They can be suspended and resumed during execution of
# your program to create results over time rather then
# all at once

# We use generators when we want to big result set, but
# we don't want to slow down the program by creating
# it all at one time

# Create a generator that calculates primes and returns
# the next prime on command

def isprime(num):
    # This for loop cycles through primes from 2 to
    # the value to check
    for i in range(2, num):

        # If any division has no remainder we know it
        # isn't a prime number
        if (num % i) == 0:
            return False
    return True

# This is the generator
def gen_primes(max_number):

    # This for loop cycles through primes from 2 to
    # the maximum value requested
    for num1 in range(2, max_number):

        if isprime(num1):

            # yield is what makes this a generator
            # When called by next it will return the
            # next result
            yield num1

# Create a reference to the generator
prime = gen_primes(50)

# Call next for each result
print("Prime :", next(prime))
print("Prime :", next(prime))
print("Prime :", next(prime))

# ---------- GENERATOR EXPRESSIONS ----------
# Generator expressions look just like list comprehensions
# but they return results one at a time
# The are surrounded by parentheses instead of [ ]

double = (x * 2 for x in range(10))

print("Double :", next(double))
print("Double :", next(double))

# You can iterate through all results as well
for num in double:
    print(num)























#~~Learn to program 14



# When you use threads it is like you are running
# multiple programs at once.

# Threads actually take turns executing. While one
# executes the other sleeps until it is its turn
# to execute.

import threading
import time
import random

def executeThread(i):

    # strftime or string formatted time allows you to
    # define how the time is displayed.
    # You could include the date with
    # strftime("%Y-%m-%d %H:%M:%S", gmtime())

    # Print when the thread went to sleep
    print("Thread {} sleeps at {}".format(i,
                    time.strftime("%H:%M:%S", time.gmtime())))

    # Generate a random sleep period of between 1 and
    # 5 seconds
    randSleepTime = random.randint(1, 5)

    # Pauses execution of code in this function for
    # a few seconds
    time.sleep(randSleepTime)

    # Print out info after the sleep time
    print("Thread {} stops sleeping at {}".format(i,
                    time.strftime("%H:%M:%S", time.gmtime())))

for i in range(10):

    # Each time through the loop a Thread object is created
    # You pass it the function to execute and any
    # arguments to pass to that method
    # The arguments passed must be a sequence which
    # is why we need the comma with 1 argument
    thread = threading.Thread(target=executeThread, args=(i,))
    thread.start()

    # Display active threads
    # The extra 1 is this for loop executing in the main
    # thread
    print("Active Threads :", threading.activeCount())

    # Returns a list of all active thread objects
    print("Thread Objects :", threading.enumerate())


# ---------- SUBCLASSING THREAD ----------
# You can subclass the Thread object and then define
# what happens each time a new thread is executed
# or run

class CustThread(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)

        self.name = name

    def run(self):

        getTime(self.name)

        print("Thread", self.name, "Execution Ends")

def getTime(name):
    print("Thread {} sleeps at {}".format(name,
                    time.strftime("%H:%M:%S", time.gmtime())))

    randSleepTime = random.randint(1, 5)

    time.sleep(randSleepTime)

# Create thread objects
thread1 = CustThread("1")
thread2 = CustThread("2")

# Start thread execution of run()
thread1.start()
thread2.start()

# Check if thread is alive
print("Thread 1 Alive :", thread1.is_alive())
print("Thread 2 Alive :", thread2.is_alive())

# Get thread name
# You can change it with setName()
print("Thread 1 Name :", thread1.getName())
print("Thread 2 Name :", thread2.getName())

# Wait for threads to exit
thread1.join()
thread2.join()

print("Execution Ends")


# ---------- SYNCHRONIZING THREADS ----------
# You can lock other threads from executing

# If we try to model a bank account we have to make sure
# the account is locked down during a transaction so
# that if more then 1 person tries to withdrawal money at
# once we don't give out more money then is in the account

class BankAccount (threading.Thread):

    acctBalance = 100

    def __init__(self, name, moneyRequest):
        threading.Thread.__init__(self)
        self.name = name
        self.moneyRequest = moneyRequest

    def run(self):
        # Get lock to keep other threads from accessing the account
        threadLock.acquire()

        # Call the static method
        BankAccount.getMoney(self)

        # Release lock so other thread can access the account
        threadLock.release()

    @staticmethod
    def getMoney(customer):
        print("{} tries to withdrawal ${} at {}".format(customer.name,
                customer.moneyRequest,
                time.strftime("%H:%M:%S", time.gmtime())))

        if BankAccount.acctBalance - customer.moneyRequest > 0:
            BankAccount.acctBalance -= customer.moneyRequest
            print("New account balance is : ${}".format(BankAccount.acctBalance))
        else:
            print("Not enough money in the account")
            print("Current balance : ${}".format(BankAccount.acctBalance))

        time.sleep(3)

# Create a lock to be used by threads
threadLock = threading.Lock()

# Create new threads
doug = BankAccount("Doug", 1)
paul = BankAccount("Paul", 100)
sally = BankAccount("Sally", 50)

# Start new Threads
doug.start()
paul.start()
sally.start()

# Have threads wait for previous threads to terminate
doug.join()
paul.join()
sally.join()

print("Execution Ends")


































#~~Learn to program 15


# Regular expressions allow you to locate and change
# strings in very powerful ways.
# They work in almost exactly the same way in every
# programming language as well.

# Regular Expressions (Regex) are used to
# 1. Search for a specific string in a large amount of data
# 2. Verify that a string has the proper format (Email, Phone #)
# 3. Find a string and replace it with another string
# 4. Format data into the proper form for importing for example

# import the Regex module
import re

# ---------- Was a Match Found ----------

# Search for ape in the string
if re.search("ape", "The ape was at the apex"):
    print("There is an ape")

# ---------- Get All Matches ----------

# findall() returns a list of matches
# . is used to match any 1 character or space
allApes = re.findall("ape.", "The ape was at the apex")

for i in allApes:
    print(i)

# finditer returns an iterator of matching objects
# You can use span to get the location

theStr = "The ape was at the apex"

for i in re.finditer("ape.", theStr):

    # Span returns a tuple
    locTuple = i.span()

    print(locTuple)

    # Slice the match out using the tuple values
    print(theStr[locTuple[0]:locTuple[1]])

# ---------- Match 1 of Several Letters ----------

# Square brackets will match any one of the characters between
# the brackets not including upper and lowercase varieties
# unless they are listed

animalStr = "Cat rat mat fat pat"

allAnimals = re.findall("[crmfp]at", animalStr)
for i in allAnimals:
    print(i)

print()

# We can also allow for characters in a range
# Remember to include upper and lowercase letters
someAnimals = re.findall("[c-mC-M]at", animalStr)
for i in someAnimals:
    print(i)

print()

# Use ^ to denote any character but whatever characters are
# between the brackets
someAnimals = re.findall("[^Cr]at", animalStr)
for i in someAnimals:
    print(i)

print()

# ---------- Replace All Matches ----------

# Replace matching items in a string

owlFood = "rat cat mat pat"

# You can compile a regex into pattern objects which
# provide additional methods
regex = re.compile("[cr]at")

# sub() replaces items that match the regex in the string
# with the 1st attribute string passed to sub
owlFood = regex.sub("owl", owlFood)

print(owlFood)

# ---------- Solving Backslash Problems ----------

# Regex use the backslash to designate special characters
# and Python does the same inside strings which causes
# issues.

# Let's try to get "\\stuff" out of a string

randStr = "Here is \\stuff"

# This won't find it
print("Find \\stuff : ", re.search("\\stuff", randStr))

# This does, but we have to put in 4 slashes which is
# messy
print("Find \\stuff : ", re.search("\\\\stuff", randStr))

# You can get around this by using raw strings which
# don't treat backslashes as special
print("Find \\stuff : ", re.search(r"\\stuff", randStr))

# ---------- Matching Any Character ----------
# We saw that . matches any character, but what if we
# want to match a period. Backslash the period
# You do the same with [, ] and others

randStr = "F.B.I. I.R.S. CIA"

print("Matches :", len(re.findall(".\..\..", randStr)))

# ---------- Matching Whitespace ----------
# We can match many whitespace characters

randStr = """This is a long
string that goes
on for many lines"""

print(randStr)

# Remove newlines
regex = re.compile("\n")

randStr = regex.sub(" ", randStr)

print(randStr)

# You can also match
# \b : Backspace
# \f : Form Feed
# \r : Carriage Return
# \t : Tab
# \v : Vertical Tab

# You may need to remove \r\n on Windows

# ---------- Matching Any Single Number ----------
# \d can be used instead of [0-9]
# \D is the same as [^0-9]

randStr = "12345"

print("Matches :", len(re.findall("\d", randStr)))

# ---------- Matching Multiple Numbers ----------
# You can match multiple digits by following the \d with {numOfValues}

# Match 5 numbers only
if re.search("\d{5}", "12345"):
    print("It is a zip code")

# You can also match within a range
# Match values that are between 5 and 7 digits
numStr = "123 12345 123456 1234567"

print("Matches :", len(re.findall("\d{5,7}", numStr)))

# ---------- Matching Any Single Letter or Number ----------
# \w is the same as [a-zA-Z0-9_]
# \W is the same as [^a-zA-Z0-9_]

phNum = "412-555-1212"

# Check if it is a phone number
if re.search("\w{3}-\w{3}-\w{4}", phNum):
    print("It is a phone number")

# Check for valid first name between 2 and 20 characters
if re.search("\w{2,20}", "Ultraman"):
    print("It is a valid name")

# ---------- Matching WhiteSpace ----------
# \s is the same as [\f\n\r\t\v]
# \S is the same as [^\f\n\r\t\v]

# Check for valid first and last name with a space
if re.search("\w{2,20}\s\w{2,20}", "Toshio Muramatsu"):
    print("It is a valid full name")

# ---------- Matching One or More ----------
# + matches 1 or more characters

# Match a followed by 1 or more characters
print("Matches :", len(re.findall("a+", "a as ape bug")))

# ---------- Problem ----------
# Create a Regex that matches email addresses from a list
# 1. 1 to 20 lowercase and uppercase letters, numbers, plus ._%+-
# 2. An @ symbol
# 3. 2 to 20 lowercase and uppercase letters, numbers, plus .-
# 4. A period
# 5. 2 to 3 lowercase and uppercase letters

emailList = "db@aol.com m@.com @apple.com db@.com"

print("Email Matches :", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}",
                                        emailList)))
























#~~Learn to program 16


import re

# Did you find a match
# if re.search("REGEX", yourString)

# Get list of matches
# print("Matches :", len(re.findall("REGEX", yourString)))

# Get a pattern object
# regex = re.compile("REGEX")

# Substitute the match
# yourString = regex.sub("substitution", yourString)

# [ ]   : Match what is in the brackets
# [^ ]  : Match anything not in the brackets
# .     : Match any 1 character or space
# +     : Match 1 or more of what proceeds
# \n    : Newline
# \d    : Any 1 number
# \D    : Anything but a number
# \w    : Same as [a-zA-Z0-9_]
# \W    : Same as [^a-zA-Z0-9_]
# \s    : Same as [\f\n\r\t\v]
# \S    : Same as [^\f\n\r\t\v]
# {5}   : Match 5 of what proceeds the curly brackets
# {5,7} : Match values that are between 5 and 7 in length

# ---------- Matching Zero or One ----------

randStr = "cat cats"

regex = re.compile("[cat]+s?")

matches = re.findall(regex, randStr)

# Match cat or cats
print("Matches :", len(matches))

for i in matches:
    print(i)

# ---------- Matching Zero or More ----------
# * matches zero or more of what proceeds it

randStr = "doctor doctors doctor's"

# Match doctor doctors or doctor's
regex = re.compile("[doctor]+['s]*")

matches = re.findall(regex, randStr)

print("Matches :", len(matches))

# You can do the same by setting an interval match
regex = re.compile("[doctor]+['s]{0,2}")

matches = re.findall(regex, randStr)

print("Matches :", len(matches))

for i in matches:
    print(i)

# ---------- PROBLEM ----------
# On Windows newlines are some times \n and other times \r\n
# Create a regex that will grab each of the lines in this
# string, print out the number of matches and each line

longStr = '''Just some words
and some more\r
and more
'''

print("Matches :", len(re.findall(r"[\w\s]+[\r]?\n", longStr)))

matches = re.findall("[\w\s]+[\r]?\n", longStr)

for i in matches:
    print(i)

# ---------- Greedy & Lazy Matching ----------

randStr = "<name>Life On Mars</name><name>Freaks and Geeks</name>"

# Let's try to grab everything between <name> tags
# Because * is greedy (It grabs the biggest match possible)
# we can't get what we want, which is each individual tag
# match
regex = re.compile(r"<name>.*</name>")

matches = re.findall(regex, randStr)

print("Matches :", len(matches))

for i in matches:
    print(i)

# We want to grab the smallest match we use *?, +?, or
# {n,}? instead

regex = re.compile(r"<name>.*?</name>")

matches = re.findall(regex, randStr)

print("Matches :", len(matches))

for i in matches:
    print(i)

# ---------- Word Boundaries ----------
# We use word boundaries to define where our matches start
# and end

# \b matches the start or end of a word

# If we want ape it will match ape and the beginning of apex
randStr = "ape at the apex"

regex = re.compile(r"ape")

# If we use the word boundary
regex = re.compile(r"\bape\b")

matches = re.findall(regex, randStr)

print("Matches :", len(matches))

for i in matches:
    print(i)

# ---------- String Boundaries ----------
# ^ : Matches the beginning of a string if outside of
#     a [ ]
# $ : Matches the end of a string

# Grab everything from the start of the string to @
randStr = "Match everything up to @"

regex = re.compile(r"^.*[^@]")

matches = re.findall(regex, randStr)

print("Matches :", len(matches))

for i in matches:
    print(i)

# Grab everything from @ to the end of the line
randStr = "@ Get this string"

regex = re.compile(r"[^@\s].*$")

matches = re.findall(regex, randStr)

print("Matches :", len(matches))

for i in matches:
    print(i)

# Grab the 1st word of each line using the the multiline
# code which allows for the targeting of each line after
# a line break with ^
randStr = '''Ape is big
Turtle is slow
Cheetah is fast'''

regex = re.compile(r"(?m)^.*?\s")

matches = re.findall(regex, randStr)

print("Matches :", len(matches))

for i in matches:
    print(i)

# ---------- Subexpressions ----------
# Subexpressions are parts of a larger expression
# If you want to match for a large block, but
# only want to return part of it. To do that
# surround what you want with ( )

# Get just the number minus the area code
randStr = "My number is 412-555-1212"

regex = re.compile(r"412-(.*)")

matches = re.findall(regex, randStr)

print("Matches :", len(matches))

for i in matches:
    print(i)

# ---------- Problem ----------

# Get just the numbers minus the area codes from
# this string
randStr = "412-555-1212 412-555-1213 412-555-1214"

regex = re.compile(r"412-(.{8})")

matches = re.findall(regex, randStr)

print("Matches :", len(matches))

for i in matches:
    print(i)

# ---------- Multiple Subexpressions ----------

# You can have multiple subexpressions as well
# Get both numbers that follow 412 separately
randStr = "My number is 412-555-1212"

regex = re.compile(r"412-(.*)-(.*)")

matches = re.findall(regex, randStr)

print("Matches :", len(matches))

print(matches[0][0])
print(matches[0][1])




































#~~Learn to program 17


import re

# Did you find a match
# if re.search("REGEX", yourString)

# Get list of matches
# print("Matches :", len(re.findall("REGEX", yourString)))

# Get a pattern object
# regex = re.compile("REGEX")

# Substitute the match
# yourString = regex.sub("substitution", yourString)

# [ ]   : Match what is in the brackets
# [^ ]  : Match anything not in the brackets
# ( )   : Return surrounded submatch
# .     : Match any 1 character or space
# +     : Match 1 or more of what proceeds
# ?     : Match 0 or 1
# *     : Match 0 or More
# *?    : Lazy match the smallest match
# \b    : Word boundary
# ^     : Beginning of String
# $     : End of String
# \n    : Newline
# \d    : Any 1 number
# \D    : Anything but a number
# \w    : Same as [a-zA-Z0-9_]
# \W    : Same as [^a-zA-Z0-9_]
# \s    : Same as [\f\n\r\t\v]
# \S    : Same as [^\f\n\r\t\v]
# {5}   : Match 5 of what proceeds the curly brackets
# {5,7} : Match values that are between 5 and 7 in length
# ($m)  : Allow ^ on multiline string

# ---------- Back References ----------
# A back reference allows you to to reuse the expression
# that proceeds it

# Grab a double word
randStr = "The cat cat fell out the window"

# Match a word boundary, 1 or more characters followed
# by a space if it is then followed by the same
# match that is surrounded by the parentheses
regex = re.compile(r"(\b\w+)\s+\1")

matches = re.findall(regex, randStr)

print("Matches :", len(matches))

for i in matches:
    print(i)

# ---------- Back Reference Substitutions ----------

# Replace the bold tags in the link with no tags
randStr = "<a href='#'><b>The Link</b></a>"

# Regex matches bold tags and grabs the text between
# them to be used by the back reference
regex = re.compile(r"<b>(.*?)</b>")

# Replace the tags with just the text between them
randStr = re.sub(regex, r"\1", randStr)

print(randStr)

# ---------- Another Back Reference Substitution ----------

# Receive this string
randStr = "412-555-1212"

# Match the phone number using multiple subexpressions
regex = re.compile(r"([\d]{3})-([\d]{3}-[\d]{4})")

# Output (412)555-1212
randStr = re.sub(regex, r"(\1)\2", randStr)

print(randStr)

# ---------- PROBLEM ----------
# Receive a string like this

randStr = "https://www.youtube.com http://www.google.com"

# Grab the URL and then provide the following output
# using a back reference substitution
# <a href='https://www.youtube.com'>www.youtube.com</a>
# <a href='https://www.google.com'>www.google.com</a>

regex = re.compile(r"(https?://([\w.]+))")

randStr = re.sub(regex, r"<a href='\1'>\2</a>\n", randStr)

print(randStr)

# ---------- Look Ahead ----------
# A look ahead defines a pattern to match but not return
# You define the expression to look for but not return
# like this (?=expression)

randStr = "One two three four"

# Grab all letters and numbers of 1 or more separated
# by a word boundary but don't include it
regex = re.compile(r"\w+(?=\b)")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)

# ---------- Look Behind ----------
# The look behind looks for what is before the text
# to return, but doesn't return it
# It is defined like (?<=expression)

randStr = "1. Bread 2. Apples 3. Lettuce"

# Find the number, period and space, but only return
# the 1 or more letters or numbers that follow
regex = re.compile(r"(?<=\d.\s)\w+")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)

# ---------- Look Ahead & Behind ----------

randStr = "<h1>I'm Important</h1> <h1>So am I</h1>"

# Use the look behind, get 1 or more of anything,
# and use the look ahead
regex = re.compile(r"(?<=<h1>).+?(?=</h1>)")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)

import re

# ---------- Negative Look Ahead & Behind ----------
# These are used to look for text that doesn't match
# the pattern

# (?!expression) : Negative Look Ahead
# (?<!expression) : Negative Look Behind

randStr = "8 Apples $3, 1 Bread $1, 1 Cereal $4"

# Grab the total number of grocery items by ignoring the $
regex = re.compile(r"(?<!\$)\d+")

matches = re.findall(regex, randStr)

print(len(matches))

# Convert from a string list to an int list
matches = [int(i) for i in matches]

from functools import reduce

# Sum the items in the list with reduce
print("Total Items {}".format(reduce((lambda x, y: x + y), matches)))






























































































































































#~~Learn to program 20 TKinter



# We are going to learn how to create Graphical User
# Interfaces (GUIs) with Tk

# Tk is a cross platform GUI toolkit that provides a
# ton of Widgets (Buttons, Scrollbars, etc.) that are
# used to build GUIs

# TkInter (tee-kay-inter) is included since Python 3.1 on Macs,
# Windows and Linux

# TkInter is a Python interface for Tk
from tkinter import *
from tkinter import ttk

# Test to see if TkInter is working
# tkinter._test()

# ---------- HELLO WORLD  ----------

# root is the main window that surrounds your interface
# This creates a Tk object
root = Tk()

# Give your app a title
root.title("First GUI")

# Put a button in the window
# Components like button are called Widgets
ttk.Button(root, text="Hello TkInter").grid()

# This keeps the root window visible and your program
# running
root.mainloop()


# ---------- MULTIPLE COMPONENTS  ----------
# Some of the different Widgets : Button, Label,
# Canvas, Menu, Text, Scale, OptionMenu, Frame,
# CheckButton, LabelFrame, MenuButton, PanedWindow,
# Entry, ListBox, Message, RadioButton, ScrollBar,
# Bitmap, SpinBox, Image

root = Tk()

# Frame widgets surround other widgets
frame = Frame(root)

# We'll use a TkInter variable for our label text
# so we can change it with set
labelText = StringVar()

# Create a label and button object
# You can set attributes on creation or by calling
# methods

label = Label(frame, textvariable=labelText)
button = Button(frame, text="Click Me")

# Change the label text
labelText.set("I am a label")

# Pack positions the widgets in the window
# It is a simple geometry manager
label.pack()
button.pack()
frame.pack()

root.mainloop()



# ---------- PACK GEOMETRY MANAGER  ----------
# Pack positions widgets by allowing them to define
# their position (Top, Right, Bottom, Left) and
# their fill direction (X, Y, BOTH, NONE) inside
# of a box

root = Tk()

frame = Frame(root)

# Define where the widgets should be placed and
# how they should be stretched to fill the space
Label(frame, text="A Bunch of Buttons").pack()
Button(frame, text="B1").pack(side=LEFT, fill=Y)
Button(frame, text="B2").pack(side=TOP, fill=X)
Button(frame, text="B3").pack(side=RIGHT, fill=X)
Button(frame, text="B4").pack(side=LEFT, fill=X)

frame.pack()

root.mainloop()


# ---------- GRID GEOMETRY MANAGER  ----------
# The Grid manager is the most useful using a series
# of rows and columns for laying out widgets

# Each cell can only hold 1 widget, but a widget
# can cover multiple cells.

root = Tk()

# rows start at 0, 1, ...
# columns start at 0, 1, ...
# sticky defines how the widget expands (N, NE, E, SE,
# S, SW, W, NW)
# padx and pady provide padding around the widget above
# and below it
Label(root, text="First Name").grid(row=0, sticky=W, padx=4)
Entry(root).grid(row=0, column=1, sticky=E, pady=4)

Label(root, text="Last Name").grid(row=1, sticky=W, padx=4)
Entry(root).grid(row=1, column=1, sticky=E, pady=4)

Button(root, text="Submit").grid(row=3)

root.mainloop()


# ---------- GRID EXAMPLE 2  ----------

root = Tk()

Label(root, text="Description").grid(row=0, column=0, sticky=W)
Entry(root, width=50).grid(row=0, column=1)
Button(root, text="Submit").grid(row=0, column=8)

Label(root, text="Quality").grid(row=1, column=0, sticky=W)
Radiobutton(root, text="New", value=1).grid(row=2, column=0, sticky=W)
Radiobutton(root, text="Good", value=2).grid(row=3, column=0, sticky=W)
Radiobutton(root, text="Poor", value=3).grid(row=4, column=0, sticky=W)
Radiobutton(root, text="Damaged", value=4).grid(row=5, column=0, sticky=W)

Label(root, text="Benefits").grid(row=1, column=1, sticky=W)
Checkbutton(root, text="Free Shipping").grid(row=2, column=1, sticky=W)
Checkbutton(root, text="Bonus Gift").grid(row=3, column=1, sticky=W)

root.mainloop()

# ---------- TKINTER EVENTS  ----------

def get_sum(event):

    # Get the value stored in the entries
    num1 = int(num1Entry.get())
    num2 = int(num2Entry.get())
    sum = num1 + num2

    # Delete the value in the entry
    sumEntry.delete(0, "end")

    # Insert the sum into the entry
    sumEntry.insert(0, sum)

root = Tk()

num1Entry = Entry(root)
num1Entry.pack(side=LEFT)

Label(root, text="+").pack(side=LEFT)

num2Entry = Entry(root)
num2Entry.pack(side=LEFT)

equalButton = Button(root, text="=")

# When the left mouse button is clicked call the
# function get_sum
equalButton.bind("<Button-1>", get_sum)

equalButton.pack(side=LEFT)

sumEntry = Entry(root)
sumEntry.pack(side=LEFT)

root.mainloop()





















#~~Learn to program 21 TKinter2


from tkinter import *
from tkinter import messagebox

# ---------- VARIABLES & UNBIND ----------
def get_data(event):

    # Output the values for the Widgets with get()
    print("String :", strVar.get())
    print("Integer :", intVar.get())
    print("Double :", dblVar.get())
    print("Boolean :", boolVar.get())

# You can unbind and rebind an event to a function
def bind_button(event):
    if boolVar.get():
        getDataButton.unbind("<Button-1>")
    else:
        getDataButton.bind("<Button-1>", get_data)

root = Tk()

# As I showed previously there are TkInter variables
# you can use with Widgets to set and get values
strVar = StringVar()
intVar = IntVar()
dblVar = DoubleVar()
boolVar = BooleanVar()

# Set the default values with set()
strVar.set("Enter String")
intVar.set("Enter Integer")
dblVar.set("Enter Double")
boolVar.set(True)

# Assign the variable to either textvariable or variable
strEntry = Entry(root, textvariable=strVar)
strEntry.pack(side=LEFT)

intEntry = Entry(root, textvariable=intVar)
intEntry.pack(side=LEFT)

dblEntry = Entry(root, textvariable=dblVar)
dblEntry.pack(side=LEFT)

# Depending on if this check button is selected or not
# will determine if we can get data on our Widgets
theCheckBut = Checkbutton(root, text="Switch", variable=boolVar)
theCheckBut.bind("<Button-1>", bind_button)
theCheckBut.pack(side=LEFT)

# Call the function get_data on click
getDataButton = Button(root, text="Get Data")
getDataButton.bind("<Button-1>", get_data)
getDataButton.pack(side=LEFT)

root.mainloop()

# ---------- STYLING WIDGETS ----------
# There are many ways to custom style your widgets

# You can open message boxes
def open_msg_box():
    messagebox.showwarning(
        "Event Triggered",
        "Button Clicked"
    )

root = Tk()

# You can define the size of the window and the
# position on the screen with
# widthxheight+xoffset+yoffset
root.geometry("400x400+300+300")

# You can make it so the window isn't resizable
root.resizable(width=False, height=False)

frame = Frame(root)

# Your can change a styling option like this
# Color option names are here http://wiki.tcl.tk/37701
# For the font list the font family, px and font style

style = ttk.Style()
style.configure("TButton",
                foreground="midnight blue",
                font="Times 20 bold italic",
                padding=20)

# Ttk widget names : TButton, TCheckbutton, TCombobox,
# TEntry, TFrame, TLabel, TLabelframe, TMenubutton,
# TNotebook, TProgressbar, TRadiobutton, TScale,
# TScrollbar, TSpinbox, Treeview

# You can change the theme style for your applications
# This shows you all the themes for your OS
print(ttk.Style().theme_names())

# You can see current style settings like this
print(style.lookup('TButton', 'font'))
print(style.lookup('TButton', 'foreground'))
print(style.lookup('TButton', 'padding'))

# Change the theme for every widget
ttk.Style().theme_use('clam')

# Have the button open a message box on click
theButton = ttk.Button(frame,
                   text="Important Button",
                   command=open_msg_box)

# You can also disable and enable buttons
theButton['state'] = 'disabled'
theButton['state'] = 'normal'

theButton.pack()

frame.pack()

root.mainloop()

# ---------- MENU BARS ----------

# Quits the TkInter app when called
def quit_app():
    root.quit()

# Opens a message box when called
def show_about(event=None):
    messagebox.showwarning(
        "About",
        "This Awesome Program was Made in 2016"
    )

root = Tk()

# Create the menu object
the_menu = Menu(root)

# ----- FILE MENU -----

# Create a pull down menu that can't be removed
file_menu = Menu(the_menu, tearoff=0)

# Add items to the menu that show when clicked
# compound allows you to add an image
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")

# Add a horizontal bar to group similar commands
file_menu.add_separator()

# Call for the function to execute when clicked
file_menu.add_command(label="Quit", command=quit_app)

# Add the pull down menu to the menu bar
the_menu.add_cascade(label="File", menu=file_menu)

# ----- FONT MENU FOR VIEW MENU -----

# Stores font chosen and will update based on menu
# selection
text_font = StringVar()
text_font.set("Times")

# Outputs font changes
def change_font(event=None):
    print("Font Picked :", text_font.get())

# Define font drop down that will be attached to view
font_menu = Menu(the_menu, tearoff=0)

# Define radio button options for fonts
font_menu.add_radiobutton(label="Times",
                          variable=text_font,
                          command=change_font)

font_menu.add_radiobutton(label="Courier",
                          variable=text_font,
                          command=change_font)

font_menu.add_radiobutton(label="Ariel",
                          variable=text_font,
                          command=change_font)

# ----- VIEW MENU -----
view_menu = Menu(the_menu, tearoff=0)

# Variable changes when line numbers is checked
# or unchecked
line_numbers = IntVar()
line_numbers.set(1)

# Bind the checking of the line number option
# to variable line_numbers
view_menu.add_checkbutton(label="Line Numbers",
                          variable=line_numbers)

view_menu.add_cascade(label="Fonts", menu=font_menu)

# Add the pull down menu to the menu bar
the_menu.add_cascade(label="View", menu=view_menu)

# ----- HELP MENU -----
help_menu = Menu(the_menu, tearoff=0)

# accelerator is used to show a shortcut
# OSX, Windows and Linux use the following options
# Command-O, Shift+Ctrl+S, Command-Option-Q with the
# modifiers Control, Ctrl, Option, Opt, Alt, Shift,
# and Command
help_menu.add_command(label="About",
                      accelerator="command-H",
                      command=show_about)

the_menu.add_cascade(label="Help", menu=help_menu)

# Bind the shortcut to the function
root.bind('<Command-A>', show_about)
root.bind('<Command-a>', show_about)

# Display the menu bar
root.config(menu=the_menu)

root.mainloop()


















#~~Learn to program 22 TKinter Calculator


Use Case Description Describes Everything the App
Does Step-By-Step

I. User clicks a number button

	N3. With each number button press add the new
	value to the end of the first and update entry

II. User clicks a math button

	N1. Make sure entry has a value

	N2. Switch boolean values representing math
	buttons to false on entry

	N2. Have Button pass in the math function
	pressed

	N4. Store the entry value on entry to this
	function (Class Field)

	N4. Clear the entry field?

III. User clicks another number button

IV. User clicks equal button and the result shows

	N1. Make sure a math function was clicked

	N2. Check which math function was clicked
	and provide the correct solution

Note 1 : Since every button requires the previous
button to have been clicked make sure the click
occurred

Note 2 : Make a way to track which math button
was clicked last

Note 3 : Think about a way to handle the user
entering both single numbers and multiple numbers

Note 4 : Track the first number in the entry box
after a math button is clicked

Note 5 : What about division problems caused by
an integer division?

	a. Convert to float each time we retrieve, or
	store values in the entry

from tkinter import *
from tkinter import ttk

class Calculator:

    # Stores the current value to display in the entry
    calc_value = 0.0

    # Will define if this was the last math button clicked
    div_trigger = False
    mult_trigger = False
    add_trigger = False
    sub_trigger = False

    # Called anytime a number button is pressed
    def button_press(self, value):

        # Get the current value in the entry
        entry_val = self.number_entry.get()

        # Put the new value to the right of it
        # If it was 1 and 2 is pressed it is now 12
        # Otherwise the new number goes on the left
        entry_val += value

        # Clear the entry box
        self.number_entry.delete(0, "end")

        # Insert the new value going from left to right
        self.number_entry.insert(0, entry_val)

    # Returns True or False if the string is a float
    def isfloat(self, str_val):
        try:

            # If the string isn't a float float() will throw a
            # ValueError
            float(str_val)

            # If there is a value you want to return use return
            return True
        except ValueError:
            return False

    # Handles logic when math buttons are pressed
    def math_button_press(self, value):

        # Only do anything if entry currently contains a number
        if self.isfloat(str(self.number_entry.get())):

            # make false to cancel out previous math button click
            self.add_trigger = False
            self.sub_trigger = False
            self.mult_trigger = False
            self.div_trigger = False

            # Get the value out of the entry box for the calculation
            self.calc_value = float(self.entry_value.get())

            # Set the math button click so when equals is clicked
            # that function knows what calculation to use
            if value == "/":
                print("/ Pressed")
                self.div_trigger = True
            elif value == "*":
                print("* Pressed")
                self.mult_trigger = True
            elif value == "+":
                print("+ Pressed")
                self.add_trigger = True
            else:
                print("- Pressed")
                self.sub_trigger = True

            # Clear the entry box
            self.number_entry.delete(0, "end")

    # Performs a mathematical operation by taking the value before
    # the math button is clicked and the current value. Then perform
    # the right calculation by checking what math button was clicked
    # last
    def equal_button_press(self):

        # Make sure a math button was clicked
        if self.add_trigger or self.sub_trigger or self.mult_trigger or self.div_trigger:

            if self.add_trigger:
                solution = self.calc_value + float(self.entry_value.get())
            elif self.sub_trigger:
                solution = self.calc_value - float(self.entry_value.get())
            elif self.mult_trigger:
                solution = self.calc_value * float(self.entry_value.get())
            else:
                solution = self.calc_value / float(self.entry_value.get())

            print(self.calc_value, " ", float(self.entry_value.get()),
                                            " ", solution)

            # Clear the entry box
            self.number_entry.delete(0, "end")

            self.number_entry.insert(0, solution)


    def __init__(self, root):
        # Will hold the changing value stored in the entry
        self.entry_value = StringVar(root, value="")

        # Define title for the app
        root.title("Calculator")

        # Defines the width and height of the window
        root.geometry("430x220")

        # Block resizing of Window
        root.resizable(width=False, height=False)

        # Customize the styling for the buttons and entry
        style = ttk.Style()
        style.configure("TButton",
                        font="Serif 15",
                        padding=10)

        style.configure("TEntry",
                        font="Serif 18",
                        padding=10)

        # Create the text entry box
        self.number_entry = ttk.Entry(root,
                        textvariable=self.entry_value, width=50)
        self.number_entry.grid(row=0, columnspan=4)

        # ----- 1st Row -----

        self.button7 = ttk.Button(root, text="7", command=lambda: self.button_press('7')).grid(row=1, column=0)

        self.button8 = ttk.Button(root, text="8", command=lambda: self.button_press('8')).grid(row=1, column=1)

        self.button9 = ttk.Button(root, text="9", command=lambda: self.button_press('9')).grid(row=1, column=2)

        self.button_div = ttk.Button(root, text="/", command=lambda: self.math_button_press('/')).grid(row=1, column=3)

        # ----- 2nd Row -----

        self.button4 = ttk.Button(root, text="4", command=lambda: self.button_press('4')).grid(row=2, column=0)

        self.button5 = ttk.Button(root, text="5", command=lambda: self.button_press('5')).grid(row=2, column=1)

        self.button6 = ttk.Button(root, text="6", command=lambda: self.button_press('6')).grid(row=2, column=2)

        self.button_mult = ttk.Button(root, text="*", command=lambda: self.math_button_press('*')).grid(row=2, column=3)

        # ----- 3rd Row -----

        self.button1 = ttk.Button(root, text="1", command=lambda: self.button_press('1')).grid(row=3, column=0)

        self.button2 = ttk.Button(root, text="2", command=lambda: self.button_press('2')).grid(row=3, column=1)

        self.button3 = ttk.Button(root, text="3", command=lambda: self.button_press('3')).grid(row=3, column=2)

        self.button_add = ttk.Button(root, text="+", command=lambda: self.math_button_press('+')).grid(row=3, column=3)

        # ----- 4th Row -----

        self.button_clear = ttk.Button(root, text="AC", command=lambda: self.button_press('AC')).grid(row=4, column=0)

        self.button0 = ttk.Button(root, text="0", command=lambda: self.button_press('0')).grid(row=4, column=1)

        self.button_equal = ttk.Button(root, text="=", command=lambda: self.equal_button_press()).grid(row=4, column=2)

        self.button_sub = ttk.Button(root, text="-", command=lambda: self.math_button_press('-')).grid(row=4, column=3)

# Get the root window object
root = Tk()

# Create the calculator
calc = Calculator(root)

# Run the app until exited
root.mainloop()





















#~~Learn to program 23 TKinter Text Editor


from tkinter import *
import tkinter.filedialog

class TextEditor:

    # Quits the TkInter app when called
    @staticmethod
    def quit_app(event=None):
        root.quit()

    def open_file(self, event=None):

        txt_file = tkinter.filedialog.askopenfilename(parent=root,
                                                      initialdir='/Users/derekbanas/PycharmProjects')

        if txt_file:

            self.text_area.delete(1.0, END)

            # Open file and put text in the text widget
            with open(txt_file) as _file:
                self.text_area.insert(1.0, _file.read())

                # Update the text widget
                root.update_idletasks()

    def save_file(self, event=None):

        # Opens the save as dialog box
        file = tkinter.filedialog.asksaveasfile(mode='w')
        if file != None:
            # Get text in the text widget and delete the last newline
            data = self.text_area.get('1.0', END + '-1c')

            # Write the text and close
            file.write(data)
            file.close()

    def __init__(self, root):

        self.text_to_write = ""

        # Define title for the app
        root.title("Text Editor")

        # Defines the width and height of the window
        root.geometry("600x550")

        frame = Frame(root, width=600, height=550)

        # Create the scrollbar
        scrollbar = Scrollbar(frame)

        # yscrollcommand connects the scroll bar to the text
        # area
        self.text_area = Text(frame, width=600, height=550,
                        yscrollcommand=scrollbar.set,
                        padx=10, pady=10)

        # Call yview when the scrollbar is moved
        scrollbar.config(command=self.text_area.yview)

        # Put scroll bar on the right and fill in the Y direction
        scrollbar.pack(side="right", fill="y")

        # Pack on the left and fill available space
        self.text_area.pack(side="left", fill="both", expand=True)
        frame.pack()

        # Create the menu object
        the_menu = Menu(root)

        # Create a pull down menu that can't be removed
        file_menu = Menu(the_menu, tearoff=0)

        # Add items to the menu that show when clicked
        # compound allows you to add an image
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)

        # Add a horizontal bar to group similar commands
        file_menu.add_separator()

        # Call for the function to execute when clicked
        file_menu.add_command(label="Quit", command=self.quit_app)

        # Add the pull down menu to the menu bar
        the_menu.add_cascade(label="File", menu=file_menu)

        # Display the menu bar
        root.config(menu=the_menu)

root = Tk()

text_editor = TextEditor(root)

root.mainloop()
























#~~Learn to program 24 TKinter Tool Bars


from tkinter import *
from PIL import Image, ImageTk

class TkInterEx:
    @staticmethod
    def quit_app(event=None):
        root.quit()

    # Handles events on list box
    def on_fav_food_select(self, event=None):

        lb_widget = event.widget

        # Get index selected
        index = int(lb_widget.curselection()[0])

        # Get value selected in list box
        lb_value = lb_widget.get(index)

        self.fav_food_label['text'] = "I'll get you " + lb_value

    def __init__(self, root):

        root.title("Toolbar Example")

        # ---------- Create Menu Bar ----------

        # Create menu object
        menubar = Menu(root)

        # Create drop down menu
        file_menu = Menu(root, tearoff=0)

        # Add menu drop down options
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_command(label="Exit", command=self.quit_app)

        # Add drop down options to File
        menubar.add_cascade(label="File", menu=file_menu)

        # ---------- Create Toolbar ----------

        # RAISED draws a line under the tool bar and bd defines the border width
        toolbar = Frame(root, bd=1, relief=RAISED)

        # Get images for toolbar
        open_img = Image.open("open.png")
        save_img = Image.open("disk.png")
        exit_img = Image.open("exit.png")

        # Create a TkInter image to be used in the button
        open_icon = ImageTk.PhotoImage(open_img)
        save_icon = ImageTk.PhotoImage(save_img)
        exit_icon = ImageTk.PhotoImage(exit_img)

        # Create buttons for the toolbar
        open_button = Button(toolbar, image=open_icon)
        save_button = Button(toolbar, image=save_icon)
        exit_button = Button(toolbar, image=exit_icon, command=self.quit_app)

        open_button.image = open_icon
        save_button.image = save_icon
        exit_button.image = exit_icon

        # Place buttons in the interface
        open_button.pack(side=LEFT, padx=2, pady=2)
        save_button.pack(side=LEFT, padx=2, pady=2)
        exit_button.pack(side=LEFT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X)

        root.config(menu=menubar)

        # ---------- Create a List Box ----------
        # A listbox displays a list of items to select

        # A label frame is a frame with a label
        lb_frame = LabelFrame(root, text="Food Options", padx=5, pady=5)

        # This label changes based on list box selections
        self.fav_food_label = Label(lb_frame,
                               text="What is your favorite food")

        self.fav_food_label.pack()

        list_box = Listbox(lb_frame)

        # Create list box options
        list_box.insert(1, "Spaghetti")
        list_box.insert(2, "Pizza")
        list_box.insert(3, "Burgers")
        list_box.insert(4, "Hot Dogs")

        # When a list box option is clicked execute the function
        list_box.bind('<<ListboxSelect>>', self.on_fav_food_select)

        list_box.pack()

        lb_frame.pack()

        # ---------- Create a Spin Box ----------
        # Provides a fixed number of values as an option

        sb_frame = Frame(root)

        quantity_label = Label(sb_frame,
                               text="How many do you want")

        quantity_label.pack()

        # Allow for the values 1 through 5
        spin_box = Spinbox(sb_frame,
                           from_=1, to=5)
        spin_box.pack()

        extras_label = Label(sb_frame,
                             text="Add on Item")

        extras_label.pack()

        # Add a list of custom items
        extras_spin_box = Spinbox(sb_frame,
                                  values=('French Fries',
                                          'Onion Rings',
                                          'Tater Tots'))

        extras_spin_box.pack()


        sb_frame.pack()

root = Tk()
root.geometry("600x550")
app = TkInterEx(root)
root.mainloop()



























#~~Learn to program 25 TKinter Paint App


from tkinter import *
import tkinter.font


class PaintApp:

    # Stores current drawing tool used
    drawing_tool = "line"

    # Tracks whether left mouse is down
    left_but = "up"

    # x and y positions for drawing with pencil
    x_pos, y_pos = None, None

    # Tracks x & y when the mouse is clicked and released
    x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt = None, None, None, None

    # ---------- CATCH MOUSE UP ----------

    def left_but_down(self, event=None):
        self.left_but = "down"

        # Set x & y when mouse is clicked
        self.x1_line_pt = event.x
        self.y1_line_pt = event.y

    # ---------- CATCH MOUSE UP ----------

    def left_but_up(self, event=None):
        self.left_but = "up"

        # Reset the line
        self.x_pos = None
        self.y_pos = None

        # Set x & y when mouse is released
        self.x2_line_pt = event.x
        self.y2_line_pt = event.y

        # If mouse is released and line tool is selected
        # draw the line
        if self.drawing_tool == "line":
            self.line_draw(event)
        elif self.drawing_tool == "arc":
            self.arc_draw(event)
        elif self.drawing_tool == "oval":
            self.oval_draw(event)
        elif self.drawing_tool == "rectangle":
            self.rectangle_draw(event)
        elif self.drawing_tool == "text":
            self.text_draw(event)

    # ---------- CATCH MOUSE MOVEMENT ----------

    def motion(self, event=None):

        if self.drawing_tool == "pencil":
            self.pencil_draw(event)

    # ---------- DRAW PENCIL ----------

    def pencil_draw(self, event=None):
        if self.left_but == "down":

            # Make sure x and y have a value
            if self.x_pos is not None and self.y_pos is not None:
                event.widget.create_line(self.x_pos, self.y_pos,                        event.x, event.y, smooth=TRUE)

            self.x_pos = event.x
            self.y_pos = event.y

    # ---------- DRAW LINE ----------

    def line_draw(self, event=None):

        # Shortcut way to check if none of these values contain None
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            event.widget.create_line(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt, smooth=TRUE, fill="green")

    # ---------- DRAW ARC ----------

    def arc_draw(self, event=None):

        # Shortcut way to check if none of these values contain None
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt,                              self.y2_line_pt):

            coords = self.x1_line_pt, self.y1_line_pt, self.x2_line_pt,                                  self.y2_line_pt

            # start : starting angle for the slice in degrees
            # extent : width of the slice in degrees
            # fill : fill color if needed
            # style : can be ARC, PIESLICE, or CHORD
            event.widget.create_arc(coords, start=0, extent=150,
                                    style=ARC)

    # ---------- DRAW OVAL ----------

    def oval_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt,                              self.y2_line_pt):

            # fill : Color option names are here http://wiki.tcl.tk/37701
            # outline : border color
            # width : width of border in pixels

            event.widget.create_oval(self.x1_line_pt, self.y1_line_pt,                                              self.x2_line_pt, self.y2_line_pt,
                                        fill="midnight blue",
                                        outline="yellow",
                                        width=2)

    # ---------- DRAW RECTANGLE ----------

    def rectangle_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt,                              self.y2_line_pt):

            # fill : Color option names are here http://wiki.tcl.tk/37701
            # outline : border color
            # width : width of border in pixels

            event.widget.create_rectangle(self.x1_line_pt, self.y1_line_pt,                  self.x2_line_pt, self.y2_line_pt,
                fill="midnight blue",
                outline="yellow",
                width=2)

    # ---------- DRAW TEXT ----------

    def text_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt):
            # Show all fonts available
            print(tkinter.font.families())

            text_font = tkinter.font.Font(family='Helvetica',
            size=20, weight='bold', slant='italic')

            event.widget.create_text(self.x1_line_pt, self.y1_line_pt,
                                      fill="green",
                                      font=text_font,
                                      text="WOW")

    def __init__(self, root):
        drawing_area = Canvas(root)
        drawing_area.pack()
        drawing_area.bind("<Motion>", self.motion)
        drawing_area.bind("<ButtonPress-1>", self.left_but_down)
        drawing_area.bind("<ButtonRelease-1>", self.left_but_up)

root = Tk()

paint_app = PaintApp(root)

root.mainloop()























#~~Learn to program 26 TKinter Database


from tkinter import *
from tkinter import ttk
import sqlite3

class StudentDB :

    # Will hold database connection
    db_conn = 0
    # A cursor is used to traverse the records of a result
    theCursor = 0
    # Will store the current student selected
    curr_student = 0

    def setup_db(self):

        # Open or create database
        self.db_conn = sqlite3.connect('student.db')

        # The cursor traverses the records
        self.theCursor = self.db_conn.cursor()

        # Create the table if it doesn't exist
        try:
            self.db_conn.execute("CREATE TABLE if not exists Students(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL);")

            self.db_conn.commit()

        except sqlite3.OperationalError:
            print("ERROR : Table not created")

    def stud_submit(self):

        # Insert students in the db
        self.db_conn.execute("INSERT INTO Students (FName, LName) " +
                             "VALUES ('" +
                             self.fn_entry_value.get() + "', '" +
                             self.ln_entry_value.get() + "')")

        # Clear the entry boxes
        self.fn_entry.delete(0, "end")
        self.ln_entry.delete(0, "end")

        # Update list box with student list
        self.update_listbox()

    def update_listbox(self):

        # Delete items in the list box
        self.list_box.delete(0, END)

        # Get students from the db
        try:
            result = self.theCursor.execute("SELECT ID, FName, LName FROM Students")

            # You receive a list of lists that hold the result
            for row in result:

                stud_id = row[0]
                stud_fname = row[1]
                stud_lname = row[2]

                # Put the student in the list box
                self.list_box.insert(stud_id,
                                     stud_fname + " " +
                                     stud_lname)

        except sqlite3.OperationalError:
            print("The Table Doesn't Exist")

        except:
            print("1: Couldn't Retrieve Data From Database")


    # Load listbox selected student into entries
    def load_student(self, event=None):

        # Get index selected which is the student id
        lb_widget = event.widget
        index = str(lb_widget.curselection()[0] + 1)

        # Store the current student index
        self.curr_student = index

        # Retrieve student list from the db
        try:
            result = self.theCursor.execute("SELECT ID, FName, LName FROM Students WHERE ID=" + index)

            # You receive a list of lists that hold the result
            for row in result:

                stud_id = row[0]
                stud_fname = row[1]
                stud_lname = row[2]

                # Set values in the entries
                self.fn_entry_value.set(stud_fname)
                self.ln_entry_value.set(stud_lname)

        except sqlite3.OperationalError:
            print("The Table Doesn't Exist")

        except:
            print("2 : Couldn't Retrieve Data From Database")

    # Update student info
    def update_student(self, event=None):

        # Update student records with change made in entry
        try:
            self.db_conn.execute("UPDATE Students SET FName='" +
                                self.fn_entry_value.get() +
                                "', LName='" +
                                self.ln_entry_value.get() +
                                "' WHERE ID=" +
                                self.curr_student)

            self.db_conn.commit()

        except sqlite3.OperationalError:
            print("Database couldn't be Updated")

        # Clear the entry boxes
        self.fn_entry.delete(0, "end")
        self.ln_entry.delete(0, "end")

        # Update list box with student list
        self.update_listbox()

    def __init__(self, root):

        root.title("Student Database")
        root.geometry("270x340")

        # ----- 1st Row -----
        fn_label = Label(root, text="First Name")
        fn_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        # Will hold the changing value stored first name
        self.fn_entry_value = StringVar(root, value="")
        self.fn_entry = ttk.Entry(root,
                                  textvariable=self.fn_entry_value)
        self.fn_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # ----- 2nd Row -----
        ln_label = Label(root, text="Last Name")
        ln_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        # Will hold the changing value stored last name
        self.ln_entry_value = StringVar(root, value="")
        self.ln_entry = ttk.Entry(root,
                                  textvariable=self.ln_entry_value)
        self.ln_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        # ----- 3rd Row -----
        self.submit_button = ttk.Button(root,
                            text="Submit",
                            command=lambda: self.stud_submit())
        self.submit_button.grid(row=2, column=0,
                                padx=10, pady=10, sticky=W)

        self.update_button = ttk.Button(root,
                            text="Update",
                            command=lambda: self.update_student())
        self.update_button.grid(row=2, column=1,
                                padx=10, pady=10)

        # ----- 4th Row -----

        scrollbar = Scrollbar(root)

        self.list_box = Listbox(root)

        self.list_box.bind('<<ListboxSelect>>', self.load_student)

        self.list_box.insert(1, "Students Here")

        self.list_box.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky=W+E)

        # Call for database to be created
        self.setup_db()

        # Update list box with student list
        self.update_listbox()

# Get the root window object
root = Tk()

# Create the calculator
studDB = StudentDB(root)

# Run the app until exited
root.mainloop()


























#~~Learn to program 27 Kivy 1


# ---------- Install Kivy on Mac ----------

1. Install Python and PyCharm like I show here : https://youtu.be/nwjAHQERL08?t=37m

2. Download Kivy for Python 3 Kivy-1.9.1-osx-python3.7z here : https://kivy.org/#download

3. In terminal : cd <Directory you Downloaded Kivy>

4. In terminal : sudo mv Kivy2.app /Applications/Kivy.app

5. In terminal : ln -s /Applications/Kivy.app/Contents/Resources/script /usr/local/bin/kivy

6. Test it works in terminal type : kivy and then import kivy

7. Run application by typing in terminal : kivy yourapp.py

# ---------- Install Kivy on Windows ----------

1. Install Python and PyCharm like I show here : https://youtu.be/nwjAHQERL08?t=37m

2. In command prompt : python -m pip install --upgrade pip wheel setuptools

3. In command prompt : python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew

4. In command prompt : python -m pip install kivy.deps.gstreamer --extra-index-url https://kivy.org/downloads/packages/simple/

5. In command prompt : python -m pip install kivy

# ---------- kivytut.py ----------

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.button import Label

# Inherit Kivy's App class which represents the window
# for our widgets
# HelloKivy inherits all the fields and methods
# from Kivy
class HelloKivy(App):

    # This returns the content we want in the window
    def build(self):

        # Return a label widget with Hello Kivy
        return Label(text="Hello Kivy")

helloKivy = HelloKivy()
helloKivy.run()

# ---------- kivytut2.py ----------

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.button import Label

# Inherit Kivy's App class which represents the window
# for our widgets
# HelloKivy inherits all the fields and methods
# from Kivy
class HelloKivyApp(App):

    # This returns the content we want in the window
    def build(self):

        # Return a label widget with Hello Kivy
        # The name of the kv file has to be hellokivy
        # minus the app part from this class to
        # match up properly
        return Label()

hello_kivy = HelloKivyApp()
hello_kivy.run()

# ---------- hellokivy.kv ----------

# We can separate the logic from the presentation layer
<Label>:
    text: "Hello Kivy"



























#~~Learn to program 28 Kivy 2


# ---------- KIVYTUT.PY ----------

# It is common practice to create your own custom
# widgets so base widgets aren't effected

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.widget import Widget

class CustomWidget(Widget):
    pass

class CustomWidgetApp(App):

    def build(self):
        return CustomWidget()

customWidget = CustomWidgetApp()

customWidget.run()

# ---------- CUSTOMWIDGET.KV ----------

# You can set default attributes that are shared by
# other widgets

# color is RGBA as a percent of 255 and alpha
# Color is the text color
# background_normal and background_down are either
# white with '' or can be set to a png
# background_color tints whatever the background is

<CustButton@Button>:
    font_size: 32
    color: 0, 0, 0, 1
    size: 150, 50
    background_normal: ''
    background_down: 'bkgrd-down-color.png'
    background_color: .88, .88, .88, 1

# Position is x and y from the bottom left hand corner
# You can define the position based on the changing
# window sizes with root.x being the left most side
# and root.y being the bottom
<CustomWidget>:
    CustButton:
        text: "Random"
        pos: root.x, 200
    CustButton:
        text: "Buttons"
        pos: 200, root.y
    CustButton:
        text: "Buttons"
        pos: 200, 400

# ---------- KIVYTUT2.PY ----------

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

# A Float layout positions and sizes objects as a percentage
# of the window size

class FloatingApp(App):

    def build(self):
        return FloatLayout()

flApp = FloatingApp()

flApp.run()

# ---------- FLOATING.KV ----------

# size_hint defines the widget width (0-1) representing
# a percentage of 100% and height of the window
<CustButton@Button>:
    font_size: 32
    color: 0, 0, 0, 1
    size: 150, 50
    background_normal: ''
    background_down: 'bkgrd-down-color.png'
    background_color: .88, .88, .88, 1
    size_hint: .4, .3

# pos_hint represents the position using either x, y, left,
# right, top, bottom, center_x, or center_y
<FloatLayout>:
    CustButton:
        text: "Top Left"
        pos_hint: {"x": 0, "top": 1}
    CustButton:
        text: "Bottom Right"
        pos_hint: {"right": 1, "y": 0}
    CustButton:
        text: "Top Right"
        pos_hint: {"right": 1, "top": 1}
    CustButton:
        text: "Bottom Left"
        pos_hint: {"left": 1, "bottom": 0}
    CustButton:
        text: "Center"
        pos_hint: {"center_x": .5, "center_y": .5}


# ---------- KIVYTUT3.PY ----------

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

# The Grid Layout organizes everything in a grid pattern

class GridLayoutApp(App):

    def build(self):
        return GridLayout()

glApp = GridLayoutApp()

glApp.run()

# ---------- GRIDLAYOUT.KV ----------

# Define the number of columns and rows
# Define the spacing between children in pixels

<GridLayout>:
    cols: 2
    rows: 2
    spacing: 10

    # Set the size by passing None to size_hint_x
    # and then pass the width

    Button:
        text: "1st"
        size_hint_x: None
        width: 200
    Button:
        text: "2nd"
    Button:
        text: "3rd"
        size_hint_x: None
        width: 200
    Button:
        text: "4th"

# ---------- KIVYTUT4.PY ----------

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# With a box layout we arrange widgets in a horizontal
# or vertical box

class BoxLayoutApp(App):

    def build(self):
        return BoxLayout()

blApp = BoxLayoutApp()

blApp.run()

# ---------- BOXLAYOUT.KV ----------

# Orientation defines whether widgets are stacked (vertical)
# or are placed side by side (horizontal)
# padding is the space between the widgets and the
# surrounding window
<BoxLayout>:
    orientation: "vertical"
    spacing: 10
    padding: 10

    # size_hint defines the percentage of space taken on the
    # x access and the percentage of space left over by the
    # other widgets
    Button:
        text: "1st"
        size_hint: .7, .5

    Button:
        text: "2nd"

    Button:
        text: "3rd"

# ---------- KIVYTUT5.PY ----------

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.stacklayout import StackLayout

# A stack layout arranges widgets vertically or horizontally
# as they best fit

class StackLayoutApp(App):

    def build(self):
        return StackLayout()

slApp = StackLayoutApp()

slApp.run()

# ---------- STACKLAYOUT.KV ----------

# orientation is lr-tb or left to right, top to bottom
# Other options are tb-lr, rl-tb, tb-rl, lr-bt, bt-lr,
# rl-bt, bt-rl
<StackLayout>:
    orientation: "lr-tb"
    spacing: 10
    padding: 10

    # size_hint defines the percentage of space taken on the
    # x access and the percentage of space left over by the
    # other widgets
    Button:
        text: "Q"
        size_hint: None, .15
        width: 100
    Button:
        text: "W"
        size_hint: None, .15
        width: 120
    Button:
        text: "E"
        size_hint: None, .15
        width: 140
    Button:
        text: "R"
        size_hint: None, .15
        width: 160
    Button:
        text: "T"
        size_hint: None, .15
        width: 180
    Button:
        text: "Y"
        size_hint: None, .15
        width: 200

# ---------- KIVYTUT6.PY ----------

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.pagelayout import PageLayout

# A page layout is used to create multi-page layouts
# that you can flip through

class PageLayoutApp(App):

    def build(self):
        return PageLayout()

plApp = PageLayoutApp()

plApp.run()

# ---------- PAGELAYOUT.KV ----------

<PageLayout>:
    Button:
        text: "Page 1"
    Button:
        text: "Page 2"
    Button:
        text: "Page 3"
































































#~~Learn to program 32 Django 1




# ---------- INSTALL DJANGO ON MAC ----------

1. Check your Python version by typing in the terminal : python --version

2. You want Python 3.4 or higher. Type the following to see if you have Python 3 in the terminal : python3 --version

3. If you need Python 3.4 or above do this

	A. Download Python at https://www.python.org/downloads

	B. Click Download Python 3.5.1 or later

	C. Click Open

	D. Click continue a few times. Agree to the terms and install. You may have to enter your password.

4. Check to see if you have pip installed in the terminal type : pip --version

5. If you don't have pip 8 or above type in the terminal : sudo easy_install pip

6. Type in the terminal : sudo pip install Django

7. Test that Django is installed in the terminal

	A. python3

	B. import django

	C. django.get_version()

	D. You should see '1.10.2' or higher

8. Create a sample site : django-admin startproject sampsite

	A. sampsite is were your project lives

		i. __init__.py tells Python that this is a Python package

		ii. settings.py has settings for the Django project

		iii. urls.py a sort of table of contents for your project

		iv. wsgi.py serves your project

	B. manage.py allows you to interact with your project

9. Start the server : python manage.py runserver

# ---------- INSTALL DJANGO ON WINDOWS ----------

1. Check your Python version by typing in the terminal : python --version
(You want Python 3.4 or higher)

2. If Python 3.4 or higher isn't installed

	A. Go to https://www.python.org/getit/windows/

	B. Click on Latest Python 3 Release

	C. Click on Windows x86 executable installer

	D. Click Run

	E. Check Install for all users and add Python 3 to path

		a. Open Control Panel -> System & Security -> System -> Advanced System Settings on the left

		b. Environment Variable button

		c. Select PATH and click edit

		d. Add c:\Pyhon34, or what ever your Python directory is

3. Install Pip in the command line type : python -m pip install -U pip

4. Create a Python Virtual Environment so we don't have to worry about changing dependencies that your system may not want edited.

	A. Type in Command Prompt : pip install virtualenv

	B. Create the virtual environment for your site in command prompt : virtualenv env_site1

	C. Activate the environment in CP

		i. cd Scripts

		ii. activate

5. Install Django in CP : pip install django

6. Test that it works

	A. python

	B. import django

	C. django.get_version()

	D. You should see '1.10.2' or higher

7. Create a sample site : django-admin startproject sampsite

	A. sampsite is were your project lives

		i. __init__.py tells Python that this is a Python package

		ii. settings.py has settings for the Django project

		iii. urls.py a sort of table of contents for your project

		iv. wsgi.py serves your project

	B. manage.py allows you to interact with your project

8. Start the server : python manage.py runserver
































#~~Learn to program 33 Django 2



# ---------- sampsite/views.py ----------

from django.http import HttpResponse

import random

# This is our View function which receives info
# on the request
def hello_world(request):

    # Return a response object with the text Hello World
    return HttpResponse("Hello World")

def root_page(request):

    return HttpResponse("Root Home Page")

# Receives the number passed in the url and then returns
# a random number
def random_number(request, max_rand=100):

    # Calculate a random number between 0 and the number passed
    random_num = random.randrange(0, int(max_rand))

    # Place the string and decimal in the output
    msg = "Random Number Between 0 and %s : %d" % (max_rand, random_num)

    return HttpResponse(msg)

# ---------- NOW ON TO SETTINGS ----------

# ---------- settings.py ----------

"""
Django settings for sampsite project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1$(46qw^uc2q&c)gad(*4^y)a8g2^dbr$%)nlvyf3jygfbv70('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # - The Django admin system
    'django.contrib.admin',

    # - The authentication system
    'django.contrib.auth',

    # - Framework for content types
    'django.contrib.contenttypes',

    # - Session Framework
    'django.contrib.sessions',

    # - Message Framework
    'django.contrib.messages',

    # - Manages static files
    'django.contrib.staticfiles',

    # 4 Include our polls app
    # 4 Run python3 manage.py makemigrations polls
    # 4 to notify Django that you have updated your Model
    # 4 Run python3 manage.py sqlmigrate polls 0001 to see
    # 4 the SQL used to create the DB
    # 4 Run python3 manage.py migrate to create the DB
    # 4 Create the models in polls/models.py
    'polls.apps.PollsConfig',
]

# 6 We can add data to the DB using the Python shell
# - python3 manage.py shell
# - Import Models : from polls.models import Question, Choice
# - Display Questions : Question.objects.all()
# - Create a Question
# - from django.utils import timezone
# - q = Question(question_text="What's New?", pub_date=timezone.now())
# - Save to the DB : q.save()
# - Get the questions id : q.id
# - Get the questions text : q.question_text
# - Get the pub date : q.pub_date
# - Change the question : q.question_text = "What's Up?"
# - Save the change : q.save()
# - Display Questions : Question.objects.all()

# 6 Change polls/models.py to provide more info on question and choice

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sampsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sampsite.wsgi.application'

# 4 Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# 4 We'll use the default database of SQLite3
# - You can use other DBs, but must add USER, PASSWORD and HOST
# - django.db.backends.mysql
# - django.db.backends.postgresql
# - django.db.backends.oracle

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

# - Change the time zone to yours using
# - https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

# - Add a path for static files
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# ---------- sampsite/urls.py ----------

"""sampsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# url matches the URL in the browser to a module
# in your Django project
from django.conf.urls import url

# Loads URLs for Admin site
from django.contrib import admin

# Reference my hello_world function
from sampsite.views import hello_world, root_page, random_number

# 3 include allows you to reference other url files
# in our project
from django.conf.urls import include

# Lists all URLs
# Add the directory in the URL you want tied to
# the hello_world function
# The r means we want to treat this like a raw string
# that ignored backslashes
# Then we define a regular expression where ^ is the
# beginning of a string, then we have the text to match
# The $ signifies the end of a Regex string

# We can pass data to a function by surrounding the part
# of the Regex to send with parentheses
# If they didn't enter a number I provide a default max
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^helloworld/$', hello_world),
    url(r'^$', root_page),
    url(r'^random/(\d+)/$', random_number),
    url(r'^random/$', random_number),

    # 3 Reference the root of the polls app
    url(r'^polls/', include('polls.urls')),
]

# 3 Test that the polls URL works by running the server
# python3 manage.py runserver
# Go to localhost:8000/polls/

# 3 Setup the database in settings.py

# ---------- polls/views.py ----------

# 1 Create the polls app inside our project
# 1 python3 manage.py startapp polls
# 1 You can have multiple apps in your project
# 1 Now we will create a view

from django.http import HttpResponse

def index(request):
    return HttpResponse("You're in the polls index")

# 1 Now attach the view to a url in urls.py

# ---------- polls/urls.py ----------

from django.conf.urls import url

from . import views

# 2 Add a reference to the view and assign it to
# the root URL for polls

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

# 2 Now point the root URL file to the polls app

# ---------- polls/models.py ----------

# 5 Here you define the names and data types for
# 5 the information you are storing in your database

from django.db import models

import datetime
from django.utils import timezone

# 5 Create your models here.
# 5 Each model is a class with class variables that
# 5 represent fields in your database
# 5 After setting the column names an data types the DB
# 5 can create the table

class Question(models.Model):

    # 5 Define a DB column called question_text which
    # 5 contains text with a max size of 200
    question_text = models.CharField(max_length=200)

    # 5 This contains a date and the text passed is an
    # 5 optional human readable name
    pub_date = models.DateTimeField('date published')

    # 7 Return the text for the question when the Question
    # 7 is called by editing __str__

    def __str__(self):
        return self.question_text

    # 7 Here is a custom method for returning whether
    # 7 the question was published recently
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):

    # 5 Define that each choice is related to a single
    # 5 Question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # 7 Return the Choice text as well
    def __str__(self):
        return self.choice_text

    # 7 Let's test our changes : python3 manage.py shell
    # 7 from polls.models import Question, Choice
    # 7 Get a detailed list of questions
    # 7 Question.objects.all()

    # 7 Get the Question with the matching id
    # 7 Question.objects.filter(id=1)

    # 7 Get the question that starts with What
    # 7 Question.objects.filter(question_text__startswith='What')

    # 7 Get Question published this year
    # 7 from django.utils import timezone
    # 7 current_year = timezone.now().year
    # 7 Question.objects.get(pub_date__year=current_year)

    # 7 If you request something that doesn't exist you
    # 7 raise an exception
    # 7 Question.objects.get(id=2)

    # 7 Search for primary key
    # 7 Question.objects.get(pk=1)

    # 7 Test was_published_recently()
    # 7 q = Question.objects.get(pk=1)
    # 7 q.was_published_recently()

    # 7 Show choices for matching question
    # 7 q.choice_set.all()

    # 7 Add new choices
    # 7 q.choice_set.create(choice_text='Not Much', votes=0)
    # 7 q.choice_set.create(choice_text='The Sky', votes=0)
    # 7 q.choice_set.create(choice_text='The Clouds', votes=0)

    # 7 Display choices
    # 7 q.choice_set.all()

    # 7 Display number of choices
    # 7 q.choice_set.count()

    # 7 Show all choices for questions published this year
    # 7 Use __ to separate relationships
    # 7 Choice.objects.filter(question__pub_date__year=current_year)

    # 7 Delete a choice
    # 7 c = q.choice_set.filter(choice_text__startswith='The Clouds')

# 5 After defining the model we include the app in our project
# 5 under INSTALLED_APPS in settings.py






























#~~Learn to program 34 Django 3



# ---------- /polls/admin.py ----------

# 1 Django automates the interface used to add, change
# and delete content
# To create a user : python3 manage.py createsuperuser
# Username: admin
# Email address: db@compuserve.com
# Enter passwords

# 1 Run the server : python3 manage.py runserver
# Open localhost:8000/admin

# 1 Tell admin that our poll system has an admin interface
# in polls/admin.py

# 1 You can change any of the options and click History
# to see a list of the changes
# You can also add or delete questions

# 1 Now add more views in polls/views.py

from django.contrib import admin

# Register your models here.

# - Import Question
from .models import Question

# - Register Question for showing in admin
admin.site.register(Question)

# ---------- /polls/views.py ----------

from django.http import HttpResponse

# 7 Opens a 404 page if get doesn't supply a result
from django.shortcuts import get_object_or_404

# 2 Each view is represented by a function
# We'll create :
# index : Display the latest questions
# detail : Display the question and the choices
# results : Display question results

# - Original index function
'''
def index(request):
    return HttpResponse("You're in the polls index")
'''

# 4
# Import Question and Choice from our models file
from .models import Question, Choice

'''
# 4 New index function
def index(request):

    # 4 Receive a list of 5 questions ordered by date
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # 4 Cycle through the questions to create a list
    output = ', '.join([q.question_text for q in latest_question_list])

    # Return the text to display
    return HttpResponse(output)

'''

# 4 This isn't the best solution because the results are
# hard coded into the Python. Let's use a template to
# separate the design from the code
# Create a directory named templates in polls
# Create a directory named polls in the templates directory
# Create a file named index.html in that polls directory
# and create the template

# 6 Create a new index function that sends the question list
# to the template

# 6 Renders a page when it is passed a template and
# any data required by the template
from django.shortcuts import render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # 6 Define the name for the data to pass to the template
    context = {
        'latest_question_list': latest_question_list,
    }

    # 6 Render the page in the browser using the template
    # and data required by the template
    return render(request, 'polls/index.html', context)


# 2 add these 3 new views

'''
def detail(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)
'''

'''
def results(request, question_id):
        response = "You're looking at the results of question %s"
        return HttpResponse(response % question_id)
'''

# 10 Let's update results() to show voting results
def results(request, question_id):

    # 10 Get the question id passed or 404
    question = get_object_or_404(Question, pk=question_id)

    # 10 Render the template
    return render(request, 'polls/results.html',
                  {'question': question})

# 10 Now create /templates/polls/results.html template

'''
def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)

# 7 Let's update detail to use a 404 page and template
'''

# 9 Now we will update vote() to except the choice picked

# 9 Used to avoid receiving data twice from a form if the user
# clicks the back button
from django.http import HttpResponseRedirect

# 9 Used to return a url we can point to based on the
# current question we are dealing with
from django.urls import reverse

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # 9 Try to get the selected radio button
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except(KeyError, Choice.DoesNotExist):

        # 9 Re-render the form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:

        # 9 If a choice was selected increment it in the DB
        selected_choice.votes += 1
        selected_choice.save()

        # 9 Protect from data being sent twice if user clicks back
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def detail(request, question_id):
    # 7 Check if the page exists, or display 404 page
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question': question})

# 7 Now create the detail.html template in templates/polls/

# 2 Add them to polls/urls.py


# ---------- /polls/urls.py ----------

from django.conf.urls import url

from . import views

# 3 Add a namespace so Django knows what directory to load
# if another app has views with the same name
app_name = 'polls'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # 3 Add the 3 views
    # The data surrounded by parentheses is sent to the function
    # ?P<question_id> defines the name for the data within
    # the parentheses
    # [0-9]+ says we will match 1 or more numbers
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

# 3 Now let's update polls/views.py

# ---------- /polls/templates/polls/index.html ----------

<!-- 5 If a list of questions is available create
an unordered list of the questions or print
that none are available -->
{% if latest_question_list %}
    <ul>
        {% for question in latest_question_list %}
            <li>
                <!-- 5 url defines directory to open based
                 on using the namespace defined in polls/urls.py
                 and the url defined in sampsite/urls.py -->
                <a href="{% url 'polls:detail' question.id %}">{{question.question_text}}</a>
            </li>
        {% endfor %}
    </ul>
{% else %}
    <p>No polls are available</p>
{% endif %}

<!-- 5 Back to polls/views.py to update index -->

# ---------- /polls/templates/polls/detail.html ----------

<!-- 8 Display the question passed and the choices
available -->

<h1>{{question.question_text}}</h1>

<!-- 8 Display error message -->
{% if error_message %}
<p><strong>{{error_message}}</strong></p>
{% endif %}

<!-- 8 Create a form which allows users to pick a choice -->
<!-- Point at the vote function in polls/views.py using
the namespace and pass the question id -->
<form action="{% url 'polls:vote' question.id %}" method="post">

<!-- 8 Protects your site from Cross Site Request Forgeries
which occur when another site tries to target your form -->
{% csrf_token %}

<!-- 8 Cycle through all choices for this question and
create a radio button for each -->
{% for choice in question.choice_set.all %}

    <!-- 8 When submitted the choice id is sent -->
    <input type="radio" name="choice"
           id="choice{{ forloop.counter }}"
           value="{{ choice.id }}" />

    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label>
    <br>

{% endfor %}

<input type="submit" value="Vote" />
</form>

<!-- 8 Now update the vote function in polls/views.py -->

# ---------- /polls/templates/polls/results.html ----------

<!-- 11 Displays choice results for the passed question -->

<h1>{{question.question_text}}</h1>

<!-- Cycle through all the choices for the question -->
<ul>
    {% for choice in question.choice_set.all %}
        <li>
            <!-- Add a s to vote if not 1 -->
            {{choice.choice_text}} -- {{choice.votes}} vote{{choice.votes|pluralize}}
        </li>
    {% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote Again</a>






























#~~Learn to program 35 Django 4


# ---------- /polls/urls.py ----------

# 1 Generic views are normally used from the beginning
# and they help you avoid having to write a lot
# of custom code

from django.conf.urls import url

from . import views

app_name = 'polls'

# 1 We'll change the urlpatterns

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

# 1 Now remove our index, detail and results views in polls/views.py

'''
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
'''

# ---------- /polls/views.py ----------

from django.http import HttpResponse

from .models import Question, Choice

from django.shortcuts import render

from django.shortcuts import get_object_or_404

from django.http import HttpResponseRedirect

from django.urls import reverse

# 2 Add the generic module
from django.views import generic

# 8 Import so we can get time information
from django.utils import timezone

# 2 The ListView displays your list of questions being
# latest_question_list
class IndexView(generic.ListView):
    template_name = 'polls/index.html'

    # 2 This defines the question list we want to use
    context_object_name = 'latest_question_list'

    # 8 Replace get_queryset and don't return questions
    #  published in the future
    '''
    def get_queryset(self):

        # 2 Return the last 5 questions entered
        return Question.objects.order_by('-pub_date')[:5]
    '''

    def get_queryset(self):

        # 8 Return only questions with a pub_date less than
        # or equal to now
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

        # 8 Add Choices to the Admin in admin.py

# 2 The DetailView displays the details on your object
# being the Question model

# 2 The generic view expects the pk (Primary Key) value
# from the URL to be called pk as we set in polls/urls.py
class DetailView(generic.DetailView):
    model = Question

    # 2 Define the template to use with this data
    template_name = 'polls/detail.html'

    # 12 Exclude questions that are not published yet
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

    # 12 Add tests in polls/tests.py

# 2
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# 2 Remove these functions

'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'polls/index.html', context)

def detail(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/results.html', {'question': question})
'''

# 2 Vote stays the same
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# 3 Now we will explore automated testing. You can either
# check your code by entering values randomly (and miss
# a bunch of errors), or you can automate the process.

# 3 We'll now explore a bug in the was_published_recently() function
# in polls/models.py in the shell : python3 manage.py shell

# 3 Create a Question with a pub_date in the future
'''
import datetime
from django.utils import timezone
from polls.models import Question
future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
future_question.was_published_recently()
Returns true even though that doesn't make sense
'''

# 3 Open the file called tests.py


# ---------- /polls/tests.py ----------

from django.test import TestCase

# 4 Import your needed modules
import datetime
from django.utils import timezone
from django.test import TestCase

from .models import Question

# 4 TestCase runs tests without effecting your data
# by creating a temporary database for testing
class QuestionMethodTests(TestCase):

    # 4 Put the code used in the shell here
    # Start the method name with test
    def test_was_published_recently_with_future_question(self):

        # 4 Create a time 30 days in the future
        time = timezone.now() + datetime.timedelta(days=30)

        # 4 Create a question using the future time
        future_question = Question(pub_date=time)

        # 4 Check to see if the output is False like we expect
        self.assertIs(future_question.was_published_recently(), False)

        # 4 Run the test in the terminal
        # python3 manage.py test polls
        # You'll see that the test failed

        # 4 Fix the bug in models.py

    # 6 Return false if pub_date is older then 1 day

    def test_was_published_recently_with_old_question(self):
        # Should return false if pub_date is older then 1 day
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    # 6 Return True if published within the last day

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    # 6 Test with : python3 manage.py test polls

    # 7 We can simulate user interaction at the view level in the shell
    # python3 manage.py shell
    '''
    # This allows us access variable values in our templates
    # We will be using our real database here
    from django.test.utils import setup_test_environment
    setup_test_environment()

    # Create the client that we'll use to run our app
    from django.test import Client
    client = Client()

    # Get the status code from localhost:8000/
    response = client.get('/')
    response.status_code

    # Get the status code for localhost:8000/polls/
    from django.urls import reverse
    response = client.get(reverse('polls:index'))
    response.status_code

    # Get the HTML content
    response.content

    # Get the value of latest_question_list
    response.context['latest_question_list']
    '''

    # 7 Let's update polls/views.py so it doesn't show
    # questions published in the future

    # 10 Create a function that creates questions at
    # a specified date

    def create_question(question_text, days):
        time = timezone.now() + datetime.timedelta(days=days)
        return Question.objects.create(question_text=question_text,
                                       pub_date=time)

# 10 Add more question tests

class QuestionViewTests(TestCase):

    # 10 Test to see what happens if there are no questions
    def test_index_view_with_no_questions(self):

        # Get the client
        response = self.client.get(reverse('polls:index'))

        # Check the status code
        self.assertEqual(response.status_code, 200)

        # Verify that response contains this string
        self.assertContains(response, "No polls are available.")

        # Check if latest_question_list is empty
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    # 10 Make sure questions with a pub_date in past are shown
    def test_index_view_with_a_past_question(self):

        # Create sample question
        create_question(question_text="Past question.", days=-30)

        # Get client
        response = self.client.get(reverse('polls:index'))

        # Verify that the question shows
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    # 10 Make sure questions with future pub_date don't show
    def test_index_view_with_a_future_question(self):

        # Create question
        create_question(question_text="Future question.", days=30)

        # Get client
        response = self.client.get(reverse('polls:index'))

        # Verify response contains text
        self.assertContains(response, "No polls are available.")

        # Verify that latest_question_list is empty
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    # 10 Verify that if past and future questions exist that only
    # past show
    def test_index_view_with_future_question_and_past_question(self):

        # Create questions
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)

        # Get client
        response = self.client.get(reverse('polls:index'))

        # Verify that question list only contains past questions
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    # 10 Make sure question list shows multiple questions
    def test_index_view_with_two_past_questions(self):

        # Create questions
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)

        # Create client
        response = self.client.get(reverse('polls:index'))

        # Verify that both questions show
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )

# 11 Make sure future questions can't be accessed if the user
# guess the URL in polls/views.py

# 13 Add tests to make sure future posts aren't shown in detail

class QuestionIndexDetailTests(TestCase):

    # 13 Make sure future question detail pages show 404
    def test_detail_view_with_a_future_question(self):

        # Create question
        future_question = create_question(question_text='Future question.', days=5)

        # Open url using the future question in the url
        url = reverse('polls:detail', args=(future_question.id,))

        # Get client response
        response = self.client.get(url)

        # Verify that it returns 404
        self.assertEqual(response.status_code, 404)

    # 13 Verify that past questions show in detail
    def test_detail_view_with_a_past_question(self):

        # Create question
        past_question = create_question(question_text='Past Question.', days=-5)

        # Open url with past question
        url = reverse('polls:detail', args=(past_question.id,))

        # Get response
        response = self.client.get(url)

        # Verify the question shows
        self.assertContains(response, past_question.question_text)


# ---------- /polls/models.py ----------

from django.db import models

import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)

    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # 5 return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        # 5 Fix the code
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

        # 5 Now the test will pass

        # 5 Add further tests to polls/tests.py

class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# ---------- /polls/admin.py ----------

from django.contrib import admin

# 9 Add choice to imports

from .models import Question, Choice

admin.site.register(Question)

# 9 Add Choice to the Admin page
admin.site.register(Choice)

# 9 Create some future questions

# 9 Add some tests in polls/tests.py
