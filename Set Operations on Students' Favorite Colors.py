"""
Title: Set Operations on Students' Favorite Colors
Name: shokomori
"""

# Creating sets of students who like each color
red = {1, 5, 6, 8}
yellow = {1, 3, 5, 6, 9}
blue = {2, 3, 4, 6, 10}
green = {2, 4, 7, 8, 9, 10}
orange = {1, 3, 4, 7, 9}
purple = {2, 5, 7, 8, 10}

# Students who like both red and orange
students_red_and_orange = red & orange

# Students who like all three: blue, green, and purple
students_blue_green_purple = blue & green & purple

# Students who do not like yellow
students_not_yellow = set(range(1, 11)) - yellow

# Students who like blue but not green
students_blue_not_green = blue - green

# Students who like at least one of red, orange, or yellow
students_red_orange_yellow = red | orange | yellow

# Displaying results
print("Students who like both red and orange:", students_red_and_orange)
print("Students who like all three colors - blue, green, and purple:", students_blue_green_purple)
print("Students who do not like yellow:", students_not_yellow)
print("Students who like blue but not green:", students_blue_not_green)
print("Union of students who like red, orange, or yellow:", students_red_orange_yellow)
