## Strategy Pattern in Python

The Strategy pattern is a behavioral design pattern that enables an object to dynamically change its behavior at runtime by encapsulating interchangeable strategies or algorithms. It allows the selection of a specific algorithm from a family of algorithms based on the current context or requirements.

### Principles Applied

When implementing the Strategy pattern, the following principles are applied:

1. **Encapsulation:** The Strategy pattern encapsulates each algorithm or strategy within separate classes, promoting code organization and separation of concerns.

2. **Abstraction:** The Strategy pattern relies on abstraction by defining a common interface or abstract class that all strategies must implement. Clients interact with the context object and strategies through this interface, without knowing the specific implementation details.

3. **Dependency Inversion Principle (DIP):** The Strategy pattern adheres to the DIP by allowing clients to depend on abstractions (interfaces or abstract classes) rather than concrete classes. This promotes loose coupling and easier maintenance.

4. **Open/Closed Principle (OCP):** The Strategy pattern supports the OCP by providing an extension point for adding new strategies or algorithms without modifying existing client code or the context class.

5. **Single Responsibility Principle (SRP):** The Strategy pattern adheres to the SRP by separating the responsibility of different algorithms or strategies into dedicated classes, ensuring each class/component has a single responsibility.

6. **Code Reusability:** The Strategy pattern promotes code reusability by encapsulating each strategy within a separate class. Strategies can be used in multiple parts of the codebase, preventing code duplication and ensuring consistent behavior.

### UML Diagram
```uml
                                                   +-----------------------+
                                                   |        Context        |
                                                   +-----------------------+
                                                   | - strategy: Strategy  |
                                                   +-----------------------+
                                                   | + set_strategy()      |
                                                   | + execute_strategy()  |
                                                   +-----------------------+
                                                              ^
                                                              |
                                              _______________/ \_______________
                                             |                                 |
                                             |                                 |
                                   +-------------------+             +-------------------+
                                   |      Strategy     |             | ConcreteStrategyA |
                                   +-------------------+             +-------------------+
                                   | - algorithm()     |             | - algorithm()     |
                                   +-------------------+             +-------------------+
                                             ^                                  ^
                                             |                                  |
                                             |                                  |
                                   +-------------------+             +-------------------+
                                   |      Strategy     |             | ConcreteStrategyB |
                                   +-------------------+             +-------------------+
                                   | - algorithm()     |             | - algorithm()     |
                                   +-------------------+             +-------------------+
```
```angelscript
This UML diagram represents the Strategy Pattern using simple ASCII characters within GitHub Markdown syntax. The diagram consists of
the following elements:

- `Context`: Represents the context object that interacts with the strategies. The context object holds a reference to the current strategy
 and can change it dynamically at runtime.
- `Strategy`: An interface or abstract class that declares the method(s) that all concrete strategies must implement.
- `ConcreteStrategyA` and `ConcreteStrategyB`: Concrete strategy classes that implement the `Strategy` interface/abstract class
and define their specific algorithm(s).

Please note that GitHub Markdown does not support interactive or dynamic diagrams. The above representation is a static UML diagram
using ASCII characters within Markdown syntax. For a more interactive and visually appealing UML diagram, you may consider using
dedicated UML diagramming tools or converting the diagram into an image format using tools like PlantUML or Mermaid.
```

## Usage
To implement the Strategy pattern in Python, follow these steps:

1. Define an interface or abstract class that represents the common interface for all strategies. This interface or abstract class should declare the method(s) that all concrete strategies must implement.

2. Create concrete classes that implement the interface or inherit from the abstract class, representing different strategies or algorithms. Each concrete class should provide its own implementation of the declared method(s).

3. Implement a context class that holds a reference to the current strategy and interacts with the strategies through the common interface. The context class should provide methods to set the strategy dynamically and execute the strategy.

4. Client code interacts with the context object to set the desired strategy and execute it. The client code can work with the strategies without knowing the specific implementation details.

Here's an example illustrating the Strategy pattern using an abstract class in Python:
```python
from abc import ABC, abstractmethod

class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

class QuickSortStrategy(SortingStrategy):
    def sort(self, data):
        print("Sorting using QuickSort")

class MergeSortStrategy(SortingStrategy):
    def sort(self, data):
        print("Sorting using MergeSort")

class Context:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, data):
        if self.strategy is not None:
            self.strategy.sort(data)
        else:
            raise ValueError("No strategy set")

# Client code
context = Context()
context.set_strategy(QuickSortStrategy())
context.execute_strategy(data=[4, 2, 7, 1])  # Output: Sorting using QuickSort

context.set_strategy(MergeSortStrategy())
context.execute_strategy(data=[4, 2, 7, 1])  # Output: Sorting using MergeSort
```
