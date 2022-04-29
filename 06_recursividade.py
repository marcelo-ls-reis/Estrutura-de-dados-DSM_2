# O faorial de um número n inteiro > 1 pode ser defeinido recursivamente, como:
# n! = n * (n -1)!
# Já o fatorial de n = 1 é definido como:
# 1! = 1

# Imprementação Interativa de um fatorial
def fatorial_int(n):
    resultado = 1 # range começa em n e vai descendo ate 1
    for i in range(n, 1, -1):
        resultado *= i
    return resultado

# Implementação RECURSIVA de um fatorial
def fatorial_rec(n):
    if n == 1 or n == 0:
        return 1 # Condição de saída
    elif n > 1:
        return n * fatorial_rec(n - 1)    
    else:
        return None # Condição de saída        

############################################################
        
print(f"6! é igual a {fatorial_int(6)}")
print(f"6! é igual a {fatorial_rec(6)}")