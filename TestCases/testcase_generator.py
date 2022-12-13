import random

for file_num in range(0, 30, 10):
    i = file_num
    i //= 10
    num_list = random.sample(range(10 ** (i * 2 + 1), 10 ** (i * 2 + 2)), 10)
    num_list.sort()
    for j in range(10):
        file_path = "./TestCases/in/input" + str(file_num + j + 1) + ".txt"
        input_file = open(file_path, "w")
        input_file.write(str(num_list[j]))
        input_file.close()