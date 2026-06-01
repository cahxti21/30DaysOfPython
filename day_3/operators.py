# Declare your age as integer variable
"""
my_age = 23
my_height = 1.64
complex_number = (4 + 4j)

# Used the (type() to check for data type
print(type(my_age))
print(type(my_height))
print(type(complex_number))


# Write a script that prompts the user to enter base and height of the triangle and
# calculate an area of this triangle (area = 0.5 x b x h).


# Don't forget to turn the input into a int or float.
# input always stores user text as a string.//
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area_of_triangle = 0.5 * base * height
print("The Area of the triangle is ", area_of_triangle)

side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is ", perimeter)

length_of_rectangle = float(input("Enter length of rectangle: "))
width_of_rectangle = float(input("Enter width of rectangle: "))
area_of_rectangle = length_of_rectangle * width_of_rectangle
print("The area of the rectangle is ", area_of_rectangle)
perimeter_of_rectangle = 2 * (length_of_rectangle + width_of_rectangle)
print("The perimeter of the rectangle is ", perimeter_of_rectangle)

"""
"""
# Define the known parameters from y = 2x - 2
m = 2  # Slope
b = -2 # y-intercept

# Calculate x-intercept by setting y = 0 -> 0 = mx + b -> x = -b / m
x_intercept = -b / m

# Display the results
print(f"Slope: {m}")
print(f"y-intercept: (0, {b})")
print(f"x-intercept: ({x_intercept}, 0)")
"""

working_hours = float(input("Enter working hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
weekly_earnings = working_hours * rate_per_hour * 5
print("Your weekly earnings is ", weekly_earnings)