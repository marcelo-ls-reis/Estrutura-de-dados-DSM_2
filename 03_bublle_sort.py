
# ALGORITIMO DE ORDENAÇÃO BUBLLE SORT
#
# Percorre a lista a ser ordenada em sucessivas passadas,
# trocando o elemento adjacentes entre si quando o segundo for 
# menor que o primeiro. Efetua tantas passadas qunto necessarias
# até que, na ultima passada, nenhuma troca seja efetuada

from data.nomes_desord import nomes
passadas = comps = trocas = 0

def bublle_sort(lista):
    global passadas, comps, trocas
    passadas = comps = trocas = 0
    # Percurso da lista da primeira até a penultima posição
    while True:
        passadas += 1
        trocou = False #vControla se houve trocas
        # primeiro da lista da primeira ate a penúltima posição
        for pos in range(len(lista)-1):
            comps += 1 
            if lista[pos] > lista[pos + 1]:
                # Troca os elementos de posição
                lista[pos], lista[pos + 1] = lista[pos + 1] , lista[pos]
                trocou = True
                trocas += 1 
        # se não houver trocas, interrompe o loop de passadas
        if not trocou:
            break 

############################################################################               
    
nums = [7,4,2,9,0,6,5,3,1,8]   

bublle_sort(nums)

print(40 * "=")
print(nums)
print(40 * "=")
print(f"passadas: {passadas}, comparacoes: {comps}, trocas: {trocas}")
print(40 * "=")