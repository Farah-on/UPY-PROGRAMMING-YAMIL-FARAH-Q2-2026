# UPY-PROGRAMMING-YAMIL-FARAH-Q2-2026

## Git/GitHub Repository

This repository contains Python-based implementations developed as part of Unit 2 for the Programming course (Q2-2026). The objective of this assignment is to calculate the verification digit (DV) of a UTFSM role using the Modulo 11 algorithm.

## Project Description

The included Python script (`cw07.py`) calculates the verification digit of a UTFSM role by following a sequence of mathematical operations.

The program performs the following steps:

* Receives a role number without its verification digit.
* Reverses the number.
* Multiplies each digit by the repeating sequence 2, 3, 4, 5, 6, and 7.
* Adds all multiplication results.
* Calculates the modulo 11 of the obtained sum.
* Subtracts the result from 11 to obtain the verification digit.
* Displays the complete role with its verification digit.

### Example

Input:

```
201012341
```

Output:

```
Verification Digit: 3
Complete Role: 201012341-3
```

## Environment & Tools

* Language: Python 3.x
* Version Control: Git
* Hosting Platform: GitHub

## How to Run the Program

1. Ensure that Python is installed on your system.
2. Clone this repository:

```bash
git clone https://github.com/Farah-on/UPY-PROGRAMMING-YAMIL-FARAH-Q2-2026.git
```

3. Navigate to the project directory and execute the script:

```bash
python cw07.py
```

## AI Use Declaration

ChatGPT was used as a learning and support tool to understand Git/GitHub commands and to review the implementation of the verification digit algorithm. All code was reviewed, tested, and submitted by the student.