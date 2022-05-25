from numpy import count_nonzero


def sum_multiples(number):
    sum = 0
    count =1
    #function count takes in a number and sums up the multiples of 3 and 5
    for count in  range(1,number):
        if count % 3 == 0 and count % 5 ==0 :
            sum += count
        elif count % 3 == 0 :
            sum += count
        elif count % 5 == 0 :
            sum += count 
        
        
    print(sum)

sum_multiples(1000)
           