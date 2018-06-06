import random
import math
import os
from decimal import Decimal as D
import sum
from sum import getSum
from functools import reduce
import threading
import time
import re
import tkinter


'''
#Hei you!
name = input("What is your name?")
print("Hello ", name)
'''
'''
#Math between numbers
num1, num2 = input('Enter 2 numbers: ').split()

num1 = int(num1)
num2 = int(num2)

sum = num1 + num2
diffrence = num1 - num2
product = num1 * num2
quotient = num1 / num2
remainder = num1 % num2

print("{} + {} = {}".format(num1,num2,sum))
print("{} - {} = {}".format(num1,num2,diffrence))
print("{} * {} = {}".format(num1,num2,product))
print("{} / {} = {}".format(num1,num2,quotient))
print("{} % {} = {}".format(num1,num2,remainder))
'''
'''
#miles to Km
miles = input('Enter number of miles: ')
miles = int(miles)
kmForMiles = miles * 1.60934
print("The excange of {}  miles is: {} Km".format(miles,kmForMiles))
'''
'''
#Calculator
num1, operator, num2 = input("Enter calculation: ").split()
num1 = int(num1)
num2 = int(num2)

#sub
if operator == "+":
    print("{}+{} = {}".format(num1, num2, (num1+num2)))
#sub
elif operator == "-":
    print("{}+{} = {}".format(num1, num2, (num1-num2)))
#mul
elif operator == "*":
    print("{}*{} = {}".format(num1, num2, (num1*num2)))
#div
elif operator == "/":
    print("{}/{} = {}".format(num1, num2, (num1/num2)))
#rem
elif operator == "%":
    print("{}%{} = {}".format(num1, num2, (num1%num2)))
#conditions
elif operator == "<":
    print("{}<{} = {}".format(num1, num2, (num1<num2)))
elif operator == ">":
    print("{}>{} = {}".format(num1, num2, (num1>num2)))
elif operator == "=":
    print("{}=={} = {}".format(num1, num2, (num1==num2)))
elif operator == "!=":
    print("{}!={} = {}".format(num1, num2, (num1!=num2)))
elif operator == "<=":
    print("{}<={} = {}".format(num1, num2, (num1<=num2)))
elif operator == ">=":
    print("{}>={} = {}".format(num1, num2, (num1>=num2)))

else:
    print("Use either + - * / % = > < ! next time!")
'''
'''
#importamt ages1
age = eval(input("Enter age: "))
imp = "your age is {}, your age is important!".format(age)
notImp = "your age is {}, your age is not important!".format(age)
if age == 18 or age == 21 or age == 50:
    print(imp)
elif age >= 65:
    print(imp)
else:
    print(notImp)
'''
'''
#importamt ages2
age = eval(input("Enter age: "))
imp = "your age is {}, your age is important!".format(age)
notImp = "your age is {}, sorry, but your age is not important!".format(age)

if (age >= 1) and (age <= 18):
    print(imp)
elif (age == 21) or (age == 50):
    print(imp)
elif not(age < 65):
    print(imp)
else:
    print(notImp)
'''
'''
age = eval(input("Enter age: "))
if age > 0:
    if (age >=1) and (age <= 5):
        print("you should be in kindergarten")
    elif (age >= 6) and (age <= 17):
        print("you should be in 1th-12th grade")
    else:
        print("you should be in college")
else:
    print("you haven't birth yet...")
'''
'''
#grades by age
age = eval(input("Enter age: "))
if age < 5:
    print("you are too young for School")
elif age == 5:
    print("go to kindergarten")
elif (age>5) and (age<=17):
    grade = age - 5
    print("you should be in {}th grade".format(grade))
else:
    print("you should be in college")
'''
'''
#check odds
i = 2
for i in range(1, 21):
    if (i%2) != 0:
        print("i= ",i)
'''
'''
#round to 2 decimals
your_float = input("Enter a float: ")

your_float = float(your_float)

print("Round to 2 decimals : {:.2f}".format(your_float))
'''
'''
#investment
investment = input("Enter your investment amount: ")
interest = input("Interest rate: ")
investment = float(investment)
interest = float(interest) * .01
for i in range(10):
    investment = investment + (investment * interest)
print("Investment after 10 years: {:.2f}".format(investment))
'''
'''
#float nonsens
i = .11111111111111111111111111111111
j = .00000000000000010000000000000001

print("Answer : {:.32}".format(i+j))
'''
'''
#order
print("3 + 4 * 5 = {}".format(3+4*5))
print("(3 + 4) * 5 = {}".format((3+4)*5))
'''
'''
#random numbers
rand_num = random.randrange(1,51)
i = 1
while (i != rand_num-1):
    i += 1
    print("The random value is bigger than : ", i)
print("The random value is : ", rand_num)
'''
'''
#odd value while loop
i = 1
while i <= 50:
    if (i%2) == 0:
        i += 1
        continue
    if i == 15:
        i += 1
        continue
    if i == 47:
        i += 1
        break
    else:
        print("Odd value: ",i)
        i += 1
'''
'''
#hashes pine tree
tree_height = input("How tall is the tree: ")
tree_height = int(tree_height)
spaces = tree_height-1
hashes = 1
stump_spaces = tree_height-1
counter = 0
while tree_height != 0:
    for i in range(spaces):
        print(' ', end="")
    for i in range(hashes):
        print('#', end="")
    print()
    spaces -= 1
    hashes += 2
    tree_height -= 1
    counter += 1
for i in range(stump_spaces):
    print(' ', end="")
print("#")
'''
'''
#basic exeption handling
while True:
    try:
        number = int(input("Please enter a number: "))
        break
    except ValueError:
        print("you didn't enter a number")
    except:
        print("Unknown error occurred")
print("Thank you for entering a number")
'''
'''
#secret number
secret_number = random.randrange(1,11)

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if (guess == secret_number):
        print("You guessed it!")
        break
'''
'''
# ---------- MATH MODULE ----------
# Python provides many functions with its Math module

# Because you used import you access methods by referencing the module
print("ceil(4.4) = ", math.ceil(4.4))
print("floor(4.4) = ", math.floor(4.4))
print("fabs(-4.4) = ", math.fabs(-4.4))

# Factorial = 1 * 2 * 3 * 4
print("factorial(4) = ", math.factorial(4))

# Return remainder of division
print("fmod(5,4) = ", math.fmod(5, 4))

# Receive a float and return an int
print("trunc(4.2) = ", math.trunc(4.2))

# Return x^y
print("pow(2,2) = ", math.pow(2, 2))

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
print("log(1000,10) = ", math.log(1000, 10))

# You can also use base 10 like this
print("log10(1000) = ", math.log10(1000))

# We have the following trig functions
# sin, cos, tan, asin, acos, atan, atan2, asinh, acosh,
# atanh, sinh, cosh, tanh

# Convert radians to degrees and vice versa
print("degrees(1.5708) = ", math.degrees(1.5708))
print("radians(90) = ", math.radians(90))
'''
'''
#diffrence between decimal and float
sum = D(0)
sum += D("0.1")
sum += D("0.1")
sum += D("0.1")
sum -= D("0.3")

print("sum = ", sum)

print(".1+.1+.1-.3", .1+.1+.1-.3)
'''
'''
#strings
print(type(3))
print(type(3.14))
print(type("3"))
print(type('3'))

samp_string = "This is a very important string"

print(samp_string[0])
print(samp_string[-1])
print(samp_string[3+5])
print("Length: ",len(samp_string))
print(samp_string[8:])
print("green " + "eggs")
print("Hello" * 5)
num_string = str(4)
print(num_string)
for char in samp_string:
    print(char, end="!~!")

    for i in range(0, len(samp_string)-1, 2):
        print(samp_string[i] + samp_string[i+1])

#A - Z 65-90
#a -z 97-122

print("A = ", ord("A"))
print("65 = ", chr(65))
'''
'''
# ---------- PROBLEM : SECRET STRING ----------
norm_string = input("Enter a string to hide in uppercase: ")

secret_string = ""

for char in norm_string:
    secret_string += str(ord(char))

print("Secret Message :", secret_string)

norm_string = ""

for i in range(0, len(secret_string)-1, 2):
    char_code = secret_string[i] + secret_string[i+1]
    norm_string += chr(int(char_code))

print("Original Message :", norm_string)
'''
'''
# ---------- PROBLEM : SECRET STRING with lowercase ----------

norm_string = input("Enter a string to hide in uppercase: ")

secret_string = ""

for char in norm_string:
    secret_string += str(ord(char)-23)

print("Secret Message :", secret_string)

norm_string = ""

for i in range(0, len(secret_string)-1, 2):
    char_code = secret_string[i] + secret_string[i+1]
    norm_string += chr(int(char_code) +23)

print("Original Message :", norm_string)
'''
'''
#homework answer1
text = input('insert your text')
for i in range(0, len(text)):
    print(ord(text[i]),' ',end='')
print()
for i in range(0, len(text)):
    print(chr(ord(text[i])),end='')
'''
'''
#cool encryption
#char_code = secret_string[i] + secret_string[i+1] + secret_string[i+2]

#homework solution2
secretMsg = ""
newMsg = ""
myMsg = input("Enter a message: ")
for char in myMsg:
    secretMsg += str(ord(char) + 1000)
    print("\n" + secretMsg)

for i in range(0, len(secretMsg)-1, 4):
    charCode = secretMsg[i] + secretMsg[i+1] + secretMsg[i+2] + secretMsg[i+3]
    newMsg += chr(int(float(charCode) - 1000))

print(newMsg)
'''
'''
rand_string = "   this is an iMPOrtant string   "
rand_string = rand_string.lstrip()
print(rand_string)
rand_string = rand_string.rstrip()
print(rand_string)
rand_string = rand_string.strip()
print(rand_string)

print(rand_string.capitalize())

print(rand_string.upper())

print(rand_string.lower())

a_list = ["Bunch", "of", "random", "words"]
print(" ".join(a_list))

a_list2 = rand_string.split()
for i in a_list2:
    print(i)

print("how many is: ", rand_string.count("is"))

print("Where is string: ", rand_string.find("string"))

print(rand_string.replace("an ", "a kind of "))
'''

