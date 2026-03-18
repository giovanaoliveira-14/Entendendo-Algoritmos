# Pesquisa Binária

# A pesquisa binária é um algoritmo. Sua entrada é uma lista ordenada de elementos. Se o elemento que você está buscando está na lista, a pesquisa binária retorna a sua localização. Caso contrário, a pesquisa binária retorna None.
# Contudo, diferentemente da Pesquisa Simples (contagem de um a um), a Pesquisa binária permite que se pesquise o elemento com a menor quantidade de chances possiveis. Sendo assim, para uma lista de N números, a pesquisa binária precisa de log(2)N (Log de N na base 2) para retornar o valor correto, enquanto a pesquisa simples precisa de N etapas para retornar o valor correto.

#Observações:
# - A pesquisa binária só funciona quando a lista está ordenada

def pesquisa_binaria(lista, item):
    # Baixo e alto acompanham a parte da lista que você está procurando
    baixo = 0
    alto = len(lista) - 1
    
    while baixo <= alto: # Enquanto ainda não conseguiu chegar a um único elemento...
        meio = (baixo + alto) // 2 # verifica o elemento central
        chute = lista[meio]
        if chute == item: # Acha o item
            return meio
        if chute > item: # O chute foi muito alto
            alto = meio - 1
        else: # O chute foi muito baixo
            baixo = meio + 1
    return None # O item não existe

minha_lista = [1, 3, 5, 7, 9] # Exemplo de lista

print (pesquisa_binaria(minha_lista, 3)) # => 1
print (pesquisa_binaria(minha_lista, -1)) # => None
        

# Tempo de execução

# Pesquisa simples é executado em tempo linear
# Pesquisa binária é executada com tempo logarítmico

#----------------------------------------------
#    Pesquisa Simples | Pesquisa Binária
#        100 items    |    100 items
#            =        |       = 
#        100 etapas   |    7 etapas
#----------------------------------------------
# 4 bilhões de items  |    4 Bilhões de items
#    =                |        =
# 4 bilhões de etapas |     32 etapas
#----------------------------------------------
# 0(n)                |       0(Log n)
#----------------------------------------------

# 100 elementos, cada elemento 1 ms, logo, 100ms na pesquisa simples
# 100 elemento, cada elemento 1 ms, 7ms na pesquisa binária
# 1 bilhão de elementos, cada elemento 1ms, logo, 11,57 dias na pesquisa simples
# 1 bilhão de elementos, cada elemento 1ms, logo, 30ms na pesquisa binária