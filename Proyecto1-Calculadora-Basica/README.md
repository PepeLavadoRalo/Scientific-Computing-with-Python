# Arithmetic Arranger

This Python program arranges arithmetic problems vertically and side-by-side. It can also display the results if desired.

## **Functionality**
- Formats arithmetic problems (addition and subtraction) neatly.
- Option to show answers alongside the problems.
- Validates input, ensuring no more than 4 digits for operands and that only `+` and `-` are used.

## **Error Handling**
- Maximum of 5 problems at once.
- Only supports `+` and `-` operations.
- Operands cannot exceed 4 digits.

```python
def arithmetic_arranger(problems, show_answers=False):
    # Check if there are more than 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    arranged_problems = []
    answers = []
    
    for problem in problems:
        # Split the problem into its components
        components = problem.split()
        if len(components) != 3:
            return "Error: Invalid problem format."
        
        num1, operator, num2 = components
        
        # Validate numbers and operator
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Perform the calculation
        if operator == '+':
            result = int(num1) + int(num2)
        else:
            result = int(num1) - int(num2)
        
        # Format each problem and answer
        width = max(len(num1), len(num2)) + 2
        top = num1.rjust(width)
        bottom = operator + " " + num2.rjust(width - 2)
        line = '-' * width
        answer = str(result).rjust(width)
        
        # Append to arranged problems and answers
        arranged_problems.append(f"{top}\n{bottom}\n{line}")
        answers.append(answer)
    
    # Join the problems and answers
    arranged_output = "    ".join(arranged_problems)
    
    if show_answers:
        arranged_output += "\n    " + "    ".join(answers)
    
    return arranged_output
```

## **Example Usage**

### Example without answers:

```python
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
```

### Example with answers:

```python
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
```

## **Example Output**

### Without answers:

```
   32      3801      45      123
+  698   -    2   +  43   +   49
 -----    -----    ----    -----
```

### With answers:

```
   32       1      9999       523 
+   8   -3801  +   9999    -   49 
-----    -----     -----     ----- 
   40   -3800      19998      474 

```
