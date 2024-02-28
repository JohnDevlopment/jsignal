from __future__ import annotations
from ..signals import signal

ConnectedNodes: list[Node] = []

class Tree:
    def __init__(self):
        self.nodes: list[Node] = []
        self.on_connected = signal('connected')

    def add_node(self, node: Node):
        self.nodes.append(node)
        self.on_connected.emit(node)

class Node:
    def __init__(self, name: str):
        self.name = name

def _on_node_connected(node: Node, **kw):
    global ConnectedNodes
    ConnectedNodes.append(node)

def test_signals() -> None:
    tree = Tree()
    tree.on_connected.connect(_on_node_connected)
    tree.add_node(Node("node-1"))
    tree.add_node(Node("node-2"))
    assert len(ConnectedNodes) == 2
