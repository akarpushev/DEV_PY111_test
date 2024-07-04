import networkx as nx
from collections import deque
from typing import Hashable, Dict
import matplotlib.pyplot as plt


def bfs(graph: nx.Graph, node: Hashable, visited: Dict[Hashable, bool]):
    """
    Обход графа в ширину.
    :param graph: Граф NetworkX.
    :param node: Начальный узел для обхода.
    :param visited: Словарь посещенных узлов.
    """
    queue = deque([node])
    visited[node] = True

    while queue:
        current_node = queue.popleft()

        for neighbor in graph.neighbors(current_node):
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True


def find_connected_components(graph: nx.Graph) -> int:
    """
    Поиск количества компонент связности в графе с использованием bfs.
    :param graph: Граф (NetworkX).
    :return: Количество компонент связности.
    """
    visited = {node: False for node in graph.nodes}
    component_count = 0

    for node in graph.nodes:
        if not visited[node]:
            bfs(graph, node, visited)
            component_count += 1

    return component_count


if __name__ == '__main__':

    graph = nx.Graph()
    graph.add_nodes_from('ABCDEFG')
    graph.add_edges_from([('A', 'B'),
                          ('B', 'C'),
                          ('C', 'D'),
                          ('F', 'G')])

    nx.draw(graph)
    plt.show()

    print("Количество компонент связности:", find_connected_components(graph))
