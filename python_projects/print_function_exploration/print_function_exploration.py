# The following programme investigates the different parameters that the print function can take.


# ========== Object ==========


# Parameter type print statements to make the final terminal output prettier.
print("===== Object =====")
print()

# The object parameter may be a simple string.
print("Hello, World!")

# The object parameter may also be of a different type and then be converted to string before being outputted.
print(0)


# ========== Separator ==========



# Parameter type print statements to make the final terminal output prettier.
print()
print("===== Separator =====")
print()

# The sep (separator) parameter specifies how to separate objects by adding the specific thing between each parameter.
# The default of this is a space (" ").

# 1. Inputting nothing as the separator will concatenate all objects ("Hello,World!").
print("Hello", ",", "World", "!", sep = "")

# 2. Inputting a space as the separator will separate all objects with a space ("Hello , World !").
print("Hello", ",", "World", "!", sep = " ")

# 3. Inputting a hyphen (-) as the separator will separate all objects with a hyphen ("Hello-,-World-!").
print("Hello", ",", "World", "!", sep = "-")

# Perhaps this is more practical here.
print("04", "03", "1958", sep = "-")
print("04", "03", "1958", sep = "/")


# ========== End ==========


# Parameter type print statements to make the final terminal output prettier.
print()
print("===== End =====")
print()

# The end parameter specifies what should come at the end of the objects in the print function.
# The default of this is a new line ("\n").

# 1. Inputting nothing as the end will replace the newline, so future print function outputs appear on the same line..
print("Hello, World!", end = "")
print("Hello, World!")

# 2. Inputting something will simply add it to the end of those objects. A newline may also be added.
print("personalemail", end = "@personaldomain.com\n")


# ========== File ==========


# Parameter type print statements to make the final terminal output prettier.
print()
print("===== File =====")
print()

# The file parameter allows for the specification of where the print function should send its output to.
# This is more complicated as it delves into file input/output (I/O), but it can be achieved in two steps:
# 1. Opening the file in Python and giving permission to write within it.
# 2. Specifying that the print() function should output to that file.
# The default is sys.stdout.

# Assign the "text_file" variable to the now open .txt file, and allow for it to be written in and read from.
text_file = open("text.txt", "w+")

# Print a string inside the text file.
print("Hello, Text File!", file = text_file)

# Move the file pointer to the beginning of the file.
text_file.seek(0)

# Assign the contents of the text file to the "text_content" variable.
text_content = text_file.read()

# Print the contents of the text file.
print(text_content)

# Close the file to release system resources and minimise the chance of data corruption.
text_file.close()


# ========== Flush ==========


# Parameter type print statements to make the final terminal output prettier.
# Printing the contents of the text file includes printing a newline at the end of said file, hence the lack of the first print().
print("===== Flush =====")
print()

# The flush parameter allows the developer to manually choose when a buffered I/O stream is outputted.
# This is used in situations where you want to guarantee that something is outputted, regardless of the buffering process.
# It does not need to be used in most cases, but may sometimes prove valuable.
# The default is False.

# The following (modified) code is taken from a Stack Overflow post made by Kurt Bourbaki on December 4th, 2022, under the "What does print()'s `flush` do?" question.
# The webpage was accessed on December 29th, 2024.

# Import the time module to use the sleep method, which will delay processing by a specified period of time.
import time

# No flush.
for i in range(5):
    print(i, end = " ", flush = False)  # Print everything together at the end.
    time.sleep(0.5)

print("End (without flush).")

# Flush.
for i in range(5):
    print(i, end = " ", flush = True)  # Print numbers as soon as they are generated.
    time.sleep(0.5)

print("End (with flush).")