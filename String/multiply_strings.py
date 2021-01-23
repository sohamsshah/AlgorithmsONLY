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
    a = b = 0
    result1 = result2 = 0
    
    for digit1, digit2 in zip(num1, num2):
        
        result1 *= 10
        result2 *= 10
        
        for d in '0123456789':
            result1 += digit1 > d
            result2 += digit2 > d
            print(result1, result2)
            
    return str(result1 * result2)