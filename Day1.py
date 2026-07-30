#Variable and Data Types

# nickname = "pao" #string
# print(nickname)

# age = 29   #integer
# print(age)

# temperature = 32.1 #float (decimal)
# print(temperature)

# is_marine = True  #boolean
# print(is_marine)

# #How to check data type
# print(type("pao"))
# print(type(29))
# print(type(32.1))
# print(type(True))

# #How to manipulate strings
# msg = "Information Warfare Center"
# print(msg.upper())
# print(msg.lower())
# print(msg.count("a"))
# print(msg.split())

# #Combination of data types and input from user
# name = input("What is your name? ")
# print("Hello " + name + "!")

# age = input("How old are you? ")
# print("You are " + age + " years old.")
# age_int = int(age)
# next_year = age_int + 1
# print("Next year, you'll be " + str(next_year) + " years old.")

# create input based query that asks the user for their name, 
# python greets the user "hello.. input"
# python asks the user for his/her year of birth, 
# converts the year of birth to integer
# calculate the user's year of mandatory retirement
# gives back the result in string "You will retire by....."

# name = input("What is your name? ")
# print("Hello " + name + "!")
# year_of_birth = input("What is your year of birth? ")
# year_of_birth = int(year_of_birth)
# retirement_year = year_of_birth + 56
# print("You will retire by " + str(retirement_year) + ".")

# UNDERSTAND THIS CODE
char = input("Enter a character: ")
if char.isupper():
    print("Uppercase")
elif char.islower():
    print("Lowercase")
else:
    print("Not a letter") 
    
#advance reading on loops  and conditional statemet
#clone the github repo to be sent to the signal group