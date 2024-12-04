def arithmetic_arranger(problems, show_answers=False):
    """
    Arrange arithmetic problems vertically and side-by-side.

    Args:
        problems (list): List of arithmetic problems as strings.
        show_answers (bool): If True, include the results of the problems.

    Returns:
        str: The formatted arithmetic problems or an error message.
    """

    # Error: Limit the number of problems to a maximum of 5.
    if len(problems) > 5:
        return "Error: Too many problems."

    # Lists to store the formatted components of each problem
    first_line = []   # To store the first operands
    second_line = []  # To store the operator and second operands
    dashes = []       # To store the dashes separating the problems
    results = []      # To store the results if show_answers is True

    for problem in problems:
        # Split the problem into its components (operands and operator)
        parts = problem.split()
        operand1, operator, operand2 = parts

        # Error: Only allow '+' or '-' operators.
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Error: Operands must only contain digits.
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        # Error: Operands cannot have more than 4 digits.
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine the width needed for formatting the problems
        max_width = max(len(operand1), len(operand2)) + 2

        # Format each part of the problem for alignment
        first_line.append(operand1.rjust(max_width))
        second_line.append(operator + operand2.rjust(max_width - 1))
        dashes.append('-' * max_width)

        # If show_answers is True, calculate the result and format it
        if show_answers:
            result = str(int(operand1) + int(operand2) if operator == '+' else int(operand1) - int(operand2))
            results.append(result.rjust(max_width))

    # Combine all formatted parts with 4 spaces between problems
    arranged_problems = "\n".join([
        "    ".join(first_line),
        "    ".join(second_line),
        "    ".join(dashes),
    ])

    # Add the results line if show_answers is True
    if show_answers:
        arranged_problems += "\n" + "    ".join(results)

    return arranged_problems

# Example usage
if __name__ == "__main__":
    # Valid input without answers
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
    print()
    # Valid input with answers
    print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
    print()
    # Invalid operator
    print(arithmetic_arranger(["32 + 698", "3801 / 2", "45 + 43", "123 + 49"]))
    print()
    # Operand length exceeds 4 digits
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "12345 + 43", "123 + 49"]))
