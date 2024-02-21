def findSubString(string,substring):
    s=string.split()
    print(s)
    if substring in string:
        return True
    else:
        return False
print(findSubString("Hello World","Hello"))