
def calculo_factorial(num):
    if num == 0:
        return 1
    else:
        return num*(calculo_factorial(num - 1))

num_global = 4
print(calculo_factorial(num_global))
