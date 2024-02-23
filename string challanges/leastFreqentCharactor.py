def least_frequent_character(input_string):
    char_count = {}  # Dictionary to store character counts
    
    # Count occurrences of each character
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    print(char_count)
    
    # Find the least frequent character
    min_count = float('inf')
    least_frequent_char = ''
    for char, count in char_count.items():
        if count < min_count:
            min_count = count
            least_frequent_char = char
    
    return least_frequent_char

# Example usage
input_string = "hello world"
result = least_frequent_character(input_string)
print(f"The least frequent character in '{input_string}' is '{result}'")
