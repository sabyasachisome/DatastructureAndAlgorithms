graph={
'a':{'b':3,'c':4,'d':7},
'b':{'c':1,'f':5},
'c':{'f':6,'d':2},
'd':{'e':3,'g':6},
'e':{'g':3,'h':4},
'f':{'e':1,'h':8},
'g':{'h':2},
'h':{'g':2}
}

graph= {
'a':{'b':10,'c':3},
'b':{'c':1,'d':2},
'c':{'b':4,'d':8,'e':2},
'd':{'e':7},
'e':{'d':9}
}



def dijkstra(graph, start, goal):
    shortest_distance={}
    predecessor={}
    unseen_nodes=graph
    infinity=9999999
    path=[]
    for node in unseen_nodes:
        shortest_distance[node]= infinity
    shortest_distance[start]= 0
    # print(shortest_distance)

    while unseen_nodes:
        min_node= None
        for node in unseen_nodes:
            if min_node is None:
                min_node= node
            elif shortest_distance[node]< shortest_distance[min_node]:
                min_node= node

        for child_node, weight in graph[min_node].items():
            # print(child_node,weight)
            if shortest_distance[min_node]+weight<shortest_distance[child_node]:
                shortest_distance[child_node]= shortest_distance[min_node]+weight
                predecessor[child_node]= min_node
        unseen_nodes.pop(min_node)
    print(shortest_distance)

dijkstra(graph, 'a','d')