"""
    ESTRUTURA DE DAOS DEQUE
    Deque (Double-Ended QUEue) é uma esrtrutura derivada 
    da fila que permite inserções e remoções em qualquer
    uma de suas extremidades. Com isso, odeque pode 
    se comortar como uma fila  
"""


class Deque:
    """ Construtor """

    def __init__(self):
        self.__data = []  # lista vazia

    """
        Método de inserção no inicio do deque
    """

    def insert_front(self, val):
        self.__data.insert(0, val)
        
    """
        Método de inserção no final do deque
    """    
    
    def insert_back(self, val):
        self.__data.append(val)
        
    """
        Método de remoção no final do deque
    """   
        
    def remove_front(self):
        if self.is_empty:
            raise Exception('ERRO: impossivel remover de um deque vazio') 
        return self.__data.pop(0) 
    
    def remove_back(self):
        if self.is_empty:
            raise Exception('ERRO: impossivel remover de um deque vazio') 
        return self.__data.pop()   
    
    """
        Método de consulta no inicio do deque
    """
        
    def peek_front(self):
        if self.is_empty:
            raise Exception('ERRO: impossivel consultar um deque vazio')
        return self.__data[0]   
    
    """
        Método de consulta no final do deque
    """
        
    def peek_back(self):
        if self.is_empty:
            raise Exception('ERRO: impossivel consultar um deque vazio')
        return self.__data[-1]     
        
    """
        Método que permite imprimir a fila
        Esse é um método especial do Python: __str__
    """    

    def __str__(self):
        return str(self.__data)

    """
        Propriedade somente-leitura que informa se a fila está 
        vazia (True) ou não (False)
    """
    @property
    def is_empty(self):
        return len(self.__data) == 0
