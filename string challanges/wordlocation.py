def findlocation(string,word):
    counter=0
    words=string.split(" ")
    for i in words:
        counter+=1
        if(i==word):
            break
    return counter
print(findlocation("animesh thomas was","thomas")) 