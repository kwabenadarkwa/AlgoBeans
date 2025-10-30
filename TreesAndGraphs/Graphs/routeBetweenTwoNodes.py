# INFO: Route Between Nodes
# Given a directed graph, design an algorithm to find out whether there is a route Between
# two nodes


import collections
from typing import Dict, List, Self


class Graph:
    def __init__(self):
        self.nodes: Dict[str, Node] = {}

    def add_node(self, node):
        if node.name in self.nodes:
            return
        self.nodes[node.name] = node

    def add_edge(self, from_name, to_name):
        self.nodes[from_name].children.append(self.nodes[to_name])


class Node:
    def __init__(self, name: str):
        self.name: str = name
        self.marked: bool = False
        self.children: List[Self] = []


# do a dfs and find all nodes that one of them is connected to once you see one that is the same as n2
# you know that there is a route between them
def routeBetweenNodes(n1: Node, n2: Node) -> bool:
    queue = collections.deque()
    n1.marked = True
    queue.append(n1)

    while len(queue) > 0:
        n1 = queue.popleft()
        print(n1.name)
        if n1 is n2:
            return True
        for child in n1.children:
            if child.marked is False:
                queue.append(child)
                child.marked = True

    return False

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

    print("the order should be")
    print(routeBetweenNodes(node_one,node_two))


