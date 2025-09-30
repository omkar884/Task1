# calculator.py

def precedence(op):
    if op in ['+', '-']:
        return 1
    elif op in ['*', '/']:
        return 2
    elif op == '^':
        return 3
    return -1

def is_right_associative(op):
    return op == '^'

def apply_op(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/':
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return a / b   # float division
    if op == '^':
        return a ** b  # exponentiation
    return None

def evaluate(expression, value_map):
    values = []
    ops = []
    i = 0
    n = len(expression)

    while i < n:
        if expression[i] == ' ':
            i += 1
            continue

        # Variable (single lowercase letter)
        if expression[i].isalpha():
            var = expression[i]
            if var in value_map:
                values.append(value_map[var])
            else:
                raise ValueError(f" $ Variable '{var}' is not defined yet $")
            i += 1

        # Number
        elif expression[i].isdigit():
            temp = 0
            while i < n and expression[i].isdigit():
                temp = temp * 10 + int(expression[i])
                i += 1
            values.append(temp)

        # Operator
        else:
            while ops and (
                precedence(ops[-1]) > precedence(expression[i]) or
                (precedence(ops[-1]) == precedence(expression[i]) and not is_right_associative(expression[i]))
            ):
                b = values.pop()
                a = values.pop()
                op = ops.pop()
                values.append(apply_op(a, b, op))
            ops.append(expression[i])
            i += 1

    while ops:
        b = values.pop()
        a = values.pop()
        op = ops.pop()
        values.append(apply_op(a, b, op))

    return values[-1]

def process(expr, value_map, history):
    if '=' in expr:
        var, rhs = expr.split('=', 1)
        var = var.strip()[0]  # variable name
        result = evaluate(rhs.strip(), value_map)
        value_map[var] = result
        history.append(f"{var} = {rhs.strip()} -> {result}")
        print(f"$ Assigned: {var} = {result}\n")
    else:
        result = evaluate(expr.strip(), value_map)
        history.append(f"{expr.strip()} = {result}")
        print(f"$  Result: {result}\n")

def main():
    value_map = {}
    history = []

    print("=" * 40)
    print("     EXPRESSION CALCULATOR (Python)")
    print("=" * 40)
    print("Features:")
    print(" - Supports +, -, *, /, ^ (with precedence)")
    print(" - Multi-digit numbers")
    print(" - Variable assignment (e.g., a = 5 + 3)")
    print(" - Use variables later (e.g., a * 2)")
    print(" - Type 'history' to view past calculations")
    print(" - Type 'vars' to view all variables")
    print(" - Type 'exit' to quit\n")

    while True:
        expr = input("$ Enter expression: ").strip()
        if not expr:
            continue

        if expr.lower() in ["exit", "quit"]:
            print("$ Exiting calculator. Goodbye!")
            break

        if expr.lower() == "history":
            if not history:
                print("$ No calculations yet.\n")
            else:
                print("\n$ Calculation History:")
                for i, h in enumerate(history, 1):
                    print(f" {i}. {h}")
                print()
            continue

        if expr.lower() == "vars":
            if not value_map:
                print("$ No variables defined yet.\n")
            else:
                print("\n$ Variables:")
                for var, val in value_map.items():
                    print(f" {var} = {val}")
                print()
            continue

        try:
            process(expr, value_map, history)
        except Exception as e:
            print(f"$ Error: {e}\n")

if __name__ == "__main__":
    main()
