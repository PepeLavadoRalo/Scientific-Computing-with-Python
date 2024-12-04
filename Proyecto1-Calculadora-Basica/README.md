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
