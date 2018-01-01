import math
import copy
import subprocess

#Using BFS to find connected element
def BFS(graph, vertexFirst, vertexStatus):
    connectedElement = [vertexFirst]
    queue = [vertexFirst]
    vertexStatus[vertexFirst] = True
    #loop until lenght in queue is 0
    while len(queue) != 0:
        vertexCheck = queue[0]
        queue = queue[1:]
        for vertexConnect in graph[vertexCheck]:
            if not vertexStatus[vertexConnect]:
                queue.append(vertexConnect)
                connectedElement.append(vertexConnect)
                vertexStatus[vertexConnect] = True
    return connectedElement
#Find connected element in graph
def findConnectedElements(graph):
    #Initial value
    vertexStatus = {}
    connectedElements = []
    for vertexIndex in graph:
        vertexStatus[vertexIndex] = False
    for vertexIndex in graph:
        if not vertexStatus[vertexIndex]:
            connectedElements.append(BFS(graph, vertexIndex, vertexStatus))
    return len(connectedElements)
def drawGraph(graph, nameGraph):
    path = 'GraphAfterDelete/' + nameGraph + '.gv'
    file = open(path, 'w')
    file.write('graph{\n')
    for vertexA in graph:
        for vertexB in graph[vertexA]:
            if vertexA < vertexB:
                file.write(str(vertexA) + '--' + str(vertexB) + '\n')
        if len(graph[vertexA]) == 0:
                file.write(str(vertexA) + '\n')
    file.write('}')
    file.close()
def mergeSort(creditEdges):
    length = len(creditEdges)
    if length == 1:
        return creditEdges
    else:
        number = math.ceil(length/2)
        #devide array
        rightSort = mergeSort(creditEdges[:number])
        leftSort = mergeSort(creditEdges[number:])
        #Initial value for merge
        indexRight = 0
        indexLeft = 0
        isEnd = False
        lengthRight = len(rightSort)
        lengthLeft = len(leftSort)
        for i in range(length):
            #merge if left or right don't have element
            if isEnd:
                if lengthLeft == indexLeft:
                    creditEdges[i] = rightSort[indexRight]
                    indexRight += 1
                else:
                    creditEdges[i] = leftSort[indexLeft]
                    indexLeft += 1
                continue
            #merge if both left and right still contain element
            if rightSort[indexRight][1] > leftSort[indexLeft][1]:
                creditEdges[i] = rightSort[indexRight]
                indexRight += 1
                if indexRight == lengthRight:
                    isEnd = True
            else:
                creditEdges[i] = leftSort[indexLeft]
                indexLeft += 1
                if indexLeft == lengthLeft:
                    isEnd = True
    return creditEdges
#Remove some edge to check
def removeEdge(graph, creditEdges, numberEdgeDelete):
    #number connectedElement
    connectedElementNumbers = [findConnectedElements(graph)]
    #sort the betweenness on set
    creditEdgesAfterSorted = []
    for key in creditEdges:
        creditEdgesAfterSorted.append([key, creditEdges[key]])
    mergeSort(creditEdgesAfterSorted)
    #remove every edge and check connected graph
    for i in range(numberEdgeDelete):
        if i == 0:
            newGraph = copy.deepcopy(graph)
        #get value
        valueRemove = creditEdgesAfterSorted[0][1]
        #remove Edge
        while creditEdgesAfterSorted[0][1] == valueRemove:
            [key, valueRemove] = creditEdgesAfterSorted.pop(0)
            #delete value
            newGraph[key[0]].remove(key[1])
            newGraph[key[1]].remove(key[0])
            #check if delete all edges
            if len(creditEdgesAfterSorted) == 0:
                print('End with value : ' + str(i) + 'th')
                connectedElementNumbers.append(len(graph))
                # drawGraph(newGraph, 'GraphAfterDelete' + str(i))
                return connectedElementNumbers
        # drawGraph(newGraph, 'GraphAfterDelete' + str(i))
        #Run command graphviz to render out data
        # command = 'dot -Tpng GraphAfterDelete' + str(i) + '.gv -o GraphAfterDelete' + str(i) + '.png'
        # subprocess.run(args=command, shell = True, check=True)
        connectedElementNumbers.append(findConnectedElements(newGraph))
    return connectedElementNumbers