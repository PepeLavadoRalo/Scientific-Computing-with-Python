# Polygon Area Calculator Project

This project defines two classes, `Rectangle` and `Square`, to calculate areas, perimeters, diagonals, and more, using Object-Oriented Programming principles. The `Square` class inherits from `Rectangle`, ensuring reusable and extendable code.

## Features:
- Set dimensions dynamically.
- Calculate area, perimeter, and diagonal length.
- Generate ASCII art representations of shapes.
- Determine how many times a smaller shape can fit into a larger one.

## Classes:
### `Rectangle`
Represents a rectangle with a specified width and height. Provides methods to calculate area, perimeter, diagonal, and generate ASCII art representation.

**Methods:**
- `set_width(width)` - Sets the width of the rectangle.
- `set_height(height)` - Sets the height of the rectangle.
- `get_area()` - Returns the area of the rectangle.
- `get_perimeter()` - Returns the perimeter of the rectangle.
- `get_diagonal()` - Returns the diagonal length of the rectangle.
- `get_picture()` - Returns an ASCII art representation of the rectangle.
- `get_amount_inside(shape)` - Calculates how many times a given shape can fit inside this rectangle.

### `Square`
Represents a square, which is a special case of the rectangle where width and height are always equal.

**Methods:**
- `set_side(side)` - Sets the side of the square, updating both width and height.
- `set_width(width)` - Overrides `Rectangle`'s method to ensure both sides are the same.
- `set_height(height)` - Overrides `Rectangle`'s method to ensure both sides are the same.

# -------------------------------
# Example Usage
# -------------------------------

# Create a rectangle
rect = Rectangle(10, 5)
print(rect)  # Output: Rectangle(width=10, height=5)
print("Area:", rect.get_area())  # Output: Area: 50
print("Perimeter:", rect.get_perimeter())  # Output: Perimeter: 30
print("Diagonal:", rect.get_diagonal())  # Output: Diagonal: 11.180339887498949
print("Picture:\n", rect.get_picture())
# Output:
# **********
# **********
# **********
# **********
# **********

# Create a square
sq = Square(9)
print(sq)  # Output: Square(side=9)
print("Area:", sq.get_area())  # Output: Area: 81
print("Diagonal:", sq.get_diagonal())  # Output: Diagonal: 12.727922061357855
print("Picture:\n", sq.get_picture())
# Output:
# *********
# *********
# *********
# *********
# *********
# *********
# *********
# *********
# *********

# Modify dimensions
sq.set_side(4)
print(sq)  # Output: Square(side=4)
print("Picture:\n", sq.get_picture())
# Output:
# ****
# ****
# ****
# ****

# Determine how many squares fit in a rectangle
rect.set_width(16)
rect.set_height(8)
print("Squares that fit:", rect.get_amount_inside(sq))  # Output: Squares that fit: 8
```
## Running the Project:
To use the Polygon Area Calculator, you can run the provided code in a Python environment. The example usage demonstrates how to create Rectangle and Square objects, set dimensions, and use the various methods to calculate areas, perimeters, diagonals, and generate ASCII representations.

