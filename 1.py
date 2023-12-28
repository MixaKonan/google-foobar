from math import sqrt

def solution(i):
    numbers = get_primes_till(i) if i > 10 else get_primes_till(15)

    return numbers[i:i + 5]


def get_primes_till(i):
    numbers = '235711'
    index = 13
    while (len(numbers) < i + 5):
        if is_prime(index):
            numbers += str(index)
        index += 1
    
    return numbers


def is_prime(n):
    if (n <= 1):
        return False
 
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            return False
 
    return True


print(solution(0))
    