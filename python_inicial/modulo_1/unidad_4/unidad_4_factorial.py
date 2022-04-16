n_aux = 0
factorial = 1

def calculo_factorial(n):
    global n_aux
    global factorial
    n_local = n_aux
    if n == n_local :
        return factorial
    else:
        n_aux += 1
        factorial = factorial * (n - n_local)
        return calculo_factorial(n)

print(calculo_factorial(10)) 
