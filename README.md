# Student Manager App

## Overview
The Student Manager App is a simple Python console-based application that allows teachers to manage student records. It is a menu-driven program developed using basic Python concepts such as conditional statements, loops, and dictionaries.

## Features
- Add Student
- View All Students
- Check Student Result
- Exit Application

## Python Concepts Used

### Conditional Statements
- if
- elif
- else

Used to perform different operations based on the user's menu selection.

### Loops
- while loop

Used to display the menu repeatedly until the user chooses to exit the application.

### Dictionary
Used to store student information such as:
- Student ID
- Student Name
- Marks
- Result

## Menu

```text
========== Student Manager ==========
1. Add Student
2. View All Students
3. Check Student Result
4. Exit
=====================================
```

## Functionality

### 1. Add Student
- Enter Student ID
- Enter Student Name
- Enter Student Marks
- Store the data in a dictionary

### 2. View All Students
- Display all student records stored in the dictionary.

### 3. Check Student Result
- Search a student using Student ID.
- Display the student's marks and result (Pass/Fail).

### 4. Exit
- Exit the application safely.

## Sample Dictionary

```python
students = {
    101: {
        "name": "Rahul",
        "marks": 85,
        "result": "Pass"
    },
    102: {
        "name": "Priya",
        "marks": 62,
        "result": "Pass"
    }
}
```

## Technologies Used
- Python 3
- Command Line Interface (CLI)

## Learning Outcomes
- Understand conditional statements.
- Learn how to use loops.
- Store and manage data using dictionaries.
- Build a menu-driven console application.

## Author
**Bablu Kataria**  
B.Tech CSE (AI & ML)