'''
# ---------- PROBLEM : ACRONYM GENERATOR ----------
# You will enter a string and then convert it to an acronym
# with uppercase letters like this

Convert to Acronym : Random Access Memory
RAM


orig_string = input("Convert to acronym: ")

orig_string = orig_string.upper()

orig_string_as_list = orig_string.split()

for i in orig_string_as_list:
    print(i[0], end="")

print()
'''

'''
letter_z = "z"
num_3 = "3"
a_space = " "
pi = "3.14"
print("Is z a letter or number", letter_z.isalnum())
print("Is z a letter : ", letter_z.isalpha())
print("Is 3 a number : ", num_3.isdigit())
print("Is z a lowercase : ", letter_z.islower())
print("Is z a uppercase : ", letter_z.isupper())
print("Is space a space : ", a_space.isspace())


def isfloat(str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False

print("Is Pi a float : ", isfloat(pi))
'''
'''
message = input("Enter the string you want to encrypt: ")
key = int(input("Enter the key of encrypting(1-26): "))

def Encrypt(message, key):

    secret_message = ""

    for char in message:

        if char.isalpha():

            char_code = ord(char)
            char_code += key


            if char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26

                if char_code < ord('A'):
                    char_code += 26

            else:
                if char_code > ord('z'):
                    char_code -= 26

                if char_code < ord('a'):
                    char_code += 26

            secret_message += chr(char_code)

        else:
            secret_message += char

    print("Encrypted : ", secret_message)

    return secret_message


def Decrypt(secret_message, key):

    key = -key
    secret_message = ""
    orig_message = ""

    for char in secret_message:

        if char.isalpha():

            char_code = ord(char)
            char_code += key


            if char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26

                if char_code < ord('A'):
                    char_code += 26

            else:
                if char_code > ord('z'):
                    char_code -= 26

                if char_code < ord('a'):
                    char_code += 26

            orig_message += chr(char_code)

        else:
            orig_message += char

    print("Decrypted : ", orig_message)



Encrypt(message, key)
secret_message = Encrypt(message, key)
Decrypt(secret_message, key)
'''


