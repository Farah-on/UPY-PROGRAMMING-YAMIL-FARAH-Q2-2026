# UPY-PROGRAMMING-YAMIL-FARAH-Q2-2026

## Classwork 10- School Management System Repository

This repository contains a Python-based implementation developed as part of Unit 2 for the Programming course (Q2-2026). The objective of this assignment is to simulate a basic school management system with different user roles, authentication, grade consultation, grade modification, and academic reporting.

## Project Description

The included Python script (`cw10.py`) implements a role-based school management system.

The program performs the following steps:

* Authenticates users with a username and password.
* Identifies the role of the authenticated user.
* Allows students to view their report card.
* Displays approved and pending subjects for students.
* Allows teachers to view students and subjects.
* Allows teachers to modify student grades.
* Allows coordinators to view teachers and a complete grade report.
* Displays information according to the permissions of each role.

## Project Files

| File | Description |
|------|-------------|
| `cw10.py` | Main Python script with the school management system logic |
| `cw10.txt` | PSeInt pseudocode of the algorithm |
| `Flowchart.png` | Flowchart diagram of the program |

## Pseudocode (cw10.txt)

The pseudocode written in PSeInt describes the full logic of the program, including:

* User authentication
* Role validation
* Student report card generation
* Approved and pending subject calculation
* Teacher grade modification process
* Coordinator reporting system
* Conditional structures and loops

## Flowchart Diagram (Flowchart.png)

The diagram visually represents the flow of the program from login to role-specific actions, including student, teacher, and coordinator functionalities.

![Flowchart](Flowchart.png)

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

3. Navigate to the CW10 directory and execute the script:

```bash
cd CW10
python cw10.py
```

## User Roles

### Student
* View personal report card.
* View approved subjects.
* View pending subjects.

### Teacher
* View students.
* View subjects.
* Modify student grades.
* Review updated grades.

### Coordinator
* View teacher information.
* View a complete grade table for all students.

## AI Use Declaration

Claude (Anthropic) was used as a learning and support tool to understand role-based programming, Python dictionaries, loops, conditional structures, generate the PSeInt pseudocode, and structure the README. All code was reviewed, tested, and submitted by the student.