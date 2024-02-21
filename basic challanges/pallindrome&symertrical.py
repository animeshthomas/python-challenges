def ispallindrome(s):
    rev = s[::-1]
    if rev == s:
        print(f"{s} is a pallindrome")
    else:
        print(f"{s} is not a pallindrome")
        
def isSymmetrical(s):
    n = len(s)
    if n%2:
        mid = n//2 + 1
    else:
        mid = n//2
    val=''
    for i in range(mid):
        val+=s[i]
    secondval = ''
    for i in range(mid,n):
        secondval+=s[i]
    if val == secondval:
        print(f"{s} is symmetrical")
    else:
        print(f"{s} is not symmetrical")
        
s = "zozo"
ispallindrome(s)
isSymmetrical(s)