'''
def add_numbers(num_1, num2):
    return num_1 + num2

print("5 + 4 =", add_numbers(5, 4))

def assign_name():
   name = "Doug"

gbl_name = "Sally"

def change_name():
    global gbl_name
    gbl_name = "Sammy"

change_name()

print(gbl_name)
'''
'''
def get_sum(num1, num2):
    sum = num1 + num2
    return sum

print(get_sum(5,4))
'''
'''
def solv_eq(equation):
    x, add, num1, eq, num2 = equation.split()

    num1, num2 = int(num1), int(num2)

    return "x = " + str(num2 - num1)

print(solv_eq("x + 3 = 7"))
print(solv_eq("x + 3 = 9"))
print(solv_eq("x + 3 = 11"))
print(solv_eq("x + 3 = 13"))
'''
'''
def mult_divide(num1, num2):
    return (num1*num2), (num1/num2)

mult, divide = mult_divide(5,4)

print("5 * 4 = ", mult)
print("5 / 4 = ", divide)
'''
'''
def is_prime(num):
    for i in range(2, num):
        if(num % i) == 0:
            return False
        if(num % i) >= 1:
            return True

    return True

def get_primes(max_number):
    list_of_primes = []

    for num1 in range(2, max_number):
        if is_prime(num1):
            list_of_primes.append(num1)

    return list_of_primes


max_num_to_check = int(input("Search for Primes up to: "))

list_of_primes = get_primes(max_num_to_check)

for prime in list_of_primes:
    print(prime)
'''
'''
def sumAll(*args):
    sum = 0

    for i in args:
        sum += i
    return sum

print("Sum : ", sumAll(1,2,3,4,5))

'''
'''
def get_area(shape):
    shape = shape.lower()

    if shape == "rectangle" or shape == "מרובע":
        rectangle_area()
    elif shape == "circle" or shape == "עיגול":
        circle_area()
    elif shape == "parallelogram" or shape == "מקבילית":
        parallelogram_area()
    elif shape == "rhombus" or shape == "מעוין":
        rhombus_area()
    elif shape == "triangle" or shape == "משולש":
        triangle_area()
    elif shape == "trapezoid" or shape == "טרפז":
        trapezoid_area()
    else:
        print("Pleas enter rectangle or circle")


def rectangle_area():
    length = float(input("Enter a length : "))
    width = float(input("Enter a width : "))
    area = length * width

    print("The area of the rectangle is שטח המרובע הוא : ", area)



def circle_area():
    radius = float(input("Enter a radius : "))
    area = math.pi * (math.pow(radius, 2))
    print("The area of the circle is : {:.2f}".format(area))

def parallelogram_area():
    length = float(input("Enter a length : "))
    heigth = float(input("Enter a heigth : "))
    area = length * heigth
    print("The area of the parallelogram is : {:.2f}".format(area))


def rhombus_area():
    slant1 = float(input("Enter a slant 1 : "))
    slant2 = float(input("Enter a slant 2 : "))
    area = slant1 * slant2 / 2
    print("The area of the rhombus is : {:.2f}".format(area))


def triangle_area():
    side = float(input("Enter one side of the triangle : "))
    heigth = float(input("Enter a heigth : "))
    area = side * heigth / 2
    print("The area of the triangle is : {:.2f}".format(area))


def trapezoid_area():
    par_side1 = float(input("Enter the 1st parallel side of the trapezoid : "))
    par_side2 = float(input("Enter 2nd parallel side of the trapezoid : "))
    heigth = float(input("Enter a heigth : "))
    sides = float(par_side1 + par_side2)
    area = sides * heigth / 2
    print("The area of the trapezoid is : {:.2f}".format(area))


def main():
    shape_type = input("Get area for what shape : ")

    get_area(shape_type)


main()
'''

