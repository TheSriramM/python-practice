output = []
while True:
    expression = input()
    if expression == "()":
        break
    elif "(" not in expression:
        output.append(f"{expression:.2f}")
    else:
        expression.removeprefix("(")
        expression.removesuffix(")")
        expression = expression.split()
        if len(expression) == 3:
            pass