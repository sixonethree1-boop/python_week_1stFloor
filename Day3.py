
# Day 3- ENCRYPTION/ DECRYPTION

# # print(ord("A"))
# # print(chr(65))+

# # letter = input("Enter your letter: ")
# # key = int(input("Enter your favorite number: "))
# # code = ord(letter) + key
# # print("Your new letter is: ", (chr(code)))

# #modulo 
# # %

# print("division: ", 100 / 2)
# print("modulo: ", 100 % 2)
# print("division: ", 101 / 2)
# print("modulo: ", 101 % 2)
# print("division: ", 25 / 3)
# print("modulo: ", 25 % 3)

# print(29 % 30)
# print(30 % 3)
# print(50 % 55)

# Wrap Around method for the ciphertext to be always composed of letters

letter = input("Input your favorite letter: ")
key = int(input("Input your favorite number: "))
if letter.isupper():
        base = ord('A')
result = chr((ord(letter) - base + key) % 26 + base)
print(result)

