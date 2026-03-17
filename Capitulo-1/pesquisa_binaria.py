# Pesquisa Binária

# A pesquisa binária é um algoritmo. Sua entrada é uma lista ordenada de elementos. Se o elemento que você está buscando está na lista, a pesquisa binária retorna a sua localização. Caso contrário, a pesquisa binária retorna None.
# Contudo, diferentemente da Pesquisa Simples (contagem de um a um), a Pesquisa binária permite que se pesquise o elemento com a menor quantidade de chances possiveis. Sendo assim, para uma lista de N números, a pesquisa binária precisa de log(2)N (Log de N na base 2) para retornar o valor correto, enquanto a pesquisa simples precisa de N etapas para retornar o valor correto.

#Observações:
# - A pesquisa binária só funciona quando a lista está ordenada

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = [1, 3, 5, 7, 9]
print (pesquisa_binaria(minha_lista, 3))
print (pesquisa_binaria(minha_lista, -1))
        

