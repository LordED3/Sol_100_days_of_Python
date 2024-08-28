import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy level
# sel_letters = random.choices(letters, k=nr_letters)
# sel_symbols = random.choices(symbols, k=nr_symbols)
# sel_numbers = random.choices(numbers, k=nr_numbers)
#
# str_passwd = sel_letters + sel_symbols + sel_numbers
# password = ''
# Hard_password = ''
# for char in str_passwd:
#     password += char
#
#
# # Hard_password = random.shuffle(str_passwd)
#
#
# print(f"Generated Password {password}")
# print(f"Total char {len(password)}")

# Hard level
sel_letters = random.choices(letters, k=nr_letters)
sel_symbols = random.choices(symbols, k=nr_symbols)
sel_numbers = random.choices(numbers, k=nr_numbers)

str_passwd = sel_letters + sel_symbols + sel_numbers

# randomize the letters, numbers and symbols
random.shuffle(str_passwd)

# password gen loop
password = ''
for char in str_passwd:
    password += char


# Hard_password = random.shuffle(str_passwd)


print(f"Generated Password {password}")
print(f"Total char {len(password)}")