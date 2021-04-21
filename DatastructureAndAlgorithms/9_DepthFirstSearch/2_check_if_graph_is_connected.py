"""
Given a directed graph. The task is to check if the given graph is connected or not.
"""
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph1= defaultdict(list)
        self.graph2 = defaultdict(list)

    def insert_edge(self, v1, v2):
        self.graph1[v1].append(v2)
        self.graph2[v2].append(v1)

    def dfs(self, start_node, graph):
        visited_set= set()
        st=[]
        st.append(start_node)

        while(len(st)):
            cur_node = st[-1]
            st.pop()
            if cur_node not in visited_set:
                print(cur_node)
                visited_set.add(cur_node)

            for neighbour in self.graph[cur_node]:
                if neighbour not in visited_set:
                    st.append(neighbour)

g= Graph()
g.insert_edge(0,1)
g.insert_edge(0,3)
g.insert_edge(1,2)
g.insert_edge(2,3)
g.insert_edge(1,3)
g.dfs(0, g.graph1)