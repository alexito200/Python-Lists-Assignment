# Task 1: Given list of temperatures, extract temp for the second week (7 days) of the month (index 7 to index 14).
# Expected outcome: 83, 85, 86, 87, 88, 89, 90,
# Task 2: Extract all the temperatures above 100.
# HINT: add the temperatures over 100 to a new list, or use list slicing to get the temperatures.

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
print(temperatures.index(100))
print(temperatures[7:14]) # Task 1
print(temperatures[24:]) # Task 2
