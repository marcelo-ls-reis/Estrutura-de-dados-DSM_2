"""
   ESTRUTURA DE PILHA (STACK)
   É uma estrutura de dados linear em que tanto a operação de inserção (push) quanto 
   a operação de retirada (pop) acontece no final (topo). Como consequência, 
   o funcionamento da pilha pode ser definido como LIFO (last In, First Out): 
   o ultimo a entrar é o primeiro a sair  
"""

# Usando um piçha rudimentar para inverter um texto
# texto = 'PINDAMONHANGABA'
texto = 'SOCORRAM ME SUBI NO ONIBUS EM MARROCOS'

# Em python, é possivel fazer com que uma lista se comporte como uma pilha
pilha = []

# Colocando cada uma lista das letras do texto no final da pilha
for letra in texto:
    pilha.append(letra)
print(pilha)

inverso = ''

# Enquanto houver elemento na pilha
while len(pilha) > 0:
    retirado = pilha.pop()
    inverso += retirado
    
print('Original: ', texto)
print('inverido: ', inverso)     