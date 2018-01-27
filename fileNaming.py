'''
Name:           Francisco McGee
Assignment:     FileNaming from CodeFights
Git:            

QUESTION TEXT:
You are given an array of desired filenames in the order of their creation. 
Since two files cannot have equal names, the one which comes later will have 
an addition to its name in a form of (k), where k is the smallest positive 
integer such that the obtained name is not used yet.

Return an array of names that will be given to the files

TEST CASES:
test1 = ["doc", "doc", "image", "doc(1)", "doc"]
test1_key = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"]

test2 = ["a(1)", "a(6)", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
test2_key = ["a(1)", "a(6)", "a", "a(2)", "a(3)", "a(4)", "a(5)", "a(7)", 
    "a(8)", "a(9)", "a(10)", "a(11)"]

SOLUTION OVERVIEW:
- My main function is fileNaming, and the helper function is extend_name
(1) The general idea is that fileNaming iterates over every name in name,
    adding each file name to a new list, new_names
(2) If a name is already in new_names (this is a list search), then you have 
    to "extend" the name appropriately
(3) After extension (if necessary), just append the name to new_names and 
    return new_names

CHALLENGES/LIMITATIONS:
- This algorithm has a poor runtime due to selection of data structures
- There is a lot of searching through the lists, which is O(n) each time
- I did it this way because it was easier to code
- With more time for the assignment, I would like to implement a dictionary
    to use with respect to searching; that is because dictionary would give
    me O(1) for each search
    - I'm doing an O(n) search 2 times, within the for loop
        (1) once in "if name in new_names"
        (2) again in extend_name, at "while new_name in new_names"
'''

def fileNaming(names):
    new_names = []
# (1)
    for name in names:
# (2)
        if name in new_names: 
            name = extend_name(name, new_names)
# (3)
        new_names.append(name)
    return new_names
    
def extend_name(name, new_names):
    count = 1
    new_name = name + "(" + str(count) + ")"
    while new_name in new_names:
        count += 1
        new_name = name + "(" + str(count) + ")"     
    return new_name
    
test1 = ["doc", "doc", "image", "doc(1)", "doc"]
test1_key = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"]

test2 = ["a(1)", "a(6)", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
test2_key = ["a(1)", "a(6)", "a", "a(2)", "a(3)", "a(4)", "a(5)", "a(7)", "a(8)", "a(9)", "a(10)", "a(11)"]

print fileNaming(test1) == test1_key
print fileNaming(test2) == test2_key