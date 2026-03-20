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
# O(n)                |       O(Log n)
#----------------------------------------------

# 100 elementos, cada elemento 1 ms, logo, 100ms na pesquisa simples
# 100 elemento, cada elemento 1 ms, 7ms na pesquisa binária
# 1 bilhão de elementos, cada elemento 1ms, logo, 11,57 dias na pesquisa simples
# 1 bilhão de elementos, cada elemento 1ms, logo, 30ms na pesquisa binária

# Não basta saber quanto tempo  de execução leva para ser executado - é necessário saber se o tempo de execução aumenta conforme a quantidade de dados aumenta.

# Notação Big O

# A notação big O informa o quão rápido é um algoritmo. 
# O tempo de execução na notação Big O é O(n) -  A notação Big O permite que você compare o número de operações, informando assim o quão rapidamente um algoritmo cresce.
# Qual é o tempo de execução na notação Big O para pesquisa binária? -> O(Log de N na base 2)
# O -> "Big O" (n) -> número de operações

# A notação Big O leva em consideração a pior das hipóteses

# Exemplos comuns de tempo de execução Big O

# O(log n): também conhecido como tempo logarítmico. Exemplo: pesquisa binária
# O(n)> conhecido como tempo linear. Exemplo: pesquisa simples
# O(n * log n): Exemplo-> um algoritmo rápido de ordenação, como a ordenação quicksort 
# O(n²): Exemplo -> um algoritmo lento de ordenação, como a ordenaçã por seleção
# O(n!): Exemplo -> um algoritmo bastante lento, como o do caixeiro viajante 