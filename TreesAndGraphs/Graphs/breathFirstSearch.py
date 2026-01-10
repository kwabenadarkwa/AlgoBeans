from collections import deque


def breadth_first_search(graph: dict, search_node: str):
    search_queue = deque()
    search_queue.append(list(graph.keys())[0])
    visited = set()

    while search_queue:
        curr_node = search_queue.pop()
        visited.add(curr_node)

        if curr_node == search_node:
            return True

        neighbours = graph.get(curr_node)

        if neighbours:
            for neighbor in neighbours:
                if neighbor not in visited:
                    search_queue.append(neighbor)

    return False


if __name__ == "__main__":
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []
    print(graph.get("you"))
    print(breadth_first_search(graph, "kwabena"))
