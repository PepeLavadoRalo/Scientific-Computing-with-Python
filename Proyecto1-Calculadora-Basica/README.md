# Arithmetic Arranger

This Python program arranges arithmetic problems vertically and side-by-side. It can also display the results if desired.

## Functionality

- Formats arithmetic problems (addition and subtraction) neatly.
- Option to show answers alongside the problems.
- Validates input, ensuring no more than 4 digits for operands and that only `+` and `-` are used.

## Example Usage

```python
from arithmetic_arranger import arithmetic_arranger

# Example without answers
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

# Example with answers
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

## Example Output
   32      3801      45      123
+  698   -    2   +  43   +  49
-----    -----    ----    -----
   730      3799      88      172

   32      3801      45      123
+  698   -  3801   +  43   +  49
-----    -----    ----    -----
   730     -3800      88      172

## Error Handling
Maximum of 5 problems at once.
Only supports + and - operations.
Operands cannot exceed 4 digits.