'''
randList = ["string", 1.234, 28]

oneToTen = list(range(10))

randList = randList + oneToTen

print(randList[0])

print("List Length: ", len(randList))

first3 = randList[0:3]

for i in first3:
    print("{} : {}".format(first3.index(i), i))

print(first3[0] * 3)

print("string" in first3)

print("Index of string: ", first3.index("string"))

print("how many strings: ", first3.count("string"))

first3[0] = "New string"

for i in first3:
    print("{} : {}".format(first3.index(i), i))

first3.append("Another")

for i in first3:
    print("{} : {}".format(first3.index(i), i))
'''
'''
numList = []
for i in range(5):
    numList.append(random.randrange(1,10))

for i in numList:
    print("{} : {}".format(numList.index(i), i))
'''


'''
numList = []
for i in range(5):
    numList.append(random.randrange(1,10))

i = len(numList) - 1

while i > 1:

    j = 0

    while j < i:

        print("\nIs {} > {}".format(numList[j], numList[j + 1]))

        if numList[j] > numList[j + 1]:

            print("Switch")

            temp = numList[j]
            numList[j] = numList[j + 1]
            numList[j + 1] = temp
        else:
            print("Don't Switch")

        j += 1

        for k in numList:
            print(k, end=", ")
        print()

    print("END OF ROUND")

    i -= 1

for k in numList:
    print(k, end=", ")

print()
'''
'''
numList = []
for i in range(5):
    numList.append(random.randrange(1,10))

numList.sort()

numList.reverse()

numList.insert(5, 10)

numList.remove(10)

numList.pop(2)



for k in numList:
    print(k, end=", ")
'''
'''
evenList = [i*2 for i  in range(10)]

for i in evenList:
    print(i)
'''
'''
numList = [1,2,3,4,5]

listOfValues = [[math.pow(m, 2),math.pow(m, 3),math.pow(m, 4)]
                for m in numList]

for i in listOfValues:
    print(i)

print()
'''

'''
multiDList = [[0] * 10 for i in range(10)]

multiDList[0][1] = 10

print(multiDList[1][1])
'''

'''
listTable = [[0] * 4 for i in range(4)]

for i in range(4):
    for j in range(4):
        listTable[i][j] = "{} : {}".format(i,j)

for i in range(4):
    for j in range(4):
        print(listTable[i][j], end=" || ")
    print()
'''

'''
multTable = [[0] * 10 for i in range(10)]

for i in range(1, 10):
    for j in range(1, 10):
        multTable[i][j] = i * j

for i in range(1, 10):
    for j in range(1, 10):
        print(multTable[i][j], end=",   ")
    print()
'''
'''
derekDict = {"fName": "Derek", "lName": "Banas", "address": "123 Main St"}

print("My Name : ", derekDict["fName"])

derekDict["address"] = "215 North St"

print(derekDict)

derekDict['city'] = 'Tel Aviv'

print(derekDict)

print("Is there a city : ", "city" in derekDict)


print(derekDict.values())

print(derekDict.keys())

for k, v in derekDict.items():
    print(k,v)

print(derekDict.get("lName", "Not Here"))
print(derekDict.get("mName", "Not Here"))

del derekDict["fName"]

print(derekDict)

for i in derekDict:
    print(i)

derekDict.clear()
print(derekDict)

employees = []

while True:
    try:
        fName, lName = input("Enter Employee Name : ").split()
        employees.append({'fName' : fName, 'lName' : lName})

        print(employees)
        break
    except:
        print("An unknown error occurred")
'''

'''
customers = []

while True:
    createEntry = input("Enter Customer? (Yes/No) : ")
    createEntry = createEntry[0].lower()

    if createEntry == 'n' or createEntry == 'no':
        break
    else:
        while True:
            try:
                fName, lName = input("Enter Customer Name : ").split()
                customers.append({'fName' : fName, 'lName' : lName})
                break
            except:
                print("pleas Insert first and last name!")

for cust in customers:
    print(cust['fName'], cust['lName'])
'''
'''
#3! = 3 * 2 * 1

def factorial(num):
    if num <= 1:
        return 1
    else:
        result = num * factorial(num - 1)
        return result

print("4! = ",factorial(4))
'''
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
print(fib(13))
print(fib(30))
'''

'''
with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nMore random text\nAnd some more")


