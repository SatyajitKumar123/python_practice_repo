## Problem 1: Basic List Operations
numbers = [1, 2, 3, 4, 5]

# 1. Add 6 to the end
numbers.append(6)
print(numbers)

# 2. Remove the first element
numbers.pop(0)
print(numbers)

# 3. Insert 0 at the beginning
numbers.insert(0,0)
print(numbers)

# 4. Remove the last element
numbers.pop()
print(numbers)

# 5. Find the index of 3
idx = numbers.index(3)
print(idx)

# Problem 2: List Sorting and Reversing
mixed_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# 1. Sort in ascending order
mixed_numbers.sort()
print(mixed_numbers)

# 2. Sort in descending order
mixed_numbers.sort(reverse=True)
print(mixed_numbers)

# 3. Reverse the list
mixed_numbers.reverse()
print(mixed_numbers)

# 4. Create a sorted copy without modifying original
mixed_copy_numbers = sorted(mixed_numbers.copy())
print(mixed_copy_numbers)


## Problem 3: Counting and Removing Elements
fruits = ['apple', 'banana', 'orange', 'apple', 'grape', 'banana', 'apple']

# 1. Count occurrences of 'apple'
count_apple = fruits.count('apple')
print(count_apple)

# 2. Remove first occurrence of 'banana'
fruits.remove('banana')
print(fruits)

# 3. Remove all 'apple' elements
new_list = [fruit for fruit in fruits if fruit != 'apple']
print(new_list)

## Alternate method
fruits = ['apple', 'banana', 'orange', 'apple', 'grape', 'banana', 'apple']
while 'apple' in fruits:
    fruits.remove('apple')
print(fruits)

# 4. Check if 'orange' exists in the list
if 'orange' in fruits:
    print("Orange is available")
else:
    print("Orange is not available")

## Alternate
has_orange = 'orange' in fruits
print(f"Has orange: {has_orange}")

## Problem 4: List Comprehensions and Filtering
numbers = list(range(1, 21))  # [1, 2, 3, ..., 20]

# 1. Create a new list with only even numbers
evens = [x for x in numbers if x%2 == 0]
print(evens)

# 2. Create a new list with squares of numbers
squares = [x**2 for x in numbers]
print(squares)

# 3. Create a new list with numbers divisible by 3 or 5
new_list = [x for x in numbers if x%3==0 or x%5==0]
print(new_list)

# 4. Filter out numbers less than 10
filtered_list = [x for x in numbers if x >= 10]
print(filtered_list)

## Problem 5: List Manipulation with Multiple Methods
grades = [85, 92, 78, 90, 85, 88, 92, 76, 85, 90]

# 1. Remove duplicates while preserving order
no_duplicates = []
for grade in grades:
    if grade not in no_duplicates:
        no_duplicates.append(grade)
print(no_duplicates)

## Alternate
no_duplicates = []
[no_duplicates.append(grade) for grade in grades if grade not in no_duplicates]
print(no_duplicates)

## Alternate
unique_dict = dict.fromkeys(grades)
print(unique_dict)

no_duplicates = list(unique_dict)
print(no_duplicates)

# 2. Find the highest and lowest grades
highest = max(grades)
lowest = min(grades)

print(f"Higest grades is {highest} and Lowest grade is {lowest}")

# 3. Calculate average grade
average_grade = sum(grades)/len(grades)
print(f"Average grade is: {average_grade:.2f}")

# 4. Replace all occurrences of 85 with 87
rep = [87 if grade==85 else grade for grade in grades]
print(rep)


# 5. Create a list of grades above average
above_average = [grade for grade in grades if grade > average_grade]
print(above_average)


## Problem 6: Nested Lists and Matrix Operations
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 1. Transpose the matrix (rows become columns)
transposed_list = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed_list)

## Alternate
transposed = []
for i in range(len(matrix[0])):
    new_row = []
    for row in matrix:
        new_row.append(row[i])
    transposed.append(new_row)
print(transposed)

# 2. Flatten the matrix into a 1D list
flat = [y for x in matrix for y in x]
print(flat)

## Alternate
flat = []
for row in matrix:
    for x in row:
        flat.append(x)
print(flat)

# 3. Calculate the sum of each row
row_sums = [sum(row) for row in matrix]
print(row_sums)

# 4. Calculate the sum of each column
transope = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
col_sums = [sum(col) for col in transope]
print(col_sums)


## Problem 7: Complex List Operations
employees = [
    {'name': 'Alice', 'department': 'Engineering', 'salary': 80000},
    {'name': 'Bob', 'department': 'Marketing', 'salary': 65000},
    {'name': 'Charlie', 'department': 'Engineering', 'salary': 90000},
    {'name': 'Diana', 'department': 'HR', 'salary': 55000},
    {'name': 'Eve', 'department': 'Marketing', 'salary': 70000}
]

# 1. Get all engineering employees
eng_employees = [emp for emp in employees if emp['department']=='Engineering']
print("Engineering employees: ")
print("Name   Salary")
for emp in eng_employees:
    print(f"{emp['name']} - {emp['salary']}")

# 2. Get names of employees with salary > 70000
high_earners = [emp['name'] for emp in employees if emp['salary']>70000]
print(high_earners)

# 3. Calculate average salary by department
from collections import defaultdict
dept_salaries = defaultdict(list)
for emp in employees:
    dept_salaries[emp['department']].append(emp['salary'])

average_salary = {dept: sum(salaries)/len(salaries) for dept, salaries in dept_salaries.items()}
print("Average salaries by department: ")
for dept, avg in average_salary.items():
    print(f"{dept}: ${avg:.2f}")


# 4. Sort employees by salary (descending)
employees_sorted = sorted(employees, key=lambda x: x['salary'], reverse=True)

print("Employees sorted by salary (descending):")
for emp in employees_sorted:
    print(f"{emp['name']}: ${emp['salary']}")

# 5. Find the highest paid employee in each department
highest_paid_by_dept ={}
for emp in employees:
    dept = emp['department']
    if dept not in highest_paid_by_dept or emp['salary'] > highest_paid_by_dept[dept]['salary']:
        highest_paid_by_dept[dept] = emp
print("Highest paid by department:")
for dept, emp in highest_paid_by_dept.items():
    print(f"{dept}: {emp['name']} - ${emp['salary']}")













