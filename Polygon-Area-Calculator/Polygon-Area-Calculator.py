class Rectangle:
    def __init__(self, width, height):
        """
        Initialize a Rectangle with width and height.
        """
        self.width = width
        self.height = height

    def set_width(self, width):
        """
        Set the width of the rectangle.
        """
        self.width = width

    def set_height(self, height):
        """
        Set the height of the rectangle.
        """
        self.height = height

    def get_area(self):
        """
        Calculate and return the area of the rectangle (width * height).
        """
        return self.width * self.height

    def get_perimeter(self):
        """
        Calculate and return the perimeter of the rectangle 
        (2 * width + 2 * height).
        """
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        """
        Calculate and return the diagonal of the rectangle using the 
        Pythagorean theorem: sqrt(width^2 + height^2).
        """
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        """
        Generate an ASCII art representation of the rectangle using '*' 
        characters. If the width or height exceeds 50, return a message 
        indicating the shape is too big for a picture.
        """
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, shape):
        """
        Calculate how many times another shape (rectangle or square) 
        can fit inside this rectangle without rotation.
        
        Args:
        - shape: Another instance of Rectangle or its subclass.
        
        Returns:
        - The number of times the shape fits inside the rectangle.
        """
        if not isinstance(shape, Rectangle):
            raise ValueError("The argument must be an instance of Rectangle or its subclasses.")
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        """
        Return a string representation of the rectangle in the format:
        'Rectangle(width=..., height=...)'.
        """
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        """
        Initialize a Square with a single side length. 
        Inherits the Rectangle class and sets width and height to the same value.
        """
        super().__init__(side, side)

    def set_side(self, side):
        """
        Set the side of the square. Updates both width and height 
        to maintain the square's proportions.
        """
        self.width = side
        self.height = side

    def set_width(self, width):
        """
        Override the Rectangle's set_width method to ensure both width 
        and height are updated to the same value in a square.
        """
        self.set_side(width)

    def set_height(self, height):
        """
        Override the Rectangle's set_height method to ensure both height 
        and width are updated to the same value in a square.
        """
        self.set_side(height)

    def __str__(self):
        """
        Return a string representation of the square in the format:
        'Square(side=...)'.
        """
        return f"Square(side={self.width})"


