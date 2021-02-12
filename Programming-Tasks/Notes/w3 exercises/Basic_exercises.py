# 1. Write a Python program to print the following string in a specific format
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" 
# Output :
# Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are

# sample_string = "Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are"
# print(sample_string)

# ----------------------------------------------------------------------------------------------------------------------

# 2. Get python version

# import sys
# print('Python version ' + sys.version)

# ----------------------------------------------------------------------------------------------------------------------

# 3. Get current time

# import datetime
# now = datetime.datetime.now()
# print(now.strftime("%Y-%m-%d %H:%M:%S"))
# print(now)

# ----------------------------------------------------------------------------------------------------------------------

# 4. Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

# Circle Area formula = pi * radius**2 
# from math import pi
# radius = input("Radius of circle =  ")
# while type(radius) != float:
#     try:
#         radius = float(radius) 
#     except:
#         print("Invalid value entered. Try again")
#         radius = input()

# area = round(pi * radius**2, 2)
# print("Area of circle = " + str(area))

# ----------------------------------------------------------------------------------------------------------------------

# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

name = input("What is your name? ")
surname = input("What is your last name? ")
print(surname + " " + name) #classic raw style
print(f"{surname} {name}") #format string style



