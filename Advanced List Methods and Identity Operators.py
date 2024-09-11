# Task 1: Given two lists, find out if Alice submitted the assignment and attended class
# Hint: use the in & and keywords.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

if "Alice" in submitted and "Alice" in attended:
    print("Alice submitted the assignment and also attended class")
else:
    print("Alice either did not submit the assignment or did not attend class")