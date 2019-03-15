# A class for building graphs of interconnected nodes
# Nodes of graph-type maps have neighbors only, with no heirarchy
# Andrew Vikartofsky, March 2019


class Node:
    def __init__(self, myValue, myNeighbors=[]):
        for n in myNeighbors:
            if type(n) is not Node:
                print('Node init error - declared neighbor is not a Node!')
                return
        self.neighbors = myNeighbors
        self.value = myValue
        for n in myNeighbors:
            n.addNeighbor(self)

    def addNeighbor(self, newNeighbor):
        if type(newNeighbor) is not Node:
            print('Node modification error - declared new neighbor is not a Node!')
            return
        if newNeighbor not in self.neighbors:
            self.neighbors.append(newNeighbor)

    def removeNeighbor(self, oldNeighbor):
        if oldNeighbor not in self.neighbors:
            print('Node modification error - requested neighbor does not exist!')
            return
        self.neighbors.remove(oldNeighbor)

    def getNeighbors(self):
        for n in self.neighbors:
            print(n.value)

    def __populate(self, myUnvisited):
        if self not in myUnvisited:
            myUnvisited.append(self)
            for n in self.neighbors:
                myUnvisited = n.__populate(myUnvisited)
        return myUnvisited

    def distance(self, otherNode):
        if otherNode.value == self.value:
            print("Well, that's easy.  The distance is zero!")
        else:  # calculate distance via Dijkstra's algorithm
            unvisited = []  # list of connected nodes in the graph, to be searched in the distance-finding algorithm.
            unvisited = self.__populate(unvisited)  # populating this list recursively

            print('The graph has these nodes:')
            for n in unvisited:  # searching the graph...
                print(n.value)
            print('The distance between node',self.value,'and node',otherNode.value,'is','undefined','.')


#
# %%
# building the simple test graph:
# 0 -- 1
# |  / | \
# | /  |  2
# |/   | /
# 4 - 3

node0 = Node(0)
node1 = Node(1, [node0])
node2 = Node(2, [node1])
node3 = Node(3, [node1, node2])
node4 = Node(4, [node0, node1, node3])

node0.getNeighbors()

# %%
node2.distance(node4)
