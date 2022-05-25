
#function check_3 takes in 2 numbers and sums up the 
#the numbers if either one of them is equal to true and returns true
#if their sum contains 3

def check_3(value1,value2):
    sum = 0
    if value1 ==3 or value2 ==3:
        sum = value1 + value2
        
        if "3" in str(sum):
            return True
        else:
            return False

print(check_3(3,20))