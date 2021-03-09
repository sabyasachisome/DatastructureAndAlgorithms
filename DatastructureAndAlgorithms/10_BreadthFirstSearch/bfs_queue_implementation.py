from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph= defaultdict(list)

    def insert_edge(self, v1, v2):
        self.graph[v1].append(v2)

    def bfs(self, start_node):
        queue= []
        visited_set=set()
        queue.append(start_node)
        while(queue):
            u= queue.pop(0)
            print(u, end=' ')

            for adj_edge in self.graph[u]:
                if adj_edge not in visited_set:
                    visited_set.add(adj_edge)
                    queue.append(adj_edge)


g= Graph()
g.insert_edge(1,2)
g.insert_edge(1,3)
g.insert_edge(3,4)
g.insert_edge(3,5)

g.bfs(1)