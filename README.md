# UPY-PROGRAMMING-YAMIL-FARAH-Q2-2026

## Classwork 13 - Error Handling Repository

This repository contains the solutions developed for Classwork 13 of the Programming course (Q2-2026). The purpose of this assignment is to demonstrate the use of Python exception handling by improving previous classwork assignments with proper input validation and error management.

The repository includes three working Python programs from previous classworks, updated using `try`, `except`, `else`, and `raise` where appropriate.

## Project Description

The repository contains the following programs:

### Classwork 07 - Verifier Digit

This program calculates and verifies the check digit of a UTFSM student ID.

Main features:

* Reads the student ID.
* Validates user input.
* Calculates the verification digit.
* Displays the result.
* Handles invalid inputs using exception handling.

### Classwork 08 - Numerical Integration

This program approximates the value of a definite integral using numerical methods.

Supported methods:

* Left Rectangle Method (LRM)
* Right Rectangle Method (RRM)
* Midpoint Rectangle Method (MRM)
* Trapezoidal Method (TRAP)

The program validates:

* Interval endpoints.
* Mathematical expressions.
* Integration method.
* Undefined functions.
* Division by zero.
* Invalid user input.

### Classwork 09 - Spanish Verb Conjugator

This program conjugates regular Spanish verbs ending in **-ar**, **-er**, and **-ir**.

The program validates:

* Empty input.
* Invalid endings.
* Uppercase input.
* Numbers or symbols.
* Invalid verbs.

## Repository Files

| File | Description |
|------|-------------|
| `verifier_digit.py` | Classwork 07 solution |
| `numerical_integration.py` | Classwork 08 solution |
| `spanish_verb_conjugator.py` | Classwork 09 solution |

## Error Handling

All programs were updated to include exception handling using Python.

The repository demonstrates the use of:

* `try`
* `except`
* `else`
* `raise`

These structures prevent program crashes and provide clear error messages for invalid user input.

## Environment & Tools

* Language: Python 3.x
* Standard Library: math
* Version Control: Git
* Hosting Platform: GitHub

## How to Run

1. Clone the repository.

```bash
git clone https://github.com/Farah-on/UPY-PROGRAMMING-YAMIL-FARAH-Q2-2026.git
```

2. Open the Classwork-13-Error-Handling folder.

```bash
cd Classwork-13-Error-Handling
```

3. Run any of the available programs.

Example:

```bash
python verifier_digit.py
```

or

```bash
python numerical_integration.py
```

or

```bash
python spanish_verb_conjugator.py
```

## Learning Objectives

This assignment demonstrates:

* Exception handling in Python.
* Input validation.
* Defensive programming.
* User-friendly error messages.
* Program reliability.

## AI Use Declaration

Claude (Anthropic) was used as a learning and support tool to understand Python exception handling, input validation, defensive programming techniques, improve the previous assignments with `try`, `except`, `else`, and `raise`, and assist in organizing the repository documentation. All code was reviewed, tested, and submitted by the student.