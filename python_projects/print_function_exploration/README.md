# Print Function Exploration

Python's **print()** function is one of the first that beginner programmers learn given its simplicity and high utility. It may become a far more complicated function, however, given its many different parameters, which are explored in this project.

## The print() function

### Brief Description

Referenced from [W3Schools: Python print() function](https://www.w3schools.com/python/ref_func_print.asp).

Prints the specified message between the brackets to the screen/standard output device.

### Input

Takes any object. In this example, **"Hello, World!"** is a string object.

### Output

Converts the specified object(s) into a string if not already a string, and prints it to the screen/standard output device.

### Parameter Values
- Object(s)
    - The object that is converted to a string before being displayed on the standard output device.
- sep = "separator"
    - Specifies how to separate objects. It will add that specific entry between each object in the function.
- end = "end"
    - Specify what to print at the end.
    - The default is "\n".
- file
    - Specify to where Python should write the output.
    - The default is sys.stdout.
- flush
    - A Boolean specifying if the output is to be flushed (True) or to be buffered (False).
      - This is especially useful when a developer wants to guarantee a given piece of output is outputted regardless of the buffering stage, essentially manually force printing.
      - Its use is not very common.
    - The default is False.
