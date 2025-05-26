import math

def is_pn(n):
    if n<2:
        return False
        
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        return True
        
        
start = int(input('Enter the Start number: '))
end = int(input('Enter the End number: '))


print(f"Here is the pn between {start} and {end}")

for num in range(start, end + 1):
    if is_pn(num):
        print(num)
            
