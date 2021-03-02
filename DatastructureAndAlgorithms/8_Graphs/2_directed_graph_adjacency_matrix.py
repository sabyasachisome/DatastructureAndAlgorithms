class Graph:
    def __init__(self, no_of_nodes):
        self.no_of_nodes= no_of_nodes+1
        self.graph= [[0 for x in range(no_of_nodes+1)]
                     for y in range(no_of_nodes+1)]

    def insert_node(self, v1, v2):
        self.graph[v1][v2]=1
        