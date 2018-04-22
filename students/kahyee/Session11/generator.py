

def intsum():
    """
    generator function that increments by the next integer starting at 0
    """
    i = 0
    sum_value = 0
    while True:
        yield sum_value
        i += 1
        sum_value += i
        
def doubler():
    """
    generator function that becomes twice the value of the previous iteration
    """
    dbl_value = 1
    while True:
        yield dbl_value
        dbl_value *= 2
        
def fib():
    """
    generator function of the fibonacci sequence starting with 1
    """
    prev_value = 0
    cur_value = 1
    intermediary = 0
    
    while True:
        yield cur_value
        intermediary = prev_value
        prev_value = cur_value
        cur_value += intermediary


def isPrime(n):
    """
    function to check if value n is prime, if not return False, otherwise True
    """
    for i in range(2,max(3,n//2)):
        if n%i == 0:
            return False
    return True

def prime():
    """
    generator function that returns prime numbers starting with 2
    """
    prime_value = 2
    while True:
        yield prime_value
        prime_value += 1
        while not isPrime(prime_value):
            prime_value += 1
        
    