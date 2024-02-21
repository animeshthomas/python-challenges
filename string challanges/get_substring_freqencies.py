def get_substring_frequencies(test_str):
    substrings = []
    for start_idx in range(len(test_str)):
        for end_idx in range(start_idx + 1, len(test_str) + 1):
            substrings.append(test_str[start_idx: end_idx])

    frequencies = {}
    for substring in substrings:
        frequencies[substring] = test_str.count(substring)
    
    return frequencies

# Test the function
test_str = "abababa"
frequencies = get_substring_frequencies(test_str)
print("Extracted frequency dictionary:", frequencies)
