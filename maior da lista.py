def maior_iterativo(lista):
    """
    Retotrna o maior elemento de uma lista usando um laço for.

    Parametros:
        Lista (list) : lista de números não vazia.

    retorna:
        int I float: o maior valor da lista.
    """
    maior = lista[0]
    for valor in lista:
        if valor > maior:
            maior = valor
    return maior
def maior_recursivo(lista):
    """
    Retorna o maior elemento de uma lista usando recursão.

    Parametros:
        lista (list): lista de números não vazia.

    retorna:
        int I float: o maior valor da lista.
    """
    if len(lista) == 1:
        return lista[0]
    maior_resto = maior_recursivo(lista[1:])
    return lista[0] if lista[0] > maior_resto else maior_resto

#testes#
print(maior_iterativo([3, 9, 2, 7]))
print(maior_recursivo([3, 9, 2, 7]))

