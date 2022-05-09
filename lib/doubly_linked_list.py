"""
    Classe que representa uma unidade de informação 
    na lista duplamente encadeada
"""

class Node:
    """ Método construtor """
    def __init__(self):
        self.prev = None  # Ponteiro para o nodo anterior
        self.date = None  # Dado do usuário
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