# physics_graph.py
import collections

class PhysicsNode:
    def __init__(self, name, type, properties=None):
        self.name = name
        self.type = type
        self.properties = properties or {}
        self.neighbors = collections.defaultdict(list)

    def __repr__(self):
        return f"Node({self.name}, {self.type}, {self.properties})"

class PhysicsGraph:
    def __init__(self):
        self.nodes = {}
        self.predicates = [] # List of (predicate_name, args)
        self.cache = set()

    def add_node(self, name, type, properties=None):
        if name not in self.nodes:
            self.nodes[name] = PhysicsNode(name, type, properties)
        return self.nodes[name]

    def add_predicate(self, name, args):
        predicate = (name, tuple(args))
        if predicate not in self.cache:
            self.predicates.append(predicate)
            self.cache.add(predicate)
            return True
        return False

    def get_predicates(self, name=None):
        if name:
            return [p for p in self.predicates if p[0] == name]
        return self.predicates

    def check(self, name, args):
        return (name, tuple(args)) in self.cache

    def __repr__(self):
        return f"PhysicsGraph({len(self.nodes)} nodes, {len(self.predicates)} predicates)"
