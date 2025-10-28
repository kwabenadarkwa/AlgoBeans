#INFO: you could implement a graph in two ways, the first way is to use the 
# Adjacency list and the second way is to use the Adjacency matrix
#in the adjacecy list you have to have a graph class because unlike a tree where you can just 
#get to every element using the root node, you can't do the same for the graph. because it might not be connected

import collections
#Adjacency List
from typing import Dict, Self,List


class Graph:
    def __init__(self):
        self.nodes:Dict[str, Node] = {}

    def add_node(self,node):
        if node.name in self.nodes: 
            return 
        self.nodes[node.name] = node

    def add_edge(self, from_name, to_name):
        self.nodes[from_name].children.append(self.nodes[to_name])


class Node:
    def __init__(self,name:str):
        self.name:str= name 
        self.marked:bool= False
        self.children:List[Self] = []

#Adjacency Matrix
# This is where we have a bunch of nodes and then we create a NxN matrix that represents the connections between these nodes

def breadth_first_search(node:Node):
    queue = collections.deque()
    node.marked = True
    queue.append(node)

    while len(queue) > 0: 
        r = queue.popleft()
        print(r.name)

        for child in r.children:
            if child.marked is False: 
                child.marked = True
                queue.append(child)


def depth_first_search(node:Node):
    if node is None: 
        return 
    node.marked = True
    print(node.name)

    for child in node.children:
        if child.marked is False: 
            depth_first_search(child)


if __name__ == "__main__":
    node_one = Node("A")
    node_two = Node("B")
    node_three = Node("C")
    node_four = Node("D")
    node_five = Node("E")


    graph = Graph()
    graph.add_node(node_one)
    graph.add_node(node_two)
    graph.add_node(node_three)
    graph.add_node(node_four)
    graph.add_node(node_five)
    graph.add_edge("A","E")
    graph.add_edge("A","B")
    graph.add_edge("B","C")
    graph.add_edge("B","D")
    graph.add_edge("C","E")
    graph.add_edge("D","E")

    print("bfs")
    # breadth_first_search(node_one)
    print("dfs")
    depth_first_search(node_one)

    # for key, value in graph.nodes.items(): 
    #     print(key,":",value.children)
    #
