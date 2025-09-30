Expression Calculator (Python)

A command-line calculator written in Python that supports multi-digit numbers, variables, operator precedence, and history tracking. This calculator is more advanced than a basic calculator because it allows variable assignments and reuse, handles arithmetic with correct precedence, and stores calculation history.

Features

Arithmetic operations: +, -, *, /, ^ (exponentiation)

Operator precedence: Correctly evaluates expressions like 2 + 3 * 4 as 14

Multi-digit numbers: Works with numbers of any length

Variable assignment: Assign values to variables for reuse (e.g., a = 5 + 3)

Variable usage: Use previously defined variables in expressions (e.g., a * 2)

History tracking: View all previous calculations

View variables: List all defined variables and their values

Error handling: Detects undefined variables, division by zero, and other invalid inputs

User-friendly interface: Simple command-line prompts and clear messages
========================================================================
How to Run

Make sure you have Python 3.x installed.

Save the code as calculator.py.

Open a terminal or command prompt.

Navigate to the folder containing calculator.py.

Run the calculator using python 3.5 or above versions:

python calculator.py
========================================================================
Usage

Basic arithmetic:

Enter expression: 5 + 3
 Result: 8


Variable assignment:

Enter expression: a = 10
Assigned: a = 10


Using variables:

Enter expression: a * 2
 Result: 20


Exponentiation:

Enter expression: 2 ^ 3
Result: 8


View history:

Enter expression: history
Calculation History:
 1. 5 + 3 = 8
 2. a = 10 -> 10
 3. a * 2 = 20


View all variables:

Enter expression: vars
Variables:
 a = 10


Exit:

Enter expression: exit
Exiting calculator. Goodbye!

Example Session
Enter expression: x = 5 + 7
Assigned: x = 12

Enter expression: y = x * 2
Assigned: y = 24

Enter expression: y / 3
  Result: 8.0

Enter expression: history
 Calculation History:
 1. x = 5 + 7 -> 12
 2. y = x * 2 -> 24
 3. y / 3 = 8.0

Enter expression: vars
 Variables:
 x = 12
 y = 24

Enter expression: exit
 Exiting calculator. Goodbye!

Improvements Over Basic Calculators

Variables: Unlike a basic calculator, you can store results in variables and reuse them.

Operator precedence: Automatically handles the correct order of operations (^ > *// > +/-).

History: Keeps track of all previous expressions and results.

Error handling: Prevents common errors like division by zero and using undefined variables.

User-friendly interface: Clear prompts, results, and notifications for assignments and errors.

Notes

Variable names must be single lowercase letters (a to z).

Expressions must be valid arithmetic expressions using numbers, variables, and supported operators.

The calculator performs floating-point division for /.

This calculator is a small but powerful tool for experimenting with expressions, assignments, and operator precedence in Python.
