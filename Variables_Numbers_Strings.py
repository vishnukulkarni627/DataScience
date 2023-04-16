# Variables
# Create a variable called break and assign it a value 5. see what happens and find out the
# reason behind the behaviour that you see
# break = 5
# print(break)
# Solution: break is a reserved keyword in python so we can't take it as a variable,
# Hence we will get invalid syntax

# --------------------------------------------------------------------------------------------------
# Create two variables. One to store your birth year and another one to store current year
# Now calculate your age using these two variables
# Logic: Current Year - Birth Year
birthyr = 1996
currentyr = 2023
Age = currentyr - birthyr
print(Age)  #27
# ------------------------------------------------------------------------------------------------------
# Store your first, middle and last name in three different variables and then print your full name
# using these variables
first = 'vishnu'
middle = 'k'
last = 'kulkarni'
fullName = f'{first} {middle} {last}'
print(fullName)
# --------------------------------------------------------------------------------------------------------
# Answer which of these are invalid names
# _nation = 5  #valid
# 1record = 5  #Invalid
# record1 = 5  #Valid
# record_one = 5  #valid
# record-one = 5  #Invalid
# record^one = 5 # Invalid
# continue = 5 #Invalid
# ----------------------------------------------------------------------------------------------------------
# Numbers
# You have a football field that is 92 meter long and 48.8 meter wide.
# Find out total area using python and print it
# Logic : length * width
length = 92
width = 48.8
area = length * width
total_area = round(area, 2)
print(total_area)
# ----------------------------------------------------------------------------------------------------
# You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and
# you gave shopkeeper 20 dollar.Find out using python how many dollars is the shopkeeper
# going to give you back
potato_per_pack = 1.49
qty = 9
potato_nine_pack = potato_per_pack * qty
cust_to_shopkeeper = 20
shopkeeper_to_customer_after_purchase = cust_to_shopkeeper - potato_nine_pack
print(shopkeeper_to_customer_after_purchase)
# --------------------------------------------------------------------------------------------------------
# You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length
# If tiles cost 500rs per sqaure feet, how much will be the total cost to replace all tiles
# Calculate and print the cost using python(Use power operator ** to find the area of square)
# ----------------------------------------------------------------------------------------------------------
# Print binary representation of number 17
print(format(17, 'b'))
# -----------------------------------------------------------------------------------------------------------
# Strings
# Create 3 variables to store street, city, country, now create address variable to store entire address
# Use two ways of creating this variable, one using + operator & the other using f-string
# Now print address in such a way that the street,city and country prints in a separate line
street = 'ganapathinagar'
city = 'Bangalore'
country = 'India'
address = street + ' ' +  city + ' ' + country
print(address)
address1 = f'{street}\n {city}\n {country}'
print(address1)
# ---------------------------------------------------------------------------------------------------------
# Create a variable to store the string "Earth revolves around the sun"
# 1. Print "revolves" using slice opeartor
a = 'Earth revolves around the sun'
print(a[6:14])
# 2.Print "sun" using negative indexing
print(a[-4:])
# ---------------------------------------------------------------------------------------------------------
# Create two variables to store how many fruits and vegetables you eat in a day
# Now print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits
# that you eat everyday. Use python f string for this
x = 5
y = 7
b = f'I eat {x} veggies and {y} fruits daily'
print(b)
# ----------------------------------------------------------------------------------------------------------
# I have a string variable called s = "maine 200 banana khaye". This of course is a wrong statement
# is 'maine 10 samosa khaye'. Replace incorrect words in original strong with new ones and
# print the new string.  Also try to do this in one line
s = 'maine 200 banana khaye'
print(s.replace('200', '10').replace('banana','samosa'))
# -----------------------------------------------------------------------------------------------------------
# User_Input
# Write a program that can find area of a triangle. It should take base and height as an input
# from the user and using that it should print an area of a triangle
# base = input("Enter the base: ")
# height = input("Enter the height: ")
# Area_of_triangle = float(base) * float(height)
# print(f'Area of triangle is: {Area_of_triangle}')
# ----------------------------------------------------------------------------------------------------
# Write a program that takes file name with extension as an input and prints just the filename without
# extension (you can assume that file extensions are always 3 character long)
file_name = input("Enter a filename with extension")
print("File name without extension:", file_name[:len(file_name)-4])
# ------------------------------------------------------------------------------------------------------
