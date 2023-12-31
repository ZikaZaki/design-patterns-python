# Factory Pattern in Python

The Factory pattern is a creational design pattern that provides an interface for creating objects, but allows subclasses to decide which class to instantiate. It encapsulates the object creation process, promotes code modularity, and adheres to key software design principles such as encapsulation, abstraction, and the SOLID principles.

## Principles Applied

When implementing the Factory pattern, the following principles are applied:

1. **Encapsulation:** The object creation process is encapsulated within a separate factory component, promoting code organization and separation of concerns.

2. **Abstraction:** The Factory pattern relies on abstraction by defining a common interface or abstract class for creating objects. Clients interact with the factory and created objects through this interface, without knowing the specific implementation details.

3. **Dependency Inversion Principle (DIP):** The Factory pattern adheres to the DIP by allowing clients to depend on abstractions (interfaces or abstract classes) rather than concrete classes. This promotes loose coupling and easier maintenance.

4. **Open/Closed Principle (OCP):** The Factory pattern supports the OCP by providing an extension point for adding new concrete classes or variants without modifying existing client code.

5. **Single Responsibility Principle (SRP):** The Factory pattern adheres to the SRP by separating the responsibility of object creation into a dedicated factory class, ensuring each class/component has a single responsibility.

6. **Code Reusability:** The Factory pattern promotes code reusability by centralizing the object creation logic. The factory can be used in multiple parts of the codebase, preventing code duplication and ensuring consistent object creation.

## UML Diagram
```uml
  +-----------------+       +------------------+
  |     Client      |       |      Factory     |
  +-----------------+       +------------------+
  |                 |       |                  |
  | + main()        |       | + createProduct()|
  |                 |       |                  |
  +--------^--------+       +--------^---------+
           |                         |
           |                         |
           |                         |
  +--------+--------+       +--------+---------+
  |   Product       |       | ConcreteFactoryA |
  +-----------------+       +------------------+
  |                 |       |                  |
  |  + operation()  |       | + createProduct()|
  |                 |       |                  |
  +-----------------+       +--------^---------+
                                     |
                                     |
                                     |
                            +--------v---------+
                            | ConcreteProductA |
                            +------------------+
                            |                  |
                            |  + operation()   |
                            |                  |
                            +------------------+
```
```angelscript
This UML diagram represents the Factory Pattern using simple ASCII characters within GitHub Markdown syntax. The diagram consists of
the following elements:

- `Client`: Represents the client code that interacts with the factory to create products.
- `Factory`: An abstract class or interface that declares the `createProduct()` method for creating products.
- `Product`: Represents the abstract product class or interface that defines the common operations that concrete products must implement.
- `ConcreteFactoryA`: A concrete factory that implements the `createProduct()` method to create `ConcreteProductA` objects.
- `ConcreteProductA`: A concrete product class that implements the `Product` interface and defines its specific `operation()`.

Please note that GitHub Markdown does not support interactive or dynamic diagrams. The above representation is a static UML diagram
using ASCII characters within Markdown syntax. For a more interactive and visually appealing UML diagram, you may consider using
dedicated UML diagramming tools or converting the diagram into an image format using tools like PlantUML or Mermaid.
```
## Usage

To implement the Factory pattern in Python, follow these steps:

1. Define an abstract class that represents the common interface for the objects to be created. This abstract class can contain common methods or properties shared by all the concrete classes.

2. Create concrete classes that inherit from the abstract class, representing different variants of the object. These concrete classes implement the specific behavior and unique characteristics of each variant.

3. Implement a factory class that encapsulates the object creation logic. The factory class should provide a method or methods to create the objects based on certain criteria or parameters. This method should return instances of the abstract class, allowing clients to interact with the objects through the common interface.

4. Client code interacts with the factory class to create objects, without knowing the specific implementation details. The client code can use the objects returned by the factory without being aware of the concrete classes.

Here's an example illustrating the Factory pattern using an **abstract** class in Python:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        else:
            raise ValueError("Invalid shape type")

# Client code
factory = ShapeFactory()
circle = factory.create_shape("circle")
circle.draw()
```

Here's another example illustrating the Factory pattern using a neat new feature **Protocols**, which is an alternative to abstract base classes:

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None:
        pass

class Circle:
    def draw(self) -> None:
        print("Drawing a circle")

class Square:
    def draw(self) -> None:
        print("Drawing a square")

def draw_shape(shape: Drawable) -> None:
    shape.draw()

circle = Circle()
square = Square()

draw_shape(circle)  # Output: Drawing a circle
draw_shape(square)  # Output: Drawing a square
```
