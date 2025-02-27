# ----------------------------------------------------------------------
# Classes and Objects
# ----------------------------------------------------------------------
# A class is a blueprint for creating objects (instances).
# An object is an instance of a class, representing real-world entities.

# Define a class
class Person:
    """A class to represent a person."""
    
    # The __init__ method is a special method called when an object is created.
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

# Create objects (instances) of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Access object attributes
print(person1.name)  # Prints: Alice
print(person2.age)   # Prints: 25

# Modify object attributes
person1.age = 31  # Change age of person1
print(person1.age)  # Prints: 31

# ----------------------------------------------------------------------
# Methods and Attributes
# ----------------------------------------------------------------------
# Methods are functions defined within a class that operate on the object's attributes.

class Circle:
    """A class to represent a circle."""
    
    def __init__(self, radius):
        self.radius = radius  # Instance attribute
    
    # Instance method
    def area(self):
        """Calculate and return the area of the circle."""
        return 3.14159 * self.radius ** 2
    
    # Instance method
    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * 3.14159 * self.radius

# Create an object of Circle
circle = Circle(5)

# Call methods
print(circle.area())  # Prints: 78.53975
print(circle.circumference())  # Prints: 31.4159

# ----------------------------------------------------------------------
# Inheritance and Polymorphism
# ----------------------------------------------------------------------
# Inheritance allows a class (child) to inherit attributes and methods from another class (parent).
# Polymorphism allows objects of different classes to be treated as objects of a common parent class.

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        """General speak method (to be overridden by child classes)."""
        return "I make a sound!"

# Child classes
class Dog(Animal):
    def speak(self):
        return f"{self.name} says: Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"

# Create objects of child classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Demonstrate polymorphism
animals = [dog, cat]
for animal in animals:
    print(animal.speak())
# Prints:
# Buddy says: Woof!
# Whiskers says: Meow!

# ----------------------------------------------------------------------
# Special Methods
# ----------------------------------------------------------------------
# Special methods (also called "magic" or "dunder" methods) are predefined methods
# with double underscores. They allow objects to interact with built-in Python functionality.

class Point:
    """A class to represent a point in 2D space."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # __str__: Defines how an object is represented as a string (e.g., print(object))
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    # __repr__: Defines the string representation of the object (used by developers).
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    # __eq__: Defines how equality (==) is determined for objects.
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    
    # __add__: Enables addition (+) for objects.
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

# Create objects
p1 = Point(2, 3)
p2 = Point(5, 7)

# Demonstrate special methods
print(p1)  # Calls __str__, Prints: Point(2, 3)
print(repr(p2))  # Calls __repr__, Prints: Point(5, 7)

# Equality
print(p1 == p2)  # Calls __eq__, Prints: False
print(p1 == Point(2, 3))  # Prints: True

# Addition
p3 = p1 + p2  # Calls __add__
print(p3)  # Prints: Point(7, 10)
