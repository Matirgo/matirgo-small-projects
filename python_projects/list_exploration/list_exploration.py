"""A list is a data structure that holds multiple items of potentially different types.
It can store multiple values in a single variable rather than in many variables."""

# ========== Characteristics of a List ==========

# 1. Unfixed size: List size is not determined upon creation and may be changed thereafter, unlike arrays.
# 2. Different data types allowed: List elements may be of different types.
# 3. Indexing: Each list element is accessible by its index, which starts from zero.
# 4. Ordered: Elements have a specified order that will not change.
# 5. Duplicate values allowed: Lists may have duplicate elements.

# ========== Simple List Invocations ==========

# 1. Create a list: = []
list1 = [1, 2]

# 2. Access an element in a list (by index): list1[i]
print("Accessing element at index 0:", list1[0], "and at index 1:", list1[1])

# 3. Update array elements: list1[i] =
list1[0] = 0
list1[1] = 1
print("After list update:", list1)

# ========== Methods on Lists ==========

# 1. Add object "e" to the end of the list "list": append
list = []
e = "e_string_object"
list.append(e)
print("Append results in:", list)

# 2. Determine the length of a list "list": len()
print("First list length:", len(list))
list.append(e)
print("Second list length:", len(list))

# 3. Return number of times that "e" occurs in "list": count
print("\"e\" object count is:", list.count(e))

# 4. Insert the object "f" into "list" at index "i": insert
f = "f_string_object"
i = 1
list.insert(i, f)
print("After insert:", list)
print("\"e\" object count is:", list.count(e))

# 5. Add items of list "list1" to end of "list": extend
list.extend(list1)
print("After extend:", list)

# 6. Delete first occurrence of "e" from "list": remove
list.remove(e)
print("After remove:", list)

# 7. Return index of the first occurrence of "e" in "list": index
print("Index of \"e\" is:", list.index(e))

# 8.1. Remove and return item at index "i" in "list": pop
i = 2
print("Popping:", list.pop(i))
print("After pop:", list)

# NOTE! If no item is specified for pop, the last element will be removed by default.

# 8.2. Remove and return item at index "i" in "list": del
del list[i]
print("After del:", list)

# NOTE! Technically, del is not a method in Python.

# 9. Reverse the order of the list "list": reverse
list.reverse()
print("After reverse:", list)

# 10. Empty the list "list":
list.clear()
print("After clear:", list)

# ========== Slicing Lists ==========

# Resource: simplilearn, Everything You Need to Know About Python Slicing
# Link: https://www.simplilearn.com/tutorials/python-tutorial/python-slicing

# Slicing is used to access a subset of a list's elements.
# This is done by using a colon (:) in the list.
# The first number specifies the starting index, the second number the final index (not included), and the third the step.
# Using negative integers will allow slicing to go from back to front (starting from -1), and no numbers does not slice.

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Simple slicing:
print("Simple 0 - 5 slice:", x[0:5])

# 2. Stepwise slicing:
print("Stepwise (2) 0 - 5 slice:", x[0:5:2])

# 3. No slicing:
print("No slice:", x[:])
print("No start slice:", x[:5:2])
print("No end slice:", x[0::2])
print("No start or end slice:", x[::2])

# 4. Negative slicing:
print("Negative slicing (last element):", x[-1:])
print("Slicing the right part of the list (-5):", x[-5:])
print("Negative slicing (middle):", x[-8:-3])
print("Slicing the left part of the list (-5):", x[:-5])
print("Reversing element order via slicing:", x[::-1]) # Start at the end of the list amd move one step until index zero.
print("Reversing element order and alternating elements:", x[::-2])

# 5. Using the slice() function.
# NOTE! The slice() function expects one - three arguments. Pass None if nothing should go through.
print("Simple function slice:", x[slice(0, 5)])
print("Stepwise function slice:", x[slice(0, 5, 2)])
print("No slicing function slice:", x[slice(None)])
print("Middle slicing function slice:", x[slice(-8, -3)])
print("Reversing element order via function slicing:", x[slice(None, None, -1)])