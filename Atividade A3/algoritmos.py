from collections import deque


def edmondsKarp(grafo, verticeInicial=1, verticeFinal=-1):
    qtdVertices = grafo.qtdVertices()

    if verticeFinal == -1:
        verticeFinal = qtdVertices

    fluxo = 0
    F = [[0 for y in range(qtdVertices + 1)] for x in range(qtdVertices + 1)]

    while True:
        caminhoAumentante = [-1 for x in range(qtdVertices + 1)]
        caminhoAumentante[verticeInicial] = -2

        capacidadeResidual = [0 for x in range(qtdVertices + 1)]
        capacidadeResidual[verticeInicial] = 999999999

        filaIterativa = deque([verticeInicial])

        fluxoCaminho, caminhoAumentante = BFSpEdmondsKarp(grafo,
                                                          verticeInicial,
                                                          verticeFinal, F,
                                                          caminhoAumentante,
                                                          capacidadeResidual,
                                                          filaIterativa)
        if fluxoCaminho == 0:
            break

        fluxo = fluxo + fluxoCaminho
        verticeAtual = verticeFinal

        while verticeAtual != verticeInicial:
            vizinho = caminhoAumentante[verticeAtual]
            F[vizinho][verticeAtual] = F[vizinho][verticeAtual] + fluxoCaminho
            F[verticeAtual][vizinho] = F[verticeAtual][vizinho] - fluxoCaminho
            verticeAtual = vizinho
    print("Fluxo máximo de ", verticeInicial, " a ", verticeFinal, ": ",
          fluxo, sep='')
    return fluxo


def BFSpEdmondsKarp(grafo, verticeInicial, verticeFinal, F,
                    caminhoAumentante, capacidadeResidual, filaIterativa):
    while len(filaIterativa) > 0:
        verticeAtual = filaIterativa.popleft()
        for vizinho in grafo.vizinhos(verticeAtual):
            residual = grafo.peso(verticeAtual, vizinho) - \
                            F[verticeAtual][vizinho]

            if (residual > 0) and (caminhoAumentante[vizinho] == -1):
                caminhoAumentante[vizinho] = verticeAtual
                capacidadeResidual[vizinho] = min(
                                             capacidadeResidual[verticeAtual],
                                             residual)
                if vizinho is not verticeFinal:
                    filaIterativa.append(vizinho)
                else:
                    return capacidadeResidual[verticeFinal], caminhoAumentante
    return 0, caminhoAumentante


def printEdmondsKarp(listaNiveis):
    for key, value in listaNiveis.items():
        print(str(key) + ":", str(value)[1:-1])


def hopcroftKarp(grafo):    # grafo bipartido, não-dirigido e não-ponderado
    pass


def coloracao(grafo):       # grafo não-dirigido e não-ponderado
    pass