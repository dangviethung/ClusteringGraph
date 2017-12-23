numberVertex = 10000
graph =[]
for i in range(numberVertex):
    graph += [[]]
file = open('F:\\4\\20171\\Big Data\\soc-LiveJournal1Adj.txt', 'r')
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
                if number > 9999:
                    break
                vertex = number
                graph[vertex].append(vertex)
            else:
                if number > 9999:
                    number = ''
                    continue
                graph[vertex].append(number)
            number = ''
file.close()
file = open('data10000.txt', 'w')
for i in range(len(graph)):
    file.write(str(graph[i][0]) + '\t')
    for j in graph[i][1:-1]:
        file.write(str(j) + ',')
    file.write(str(graph[i][-1]) + '\n')
file.close()

