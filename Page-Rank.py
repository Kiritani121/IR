def incomingNodes(graph: dict, node: str):
    nodeList = []
    for key in graph.keys():
        if node in graph[key]:
            nodeList.append(key)

    return nodeList


def calcRanks(graph: dict, ranks: dict, dampFactor: int) -> None:
    for i in range(3):
        print(f"Iteration {i+1}")
        for node in graph.keys():
            incoming = incomingNodes(graph, node)
            ranks[node] = (1-dampFactor) + dampFactor * \
                sum([(ranks[income] / len(graph[income]))
                    for income in incoming])
            print(f"{node}: {ranks[node]}")
        print()


if __name__ == "__main__":
    # The graph contains nodes in the format {Node: outgoing links}
    graph = {
        "A": ["B", "C"],
        "B": ["C"],
        "C": ["A", "D"],
        "D": []
    }

    ranks = {
        "A": 1,
        "B": 1,
        "C": 1,
        "D": 1
    }

    dampFactor = 0.85
    calcRanks(graph, ranks, dampFactor)