with open("mydata.txt", encoding="utf-8") as myFile:
    print(myFile.read())

print(myFile.closed)

print(myFile.name)

print(myFile.mode)

os.rename("mydata.txt", "mydata2idan.txt")

os.remove("mydata2idan.txt")

os.mkdir("mydir")

os.chdir("mydir")

print("Current Directory :", os.getcwd())

os.chdir("..")

os.rmdir("mydir")
'''
'''
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib(n-1) + fib(n-2)
        return result

numFibValues = int(input("How many Fibonacci values should be found : "))

i = 1

while i < numFibValues:
    fibValue = fib(i)
    print(fibValue)
    i += 1

print("All Done!")
'''
'''
with open("mydata2.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nMore random text\nAnd some more")

with open("mydata2.txt", encoding="utf-8") as myFile:

    lineNum = 1

    while True:
        line = myFile.readline()
        if not line:
            break

        #print("Line", lineNum, " : ", line, end="")
        print("Line", lineNum)

        wordList = line.split()

        print("Number of Words : ", len(wordList))

        charCount = 0

        for word in wordList:
            for char in word:
                charCount += 1

        avgNumChars = charCount / len(wordList)

        print("Avg Word Length : {:.2}".format(avgNumChars))

        lineNum += 1
'''

'''
myTuple = (1,2,3,4,5)

print("1st Value : ", myTuple[0])

print(myTuple[0:3])

print("Tuple Length : ", len(myTuple))

moreFibs = myTuple + (13, 21, 34)

print("34 in Tuple :", 34 in moreFibs)

for i in moreFibs:
    print(i)

aList = [89, 55, 144]
aTuple = tuple(aList)

aList = list(aTuple)

print("Min :", min(aTuple))
print("Max :", max(aTuple))
'''
'''
class Dog:

    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print("{} the dog runs".format(self.name))

    def eat(self):
        print("{} the dog eats and gain one Kg more, so now his weight is {}".format(self.name, (self.weight+1)))

    def bark(self):
        print("{} the dog barks".format(self.name))


def main():
    spot = Dog("Spot", 66, 26)

    spot.bark()
    spot.eat()

    bowser = Dog()
    bowser.name = "Bowser"

    bowser.eat()


main()
'''

'''
class Square:

    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    @property
    def height(self):
        print("Retrieving the height")

        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Please only entr numbers for height.")

    @property
    def width(self):
        print("Retrieving the width")

        return self.__width

    @height.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please only entr numbers for width.")

    def getArea(self):
        return int(self.__height) * int(self.__width)

def main():
    aSquare = Square()

    height = input("Enter height : ")
    width = input("Enter width : ")

    aSquare.height = height
    aSquare.width = width

    print("height : ", aSquare.height)
    print("Width : ", aSquare.width)
    print("The Area is :", aSquare.getArea())


main()
'''

'''
class Warrior:
    def __init__(self, name="warrior", health=0, attkMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax

    def attack(self):
        attkAmt = self.attkMax * (random.random() + .5)

        return attkAmt

    def block(self):
        blockAmt = self.blockMax * (random.random() + .5)

        return blockAmt

class Battle:
    def startFight(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break
            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break

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

    paul = Warrior("Paul", 50, 20, 10)
    sam = Warrior("Sam", 50, 20, 10)

    battle = Battle()

    battle.startFight(paul, sam)

main()
'''



'''
class Animal:

    def __init__(self, birthType="Unknown", appearance="Unknown", blooded="Unknown"):
        self.__birthType = birthType
        self.__appearance = appearance
        self.__blooded = blooded


    @property
    def birthType(self):
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




    def __str__(self):
        return "A {} is {} it is {} it is {}".format(type(self).__name__,
                                                          self.birthType,
                                                          self.appearance,
                                                          self.blooded)

class Mammal(Animal):
        def __init__(self, birthType="born live",
                     appearance = "hair or fur",
                     blooded= "warm blooded",
                     nurseYoung=True):

            Animal.__init__(self, birthType, appearance, blooded)

            self.__nurseYoung = nurseYoung

        @property
        def nurseYoung(self):
            return self.__nurseYoung

        @nurseYoung.setter
        def nurseYoung(self, nurseYoung):
            self.__nurseYoung = nurseYoung

        def __str__(self):
            return super().__str__() + " and it is {} they nurse their young".format(self.nurseYoung)



class Reptile(Animal):
    def __init__(self, birthType="born in an egg or born alive",
                 appearance="dry scales",
                 blooded="cold blooded"):

        Animal.__init__(self, birthType, appearance, blooded)

    def sumAll(self, *args):
        sum = 0
        for i in args:
            sum += i
        return sum

def getBirthType(theObject):
    print("The {} is {}".format(type(theObject).__name__,
                                theObject.birthType))

def main():

    animal1 = Animal("born alive")
    print(animal1.birthType)
    print(animal1)
    print()

    mammal1 = Mammal()
    print(mammal1.birthType)
    print(mammal1.appearance)
    print(mammal1.blooded)
    print(mammal1.nurseYoung)
    print(mammal1)


    reptile1 = Reptile()
    print(reptile1.birthType)
    print(reptile1)

    print("Sum : {}".format(reptile1.sumAll(1,2,3,4,5)))

    def getBirthType(theObject):
        print("The {} is {}".format(type(theObject).__name__,
                                theObject.birthType))

    getBirthType(mammal1)
    getBirthType(reptile1)





main()
'''


'''
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

    def __str__(self):
        return "{}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)

    def __add__(self, other_time):
        new_time = Time()

        if(self.second + other_time.second) > 60:
            self.minute += 1
            new_time.second = (self.second + other_time.second) - 60
        else:
            new_time.second = self.second - other_time.second


        if(self.minute + other_time.minute) > 60:
            self.hour += 1
            new_time.minute = (self.minute + other_time.minute) - 60
        else:
            new_time.minute = self.minute - other_time.minute


        if(self.hour + other_time.hour) > 24:
            new_time.hour = (self.hour + other_time.hour) - 24
        else:
            new_time.hour = self.hour - other_time.hour

        return new_time

def main():
    time1 = Time(1, 20, 30)
    print(time1)

    time2 = Time(24,41,30)
    print(time1 + time2)
main()
'''
'''
class Sum:
    @staticmethod
    def getSum(*args):

        sum = 0

        for i in args:
            sum += i

        return sum

def main():
    print("Sum : ", Sum.getSum(1,2,3,4,5))

main()
'''

'''
class Dog:
    num_of_dogs = 0

    def __init__(self, name="Unknown"):
        self.name = name

        Dog.num_of_dogs += 1

    @staticmethod
    def getNumOfDogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))


