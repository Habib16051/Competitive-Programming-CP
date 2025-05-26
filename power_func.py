def power(base, exp):
    # Initially we take the final result as 1 by default
    result = 1    

    # this loop is used based on the exponent! If the exponent we take 3 , this loop will run 3 times and so on
    for _ in range(abs(exp)):
        # After each execution of this loop, it will multiply the result and base and will store it to the result variable
        result *= base
        #  if the exponent is negative then it will give 1/result (1/3) = 0.3333
    if exp < 0:
        return 1/result
        #  and if the exponent is positive number then it will return result. As example : 2**3 = 8 where, two is base, 3 is exponent and 8 is result.
    return result
    
    # Print the result
print(power(2,3))
print(power(3,3))
