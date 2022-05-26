from re import X


def triangle(number):
   
    if number >1 :

        for x in range(1,number+1):
             print(x*"#")
    else :
        for x in range(number ,0):
             print("#" *(x*-1) )

triangle(-4)