def main():
    spot = Dog("Spot")

    doug = Dog("Doug")

    spot.getNumOfDogs()
    doug.getNumOfDogs()

main()
'''
'''
print("Sum: ", sum.getSum(1,2,3,4,5))

print("Sum: ", getSum(1,2,3,4,5))
'''
'''
try:
    aList = [1,2,3]

    print(aList[3])

except(IndexError, NameError):
    print("Sorry that index and name doesn't exist")

except:
    print("An unknown error occurred")
'''


'''
class DogNameError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

try:
    dogName = input("What is your dogs name : ")

    if any(char.isdigit() for char in dogName):
        raise DogNameError

except DogNameError:
     print("Your dogs name can't contain a number")
'''

'''
num1, num2 = input("Enter to values to divide : ").split()

try:
    qoutient = int(num1) / int(num2)

    print("{}/{}={}".format(num1, num2, qoutient))

except ZeroDivisionError:
    print("You can't divide by zero")

else:
    print("You didn't raise an exception")

finally:
    print("I execute no matter what")
'''

'''
try:
    myFile = open("mydata3.txt", encoding="utf-8")

except FileNotFoundError as ex:
    print("That file was not found")
    print(ex.args)

else:
    print("File: ", myFile.read())
    myFile.close()

finally:
    print("Finish working with file")

'''

'''
def mult_by_2(num):
    return num * 2

times_two = mult_by_2

#print("4 * 2 = ", times_two(4))

def do_math(func, num):
    return func(num)

print("8 * 2 =", do_math(mult_by_2, 8))



def get_func_mult_by_num(num):
    def mult_by(value):
        return num * value
    return mult_by
generated_func = get_func_mult_by_num(5)

print("5*10 =", generated_func(10))


listOFuncs = [times_two, generated_func]
print("5 * 9 =", listOFuncs[0](9))
'''

'''
def isOdd(num):
    if num%2 == 0:
        return False
    else:
        return True

def change_list(list, func):
    oddList = []

    for i in list:
        if func(i):
            oddList.append(i)
            i += 1
    return oddList


aList = range(1,20)

print(change_list(aList, isOdd))
'''

'''
def random_func(name: str, age: int, weight:float) -> str:
    print("Name :", name)
    print("Age :", age)
    print("Weight :", weight)
    return "{} is {} years old and weighs {}".format(name, age, weight)

print(random_func("Derek", 41, 165.5))
print(random_func(89, "Derek", "Turtle"))
print(random_func.__annotations__)
'''

'''
sum = lambda x,y : x + y

print("Sum : ", sum(4,5))


can_vote = lambda age: True if age >= 18 else False
print("Can Vote :", can_vote(19))


power_list = [lambda x: x **2,
              lambda x: x **3,
              lambda x: x **4,
              lambda x: x **5]


for func in power_list:
    print(func(2))

'''
'''
attack = {'quick': (lambda: print("Quick Attack")),
           'power': (lambda: print("Power Attack")),
           'miss': (lambda: print("The Attack Missed"))}

attack['quick']()

import random

attackKey = random.choice(list(attack.keys()))

attack[attackKey]()
'''
'''
flipList = []
for i in range(1, 101):
    flipList += random.choice(['H', 'T'])


print("Heads :", flipList.count('H'), "Tiles : ", flipList.count('T'))
'''


'''
# ---------- MAP ----------
# Map allows us to execute a function on each item in a list

