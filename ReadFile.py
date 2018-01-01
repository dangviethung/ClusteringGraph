def preprocessingData():
    numberVertex = 500
    maxValueVertex = 499
    graph =[]
    for i in range(numberVertex):
        graph += [[]]
    file = open('soc-LiveJournal1Adj.txt', 'r')
    for line in file:
        number = ''
        vertex = -1
        for char in line:
            number += char
            if char == '\n' or char == '\t' or char == ',':
                number = number.strip('\n\t,')
                if number == '':
                    continue
                number = int(number)
                if char == '\t':
                    if number > maxValueVertex:
                        break
                    vertex = number
                    graph[vertex].append(vertex)
                else:
                    if number > maxValueVertex:
                        number = ''
                        continue
                    graph[vertex].append(number)
                number = ''
    file.close()
    file = open('data.txt', 'w')
    for i in range(len(graph)):
        file.write(str(graph[i][0]) + '\t')
        for j in graph[i][1:-1]:
            file.write(str(j) + ',')
        file.write(str(graph[i][-1]) + '\n')
    file.close()
#read Data from file data
def getData():
    preprocessingData()
    graph = {}
    file = open('data.txt')
    for line in  file:
        numbers = []
        number = ''
        vertex = -1
        for char in line:
            number += char
            if char == ',' or char == '\t' or char == '\n':
                number = number[:-1]
                if char == '\t':
                   vertex = int(number)
                else:
                    number = int(number)
                    numbers.append(number)
                number = ''
        graph[vertex] = numbers
    file.close()
    return graph

#Save graph
def saveGraph(graph, nameGraph):
    file = open(nameGraph, 'w')
    for vertexIndex in graph:
        file.write(str(vertexIndex) + '\t')
        for vertexConnect in graph[vertexIndex][:-1]:
            file.write(str(vertexConnect) + ',')
        if len(graph[vertexIndex]) != 0:
            file.write(str(graph[vertexIndex][-1]) + '\n')
        else:
            file.write('\n')
    file.close()