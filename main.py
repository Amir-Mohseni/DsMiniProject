import matplotlib.pyplot as plt
import pandas as pd
import Algorithms.naive_algorithm as naive_algorithm
import Algorithms.array_optimization as array_optimization
import Algorithms.sqrt_optimization as sqrt_optimization
import Algorithms.sieve_optimization as sieve_optimization

naive_time = []
naive_num = []

array_time = []
array_num = []

sqrt_time = []
sqrt_num = []

sieve_time = []
sieve_num = []

for program in [naive_algorithm, sieve_optimization, array_optimization, sqrt_optimization]:
    for file_num in range(30):
        file_path = "./TestCases/in/input" + str(file_num + 1) + ".txt"
        with open(file_path, "r") as file:
            n = int(file.readline())

            if program == naive_algorithm:
                result, execution_time = program.return_results(n)
                if result == -1:
                    naive_time.append(10)
                    naive_num.append(n)
                    break
                else:
                    naive_time.append(float(execution_time))
                    naive_num.append(n)
            elif program == array_optimization:
                result, execution_time = program.return_results(n)
                if result == -1:
                    array_time.append(10)
                    array_num.append(n)
                    break
                else:
                    array_time.append(float(execution_time))
                    array_num.append(n)
            elif program == sqrt_optimization:
                result, execution_time = program.return_results(n)
                if result == -1:
                    sqrt_time.append(10)
                    sqrt_num.append(n)
                    break
                else:
                    sqrt_time.append(float(execution_time))
                    sqrt_num.append(n)
            elif program == sieve_optimization:
                result, execution_time = program.return_results(n)
                if result == -1:
                    sieve_time.append(10)
                    sieve_num.append(n)
                    break
                else:
                    sieve_time.append(float(execution_time))
                    sieve_num.append(n)

plt.plot(naive_num, naive_time, label="Naive Algorithm")
plt.plot(sqrt_num, sqrt_time, label="Sqrt Optimization")
plt.plot(array_num, array_time, label="Array Optimization")
plt.plot(sieve_num, sieve_time, label="Sieve Algorithm")

plt.title("Finding prime numbers up to N Algorithm - Time Complexity")
plt.xlabel('N')
plt.ylabel('Execution Time (s)')
plt.legend()
plt.savefig("output.png")
