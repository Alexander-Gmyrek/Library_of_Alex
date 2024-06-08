# Python Notes

Created: June 2, 2024 2:15 PM

## Quick Notes

- NO you can’t do switch cases in Python! *Actually you can now in Python 3.10
    - *This is now for Python ≥3.9
    - Try: Using a dictionary:
    
    ```python
    def f(x):
        return {
            'a': 1,
            'b': 2
        }.get(x, 9)    # 9 will be returned default if x is not found
    ```
    
- What is lambda
    - It’s an inline function and if you use it it makes you look cool?
    - Ok update apparently it has something to do with functional programming. Functional programming is basically programming using only functions with no changing state. This means that for any given input you get the same output every time. One of the concepts from functional programming is passing one function into another broader function. From that you get the idea of “currying” where instead of handling the entire operation at once it instead Returns a function that handles the next part of the operation. The later part has the previous state “bound” to it and the new on the fly created function is what gets called when we want to check a condition. So instead of binding function to an object you bind objects to a function. Labda is the next step and basically allows you to simplify and chain these together to basically create a data pipeline out of “fundamental functions” like map, filter, slice, or take. In functional programming, “fundamental functions” are often referred to as “higher-order functions” or “functional programming primitives.”
- Testing notes
    - Pure Function: A function that has no side effects.
    - Side Effect: these are things like accessing the file system, making network calls, accessing global variables, accessing the current time, or random number generators.
    - Make code easier to test by removing or isolating side effects
    - Use abstraction by defining a “contract” with any outside modules. This contract governs inputs and outputs and allows you to swap out the outside modules with different ones so long as they follow the contract. This allows you to customize the behavior without having to change big parts of the program.
    - If your program is performing a function that is not behind an interface that function is “tightly coupled” to that part of the code because it is hard to customize. By extracting that functionality to a separate module, we gain the ability to customize it by writing different modules that implement the same interface. This also goes by the name “dependency injection”.

## Memory Leaks In Python

Apparently Python can have memory leaks. Here are some common ones:

- **Reference Cycles**: When two or more objects reference each other, they can create a cycle that the garbage collector can't resolve, leading to memory not being freed.
    - Example
    
    ```python
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
    
    a = Node(1)
    b = Node(2)
    a.next = b
    b.next = a  # This creates a cycle
    ```
    
- **Unreleased Resources**:
    - Example: Failing to close file handles, network connections, or database connections can lead to memory leaks.
    
    ```python
    file = open('file.txt')
    # If you forget to close the file, it can lead to a memory leak
    ```
    
- **Large Objects in Global Scope**: Keeping large objects or data structures in the global scope can prevent them from being garbage collected.
    - Example:
    
    ```python
    large_list = [i for i in range(1000000)]  # This large list remains in memory
    ```
    
- **Mutable Default Arguments**: Using mutable default arguments in functions can cause unexpected behavior and memory leaks.
    - Example:
    
    ```python
    def append_to_list(value, my_list=[]):
        my_list.append(value)
        return my_list
    
    list1 = append_to_list(1)
    list2 = append_to_list(2)
    # list1 and list2 share the same list object
    ```
    
- **Holding References in Data Structures**: Keeping references to objects in data structures like lists or dictionaries can prevent the garbage collector from freeing the memory.
    - Example:
    
    ```python
    class MyClass:
        instances = []
    
        def __init__(self):
            MyClass.instances.append(self)
    ```
    

### Tools to Identify and Fix Memory Leaks

- **Memory Profilers**:
    - Use memory profiling tools like `memory_profiler`, `tracemalloc`, or `objgraph` to identify memory leaks. First try “pip install memory_profiler” in your terminal.
        
        ```python
        from memory_profiler import profile
        
        @profile
        def my_func():
            a = [i for i in range(1000000)]
            return a
        
        my_func()
        ```
        
- **Garbage Collector Module**:
    - Use the `gc` module to identify reference cycles and uncollectable objects.
        
        ```python
        import gc
        gc.collect()
        print(gc.garbage)
        ```
        
- **Context Managers**:
    - Use context managers (`with` statements) to ensure resources are properly managed and released.
        
        ```python
        with open('file.txt') as file:
            data = file.read()
        # The file is automatically closed after the block
        ```