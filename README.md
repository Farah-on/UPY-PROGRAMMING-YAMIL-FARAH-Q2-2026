# UPY-PROGRAMMING-YAMIL-FARAH-Q2-2026

## Numerical Integration Repository

This repository contains Python-based implementations developed as part of Unit 2 for the Programming course (Q2-2026). The objective of this assignment is to calculate the numerical integration of a function using four different methods: Left Rectangle Method (LRM), Right Rectangle Method (RRM), Midpoint Rectangle Method (MRM), and the Trapezoidal Rule (TRAP).

## Project Description

The included Python script (`cw08.py`) calculates the numerical integration of a user-defined function over a given interval using Riemann sums and the trapezoidal rule.

The program performs the following steps:

* Receives the left and right endpoints of the interval (supports expressions with `pi`).
* Receives the function to integrate as a string expression.
* Receives the integration method (LRM, RRM, MRM, or TRAP).
* Divides the interval into 1000 subintervals.
* Calculates the width `h` of each subinterval.
* Applies the selected method to approximate the area under the curve.
* Displays the result of the integration.

## Project Files

| File | Description |
|------|-------------|
| `cw08.py` | Main Python script with the integration logic |
| `cw08.txt` | PSeInt pseudocode of the algorithm |
| `cw08.png` | Flowchart diagram of the program |

## Pseudocode (cw08.txt)

The pseudocode written in PSeInt describes the full logic of the program, including:

* Input parsing with `pi` support
* Variable initialization
* Conditional method selection (LRM, RRM, MRM, TRAP)
* Loop structure for area accumulation
* Output display

## Flowchart Diagram (cw08.png)

The diagram visually represents the flow of the program from input to output, including all conditional branches for each integration method.

![Flowchart](cw08.png)

## Environment & Tools

* Language: Python 3.x
* Pseudocode Tool: PSeInt
* Version Control: Git
* Hosting Platform: GitHub

## How to Run the Program

1. Ensure that Python is installed on your system.
2. Clone this repository:

```bash
git clone https://github.com/Farah-on/UPY-PROGRAMMING-YAMIL-FARAH-Q2-2026.git
```

3. Navigate to the CW08 directory and execute the script:

```bash
cd CW08
python cw08.py
```

## AI Use Declaration

Claude (Anthropic) was used as a learning and support tool to understand numerical integration methods, debug the Python implementation, generate the PSeInt pseudocode, and structure the README. All code was reviewed, tested, and submitted by the student.