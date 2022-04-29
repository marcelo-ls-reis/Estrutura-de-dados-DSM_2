# ALGORITIMO DE ORDENAÇÃO QUICK SORT

# Escolhe um dos elementos da listapara ser o pivô (na nossa implementação, o ultimo elemento)
# e, na primeira passada, divide a lista, a partir da posição final da lista, em uma sublista
# á esquerda contendo apenas valores menores que o pivô em seguida, recursivamente, repete o
# processo em cada

from data.nomes_desord import nomes
from time import time
import tracemalloc

passadas = comps = trocas = 0

def quick_sort(lista, ini=0, fim=None):
    if fim is None:    # Se o fim for none, o colocamaos na posição do ultimo elemento da lista
        fim = len(lista) - 1
    if fim <= ini:    # Para que o algoritimo de oredenação trabalhe, é necessario que haja, pelo menos, dois elementos na faixa delimitadapor ini e fim
        return

    global passadas, comps, trocas

    passadas += 1

    # inicia as variáveis de controle
    pivot = fim
    div = ini - 1

    for i in range(ini, fim):    # Percorre a lista da posição ini até a posição fim - 1
        comps += 1
        if lista[i] < lista[pivot]:    # Compara os elementos da posição i e pivot
            div += 1    # incrementa a posição do divisor
            if div != i:    # Se i e div não forem mesma posição, os respectivos trocam de posição entre si
                lista[i], lista[div] = lista[div], lista[i]
                trocas += 1
    div += 1    # Depois que o loop acaba, o divisor sofre um último inclemento
    # Os elemntos da posição de div e da posição de pivot trocam de lugar entre si se:
    # 1) as posições div e pivot forem diferentes entre si
    # 2) lista[pivot] for menor que lista[div]
    comps += 1
    if div != pivot and lista[pivot] < lista[div]:
        lista[pivot], lista[div] = lista[div], lista[pivot]
        trocas += 1
    # chamada recursiva à função para ordenar a sublista à esquerda da posição da div
    quick_sort(lista, ini, div - 1)

    # chamada recursiva à função para ordenar a sublista à direita da posição da div
    quick_sort(lista, div + 1, fim)

    #########################################################################################

divs = juncoes = comps = 0

nums = [7, 4, 2, 9, 0, 6, 5, 3, 1, 8]
resultado = quick_sort(nums)
print(resultado)
print(f"Divisoes: {divs}, Comparações: {comps}, Junções: {juncoes}")

hora_ini = time()
tracemalloc.start()

resultado = quick_sort(nomes)

mem_atual, mem_pico = tracemalloc.get_traced_memory() # Captura as estatisticas de uso de memória
hora_fim = time()

print(nomes[:100]) # imprime só os 100 primeiros nomes

print(f"Tempo gasto para ordenar: {(hora_fim - hora_ini) * 1000:.2f}ms")
print(f"Pico de memoria: {mem_pico / 1024 / 1024:.2f}MB")
print(f"Divisoes: {divs}, Comparações: {comps}, Junções: {juncoes}")