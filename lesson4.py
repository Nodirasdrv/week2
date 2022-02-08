# Loop operators

# str = "123456789"
# for i in str:
#     print(int(i))

# num = [1, 12, 14, 15]
# for i in num:
#     print(i)

# num = [1, 12, 14, 15]
# for i in num:
#     print(i**2)

# from math import sqrt
# num = [1, 12, 14, 15]
# for i in num:
#     print(sqrt(i))

# num = [1, 12, 14, 15]
# for i in num:
#     print("hello")

# range - first num is start second is stop and third is step
# lists = list(range(2, 11, 2))
# print(lists)

# tuples = tuple(range(2, 11, 2))
# print(tuples)

# lists = list(range(101))
# print(lists)

# python = [" I love Python"]
# for i in range(1, 11):
#     print(python[0])
#     print(i)

# for i in range(1, 11):
#     print("I love python!")


# i = 1
# while i < 12:
#     print(i)
#      i = i + 1
#     i += 1

# infinite
# while True:
#     print("Hello")


# i = 5
# while True:
#     print(i)
#     if i == 15:
#         break
#     i += 1


# lists = []
# for i in range(0, 101):
#     if 0 == i % 3:
#         lists.append(i)
# print(lists)

# for i in range(5):
#     print("*" * 5)

# for i in range(1, 5):
#     print("*" * i)


# for i in range(1, 5):
#     if i == 1 or i == 4:
#         print("*" * 6)
#     else:
#         print("*", " " * 2, "*")

# for i in range(5, 1, -1):
#     print(i * "*")


# lists = []
# for i in range(0, 101):
#     if 0 == i % 3:
#         lists.append(i)
# print(lists)

# for i in range(1, 101):
#     if i % 3 == 0:
#         print(i)

# for i in range(1, 101):
#     if i % 4 == 0:
#         print(i)

# i = 0
# while i < 1001:
#     print(i)
#     i+=1



# total = 1
# while total < 1000:
#     if total > 512:
#         pass
#     total = total + total
#     break
#     print(total)



# Написать
# программу, которая будет складывать, вычитать, умножать или делить два
# числа. Числа и знак операции вводятся пользователем. После выполнения
# вычисления программа не должна завершаться, а должна запрашивать новые
# данные для вычислений. Завершение программы должно выполняться при вводе
# символа '0' в качестве знака операции. Если пользователь вводит
# неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать
# ему об ошибке. Также сообщать пользователю о невозможности деления на
# ноль, если он ввел 0 в качестве делителя.


# func = True
# while func:
#
#     num1 = int(input("Input num 1: "))
#     op = input("Input operator: ")
#     num2 = int(input("Input num 2: "))
#     result = 0
#     if op == "+":
#         result = num1 + num2
#     elif op == "-":
#         result = num1 - num2
#     elif op == "*":
#         result = num1 * num2
#     elif op == "/":
#         result = num1 / num2
#     else:
#         print("Invalid operator")
#     print(result)
#     choose = input("Do you want to continue? y - Yes, n - No")
#     if choose.lower() == 'n':
#         func = False
#     elif choose.lower() == 'y':
#         func = True
#     else:
#         print("Sorry, bye bye, idiot!")
#         func = False


# user_money = int(input("Сколько хотите накопить? "))
# contribute = int(input("Взнос: "))
# while user_money > contribute:
#     contribute = (int(input("Взнос: ")))
#     contribute = contribute + contribute
# print("Поздравляю! Вы накопили", user_money)

# counter = 0
# total = 0
# while counter <= 1000:
#     print(counter)
#     counter += 1

# mas = [[8, 6, 3], [9, 5, 2], [10, 8, 7]]
# for i in range(len(mas)):
#     for y in range(len(mas[i])):
#         if i < y:
#             mas[i][y] = 0
#     print(mas[i])


# counter = 0
# total = 0
# while total <= 1000:
#     print(counter)
#     counter += 1
#     total += counter

# user_num = int(input("Input a number: "))
# while user_num <= 100:
#     user_num = int(input("Enter again: "))
# print("Done")




























