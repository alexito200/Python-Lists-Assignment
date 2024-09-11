# Task 1: Given list of grades, sort them in descending order and print sorted list.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
grades.reverse()

grades_clone = grades.copy()

# Task 2: Calculate the average and print it.

total = sum(grades)
average = total / len(grades)

print(grades_clone)
print(average)