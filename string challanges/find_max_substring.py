def find_max_substring(test_str, sub_str):
    max_sub = ''
    for n in range(len(test_str)//len(sub_str)+1):
        if sub_str * n in test_str:
            max_sub = sub_str * n
    return max_sub

test_str = 'geeksgeeks are geeks for all geeksgeeksgeeks'
sub_str = 'geeks'

print("The maximum run of Substring:", find_max_substring(test_str, sub_str))
