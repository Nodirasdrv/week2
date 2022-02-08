# print(len(name)) - length of the string
# print(name[::3])
# print(name[::-1])
# print(dir(name)) - shows the methods
# print(name.find("a", 2, 4)) - finds a letter and shows and index of the letter
# print(name.index("z")) - returns an index of certain element
# print(name.split("z")) - splits the string and changes to lists

# print(name.startswith("b")) - checks if the letter starts with teh certain letter and returns TRUE OR FALSE
# print(name.endswith("a")) - checks if the letter ends with teh certain letter and returns TRUE OR FALSE

# date = input("date: ")
# name = f"Nazgul Tabyldieva {date}" - adds another string to the current one that always changes
# print(name)

# name = input("Name: ")
# age = input("Age: ")
# job = input("Job: ")
# sentence = f"My name is {name}, I am {age} years old, I work as a {job}"
# print(sentence)


# name = input("Name: ")
# age = input("Age: ")
# job = input("Job: ")
# print("My name is {0}, I am {1} years old, I work as a {2}".format(name, age, job)) - format is similar to f str but
# you can write down the order


# sen = "dsjfg5"
# print(sen.isdigit()) - checks if the string consists only of numbers or not
# print(sen.isalnum()) - checks if the strings has letters and numbers
# print(sen.isalpha()) - checks if the string consists only of letters

# Условные операторы
# name = input("name: ")
# if name == "Nazgul":
#     print(f"{name} Tabyldieva")
# elif name == "Nodira":
#     print(f"{name} Sadyrova")
# else:
#     print("Name not found")

# num1 = int(input("Number 1: "))
# num2 = int(input("Number 2: "))
# symbol = input("Symbol: ")
# if symbol == "+":
#     print(num1 + num2)
# elif symbol == "-":
#     print(num1 - num2)
# elif symbol == "*":
#     print(num1 * num2)
# elif symbol == "/":
#     print(num1 / num2)
# else:
#     print("Invalid Value")

# num = int(input("Enter a number: "))
# if num == num / 2:
#     print(f"{num} is even number")
# else:
#     print(f"{num} is odd number")


# password = input("Enter a password: ")
# if len(password) <= 6:
#     print("Your password length must be greater than 6")
# else:
#     print(f"Your password is {password}")

# score = int(input("Enter the score: "))
#
# if 85 <= score <= 100:
#     print("Excellent")
# elif 70 <= score <= 84:
#     print("Good")
# elif 50 <= score <= 69:
#     print("Average")
# elif 0 <= score <= 49:
#     print("Less than average")
# else:
#     print("Invalid value")


# length = float(input("Enter length in cm: "))
# if length >= 0:
#     print(f"{length} cm is {length / 2.54} inches")
# else:
#     print("Invalid Value")

# Ввести логин и пароль и сравнить. Вывести результат авторизации: True или False
# login = "hello"
# password = "world"
# login_in = input("Login: ")
# password_in = input("Password: ")
# if login_in == login and password_in == password:
#     print(f"Login: {login}, Password: {password}")
# else:
#     print("Invalid")





