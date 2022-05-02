# """
#    ESTRUTURA DE FILA (QUEUE)
#    É uma estrutura de dados linear em que tanto a operação de inserção (enqueue) 
#    acontece no final (ou calda) da estrutura e da opração de remoção (dequeue) 
#    ocorre no inicio (ou cabeça) 
# """
  
from logging import exception

class Queue:        
    #metodo contrutor
    def __init__(self):
        #inicializa uma lista vazia
        self.__data =[]
# Metodo para inserção na fila

    def enqueue (self, val):
        self.__data.append(val)

    #metodo para a remoção na fila 
    def dequeue(self):
        if self.is_empty:
            raise Exception("Erro: Impossivel remover de uma fila vazia")    
            #remove o primeiro elemento da fila 
        return self.__data.pop(0)

    def peek(self):
        if self.is_empty:
            raise Exception("Erro> impossivel consultar a cabeça de uma fila vazia")
        return self.__data[0]
    

    #metodo que permite imprimir a fila Esse é um metodo especial do python
    def _str_(self):
        return str(self.__data)



    # propriedade somente para leitura que informa se a pilha esta vazia (true)
    #ou não (false)
        
    @property
    def is_empty(self):
        return len(self.__data) == 0        