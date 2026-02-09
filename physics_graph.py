# physics_graph.py
import collections

class PhysicsGraph:
    def __init__(self):
        self.predicates = [] # List of (predicate_name, args)
        self.cache = set()

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
        return f"PhysicsGraph({len(self.predicates)} predicates)"
