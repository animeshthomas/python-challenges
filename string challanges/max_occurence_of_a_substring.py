def maxOccurenceofASubstring(s, sub_list):
    max_count = 0
    max_sub = ""
    for letters in sub_list:
        count=s.count(letters)
        if(count>=max_count):
        
            max_count=count
            max_sub=letters
    return max_sub

test_str = "gfghsisbjknlmkesbestgfgsdcngfgcsdjnisdjnlbestdjsklgfgcdsbestbnjdsgfgdbhisbhsbestdkgfgb"
test_list = ['gfg', 'is', 'best']

print("The maximum run of Substring:", maxOccurenceofASubstring(test_str, test_list))
