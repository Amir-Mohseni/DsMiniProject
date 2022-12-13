from datetime import datetime


def find_prime_algorithms(n):
    if type(n) != int:
        raise Exception
    found_prime_divs = [False] * (n + 1)
    prime_numbers = 0
    start_time = datetime.now()
    for i in range(2, n + 1):
        elapsed_time = (datetime.now() - start_time).seconds
        if elapsed_time > 10:
            return -1
        if not found_prime_divs[i]:
            prime_numbers += 1
        j = i
        while j <= n:
            found_prime_divs[j] = True
            j += i
    return prime_numbers


def return_results(n):
    start_time = datetime.now()
    result = find_prime_algorithms(n)
    end_time = datetime.now()
    execution_time = float((end_time - start_time).microseconds / 1000000)
    if result == -1:
        execution_time = 20
    return result, execution_time
