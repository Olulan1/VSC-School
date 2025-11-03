# Week 4, Session 1: Task 4

# You are given an incomplete function count_occurences with docstring.
# Your task is to complete the function that takes two arguments:
#   (1) a list of string
#   (2) a string to search.

# This function returns the number of times a string appears in the list.
# This function is restricted to only accept positional arguments.
# Test the function with different list of strings and string to search


def count_occurences(l_strings, target, /):
    """
    Count how many times target appears in the list l_strings.

    Returns:
        int: number of occurences of target in l_strings.
    """
    count = 0
    target = target.upper()
    for i in range(0, len(l_strings)-1):
        if l_strings[i].upper() == target:
            count+=1
    
    return count

print("Number of occurences of target: ",count_occurences(["hi", "hello", "konbanwa", "Hi", "ciao", "boungiorno", "hiya", "yo"], "hi"))

# Write code to call the function and check if 
# correct output is produced