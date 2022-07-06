import math

# this script does a few things.
# 1. Checks if number is prime
# 2. Shows all Prime Factors
# 3. Determines largest Prime Factor

# Checks if Prime
print("Enter a number to check if it's a Prime Number: ")
a = int(input())
if a % 2:
    print(a , " Isn't Prime! ")
else:
    print(a , " Is Prime! ")

# Gets Prime Factors
def prime_factors(num):  
    while num % 2 == 0:
        print(2,)
        num =  num/2
    for i in range(3, int(math.sqrt(num)) +1,2):
        while num % i == 0:
            print(i,)
            num = num/i
    if num >2:
        print(num)

num = a
prime_factors(num)

# Gets largest Prime Factor
def largest_prime_factor(num):
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
           num //= i
           return num
print("Largest Prime factor: ", largest_prime_factor(num))  






