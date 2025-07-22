# Question 3. Largest Item in List
# Question Pack: https://www.w3resource.com/python-exercises/list/

# ========== Instructions ==========
# Write a Python programme to find the largest item in a list.

# Basic function calculating the largest item in the lst.
def find_largest_item_basic(list_object):
    """A function that takes a list as input and finds the largest of its elemetns.
    The function assumes the list only contains numeric elements and is at least two elements long."""
    largest_item = list_object[0] # Assign largest_item to the first element in the list.
    for i in list_object: # Iterate through all the elements in the list.
        if largest_item < i: # If the current element is larger than the largest element, assign a new largest element.
            largest_item = i
    return largest_item # Return the largest element.

# Largest item function using the max() method.
def find_largest_item(list_object):
    """A function that takes a list as input and finds the largest of its elemetns using the max() method.
    The function checks if the elements are numeric, and if not, raises a type error.
    The function checks if there is at least one element in the list, and if not, raises a value error."""
    # Check element types.
    if not all(isinstance(i, (int, float)) for i in list_object):
        raise TypeError("All elements in the list must be integers of floats.")
    elif len(list_object) < 1:
        raise ValueError("List must contain at least one element.")
    return max(list_object)

# Combining error handling logic without the max method.
def find_largest_item_advanced(list_object):
    """A function that takes a list as input and finds the largest of its elemetns without using the max() method.
    The function checks if the elements are numeric, and if not, raises a type error.
    The function checks if there is at least one element in the list, and if not, raises a value error."""
    # Check element types.
    if not all(isinstance(i, (int, float)) for i in list_object):
        raise TypeError("All elements in the list must be integers of floats.")
    elif len(list_object) < 1:
        raise ValueError("List must contain at least one element.")
    elif len(list_object) == 1: # If there is only one element in the list, then that is the largest element.
        return list_object[0]
    largest_item = list_object[0]
    for i in list_object[1:]: # Since index zero has already been applied, there is no need to compare it to itself.
        if largest_item < i:
            largest_item = i
    return largest_item

# ========== Test Cases ==========

# Test Case 1
list1 = [1, 2, 3]
if find_largest_item_basic(list1) == 3:
    print("Test Case 1 passed.")
else:
    print("Test Case 1 failed.")

# Test Case 2
list2 = [-1, -2, -3]
if find_largest_item_basic(list2) == -1:
    print("Test Case 2 passed.")
else:
    print("Test Case 2 failed.")

# Test Case 3
list3 = []
try:
    find_largest_item(list3)
    print("Test Case 3 failed.")
except ValueError:
    print("Test Case 3 passed.")
except Exception as e:
    print(f"Test Case 3 failed. Unexpected exception: {e}.")

# Test Case 4
list4 = [42]
if find_largest_item(list4) == 42:
    print("Test Case 4 passed.")
else:
    print("Test Case 4 failed.")

# Test Case 5
list5 = [1.5, 2.5, 3.5]
if find_largest_item_basic(list5) == 3.5:
    print("Test Case 5 passed.")
else:
    print("Test Case 5 failed.")

# Test Case 6
list6 = [-1, 42, "C"]
try:
    find_largest_item(list6)
    print("Test Case 6 failed.")
except TypeError:
    print("Test Case 6 passed.")
except Exception as e:
    print(f"Test Case 6 failed. Unexpected exception: {e}.")