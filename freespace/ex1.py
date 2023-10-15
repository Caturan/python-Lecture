"""
1-) A function with the name:
 remove_duplicated(list -> list)
"""
def remove_duplicates(input_list):
    # Sets are used store multiple items in a single variable. 
    return list(set(input_list))

# Example usage
input_list = [1, 2, 3, 2, 1, 4, 5]
unique_list = remove_duplicates(input_list)
print(unique_list)  


"""
2-) A function with the name: list_counts(list -> dict)
To count the occurance of each item, in a list and return as a dictionary.  
"""
def list_counts(input_list):
    """
    Counts the occurrences of each item in a list and returns a dictionary with counts.
    Returns:
    dict: A dictionary where keys are items from the input list, and values are their counts.
    """
    counts = {}
    for item in input_list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

# Example usage
input_list = [1, 2, 3, 2, 1, 4, 5]
element_counts = list_counts(input_list)
print(element_counts)


"""
3-) A function with the name: reverse_dict(dict -> dict)
To reverse a dictionary, switch values and keys with each other. 
"""
def reverse_dict(input_dict):
    """
    Reverse a dictionary by switching keys and values.
    Parameters:
    input_dict (dict): The input dictionary to be reversed.
    Returns:
    dict: A new dictionary with keys and values swapped.
    """
    reversed_dict = {v: k for k, v in input_dict.items()}
    return reversed_dict

# Example usage
original_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
reversed_dict = reverse_dict(original_dict)
print(reversed_dict)




