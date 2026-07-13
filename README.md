# UPY-PROGRAMMING-YAMIL-FARAH-Q2-2026

## Classwork 14 - Error Handling Repository

This repository contains the solutions developed for Classwork 14 of the Programming course (Q2-2026). The purpose of this assignment is to improve previous classwork assignments by implementing Python exception handling with `try`, `except`, `else`, and `raise` to validate user input and prevent program crashes.

The repository includes three working Python programs from previous classworks, updated with proper error handling while preserving their original functionality.

---

## Project Description

The repository contains the following programs:

### Classwork 10 - School Management System

This program simulates a school management system with three different user roles.

Main features:

* User authentication.
* Student grade consultation.
* Teacher grade modification.
* Coordinator grade report.
* Validation of usernames and passwords.
* Validation of subjects and students.
* Validation of grade ranges.
* Exception handling for invalid input.

---

### Classwork 11 - The Mandelbrot Set

This program generates the iteration data required to create a Mandelbrot Set image.

Main features:

* Reads configuration values from `config.txt`.
* Generates Mandelbrot iteration values.
* Creates a CSV file containing all pixel iterations.
* Validates configuration parameters.
* Detects missing configuration values.
* Handles invalid configuration files.
* Handles file reading and writing errors.

---

### Classwork 12 - The Mandelbrot Set Visualization

This program creates an image of the Mandelbrot Set using the CSV file generated in Classwork 11.

Main features:

* Reads configuration values.
* Loads Mandelbrot iteration data.
* Creates an HSV image.
* Converts the image to RGB.
* Saves the generated image.
* Validates configuration values.
* Detects missing files.
* Handles image generation errors.

---

## Repository Files

| File | Description |
|------|-------------|
| `school_management_system.py` | Classwork 10 solution with exception handling |
| `mandelbrot_set_math.py` | Classwork 11 solution with exception handling |
| `mandelbrot_set_image.py` | Classwork 12 solution with exception handling |

---

## Error Handling

All programs were updated to include Python exception handling.

The repository demonstrates the use of:

* `try`
* `except`
* `else`
* `raise`

These structures validate user input, detect invalid data, prevent unexpected program termination, and provide meaningful error messages.

---

## Environment & Tools

* Language: Python 3.x
* External Library: Pillow (PIL)
* Standard Library: math
* Version Control: Git
* Hosting Platform: GitHub

---

## How to Run

1. Clone the repository.

```bash
git clone https://github.com/Farah-on/UPY-PROGRAMMING-YAMIL-FARAH-Q2-2026.git
```

2. Open the **Classwork-14-Error-Handling** folder.

```bash
cd Classwork-14-Error-Handling
```

3. Run any of the available programs.

Examples:

```bash
python school_management_system.py
```

```bash
python mandelbrot_set_math.py
```

```bash
python mandelbrot_set_image.py
```

---

## Learning Objectives

This assignment demonstrates:

* Exception handling in Python.
* Input validation.
* Defensive programming.
* File handling.
* User-friendly error messages.
* Program reliability.

---

## AI Use Declaration

Claude (Anthropic) was used as a learning and support tool to understand Python exception handling, improve previous assignments using `try`, `except`, `else`, and `raise`, implement defensive programming techniques, validate user input, handle file-related exceptions, and assist in organizing the repository documentation. All code was reviewed, tested, and submitted by the student.