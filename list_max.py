# Author: Rajvi Rajput
# GitHub username: rrajput22
# Date: 11/08/2023
# Description: Recursive function named list_max that takes as its parameter a list of numbers
# and returns the maximum value in the list


def list_max(lst):
    """
    Recursive function to find the maximum value in a list.
    """
    # Base case to if the list has only one element, return that element
    if len(lst) == 1:
        return lst[0]
    else:
        # Recursive case to find the maximum of the last element and the remaining list
        return max(lst.pop(), list_max(lst))