# Generate a list from 1 to 10
oneTo10 = range(1, 11)

# The function to pass into map
def dbl_num(num):
    return num * 2


print(list(map(dbl_num, oneTo10)))


print(list(map((lambda x: x * 3), oneTo10)))

# You can perform calculations against multiple lists
aList = list(map((lambda x, y: x + y), [1, 2, 3], [1, 2, 3, 4]))
print(aList)


def mult_board():
    print(list(map((lambda x: x * 1), oneTo10)))
    print(list(map((lambda x: x * 2), oneTo10)))
    print(list(map((lambda x: x * 3), oneTo10)))
    print(list(map((lambda x: x * 4), oneTo10)))
    print(list(map((lambda x: x * 5), oneTo10)))
    print(list(map((lambda x: x * 6), oneTo10)))
    print(list(map((lambda x: x * 7), oneTo10)))
    print(list(map((lambda x: x * 8), oneTo10)))
    print(list(map((lambda x: x * 9), oneTo10)))
    print(list(map((lambda x: x * 10), oneTo10)))


#mult_board()

#my first function alone!!!!!
def mult_board2(range_of_mult, rows):
    oneToWhat = range(1, range_of_mult+1)
    mult_param = 1

    while True:
        if mult_param <= rows:
            print(list(map((lambda x: x * mult_param), oneToWhat)))
            mult_param += 1
        else:
            break


mult_board2(10, 20)
'''

'''
print(list(filter((lambda x: x % 2 == 0), range(1,11))))
'''
'''
randlist = list(random.randint(1, 1001) for i in range(100))
print(list(filter((lambda x : x%9 == 0), randlist)))
'''

'''
print(reduce((lambda x, y: x + y), range(1, 6)))
'''

'''
sampStr = iter("Sample")

print("Char :", next(sampStr))
print("Char :", next(sampStr))
print("Char :", next(sampStr))
'''

'''
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
'''
'''
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

for i in range(50):
    print("Fib :", next(fibSeq))
'''


'''
print(list(map((lambda x: x*2), range(1, 11))))

print([2 * x for x in range(1, 11)])


print(list(filter((lambda x: x % 2 != 0), range(1, 11))))

print([x for x in range(1, 11) if x % 2 != 0])


print([i ** 2 for i in range(50) if i % 8 == 0])

print([x * y for x in range(1, 4) for y in range(11, 16)])
'''
'''
print([x for x in [i * 2 for i in range(10)] if x % 8 == 0])
'''

'''
print([x for x in [random.randint(1, 1001) for i in range(50)] if x % 9 == 0])
'''

'''
multiList = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

print([col[1] for col in multiList])


print([multiList[i][i] for i in range(len(multiList))])
'''

'''
def isprime(num):
    for i in range(2, num):
        if(num % i) == 0:
            return False
    return True

def gen_primes(max_number):
    for num1 in range(2, max_number):
        if isprime(num1):
            yield num1

prime = gen_primes(50)

print("Prime :", next(prime))
print("Prime :", next(prime))
print("Prime :", next(prime))
print("Prime :", next(prime))
print("Prime :", next(prime))
print("Prime :", next(prime))
'''

'''
double = (x * 2 for x in range(10))

print("Double :", next(double))
print("Double :", next(double))

for num in double:
    print(num)
'''

'''
def executeThread(i):
    print("Thread {} sleeps at {}".format(i,
                    time.strftime("%H:%M:%S", time.gmtime())))
    randSleepTime = random.randint(1, 5)
    time.sleep(randSleepTime)
    print("Thread {} stops sleeping at {}".format(i,
                    time.strftime("%H:%M:%S", time.gmtime())))
for i in range(10):
    thread = threading.Thread(target=executeThread, args=(i,))
    thread.start()
    print("Active Threads :", threading.activeCount())
    print("Thread Objects :", threading.enumerate())
'''

'''
class CustThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)

        self.name = name

    def run(self):
        getTime(self.name)

        print("Thread", self.name, "Excution Ends")


def getTime(name):
    print("Thread {} stops sleeping at {}".format(name,
                    time.strftime("%H:%M:%S", time.gmtime())))
    randSleepTime = random.randint(1, 5)
    time.sleep(randSleepTime)


thread1 = CustThread("1")
thread2 = CustThread("2")


thread1.start()
thread2.start()

print("\nThread 1 Alive :", thread1.is_alive())
print("Thread 2 Alive :", thread2.is_alive())

print("Thread 1 Name :", thread1.getName())
print("Thread 2 Name :", thread2.getName())

thread1.join()
thread2.join()

print("Execution Ends")
'''
'''
class BankAccount(threading.Thread):

    acctBalance = 100

    def __init__(self, name, moneyRequest):
        threading.Thread.__init__(self)
        self.name = name
        self.moneyRequest = moneyRequest

    def run(self):
        threadLock.acquire()
        BankAccount.getMoney(self)
        threadLock.release()

    @staticmethod
    def getMoney(customer):
        print("{} tries to withdrawal ${} at {}".format(customer.name,
                customer.moneyRequest,
                time.strftime("%H:%M:%S", time.gmtime())))

        if BankAccount.acctBalance - customer.moneyRequest > 0:
            BankAccount.acctBalance -= customer.moneyRequest
            print("New account balance : ${}".format(BankAccount.acctBalance))

        else:
            print("Not enough money in the account")
            print("Current balance : ${}".format(BankAccount.acctBalance))

        time.sleep(3)

