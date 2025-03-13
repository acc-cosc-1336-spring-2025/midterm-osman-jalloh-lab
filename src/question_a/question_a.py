#write functions here, don't add input('') statements here!
def is_prime(n):
    if n <= 1:  # Numbers less than 1 are not prime
        return False
    for i in range(2, int(n**0.5) + 1):  # Check divisors up to the square root
        if n % i == 0:
            return False
    return True

