# write a program to  create random password
import random
# those are the character we used for password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# input from user for letters,numbers and symbols
nu_letters = int(input("How many  no. of letter you want to enter="))
nu_numbers = int(input("Enter the no. of number you want to enter="))
nu_symbols = int(input("Enter the no. of symbols you want to enter="))
# following is the logic for program
# create the variable store for password
##################################### Simple Password Method #############################################
# passward = "0"
# # for loop for letters
# for char in range(1, nu_letters + 1):
#     rand_letter = random.choice(letters)
#     password = passward + rand_letter
#
# # for loop for numbers
# for char in range(1, nu_numbers + 1):
#     rand_number = random.choice(numbers)
#     password += rand_number
#
# # for loop for symbols
# for char in range(1, nu_symbols + 1):
#     rand_symbols = random.choice(symbols)
#     password += rand_symbols
# # this is the total password concatenation  into single word
# print(password)


############################ Hard Password Method ################################

password_list =[] # this is the list where we store the password
# for loop for letters
for char in range(1, nu_letters + 1):
    # rand_letter = random.choice(letters)
    # # password_list += rand_letter
    password_list.append(random.choice(letters))  # u can used append method  for minimize the code

# for loop for numbers
for char in range(1, nu_numbers + 1):
    # rand_number = random.choice(numbers)
    # password_list += rand_number
    password_list.append(random.choice(numbers))

# for loop for symbols
for char in range (1, nu_symbols + 1):
    # rand_symbols = random.choice(symbols)
    # password_list += rand_symbols
    password_list.append(random.choice(symbols))

# this is the total password concatenation  into single word.
# print(password_list)  # password  without shuffle
#  is the function allowed us to re locate the order of list items randomly
random.shuffle(password_list)
# print(password_list)  # password with shuffle

strong_password = ""
# now to convert the list into string following method is used
for i in password_list:
    strong_password += i

print("This is your random generated password=", strong_password)




