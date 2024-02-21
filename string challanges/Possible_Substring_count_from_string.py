
test_str = "geksefokesgergeeks"
print("The original string is: ",test_str)
arg_str = "geeks"
arg_str=set(arg_str)
print("The substring to be searched is: ",arg_str)
cnt=10000

for i in arg_str:
    m_cnt=test_str.count(i)
    if m_cnt<cnt:
	    cnt=m_cnt
# printing result
print("Possible substrings count: ",cnt)

