# CSS125 - FA1.1

## QUESTION 1.8

![[CSS125 - FA1.1_1.8.png]]

## QUESTION 1.11

### 1. **Abstraction And Information Hiding**

Procedures allow us to hide implementation details behind a well-defined interface. The caller only needs to know _what_ the function does (its contract), not _how_ it accomplishes the task. This reduces cognitive load and allows programmers to think at higher levels of abstraction.

> [!EXAMPLE]
> The `factorial_of()` function hides the recursive implementation details. Users only need to know it takes an unsigned integer and returns the factorial value.
>

### 2. **Code Reusability and DRY Principle**

By packaging common operations into functions, we avoid duplicating code throughout our program (Don't Repeat Yourself). This makes our codebase more maintainable and reduces the chance of introducing bugs through copy-paste errors.

> [!EXAMPLE]
> Instead of writing the factorial calculation logic multiple times, we can call `factorial_of(n)` wherever needed.

### 3. **Modularity And Testing**

Functions create discrete, testable units that can be developed, debugged, and verified independently. This modular approach makes complex programs more manageable by breaking them into smaller, understandable components.

> [!EXAMPLE]
> Testing the `factorial_of()` function in isolation with various inputs (0, 1, 5, 20) to ensure it behaves correctly before integrating it into larger programs.

