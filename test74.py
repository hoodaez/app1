def search_number( number , target):
    """
    This function searches for a number in a given array.
    """
    for i in range (len(number)):
        if number[i] == target:
            return f"The number is found at index {i}"
    
    return "The number is not found"

# Example usage
my_list = [10, 20, 30, 40, 50]
target = 50

result = search_number(my_list, target)
print(result)    