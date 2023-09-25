# TODO: Implement a function that returns a list of numbers from 1 to n
def generate_numbers(n):
 return list(range(1, n + 1))

# TODO: Implement a function that returns a dictionary where keys are numbers from 1 to n and values are their squares
def generate_squares(n):
    squares_dict = {}
    for i in range(1, n + 1):
        squares_dict[i] = i ** 2
    return squares_dict

# TODO: Implement a function that merges two lists in an alternating fashion
def merge_lists(list1, list2):
    merged_list = []
    min_len = min(len(list1), len(list2))
    
    for i in range(min_len):
        merged_list.append(list1[i])
        merged_list.append(list2[i])
 
    if len(list1) > min_len:
        merged_list.extend(list1[min_len:])
    elif len(list2) > min_len:
        merged_list.extend(list2[min_len:])
    
    return merged_list

# TODO: Implement a function that returns a list and replicates the dictionary keys based on their respective values
def multiply_keys(data):
    result = []
    for key, value in data.items():
        result.extend([key] * value)
    return result


# TODO: Implement a function that converts a list of strings to a dictionary with the string as the key and its length as the value
def list_to_dict(items):
    result = {}
    for string in items:
        result[string] = len(string)
    return result


# TODO: Implement a function to find the majority element in a list
def majority_element(nums):
    c = None
    count = 0

    for num in nums:
        if count == 0:
            c = num
            count = 1
        elif num == c:
            count += 1
        else:
            count -= 1

    count = 0
    for num in nums:
        if num == c:
            count += 1

    if count > len(nums) // 2:
        return c
    else:
        return None 

# TODO: Implement a function that filters a dictionary based on a threshold value. If the value of any key in the dictionary is greater than the threshold, that key-value pair should be retained in the output dictionary. Otherwise, it should be excluded.
def filter_dictionary(data, threshold):
    fi = {}
    for key, value in data.items():
        if value > threshold:
            fi[key] = value
    return fi