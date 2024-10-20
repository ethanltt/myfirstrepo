# Python Curriculum for a 10-Year-Old

## Week 1: Introduction to Python and Basic Syntax
- **Day 1: Introduction to Programming**
  - What is Python?
  - Installing Python and using an IDE (e.g., Thonny or Repl.it).
  - Running your first program: `print("Hello, World!")`.
  
- **Day 2-3: Variables and Data Types**
  - Variables: What are they and how to use them?
  - Data types: Strings, integers, floats.
  - Simple arithmetic operations: addition, subtraction, multiplication, division.
  
- **Day 4-5: Basic Input and Output**
  - `input()` function for user interaction.
  - Using `print()` to display results.
  - Simple calculator program.

```python
# Tutorial for Using Input() in Python

# Getting User Input with input()

def get_user_name():
    """Asks the user for their name and returns it."""
    return input("Please enter your name: ")

def get_user_age():
    """Asks the user for their age and returns it."""
    while True:
        try:
            age = int(input("Please enter your age: "))
            if age < 0:
                print("Age cannot be negative.")
            else:
                return age
        except ValueError:
            print("Invalid input. Please enter a valid age.")

# Example usage:

def greet_user(name):
    """Greets the user by name."""
    print(f"Hello, {name}!")

def main():
    # Get the user's name and age
    name = get_user_name()
    age = get_user_age()

    # Greet the user with their name
    greet_user(name)

    # Print a message with their age
    print(f"You are {age} years old.")

if __name__ == "__main__":
    main()
```


## Week 2: Control Structures and Loops
- **Day 1-2: Conditionals (if, else, elif)**
  - Explaining true/false conditions.
  - Writing programs with decision-making (e.g., "Guess the Number" game).
  
- **Day 3-4: Loops (for and while)**
  - `for` loops: Looping over a range or list.
  - `while` loops: Repeating until a condition is met.
  - Fun project: Multiplication tables generator.
  
- **Day 5: Combining Loops and Conditionals**
  - More complex decision-making with loops.
  - Project: Simple guessing game.

## Week 3: Functions and Modular Programming
- **Day 1-2: Functions**
  - Defining and calling functions.
  - Parameters and return values.
  - Project: Temperature converter (Celsius to Fahrenheit).
  
- **Day 3-4: Organizing Code with Functions**
  - Using functions to break down complex problems.
  - Project: Simple calculator with functions for each operation.
  
- **Day 5: Debugging and Error Handling**
  - Understanding common Python errors (syntax errors, logic errors).
  - Using `try` and `except` for error handling.

## Week 4: Lists and Basic Data Structures
- **Day 1-2: Lists**
  - Introduction to lists: creating, indexing, adding, removing items.
  - Using loops with lists.
  - Project: List of favorite movies.
  
- **Day 3-4: List Methods and Operations**
  - Sorting, reversing, and searching lists.
  - Project: To-do list manager.
  
- **Day 5: Introduction to Tuples and Dictionaries**
  - Understanding tuples (immutable lists) and dictionaries (key-value pairs).
  - Project: Simple dictionary-based word translator.

## Week 5: Working with Libraries and Simple Projects
- **Day 1-2: Introduction to Python Libraries**
  - What are libraries? How to import and use them.
  - Using `random` for generating random numbers.
  - Project: Number guessing game with random number generation.
  
- **Day 3-4: Working with Time and Math Libraries**
  - Using `time` for delays and timing events.
  - Simple math operations with the `math` library.
  - Project: A timer or stopwatch.
  
- **Day 5: Final Project**
  - Creating a basic game: Rock, Paper, Scissors.
  - Use of functions, loops, conditionals, and user input.

## Week 6: More Advanced Concepts (Optional)
- **Day 1-2: File Handling**
  - Reading from and writing to files.
  - Project: Save high scores to a file.
  
- **Day 3-4: Introduction to Object-Oriented Programming**
  - Basic concepts: classes and objects.
  - Simple example: Creating a "pet" object with attributes like name and age.
  
- **Day 5: Fun Projects**
  - Choose a final project based on the child’s interests (e.g., a simple adventure game or quiz).
