# #Day 2- conditional statements

# # make the program check first if the user input only one character using !=

# char = input("Enter a character: ")

# if len(char) != 1: 
#     print("Please enter only one character.")
# if char.isupper():
#     print("Uppercase")
# elif char.islower():
#     print("Lowercase")
# else:
#     print("Not a letter") 


# char ~ variable
# input/ print ~ function
# if/elif/else ~ conditional statement
# isupper()/islower() ~ method
# () ~ run this function now

#Condititional statements

    # print(20 >= 18)
    # print(15 <= 18)
    # print(15 != 18)
    # print(15 == 18)

# conditional expressions/ operands
    #  > greater than
    #  < less than
    #  <= less than or equal to
    #  >= greater than or equal to
    #  != not equal to
    #  == equal to   **= assignment operator

#PFT EXERCISE
# pft = int(input("Enter PFT score: "))

# if pft.isdigit():
#     pft = int(pft)

#     if pft >= 85:
#         print("Pwede na mag MWB")
#     else:
#         print("Next time na lang")
# else:
#     print("Invalid input. Integer only.")
    
# try:
#     pft = float(input("Enter PFT score: "))

#     if pft >= 85:
#         print("Pwede na mag MWB")
#     elif pft >= 0:
#         print("Next time na lang")
#     else:
#         print("Invalid score")

# except ValueError:
#     print("Invalid input. Please enter an integer only.")


#LOOPING THOURGH STRINGS

# for q in "pmc":
#     print(q)

#use looping method to create a program that automatically transforms the 
# letter into uppercase


# text = input("Enter word here: ")
# result = ""
# for letter in text:
#     result = result + letter.upper()
# print(result) 



# text = "philippine marines"
# textResult = ""
# for letter in text:
#     textResult += letter.upper()
# print(textResult)   


#ASSIGNMENT
#create a program that asks the user for a word,
#the program will loop each letter of the word and
#gives back the word in reverse order 


#READING ASSIGNMENT- SEARCH ABOUT ASCII


word = input("Enter a word: ")
result = ""
for letter in word:
    result = letter + result + letter
print("Reversed word:", result)
