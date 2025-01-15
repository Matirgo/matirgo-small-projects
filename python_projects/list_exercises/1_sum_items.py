# Question 1. Sum Items in List
# Question Pack: https://www.w3resource.com/python-exercises/list/

# ========== Instructions ==========
# Write a Python programme to sum all the items in a list.

# Basic function that assumes input is already correct.
def sum_list_basic(list_object):
    """A function that takes a list as input and sums all of its elements.
    The function assumes the list only contains numeric elements."""
    total = 0
    for i in list_object:
        total += i
    return total

# Advanced function that checks element types and simplifies the calculations.
def sum_list(list_object):
    """A function that takes a list as input and sums all of its elements.
    The function checks if the elements are numeric, and if not, raises an error."""
    # Check element types.
    if not all(isinstance(i, (int, float)) for i in list_object):
        raise TypeError("All elements in the list must be integers or floats.")
    return sum(list_object)

# ========== Test Cases ==========

# Test Case 1
list1 = [1, 2, 3]
if sum_list_basic(list1) == 6:
    print("Test Case 1 passed.")
else:
    print("Test Case 1 failed.")

# Test Case 2
list2 = [-1, -2, -3]
if sum_list_basic(list2) == -6:
    print("Test Case 2 passed.")
else:
    print("Test Case 2 failed.")

# Test Case 3
list3 = []
if sum_list_basic(list3) == 0:
    print("Test Case 3 passed.")
else:
    print("Test Case 3 failed.")

# Test Case 4
list4 = [42]
if sum_list_basic(list4) == 42:
    print("Test Case 4 passed.")
else:
    print("Test Case 4 failed.")

# Test Case 5
list5 = [1.5, 2.5, 3.5]
if sum_list_basic(list5) == 7.5:
    print("Test Case 5 passed.")
else:
    print("Test Case 5 failed.")

# Test Case 6
list6 = [-1, 42, "C"]
try:
    sum_list(list6)
    print("Test Case 6 failed.")
except TypeError:
    print("Test Case 6 passed.")
except Exception as e:
    print(f"Test Case 6 failed. Unexpected exception: {e}.")