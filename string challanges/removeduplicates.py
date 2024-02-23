def removeDuplicate(input_string): 
    result = ''
    for char in input_string: 
        if char in result: 
            pass
        else: 
            result = result + char 
    print("With Order:", result) 
    
input_str = "geeksforgeeks"
removeDuplicate(input_str)
