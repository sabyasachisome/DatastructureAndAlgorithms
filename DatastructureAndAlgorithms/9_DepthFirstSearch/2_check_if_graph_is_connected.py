"""
Given a directed graph. The task is to check if the given graph is connected or not.
"""

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph= defaultdict(list)

    def insert_edge(self, v1, v2):
        self.graph[v1].append(v2)

    def dfs(self, start_node):
        self.visited_set= set()
        st=[]
        st.append(start_node)

        while(len(st)):
            cur_node = st[-1]
            st.pop()
            if cur_node not in self.visited_set:
                # print(cur_node)
                self.visited_set.add(cur_node)

            for neighbour in self.graph[cur_node]:
                if neighbour not in self.visited_set:
                    st.append(neighbour)

class Solution:
    def check_connected(self, set1, set2):
        if len(set1.difference(set2)) ==0 and len(set2.difference(set1))==0:
            return True
        return False

if __name__=='__main__':
    g= Graph()
    g.insert_edge(0,1)
    g.insert_edge(0,3)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(1,3)
    g.dfs(0)

    list_of_nodes= [0,1,0,3,1,2,2,3,1,3]
    list_of_distinct_nodes= set(list_of_nodes)

    sol= Solution()
    print(sol.check_connected(list_of_distinct_nodes, g.visited_set))
