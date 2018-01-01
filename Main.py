import numpy as np
import ReadFile
import GirvanNewman as gn
import Betweenness as bt

graph = ReadFile.getData()
creditEdges = gn.girvanNewman(graph)
connectedElements = bt.removeEdge(graph, creditEdges, 550)
file = open('connected.csv', 'w')
for i in range(len(connectedElements)):
    print('Delete ' + str(i+1) + 'th value have: ' + str(connectedElements[i]) + ' connected elements')
    file.write(str(connectedElements[i]) + ',')
file.close()