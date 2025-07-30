# import re

# my_regex = re.compile("[0-9]+", re.I) 

# import matplotlib.pyplot as plt

# plt.plot(...)

# from collections import defaultdict, Counter
# lookup = defaultdict(int)
# my_counter = Counter()

# def double(x):
#     return x * 2

 

# def apply_to_one(f):
#     """Calls the function f with 1 as its argument"""
#     return f(1)

# my_double = double             # refers to the previously defined function
# x = apply_to_one(my_double)
# # It is also easy to create short anonymous functions, or lambdas:

# y = apply_to_one(lambda x: x + 4) # (x) => x + 4  

# def full_name(first = "What's-his-name", last = "Something"):
#     return first + " " + last

# full_name("Joel", "Grus")     # "Joel Grus"
# full_name("Joel")             # "Joel Something"
# print(full_name(last="Grus") )       # "What's-his-name Grus"

# first_name = "Joel"
# last_name = "Grus"

# full_name3 = f"{first_name} {last_name}" # `${} ${}` = f"{}{}"

# try:
#     print(0/0)
# except:
#     print("ERROR")

# integer_list = [1,2,3,4]
# heterogenous_list = ["string", 0.1, True]

# first_three = integer_list[:3]
# three_to_end = integer_list[3:]
# last_three = integer_list[-3:]
# copy_of = integer_list[:]

# # concat list use extend cd ..
# integer_list.extend([1,2,3])
# x,y = [1,2]


# my_tuple = (1,2)

# # You cannot modify a tuple


# def sum_and_product(x, y):
#     return (x + y), (x * y)

# sp = sum_and_product(2, 3)     # sp is (5, 6)
# s, p = sum_and_product(5, 10)  # s is 15, p is 50

# joels_grade = grades.get("Joel", 0)   # equals 80
# kates_grade = grades.get("Kate", 0)  
# grades["Tim"] = 99                    # replaces the old value
# grades["Kate"] = 100                  # adds a third entry
# num_students = len(grades)            # equals 3