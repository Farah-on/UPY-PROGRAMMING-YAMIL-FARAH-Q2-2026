# UPY-PROGRAMMING-YAMIL-FARAH-Q2-2026

## Spanish Verb Conjugator Repository

This repository contains a Python-based implementation developed as part of Unit 2 for the Programming course (Q2-2026). The objective of this assignment is to conjugate a regular Spanish verb in the present tense using lists, dictionaries, loops, and string manipulation.

## Project Description

The included Python script (`cw09.py`) conjugates a regular Spanish verb entered by the user.

The program performs the following steps:

* Receives a verb in infinitive form.
* Extracts the stem of the verb (all letters except the last two).
* Extracts the ending of the verb (`ar`, `er`, or `ir`).
* Looks up the corresponding list of endings in a dictionary.
* Combines each pronoun with the stem and its matching ending.
* Displays the six conjugated forms.

## Project Files

| File | Description |
|------|-------------|
| `cw09.py` | Main Python script with the verb conjugation logic |
| `cw09.txt` | PSeInt pseudocode of the algorithm |
| `cw09.png` | Flowchart diagram of the program |

## Pseudocode (cw09.txt)

The pseudocode written in PSeInt describes the full logic of the program, including:

* User input
* Pronoun list initialization
* Dictionary of verb endings
* Stem and ending extraction
* Loop structure for conjugation generation
* Output display

## Flowchart Diagram (cw09.png)

The diagram visually represents the flow of the program from input to output, including the selection of the proper verb ending and the generation of all conjugated forms.

![Flowchart](cw09.png)

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

3. Navigate to the CW09 directory and execute the script:

```bash
cd CW09
python cw09.py
```

## AI Use Declaration

Claude (Anthropic) was used as a learning and support tool to understand Python lists, dictionaries, loops, string slicing, generate the PSeInt pseudocode, and structure the README. All code was reviewed, tested, and submitted by the student.