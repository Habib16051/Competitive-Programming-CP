def pow_function(base, exponent):
    result = 1
    for i in range(abs(exponent)):
        result *= base

    if result >= 0:
        return result
    else:
        return 1/result

print(pow_function(2,3))