def numtoString(s):
    numdict={
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9,
        "ten":10,
    }
    print(numdict["one"])
    value=1
    for key, val in numdict.items():
        if val == value:
            print(key)

    words=s.split()
    numbers=[]
    for i in words:
        if i in numdict:
            numbers.append(numdict[i])
    return numbers

print(numtoString("one two three"))