threadLock = threading.Lock()

doug = BankAccount("Doug", 1)
paul = BankAccount("Paul", 100)
sally = BankAccount("Sally", 50)



doug.start()
paul.start()
sally.start()

doug.join()
paul.join()
sally.join()
'''

'''
if re.search("ape", "The ape was at the apex"):
    print("There is an ape")

allApes = re.findall("ape", "The ape was at the apex")

for i in allApes:
    print(i)
'''

'''
theStr = "The ape was at the apex"

for i in re.finditer("ape.", theStr):

    locTuple = i.span()

    print(locTuple)

    print(theStr[locTuple[0]:locTuple[1]])
'''

animalStr = "Cat rat mat pat"
'''
allAnimals = re.findall("[crmfp]at", animalStr)

for i in allAnimals:
    print(i)
'''
'''
somaAnimals = re.findall("[c-mC-M]at", animalStr)
somaAnimals = re.findall("[^Cr]at", animalStr)
for i in somaAnimals:
    print(i)
'''

'''
owlFood = "rat cat mat pat"

regex = re.compile("[cr]at")

owlFood = regex.sub("owl", owlFood)

print(owlFood)
'''

'''
randStr = "Here is \\stuff"

print("Find \\stuff : ", re.search("\\stuff", randStr))

print("Find \\stuff : ", re.search("\\\\stuff", randStr))

print("Find \\stuff : ", re.search(r"\\stuff", randStr))
'''
'''
randStr = "F.B.I. I.R.S. CIA"

print("Matches :", len(re.findall(".\..\..\.", randStr)))
'''
'''
randStr = """This is a long
string that goes
on for many lines"""

print(randStr)

# Remove newlines
regex = re.compile("\n")
randStr = regex.sub(" ", randStr)


print(randStr)
'''

'''
randStr = "12345"

print("Matches :", len(re.findall("\d{}", randStr)))
'''

'''
numStr = "123 12345 123456 1234567"

print("Matches :", len(re.findall("\d{5,7}", numStr)))


phNum = "412-555-1212"

if re.search("\w{3}-\w{3}-\w{4}", phNum):
    print("It is a phone number")

if re.search("\w{2,20}", "Ultraman"):
    print("It is a valid name")

if re.search("\w{2,20}\s\w{2,20}", "Toshio Muramatsu"):
    print("It is a valid full name")

print("Matches :", len(re.findall("a+", "a as ape bug")))

EmailIdan = "db@aol.com m@.com @apple.com db@.com t882200@gmail.com"

print("Email Matches :", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[a-zA-Z]{2,3}", EmailIdan)))
'''
'''
randStr = "cat cats"

regex = re.compile("[cat]+s?")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)
'''


'''
randStr = "doctor doctors doctor's"

regex = re.compile("[doctor]+['s]*")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)
'''

'''
#longStr = "Just some words and some more\r and more"



matches = re.findall("[\w\s]+[\r]?\n", longStr)

print("Matches :", len(matches))

for i in matches:
    print(i)
'''

'''
randStr = Just some words
and some more\r
and more


regex = re.compile("[\w\s]+[\r]?\n")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)
'''
'''
randStr = "<name>Life on Mars</name><name>Freaks and Geeks</name>"

regex = re.compile("<name>(.*?)</name>")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)
'''

'''
randStr = "ape at the apex"

regex = re.compile(r"\bape\b")

matches = re.findall(regex, randStr)

print(len(matches))
for i in matches:
    print(i)
'''

'''
randStr = "Match everything up to @"

regex = re.compile(r"^.*[^@]")

matches = re.findall(regex, randStr)

print(len(matches))
for i in matches:
    print(i)
'''


'''
randStr = "@ Get this string"

regex = re.compile(r"[^@\s].*$")

matches = re.findall(regex, randStr)

print(len(matches))
for i in matches:
    print(i)
'''
'''
randStr = "Ape is big
Turtle is slow
Cheetah is fast"

regex = re.compile(r"(?m)^.*?\s")

matches = re.findall(regex, randStr)

print("Matches :", len(matches))

for i in matches:
    print(i)
'''

'''
randStr = "My number is 412-555-1212"

regex = re.compile(r"412-(.*)")

matches = re.findall(regex, randStr)

print("Matches :", len(matches))

for i in matches:
    print(i)
'''

'''
randStr = "412-555-1212 412-555-1213 412-555-1214"

regex = re.compile(r"412-(.{8})")

matches = re.findall(regex, randStr)

print("Matches :", len(matches))

for i in matches:
    print(i)
'''

'''
randStr = "My number is 412-555-1212"

regex = re.compile(r"412-(.*)-(.*)")

matches = re.findall(regex, randStr)

print("Matches :", len(matches))

print(matches[0][0])
print(matches[0][1])
'''


































