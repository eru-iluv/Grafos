def encontraCiclo(listasAdj, vertice, NumArestas, caminho):

    caminho = caminho + [vertice]
    if NumArestas == 0:
        return caminho; 

    if len(caminho) > 2 and caminho[0] == caminho[-1]:
        # Nesse caso, completamos um ciclo, mas não passamos por todas arestas
        for verticeDoCaminho in reversed(caminho[0:len(caminho)-1]):
            soma = sum(listasAdj[verticeDoCaminho])
            if sum(listasAdj[verticeDoCaminho]) != 0:
                proxVertice = verticeDoCaminho
                break
        
        indexProxVertice = caminho.index(proxVertice)
        caminho = caminho[0:indexProxVertice] + encontraCiclo(listasAdj, proxVertice, NumArestas, []) + caminho[indexProxVertice+1:]
    else:    
        proxVertice = listasAdj[vertice][0]
        # Queimamos o vértice
        listasAdj[vertice].pop(0)
        listasAdj[proxVertice].pop(listasAdj[proxVertice].index(vertice))
        NumArestas -= 1

    return encontraCiclo(listasAdj, proxVertice, NumArestas, caminho)

