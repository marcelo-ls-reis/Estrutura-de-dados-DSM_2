"""  
    classes que implementam a estrutura de dados Pilha
"""
from logging import exception


class Stack:
    """ Método construtor """
    def __init__(self):
        self.__data = []  # Inicializa uma lista vazia
        
    """ Método para inserção 
        O nome do método de inserção em pilha é padronizado: push()
    """    
    def push(self, val):
        # Insere val no final (topo) da pilha
        self.__data.append(val)
    
    """
       Método para remoçao 
       o nome tambem é padronizado: pop() 
    """
    def pop(self):
        if self.is_empty: # Tentativa de retirar de uma pilha vazia
            # Gera um erro
            raise Exception('ERRO: impossível retirar de uma pilha vazia')
        # A pilha não está vazia, retirada pode ser feita
        return self.__data.pop()
        
    """
       Método que consulta o valor no topo da pilha, sem retirá-lo de lá
       Nome padronisado: peek()
    """    
    def peek(self):
        if self.is_empty:
            raise exception("ERRO: imposivel consultar o topo de uma pilha vazia")
    # Retorna o último elemento da lista
        return self.__data[-1] 
    """ 
       Método que permite imprimir a pilha
       esse é um metodo especial do python: __str__
    """    
    def __str__(self):
        return str(self.__data)
    
    """
       Propiedades somente-leitura que informa se a pilha está vazia (True) ou não (False)
    """    
    @property
    def is_empty(self):
        return len(self.__data) == 0