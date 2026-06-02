'''
4 Types:
List - ordered and changeable (modifiable). Allows duplicates.
Tuple - ordered and unchangeable (unmodifiable). Allows duplicates.
Set - unordered, un-indexed, and unchangeable (unmodifiable), but can add new items to the set.
        Does not allow duplicates.
Dictionary - unordered and changeable (modifiable). Indexed. Does not allow duplicates.
'''

# List - collection of different data types, which is ordered and mutable.
# Can be empty or may have different data types.

# Can be created in 2 ways: 1) Built-in function, 2) Using "[]"
# use len() to find the length of a list.

#1) Built-in function
lst = list()
print(len(lst))         # 0

empty_list = list()     # this is an empty list (no items in it).
print(len(empty_list))  # 0

#2) Using "[]"

lst2 = []
print(len(lst2))        # 0

empty_list2 = []
print(len(empty_list2)) # 0

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['tomato', 'potato', 'cabbage', 'onion', 'carrot']
animal_products = ['milk', 'meat', 'butter', 'yogurt']
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']
countries = ['Finland', 'Estonina', 'Denmark', 'Sweden', 'Norway']

print(len(fruits))
print("Number of fruits: ", len(fruits))

print(len(vegetables))
print("Number of vegetables: ", len(vegetables))

print(len(animal_products))
print("Number of animal products: ", len(animal_products))

print(len(web_techs))
print("Number of web technologies: ", len(web_techs))

print(len(countries))
print("Number of countries: ", len(countries))

# Lists can have items of different data types

lst3 = ['gian', 23, True, {'country' : 'Philippines', 'city' : 'Iloilo'}]

# We can access each item in a list using their index.
# Positive indexing (left to right: 0 to ...n)
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Negative indexing (Right to left: -1 to -...n)

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango

# Unpacking List Items

lst = ['item1', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

# Second Example about unpacking list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
# Third Example about unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

# slicing items from a list

# Positive indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']
print(all_fruits)

# Negative indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']

# Modifying Lists

my_rig = ['Monitor', 'PC', 'Speakers', 'Keyboard', 'Mouse']
# It uses indexing, so:
my_rig[0] = 'Desk Mat'
print(my_rig)       # Now, it replaces "Monitor" with "Desk Mat"

last_index = len(my_rig) -1
my_rig[last_index] = 'Mouse Mat'
print(my_rig)       # Now, it replaces "Mouse" with "Mouse Mat"

# Checking items in a list.
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False