# A class for building graphs of interconnected nodes
# Nodes of graph-type maps have neighbors only, with no heirarchy
# Andrew Vikartofsky, March 2019


class Node:
    def __init__(self, myValue, myNeighbors=[]):
        for n in myNeighbors:
            if type(n) is not Node:
                print('Node init error - declared neighbor is not a Node!')
                return
        self.myNeighbors = myNeighbors
        self.myValue = myValue
        for n in myNeighbors:
            n.addNeighbor(self)

    def addNeighbor(self, newNeighbor):
        if type(newNeighbor) is not Node:
            print('Node modification error - declared new neighbor is not a Node!')
            return
        if newNeighbor not in self.myNeighbors:
            self.myNeighbors.append(newNeighbor)

    def removeNeighbor(self, oldNeighbor):
        if oldNeighbor not in self.myNeighbors:
            print('Node modification error - requested neighbor does not exist!')
            return
        self.myNeighbors.remove(oldNeighbor)

    def getNeighbors(self):
        for n in self.myNeighbors:
            print(n.value())

    def value(self):
        return self.myValue


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
