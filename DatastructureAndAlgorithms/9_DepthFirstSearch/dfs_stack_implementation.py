from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph= defaultdict(list)

    def insert_edge(self, v1, v2):
        self.graph[v1].append(v2)

    def dfs(self, start_node):
        visited=set()
        st=[]
        st.append(start_node)
        while(len(st)):
            cur= st[-1]
            st.pop()
            if cur not in visited:
                print(cur, end=' ')
                visited.add(cur)

            for adj_vertex in self.graph[cur]:
                if (adj_vertex not in visited):
                    st.append(adj_vertex)


g= Graph()
g.insert_edge(2,5)
g.insert_edge(2,1)
g.insert_edge(5,6)
g.insert_edge(5,8)
g.insert_edge(6,9)

g.dfs(2)