from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph= defaultdict(list)

    def insert_edge(self, v1, v2):
        self.graph[v1].append(v2)

    def print_graph(self):
        for node in self.graph:
            for value in self.graph[node]:
                print(node,'=>',value)

g= Graph()
g.insert_edge(1,2)
g.insert_edge(2,3)
g.insert_edge(3,4)
g.insert_edge(4,1)
g.insert_edge(4,100)

g.print_graph()