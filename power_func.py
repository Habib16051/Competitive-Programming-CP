def power(base, exp):
    result = 1
    
    for _ in range(abs(exp)):
        result *= base
        
    if exp < 0:
        return 1/result
        
    return result
    
    
print(power(2,3))
print(power(3,3))
