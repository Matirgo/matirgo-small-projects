# Question 1. Sum Items in List
# Question Pack: https://www.w3resource.com/python-exercises/list/

# ========== Instructions ==========
# Write a Python programme to sum all the items in a list.

# Basic function that assumes input is already correct.
def sum_list_basic(list_object):
    """A function that takes a list as input and sums all of its elements.
    The function assumes the list only contains numeric elements.
    Time Complexity: O(6n + 5) -> O(n).
        Linear Operations: 
            1. Iterate through "list_object" in the for loop.
            2. Assign the current "list_object" value to "i".
            3. Read the value of "total" inside the first step of the for loop.
            4. Read the value of "i" inside the first step of the for loop.
            5 + 6. Add "total" by "i" for each pass, involving addition and assignment.
        Constant Operations:
            1. Create the "total" variable.
            2. Assign the "total" variable to the value of zero.
            3. Create the "i" variable inside the for loop.
            4. Access the "list_object" in the for loop.
            5. Return the value in "total".
    Space Complexity: O(1).
        Constant Storage:
            1. The value within the "total" variable."""
    total = 0
    for i in list_object:
        total += i
    return total

# Advanced function that checks element types and simplifies the calculations.
def sum_list(list_object):
    """A function that takes a list as input and sums all of its elements.
    The function checks if the elements are numeric, and if not, raises an error.
    Time Complexity (assuming no errors): O(5n + 4) -> O(n).
        Linear Operations:
            1. Iterate through "list_object" in the all() function.
            2. Assign the current "list_object" value to "i".
            3 + 4. Check if all values of "i" are integers OR floats.
                i. Python short-circuits this comparison, so it will be faster than 2n in most cases.
            5. Sum all of the elements in "list_object".
        Constant Operations:
            1. Create "i" in the for loop.
            2. Access the elements inside "list_object" for the all() loop.
            3. Access the elements inside "list_object" for the sum() function.
            4. Return "sum(list_object)".
    Space Complexity: O(1).
        Constant Storage:
            1. The value that is returned from "sum(list_object)"."""
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