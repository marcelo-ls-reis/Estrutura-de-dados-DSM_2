# Classse é uma estrutura que representa conjuntamente dados e algoritimos.
# Uma classe é como uma forma de bolo com a qual se pode criar diferentes bolos (objetos),
# variando os ingredientes (dados) e o modo de fazer (algoritimo). Apesar dessa variação,
# os objetos criados a partir da classe sempre terão o formato determinado por esta.

from math import pi

class FormaGeomatrica:

    # uma classe pode ter, dentro de si, tanto dados qunto funções (estas representando os algoritimos).
    # Uma função especial, denominada __init__, é chamada sempre que um novo objeto é criado a partir 
    # da classe. Qundo estão dentro de uma classe, as funções passam a ser chamadas de metodos, e *sempre*
    # tem self como primeiro parâmetro, representando o própio objeto.

    def __init__(self, base, altura, tipo):
        
        # Validação dos dados recebidos
        
        # Recebemos os parâmetros no construtor e armazenamos dentro do objeto que está sendo criado
        self.base = base
        self.altura = altura
        self.tipo = tipo
        
    # Métodos setter (ajusta o valor de atributoos __privados)

    # def set_base(self, valor):
    #     if type(valor) not in [int, float] or valor <= 0:
    #         raise Exception("* A base deve ser numérica e maior que zero.")
    #     self.__base = valor 
               
    # def set_altura(self, valor):
    #     if type(valor) not in [int, float] or valor <= 0:
    #         raise Exception("* A altura deve ser numérica e maior que zero")
    #     self.__altura = valor
        
    # def set_tipo(self, valor):
    #     if valor not in ["R", "T", "E"]:
    #         raise Exception("* Otipo deve ser 'R', 'T' ou 'E'")
    #     self.__tipo = valor
        
    # # Método getter (retornam o valor de atributos __privados)
    
    # def get_base(self):
    #     return self.__base
    
    # def get_altura(self):
    #     return self.__altura
    
    # def get_tipo(self):
    #     return self.__tipo    
        
    @property        # Anotation
    def base(self):          # getter disfarçado
        return self.__base   
    
    @base.setter
    def base(self, valor):
        if type(valor) not in [int, float] or valor <= 0:
            raise Exception("* A base deve ser numérica e maior que zero.") 
        self.__base = valor 
        
    @property        # Anotation
    def altura(self):          # getter disfarçado
        return self.__altura
    
    @altura.setter
    def altura(self, valor):  
        if type(valor) not in [int, float] or valor <= 0:
            raise Exception("* A altura deve ser numérica e maior que zero")
        self.__altura = valor      
        
    @property        # Anotation
    def tipo(self):          # getter disfarçado
        return self.__tipo    
    
    @tipo.setter
    def tipo(self, valor):
        if valor not in ["R", "T", "E"]:
           raise Exception("* Otipo deve ser 'R', 'T' ou 'E'")
        self.__tipo = valor
        
######################################################################################   

    # Método para cáuculo da área da forma geometrica
    @property
    def area(self):
        from math import pi
        if(self.tipo == 'R'):    #Retangulo
            return self.base * self.altura
        elif(self.tipo == 'T'):    #Triangulo
            return self.base * self.altura / 2
        else:                      #Elipse
            return(self.base / 2) * (self.altura / 2) * pi    
            
######################################################################################

# Criando objetos a partir da classe
forma1 = FormaGeomatrica(12, 7, "R") # Isso chama __init__()
forma2 = FormaGeomatrica(7.5, 8.2, "T")


print(40 * "-")
print(f"forma1: base {forma1.base}, altura {forma1.altura}, tipo {forma1.tipo}, área: {forma1.area}")
print(40 * "-")
print(f"forma2: base {forma2.base}, altura {forma2.altura}, tipo {forma2.tipo}, área: {forma2.area:.3f}")
print(40 * "-")
       
