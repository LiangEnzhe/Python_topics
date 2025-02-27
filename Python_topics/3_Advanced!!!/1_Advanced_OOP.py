# ----------------------------------------------------------------------
# Advanced OOP Concepts in Python
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# 1. Abstract Base Classes (ABC) and Interfaces
# ----------------------------------------------------------------------
# Abstract Base Classes (ABCs) define a blueprint for other classes.
# ABCs cannot be instantiated directly and require child classes to implement
# specific methods. This enforces a common interface across related classes.

from abc import ABC, abstractmethod

# Define an abstract base class
class Shape(ABC):
    """Abstract base class for shapes."""
    
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass

# Subclassing the abstract class
class Rectangle(Shape):
    """Rectangle implements the Shape interface."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    """Circle implements the Shape interface."""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Using the abstract base class
shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")

# ----------------------------------------------------------------------
# 2. Composition Over Inheritance
# ----------------------------------------------------------------------
# Composition is an alternative to inheritance. Instead of extending functionality
# by subclassing, we create a class that contains other objects and delegates work to them.

# Example: Using Composition for Reusability
class Engine:
    """A class representing an engine."""
    def start(self):
        return "Engine started"
    
    def stop(self):
        return "Engine stopped"

class Car:
    """A car class using composition to include an engine."""
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.engine = Engine()  # Car "has-a" Engine
    
    def start(self):
        return f"{self.make} {self.model}: {self.engine.start()}"
    
    def stop(self):
        return f"{self.make} {self.model}: {self.engine.stop()}"

# Using composition
car = Car("Toyota", "Corolla")
print(car.start())  # Prints: Toyota Corolla: Engine started
print(car.stop())   # Prints: Toyota Corolla: Engine stopped

# ----------------------------------------------------------------------
# 3. Design Patterns
# ----------------------------------------------------------------------
# Design patterns are reusable solutions to common problems in software design.

# ----------------------------------------------------------------------
# 3.1 Singleton Pattern
# ----------------------------------------------------------------------
# Ensure that only one instance of a class is created.

class Singleton:
    _instance = None  # Class-level attribute to hold the single instance
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:  # If instance does not exist, create one
            cls._instance = super().__new__(cls)
        return cls._instance

# Using the Singleton
singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # Prints: True (both are the same instance)

# ----------------------------------------------------------------------
# 3.2 Factory Pattern
# ----------------------------------------------------------------------
# A factory creates objects without specifying the exact class of the object.

class ShapeFactory:
    """A factory class for creating shapes."""
    @staticmethod
    def create_shape(shape_type, *args):
        if shape_type == "rectangle":
            return Rectangle(*args)
        elif shape_type == "circle":
            return Circle(*args)
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

# Using the Factory
factory = ShapeFactory()
shape = factory.create_shape("rectangle", 4, 5)
print(f"Rectangle Area: {shape.area()}")  # Prints: Rectangle Area: 20

# ----------------------------------------------------------------------
# 3.3 Observer Pattern
# ----------------------------------------------------------------------
# The observer pattern defines a one-to-many relationship, where one object (subject)
# notifies multiple observers of changes to its state.

class Subject:
    """Subject that notifies observers."""
    def __init__(self):
        self._observers = []  # List of observers
    
    def add_observer(self, observer):
        self._observers.append(observer)
    
    def remove_observer(self, observer):
        self._observers.remove(observer)
    
    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    """Observer interface."""
    def update(self, message):
        raise NotImplementedError

class ConcreteObserver(Observer):
    """Concrete implementation of an observer."""
    def __init__(self, name):
        self.name = name
    
    def update(self, message):
        print(f"{self.name} received message: {message}")

# Using the Observer Pattern
subject = Subject()
observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")

subject.add_observer(observer1)
subject.add_observer(observer2)

subject.notify_observers("The state has changed!")
# Prints:
# Observer 1 received message: The state has changed!
# Observer 2 received message: The state has changed!

# ----------------------------------------------------------------------
# Final Thoughts
# ----------------------------------------------------------------------
# Summary of Advanced OOP Concepts:
# - **Abstract Base Classes (abc module)**: Define common interfaces and enforce implementation in subclasses.
# - **Composition over Inheritance**: Reuse functionality by composing objects instead of inheriting from base classes.
# - **Design Patterns**:
#     - **Singleton**: Ensures only one instance of a class exists.
#     - **Factory**: Creates objects dynamically without specifying their exact class.
#     - **Observer**: Allows multiple objects to listen for changes in a subject.

# Advanced OOP techniques and design patterns make code more flexible, reusable, and maintainable.
