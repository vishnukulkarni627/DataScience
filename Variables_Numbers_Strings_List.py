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
# file_name = input("Enter a filename with extension")
# print("File name without extension:", file_name[:len(file_name)-4])
# ------------------------------------------------------------------------------------------------------
# List
exp = [2200, 2350, 2600, 2130, 2190]
# 1. In feb, how many dollars you spent extra compare to january?
dol = exp[1]-exp[0]
print(dol)
# 2. Find out your total expenses in first quater(3M) of the year
threeM = exp[0]+exp[1]+exp[2]
print(threeM)
# 3. Find out if you spent exactly 2000 dollars in any month
doll = 2000 in exp
print(doll)
# 4. June month just finished and your expense is 1980 dollar . Add this item to our monthly expense list
exp.append(1980)
print(exp)
# 5. You returned an item that you bought in a month of april and got a refund of 200$, make a correction to your monthly expense list based on this
mod = exp[3]-200
print(mod)
exp.insert(3,mod)
print(exp)
# ---------------------------------------------------------------------------------------------------------
# List_2
heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
# 1. Length of the list
print(len(heros))
# 2. Add 'black panther' at the end of the list
heros.append('black panther')
print(heros)
# 3. you realize that you need to add 'blank panther' after 'hulk' so remove it from list first and then add it after 'hulk'
heros.remove('black panther')
print(heros)
heros.insert(3, 'black panther')
print(heros)
# 4. Now you don't like thor and hulk because they get angry easily so remove thor and hulk from list and replace them with doctor strange do that with one line of code'
heros[1:3]=['doctor strange']
print(heros)
# 5. sort the heros list in alphabetical order
heros.sort()
print(heros)
# ----------------------------------------------------------------------------------------------
# If condition
India = ['mumbai', 'bangalore', 'chennai', 'delhi']
Pakistan = ['lahore', 'karachi', 'islamabad']
Bangladesh = ['dhaka', 'khulna', 'rangpur']
# 1. Write a program that asks user to enter a city name and it should tell which
# country the city belongs to
# City_name = input("Enter the city name: ")
# if City_name in India:
#     print(f'{City_name} belongs to India')
# elif City_name in Pakistan:
#     print(f'{City_name} belongs to Pakistan')
# elif City_name in Bangladesh:
#     print(f'{City_name} belongs to Bangladesh')
# else:
#     print("Error:Please check City name")
# 2. Write a program that asks user to enter two cities and it tells you if they both are in
# same country or not. For example if i enter mumbai and chennai, it will print both cities are in India
# but if i enter mumbai and dhaka it should print they don't belong to same country'
# city_1 = input('Enter city_1 name: ')
# city_2 = input('Enter city_2 name: ')
# if city_1 and city_2 in India:
#     print(f'{city_1} {city_2} Both cities are in India')
# else:
#     print(f'{city_1} {city_2} They not belong to same country')
# 3. Write a python program that can tell you if your sugar is normal or not.
# Normal fasting level sugar range is 80 to 100
# 1. Ask user to enter his fasting sugar level
# Sugar_level = input('Enter your sugar level: ')
# Sugar_level = float(Sugar_level)
# 2. If it is below 80 to 100 range then print that sugar is low
# if Sugar_level < 80:
#     print("Your sugar is low")
# elif Sugar_level > 100 :
#     print('Sugar level is high')
# else:
#     print("Your sugar level is normal")
# ----------------------------------------------------------------------------------------------------------
