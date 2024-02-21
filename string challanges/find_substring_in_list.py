def checkSubstr(list1, list2):
    res = []
    for i in list1:
        temp = False
        for j in list2:
            if i in j:
                temp = True
                break
        res.append(temp)
    return res

print(checkSubstr(["hello", "world", "earth"], ["hello world", "world"]))  # [True, True, False]
