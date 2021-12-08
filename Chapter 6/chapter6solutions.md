# Chapter 6 - Review Questions

## True/False

1. False.
2. False. It can be called multiple times.
3. True.
4. True. If no return statement is present, `None` is returned by default.
5. False. Python parameters are passed by value.
6. False. A Python function can return multiple values.
7. False.
8. True.
9. True.
10. False.

## Multiple Choice

1. b.
2. a.
3. a.
4. b.
5. d.
6. a.
7. d.
8. a.
9. d.
10. a.

## Discussion

1. One motivation is to avoid duplicate code in a program. If you are repeating some block of code, you can construct a function which makes that block, and may depend on some parameters. The other motivation is to make the code more *modular*. This means separating the code into small pieces to make it more readable. [Modular programming in Wikipedia](https://en.wikipedia.org/wiki/Modular_programming).
2. When a program contains a function, it doesn't follow this model, because the function may be defined at the end of the code. When the function is called, the program jumps to the function definition and once it finishes executing it, it comes back to the point it left off.
3. Parameters:
    * a) We can pass custom values to a function through parameters.
    * b) The formal parameter is the name it has in the function definition (they are *variables*), while the actual parameter is the value that is passed.
    * c) Parameters and variables are similar because they can take different values, and they are different because parameters take only one value, while variables can take multiple values.

4. Input and output:
    * a) *Inputs* are provided through the use of parameters.
    * b) *Outputs* are provided through the `return` keyword.
    
5. Consider:

```
def cube(x):
    answer = x * x * x
    return answer
```
Then:
    * a) This function computes the cube of a number and return its value.
    * b) `print(cube(y))`.
    * c) Because `answer` from the function definition is local to that function, while `answer` from outside the function is another different variable.