# Um dicionário é uma estrutura de dados fornecida pela linguagem python
# capaz de armazenar múltiplos valores em uma unica variável, por meio
# de pares de chave valor

pessoa = {
    # "nome" é a chave
    # "Gervásio Gomes Garcia" é o valor
    "nome": "Gervásio Gomes Garcia",
    "sexo": "M",
    "idade": 69,
    "peso": 76,
    "altura": 1.77
}

# Acessando os valores armazenados no dicionário
print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa['idade']}")

# Calculando o índice de massa corpórea (IMC)
imc = pessoa["peso"] / pessoa["altura"] ** 2
print(f"IMC: {imc:.2f}")

#################################################

forma1 = {
    "base": 7.5,
    "altura": 12,
    "tipo": "R"    # Retangulo
}

forma2 = {
    "base": 6,
    "altura": 2.5,
    "tipo": "T"    # Triangulo
}

forma3 = {
    "base": 5,
    "altura": 3,
    "tipo": "E"    # Elipse
}

forma4 = {
    "base": 10,
    "altura": 5,
    "tipo": "R"    # Retangulo
}

# Forma geométrica compretamente anômola
forma5 = {
    "legume": "batata",
    "fruta": "jabuticaba",
    "tipo": "T"    # Triangulo
}

# Inserir as formas em uma lista para percorrer com for
lista_formas = [forma1, forma2, forma3, forma4, forma5]

from math import pi

def calcular_area(forma):
    if forma["tipo"] == "R": # Retangulo
        return forma["base"] * forma["altura"]
    elif forma["tipo"] == "T": # Triangulo
        return forma["base"] * (forma["altura"] / 2) * pi   
    elif forma["tipo"] == "E": # Elipse
        return (forma["base"] / 2) * (forma["altura"] / 2) * pi
    else: # forma desconhecida
        # gera erro
        raise Exception("ERRO: Tipo de formanão conhecida.")

# calculando a área das formas da lista               

for i in range(0, len(lista_formas)):
    print("-" * 30)
    print(f"Calculando área da forma{i + 1}:")
    print(f"Tipo: {lista_formas[i]['tipo']}; base: {lista_formas[i]['base']}; altura: {lista_formas[i]['altura']}; Área: {calcular_area(lista_formas[i])}")