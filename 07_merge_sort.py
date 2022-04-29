# ALGORITIMO DE ORDENAÇÃO MERGE SORT
#
# No processo de ordenação, esse algoritimo "desmonta" o vetor original
# contendo n elementos até obter n vetores de apenas um elemento cada um.
# Em seguida, usando a técnica de mesclagem (merge), "remonta" o vetor,
# dessa vez com os elementos já em ordem.

from data.nomes_desord import nomes
from time import time
import tracemalloc

divs = juncoes = comps = 0

def merge_sort(lista):
    
    global divs, juncoes, comps

    if len(lista) <= 1:  # Só continua se o comprimento da lista for maior que 1
        return lista
    meio = len(lista) // 2  # encontrar a posição do meio da lista
    sublista_esq = lista[:meio]  # Copia da primeira metade da lista
    sublista_dir = lista[meio:]  # Copia da segunda metade da lista

    divs += 1

    # Chamamos recursivamente a função para que ela continue repartindo cada uma das sublistas em metade
    sublista_esq = merge_sort(sublista_esq)
    sublista_dir = merge_sort(sublista_dir)

    # AQUI COMEÇA A JUNÇÃO DAS DUAS METADE DA LISTA, ORDENADAMENTE
    pos_esq = pos_dir = 0
    ordenada = []  # lista vazia

    # Comparar os elementos da sublista entre si e insere na lista ordenada o que for menor
    while pos_esq < len(sublista_esq) and pos_dir < len(sublista_dir):
        # O elemento que se encontra na posição da sublista esquerda é menor que o que se encontra na posição da sublista direita
        comps += 1
        if sublista_esq[pos_esq] < sublista_dir[pos_dir]:
            ordenada.append(sublista_esq[pos_esq])
            pos_esq += 1
        else:
            ordenada.append(sublista_dir[pos_dir])
            pos_dir += 1
    sobra = []  # Verificação da sobra
    if pos_esq < pos_dir:  # Sobra a esquerda
        sobra = sublista_esq[pos_esq:]
    else:  # Sobra a direita
        sobra = sublista_dir[pos_dir:]
    juncoes += 1    

    # O resultado final é a concatenação da lista ordenada + sobra
    return ordenada + sobra

#########################################################################

divs = juncoes = comps = 0

nums = [7, 4, 2, 9, 0, 6, 5, 3, 1, 8]
resultado = merge_sort(nums)
print(resultado)
print(f"Divisoes: {divs}, Comparações: {comps}, Junções: {juncoes}")

hora_ini = time()
tracemalloc.start()

resultado = merge_sort(nomes)

mem_atual, mem_pico = tracemalloc.get_traced_memory() # Captura as estatisticas de uso de memória
hora_fim = time()

print(resultado[:100]) # imprime só os 100 primeiros nomes

print(f"Tempo gasto para ordenar: {(hora_fim - hora_ini) * 1000:.2f}ms")
print(f"Pico de memoria: {mem_pico / 1024 / 1024:.2f}MB")
print(f"Divisoes: {divs}, Comparações: {comps}, Junções: {juncoes}")