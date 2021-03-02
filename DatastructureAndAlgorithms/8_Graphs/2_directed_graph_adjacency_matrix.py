class Graph:
    def __init__(self, no_of_nodes):
        self.no_of_nodes= no_of_nodes+1
        self.graph= [[0 for x in range(no_of_nodes+1)]
                     for y in range(no_of_nodes+1)]

    def insert_edge(self, v1, v2):
        self.graph[v1][v2]=1

    def within_bounds(self, v1, v2):
        return (v1>=0 and v1<=self.no_of_nodes and v2>=0 and v2<=self.no_of_nodes)

    def print_graph(self):
        print('As Adjacency Matrix')
        for i in range(len(self.graph)):
            print(self.graph[i])

        print('As graph')
        for i in range(self.no_of_nodes):
            for j in range(len(self.graph[i])):
                if self.graph[i][j]:
                    print(i,'->',j)

g= Graph(5)
g.insert_edge(1,2)
g.insert_edge(1,3)
g.insert_edge(2,3)
g.insert_edge(4,5)

g.print_graph()