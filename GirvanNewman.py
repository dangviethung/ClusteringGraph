import numpy as np
def initialNode(tree, vertex):
    tree[vertex] = {}
    tree[vertex]['parents'] = []
    tree[vertex]['children'] = []
def BFS(graph, vertex):
    tree = {}
    #Status in each vertex: checked or
    vertexLevel = {}
    for i in graph:
        vertexLevel[i] = -1

    queue = [vertex]
    level = 0
    vertexLevel[vertex] = 0
    initialNode(tree, vertex)
    while len(queue) != 0:
        #Get vertex to check near vertex
        vertexCheck = queue[0]
        queue = queue[1:]
        for i in graph[vertexCheck]:
            if vertexLevel[i] < 0:
                queue.append(i)
                initialNode(tree, i)
                tree[i]['parents'].append(vertexCheck)
                tree[vertexCheck]['children'].append(i)
                vertexLevel[i] = vertexLevel[vertexCheck] + 1
            elif (vertexLevel[i] - 1) == vertexLevel[vertexCheck]:
                tree[i]['parents'].append(vertexCheck)
                tree[vertexCheck]['children'].append(i)
    #Add level and label of node to tree
    for i in tree:
        #Level of node in tree
        tree[i]['level'] = vertexLevel[i]
        #Label of node in tree
        if i == vertex:
            tree[i]['label'] = 1
        else:
            sum = 0
            for k in tree[i]['parents']:
                sum += tree[k]['label']
            tree[i]['label'] = sum
    return tree
#Caculate credit for node and edge
def credit(tree):
    #Initial creditNode
    creditNode = {}
    for i in tree:
        creditNode[i] = 1
    #Initial creaditEdge
    creditEdge = {}
    # queue = [vertex]
    # while len(queue) != 0:
    #     vertexCheck = queue[0]
    #     queue.extend(tree[vertexCheck]['children'])
    #     queue = queue[1:]
    #     for i in tree[vertexCheck]['children']:
    #         creditEdge[vertexCheck, i] = 0
    #Credit every node and edge in tree
    for i in tree:
        if len(tree[i]['children']) == 0:
            queue = [i]
            while len(queue) != 0:
                #Get a vertex from queue to credit value
                vertexCheck = queue[0]
                queue = queue[1:]
                #Credit value from bottom to top
                for k in tree[vertexCheck]['parents']:
                    edge = (min(k, vertexCheck), max(k, vertexCheck))
                    if edge in creditEdge.keys():
                        creditNode[k] = creditNode[k] - creditEdge[edge]
                        creditEdge[edge] = (tree[k]['label'] * creditNode[vertexCheck]) / tree[vertexCheck]['label']
                        creditNode[k] = creditNode[k] + creditEdge[edge]
                    else:
                        creditEdge[edge] = (tree[k]['label'] * creditNode[vertexCheck]) / tree[vertexCheck]['label']
                        creditNode[k] = creditNode[k] + creditEdge[edge]
                queue.extend(tree[vertexCheck]['parents'])
    return creditEdge

def girvanNewman(graph):
    trees = {}
    creditEdges = {}
    creditEdgesInTrees = {}
    for vertex in graph:
        trees[vertex] = BFS(graph, vertex)
        creditEdgesInTrees[vertex] = credit(trees[vertex])
    for vertexA in graph:
        for vertexB in graph[vertexA]:
            if vertexA < vertexB:
                creditEdges[vertexA, vertexB] = 0
    for key in creditEdges:
        for treeIndex in creditEdgesInTrees:
            if key in creditEdgesInTrees[treeIndex]:
                creditEdges[key] += creditEdgesInTrees[treeIndex][key]
        creditEdges[key] /= 2
    return creditEdges