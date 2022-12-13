import math
from datetime import datetime


def check_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def find_prime_algorithms(n):
    if type(n) != int:
        raise Exception
    start_time = datetime.now()
    prime_numbers = 0
    for i in range(1, n + 1):
        elapsed_time = (datetime.now() - start_time).seconds
        if elapsed_time > 10:
            return -1
        if check_prime(i):
            prime_numbers += 1
    return prime_numbers


def return_results(n):
    start_time = datetime.now()
    result = find_prime_algorithms(n)
    end_time = datetime.now()
    execution_time = float((end_time - start_time).microseconds / 1000000)
    if result == -1:
        execution_time = 20
    return result, execution_time
