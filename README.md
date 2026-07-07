# Python Basics - Week 1

Welcome to my first Python repository! This project contains three terminal-based applications built from scratch to master the foundational concepts of Python programming during Week 1.

## Projects Included

1. **Calculator App (`calculator.py`)**
   * A clean, menu-driven command-line calculator.
   * **Key Features:** Supports addition, subtraction, multiplication, and division; contains built-in validation to handle division-by-zero errors gracefully.
   * **Core Logic:** Uses Python 3.10's modern `match/case` conditional statements for dynamic routing.

2. **Todo App (`todo_app.py`)**
   * A terminal task manager to track daily workflows.
   * **Key Features:** Users can view live tasks, append new tasks, and delete tasks by entering their list number. 
   * **Core Logic:** Uses a mutable Python `list` structure combined with `enumerate(..., start=1)` to dynamically match display indices with zero-based list offsets.

3. **Student Management System (`student_management.py`)**
   * A miniature console-based database simulator for handling structured records.
   * **Key Features:** Allows adding new student records, displaying all entries with total live counts, and searching the data pool for specific individual IDs.
   * **Core Logic:** Implements **nested data structures** (a `list` containing multiple individual `dictionary` rows) along with boolean tracking flags for error handling.

---

## What I Learned This Week

* **Control Flow:** Creating infinite application loops (`while True`) and handling options safely using nested `if/elif/else` blocks and `match/case`.
* **Data Structures:** Dynamically manipulating sequences using standard list methods (`.append()`, `.pop()`) and processing key-value collections (`dict`).
* **Input & Formatting:** Validating raw string data types from console inputs, converting values (`int()`, `float()`), and utilizing readable Python f-strings.
* **Defensive Programming:** Writing structural conditions to prevent user input errors from crashing runtime execution.

---

## How to Run the Applications

Ensure you have Python installed on your computer. 

1. Clone or download this repository.
2. Open your terminal or command prompt inside the project folder.
3. Run any of the applications using the following commands:

```bash
python calculator.py
python todo_app.py
python student_management.py
