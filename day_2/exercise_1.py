# Day 2: 30 Days of Python Programming

first_name = "giancarlo"
last_name = "daniel"
full_name = "giancarlo daniel"
country = "Philippines"
city = "Iloilo"
age = 23
is_married = False


# ways to print:
full_name = f"{first_name} {last_name}"
print(full_name)

# or
print(first_name, last_name)

# Check data type with print(type())
print(type(first_name), type(last_name), type(full_name), type(country), type(city), type(age), type(is_married))

length_of_first_name = len(first_name)
length_of_last_name = len(last_name)

difference = abs(length_of_first_name - length_of_last_name)

print("First name length: ", length_of_first_name)
print("Last name length: ", length_of_last_name)
print("The difference between first_name and last_name is: ", difference)

# Exercise 2

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print("Number one is:", num_one)
print("Number two is:", num_two)
print("Adding Number one and Number two, we get", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Floor division:", floor_division)


radius = 30
area = 3.142 * radius ** 2
circumference = 2 * 3.142 * radius

print("The radius of the circle is:", radius, "Its area is:", area, "and its circumference is:", circumference)





