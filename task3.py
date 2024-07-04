import networkx as nx
from typing import Hashable, Dict
import matplotlib.pyplot as plt


def dfs(graph: nx.Graph, node: Hashable, visited: Dict[Hashable, bool]):
    """
    Обход графа в глубину.
    :param graph: Граф NetworkX.
    :param node: Начальный узел для обхода.
    :param visited: Словарь посещенных узлов.
    """
    visited[node] = True

    for neighbor in graph.neighbors(node):
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)


def find_connected_components(graph: nx.Graph) -> int:
    """
    Поиск количества компонент связности в графе с использованием dfs.
    :param graph: Граф (NetworkX).
    :return: Количество компонент связности.
    """
    visited = {node: False for node in graph.nodes}
    component_count = 0

    for node in graph.nodes:
        if not visited[node]:
            dfs(graph, node, visited)
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
