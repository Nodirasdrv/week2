# list

# lists = list()
# print(type(lists))  - first way of writing lists
#
# lists_1 = []
# print(type(lists_1))  - second way of writing lists

# lists = [1, 2, "Nodira", "Samat"]
# lists[-1] = "Ulukbek"
# print(lists[-1])

# lists = [1, 2, "Nodira", "Samat"]
# for i in lists:
#     print(i)

# append() method - adds another value in the end of the list
# lists = [1, 2, "Nodira", "Samat"]
# lists.append(10)
# print(lists)

# pop method - removes from the lists but does not delete
# lists = [1, 2, "Nodira", "Samat"]
# black_lists = lists.pop(2)
# print(black_lists)

# insert method - adds an index to the certain value
# lists = [1, 2, "Nodira", "Samat"]
# black_lists = lists.pop(2)
# print(lists)
# print(black_lists)
# lists.insert(2, black_lists)
# print(lists)

# str = "1.3.A.f"
# lists = str.split(".")
# print(lists) - changed the string to the lists the dot is the splitting point.

#join method - changes the lists to the string and
# before the dot is the splitting point btw the objects
# fruits = ["banana", "apple", "blueberry"]
# sentence = " ".join(fruits)
# print(sentence)

# in, not in
# student = input("Student: ")
# students = ["Azamat", "Samat", "Nodira", "Kunduz", "Ruslan"]
# if student in students:
#     print("The students is in the group.")
# else:
#     print("Enroll!")

# index method - shows an index of the object in the list.
# students = ["Azamat", "Samat", "Samat", "Nodira", "Kunduz", "Ruslan"]
# print(students.index("Samat", 2))

# Count method - tells how many same objects in the list
# students = ["Azamat", "Samat", "Samat", "Nodira", "Kunduz", "Ruslan"]
# print(students.count("Azamat"))

# len - tells how many objects in the list
# students = ["Azamat", "Samat", "Samat", "Nodira", "Kunduz", "Ruslan"]
# print(len(students))

# extend method - extends the list and add smth though the brackets
# students = ["Azamat", "Samat", "Samat", "Nodira", "Kunduz", "Ruslan"]
# students.extend([10, 29, 17])
# print(students)


# kpi = [45, 61, 87, 91]
# for i in kpi:
#     if i >= 87 and i <= 100:
#         print(i)

# students = ["Azamat", "Samat", "Samat", "Nodira", "Kunduz", "Ruslan"]
# students.append([[10, 1], 29, 17])
# print(students[6][0][1])

# student1 = int(input("Score: "))
# student2 = int(input("Score: "))
# students = [student1, student2, "student 3", "student 4", "student 5"]

# kpi = [45, 61, 87, 91]
# excellent = []
# good = []
# average = []
# less_average = []
# for i in kpi:
#     if 87 <= i <= 100:
#         excellent.append(i)
#     elif 61 <= i <= 87:
#         good.append(i)
#     elif 45 <= i <= 61:
#         average.append(i)
#     elif 0 <= i <= 45:
#         less_average.append(i)
# print("Excellent:", excellent,  "Good:", good,  "Average:", average,  "Less than average:", less_average)


# num = [2, 3, 4, 5, 6]
# square = []
# for i in num:
#     square.append(i*i*i)
# print(square)

# nums = [1, 2, 3, 6, 7, 8]
# ent_num = int(input("Enter a number: "))
# nums.append(ent_num)
# nums.sort()
# print(nums)

# nums = [1, 2, 3, 6, 7, 8]
# ent_num = int(input("Enter a number: "))
# for i in nums:
#     if nums <= i:
#         nums.append(ent_num)
# print(nums)











