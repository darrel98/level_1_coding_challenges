list1 = ["jack","manymenn","kingsley","manymen"]
def longest(string1):
    long = max(string1)#set long = longest string
    long2 =[]
    for x in string1:
        
        if len(x) == len(long) :#check if there are other strings equal to longest
            long2.append(x)#append the longest strings
        
        
    for y in long2:
        print(y)
longest(list1)
