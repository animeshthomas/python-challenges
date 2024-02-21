def find_max_substring(test_str, sub_str):
    max_count = 0
    max_sub = ""
    words = test_str.split()
    print(words)

    for word in words:
        count = word.count(sub_str)
        if count >= max_count:
            max_count = count
            max_sub = sub_str * max_count

    return max_sub

test_str = 'geeksgeeks are geeks for all geeksgeeksgeeks'
sub_str = 'geeks'

print("The maximum run of Substring:", find_max_substring(test_str, sub_str))
