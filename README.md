# UPY-PROGRAMMING-YAMIL-FARAH-Q2-2026

## Classwork 16 - Recursive Functions Repository

This repository contains the solutions developed for Classwork 16 of the Programming course (Q2-2026). The purpose of this assignment is to implement a set of classic recursive functions in Python — covering numeric recursion, mathematical recursion, and recursion over data structures — while making sure every function handles invalid input gracefully instead of crashing.

The repository includes a working Python program with all required recursive functions, the pseudocode (PPP) written before coding, and the corresponding flowcharts.

---

## Project Description

The program implements the following:

### Recursive Functions

* **recursiva** — counts down from `n` to `0`, printing each step, and returns a final message.
* **fibonacci** — computes the n-th Fibonacci number using pure recursion.
* **factorial** — computes the factorial of `n` using pure recursion.
* **multiplicacion_recursiva** — computes `n * m` by repeated recursive addition.
* **division_entera_recursiva** — computes integer division of `dividendo / divisor` by repeated recursive subtraction.
* **potencia_recursiva** — computes `base ^ exponente` using pure recursion.
* **serie_collatz** — prints the Collatz sequence starting from `n` until it reaches `1`.
* **aplanar_json** — flattens a nested dictionary (JSON-like structure) into a single-level dictionary using dotted keys.

### Error Handling

* Every function validates its input before recursing (e.g. negative numbers that would never reach the base case) and returns a clear error message instead of crashing.
* `TypeError` is caught where invalid types (e.g. strings instead of numbers) could otherwise break the recursion.
* `aplanar_json` catches `AttributeError` for inputs that are not dictionaries (e.g. a list).

---

## Repository Files

| File | Description |
|------|-------------|
| `recursive_functions.py` | Working Python program implementing all recursive functions with error handling |
| `recursive_functions_ppp.txt` | Pseudocode (PPP) for all recursive functions, written before coding them |
| `recursive_functions_flowchart.png` | Flowchart(s) matching the logic described in the PPP |

---

## Environment & Tools

* Language: Python 3.x
* Version Control: Git
* Hosting Platform: GitHub

---

## How to Run

1. Clone the repository.

```bash
git clone https://github.com/Farah-on/UPY-PROGRAMMING-YAMIL-FARAH-Q2-2026.git
```

2. Open the **Classwork-16-Recursive-Functions** folder.

```bash
cd Classwork-16-Recursive-Functions
```

3. Run the program.

```bash
python recursive_functions.py
```

---

## Learning Objectives

This assignment demonstrates:

* Implementation of classic recursive functions (numeric, mathematical, and structural recursion).
* Identifying base cases and recursive cases for different types of problems.
* Pseudocode planning before implementation (PPP).
* Flowchart design matching algorithmic logic.
* Defensive programming: handling invalid input without crashing the program.

---

## AI Use Declaration

Claude (Anthropic) was used as a learning and support tool to understand and implement the recursive functions, add error handling for invalid inputs, write the pseudocode (PPP) before coding, generate the flowcharts matching that logic, and assist in organizing the repository documentation. All code was reviewed, tested, and submitted by the student.