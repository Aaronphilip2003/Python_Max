def find_max(lst):
    if not lst:
        return None

    max_element = lst[0]
    for item in lst:
        if item > max_element:
            max_element = item

    return max_element

# Example usage:
if __name__ == "__main__":
    my_list = [3, 8, 1, 5, 10, 4]
    max_value = find_max(my_list)
    print("The maximum value in the list is:", max_value)
