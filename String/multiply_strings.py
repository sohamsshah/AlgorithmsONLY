def multiplyStrings(num1,num2):
    # code here
    # return the product string
    #if len(num1) == len(num2): pass
    
        
        #equalizing the lenth by adding zeros
        
    if len(num1) > len(num2):
        
        zero = (len(num1) - len(num2)) * '0'
        num2 = zero + num2
    
    if len(num2) > len(num1):
        
        zero = (len(num2) - len(num1)) * '0'
        num1 = zero + num1 
    
    
    #string to int
    result1 = result2 = 0
    
    for digit1, digit2 in zip(num1, num2):
        
        result1 *= 10
        result2 *= 10
        
        for d in '0123456789':
            result1 += digit1 > d
            result2 += digit2 > d
            print(result1, result2)
            
    return str(result1 * result2)

# to handle negative cases

def multiplyString(num1,num2):
    # code here
    # return the product string
    #if len(num1) == len(num2): pass
    
        
    #equalizing the lenth by adding zeros
    
    num1 = list(num1)
    num2 = list(num2)
    ansPositive = 0
    if num1[0] == '-':
        ansPositive+=1
        num1.pop(0)
    if num2[0] == '-':
        ansPositive+=1
        num2.pop(0)
    
    
    if len(num1) >= len(num2):
        num1 = int("".join(num1))
        total = len(num2)
        for i in range(len(num2)):
            num2[i] = int(num2[i])*10**(total-1)
            total-=1
        ans = 0
        for i in num2:
            ans+=(i*num1)
        
            
    else:
        num2 = int("".join(num2))
        total = len(num1)
        for i in range(len(num1)):
            num1[i] = int(num1[i])*10**(total-1)
            total-=1
        ans = 0
        for i in num1:
            ans+=(i*num2)
    if ansPositive%2 != 0:
        ans*=-1
    return ans