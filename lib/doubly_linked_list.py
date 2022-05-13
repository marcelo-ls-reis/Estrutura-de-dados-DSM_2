"""
    Classe que representa uma unidade de informação 
    na lista duplamente encadeada
"""

from readline import insert_text


class Node:
    """ Método construtor """
    def __init__(self, data):
        self.prev = None  # Ponteiro para o nodo anterior
        self.date = data  # Dado do usuário
        self.next = None  # Ponteiro para o nodo seguinte
        
##########################################################

"""
    ESTRUTURA DE DADOS LISTA DUPLAMENTE ENCADEADA
    Trata-se de uma lista linear, em que seus elementos (nodos)
    não estão adjcentes fisicamente uns aos outros, mas ligados
    logicamente por meios de ponteiros que indicam o anterior e
    o próximo nodo da sequência, Não tem restrição de acesso -
    inserções, exclusões e consulta podem ser realizadas em 
    qualquer posição da lista. 
"""        
class DoublyLinkedList:
    """ Método construtor """
    def __init__(self):
        self.__head = None  # Aponta para o primeiro nodo da lista
        self.__tail = None  # Aponta para o ultimo nodo da lista
        self.__count = 0  # Mantem o número de nodo da lista
    """
        Propiedade que retorna a quantidade de itens da lista
    """    
    @property
    def count(self):
        return self.__count
    
    """
        Propiedade que retorna se lista está ou não vazia
    """ 
    @property
    def is_empty(self):
        return self.__count == 0
    
    """
        Método que insere um valor na posição especificada
    """
    def insert(self, pos, val):
        
        # Criamos um nodo que contem a informação do usuário e
        # tambem os ponteiros prev e next apontondo nodo
        inserted = Node(val)
        
        # 1º caso: alista esta vazia e este é o primeiro nodo a ser inserido
        if self.is_empty:
            self.__head = inserted
            self.__tail = inserted
        
        # 2º caso: inserção na posição inicial (posição 0)
        elif pos == 0:
            inserted.next = self.__head
            self.__head.prev = inserted
            self.__head = inserted
            
        # 3º caso: inserção na posição final(qualquer posição >= count)
        elif pos >= self.count:
            inserted.prev = self.__tail
            self.__tail.next = inserted
            self.__tail = inserted 
            
        # 4º caso: inserção em posições intermediaria
        else:
            # encontrar o node atualmente na posição de inserção         
            node_pos = self.__find_node(pos)
            # encontra o nodo da posição anterior á inserção
            before = node_pos.prev
            
            before.next = inserted
            inserted.prev = before
            inserted.next = node_pos
            node_pos.prev = inserted
            
            
        # Incremento a contagem de itens
        self.__count += 1 
        
"""
    Função privada que encontra o nodo da posição especificada
"""             
def __find_node(self, pos):
    # 1º caso: posição 0, retorna __head
    if pos == 0:
        return self.__head
    # 2º caso: posição == count -1, retorna __tail
    elif pos == self.count - 1:
        return self.__tail
    # 3º caso: nodo intermediário
    else:
        # se o nodo estiver na primeira metade da lista,
        # faz o percurso a partir de __head, seguindo next
        if pos < self.count // 2:
            node = self.__head
            for i in range(1, pos):
                node = node.next 
        # Senão, faz o percurso a parir de __tail, seguindo prev
        else:
            node = self.__tail
            for i in range(self.count - 2, pos - 1, -1):
                node = node.prev        
        return node        
        