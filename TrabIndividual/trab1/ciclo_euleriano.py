from copy import deepcopy

def algoritmoHierholzer(grafo):
    listasAdj= deepcopy(grafo)
    ciclo = encontraCiclo(listasAdj, 0, [])
    return ciclo

def encontraCiclo(listasAdj, vertice, ciclo):
    ciclo = ciclo + [vertice]
    if len(ciclo) > 2 and ciclo[0] == ciclo[-1]: # Se completou um ciclo
        # Verificamos se há arestas não percorridas
        for verticeIndex in range(len(ciclo)-1, 0, -1): 
            vertice = ciclo[verticeIndex]
            if (len(listasAdj[vertice]) != 0):
                # Fazemos um ciclo composto apenas das arestas não perocorridas 
                # e a adicionamos ao ciclo que já temos
                subtour = encontraCiclo(listasAdj, vertice, [])
                ciclo = ciclo[0: verticeIndex] + subtour + ciclo[verticeIndex+1:]
        return ciclo
    else:    
        proxVertice = listasAdj[vertice][0]
        # Queimamos o vértice
        listasAdj[vertice].pop(0)
        listasAdj[proxVertice].remove(vertice)

    return encontraCiclo(listasAdj, proxVertice, ciclo)

def leGrafo():
    fileName = input()
    fileHandle = open(fileName, 'r')

    NumVertices, NumArestas = fileHandle.readline().split()
    NumVertices, NumArestas = int(NumVertices), int(NumArestas)

    # Inicializa grafo
    grafo = [[] for i in range(NumVertices)]

    # Le arestas
    for aresta_i in range(NumArestas):
        i, j = fileHandle.readline().split()
        i, j = int(i), int(j)
        grafo[i].append(j)
        grafo[j].append(i)

    fileHandle.close()
    
    return grafo

def main():
    grafo = leGrafo()
    # Checa ciclo euleriano
    permiteCicloEuleriano = True
    for arestas_vertice in grafo:
        arestas_vertice.sort()
        if(len(arestas_vertice) % 2 == 1):
            permiteCicloEuleriano = False
            print("Não")
            break

    if (permiteCicloEuleriano):
        print("Sim") 
        # Encontra e imprime ciclo
        ciclo = algoritmoHierholzer(grafo)
        print(" ".join([str(i) for i in ciclo]))

main()