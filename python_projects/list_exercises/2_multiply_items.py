# Question 2. Multiply Items in List
# Question Pack: https://www.w3resource.com/python-exercises/list/

# ========== Instructions ==========
# Write a Python programme to multiply all the items in a list.

# Basic function that assumes input is already correct.
def multiply_list_basic(list_object):
    """A function that takes a list as input and multiplies all of its elements.
    The function assumes the list only contains numeric elements."""
    # Account for an empty list by initialising the total to zero if needed.
    if len(list_object) > 0:
        total = 1
        for i in list_object:
            total *= i
    else:
        total = 0
    return total

# Advanced function that checks element types and simplifies the calculations.
def multiply_list(list_object):
    """A function that takes a list as input and multiplies all of its elements.
    The function checks if the elements are numeric, and if not, raises an error."""
    # Check element types.
    if not all(isinstance(i, (int, float)) for i in list_object):
        raise TypeError("All elements in the list must be integers or floats.")
    if len(list_object) > 0:
        total = 1
        for i in list_object:
            total *= i
    else:
        total = 0
    return total

# ========== Test Cases ==========

# Test Case 1
list1 = [2, 3, 4]
if multiply_list_basic(list1) == 24:
    print("Test Case 1 passed.")
else:
    print("Test Case 1 failed.")

# Test Case 2
list2 = [-2, -3, -4]
if multiply_list_basic(list2) == -24:
    print("Test Case 2 passed.")
else:
    print("Test Case 2 failed.")

# Test Case 3
list3 = []
if multiply_list_basic(list3) == 0:
    print("Test Case 3 passed.")
else:
    print("Test Case 3 failed.")

# Test Case 4
list4 = [42]
if multiply_list_basic(list4) == 42:
    print("Test Case 4 passed.")
else:
    print("Test Case 4 failed.")

# Test Case 5
list5 = [1.5, -2.5, 3.5]
if multiply_list_basic(list5) == -13.125:
    print("Test Case 5 passed.")
else:
    print("Test Case 5 failed.")

# Test Case 6
list6 = [-1, 42, "C"]
try:
    multiply_list(list6)
    print("Test Case 6 failed.")
except TypeError:
    print("Test Case 6 passed.")
except Exception as e:
    print(f"Test Case 6 failed. Unexpected exception: {e}.")