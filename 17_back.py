from lib.deque import Deque

deque = Deque()

# inserção de pessoas de prioridade normal
deque.insert_back('Deusdete')
deque.insert_back('Glaudemir')
deque.insert_back('Invanilson')
deque.insert_back('Robledo')
deque.insert_back('Otaviano')

# Imprime o deque
print(deque)

# Inserção de uma pessoa prioritaria
deque.insert_front('Berenice')

# Imprime o deque
print(deque)

# Remoção no final
desistente = deque.remove_back()

print("Desistente: ", desistente)

# Imprime o deque
print(deque)

# Outra inserção prioritária

deque.insert_front('Laudenisa')

# Imprime o deque
print(deque)

# Remoção no inicio da lista
atendido = deque.remove_front()

print('Atendido: ',atendido)

# Imprime o deque
print(deque)

# Consultando o Próximo de ser atendido
proximo = deque.peek_front()

# Consultando o último da fila
ultimo = deque.peek_back()

print('Proximo:', proximo)
print('Último: ', ultimo)

# Imprime o deque
print(deque)
