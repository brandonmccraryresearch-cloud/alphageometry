# test_alphaphysics.py
import physics_graph
import physics_engine
import unittest

class TestPhysicsSystem(unittest.TestCase):
    def test_symbolic_derivation(self):
        graph = physics_graph.PhysicsGraph()
        # Premises
        graph.add_predicate("lattice_structure", ["L1", "D4"])
        graph.add_predicate("degree_of_freedom", ["L1", "137"])

        # Manually add a rule that bridges them to explained_constant
        # In physics_rules.txt: "lattice_structure L "D4", degree_of_freedom L 137 => inverse_coupling L 137"
        # and "degree_of_freedom L N, inverse_coupling L C, N == C => explained_constant C L"
        # Note: My simple engine needs exact matches and doesn't handle N == C yet unless I hardcode it.
        # Let's add a more direct rule for the test.

        rules = [
            physics_engine.PhysicsRule(
                [("lattice_structure", ["L", "D4"]), ("degree_of_freedom", ["L", "137"])],
                ("inverse_coupling", ["L", "137"]),
                "Lattice Scattering Rule"
            ),
            physics_engine.PhysicsRule(
                [("degree_of_freedom", ["L", "N"]), ("inverse_coupling", ["L", "N"])],
                ("explained_constant", ["N", "L"]),
                "Explanation Rule"
            )
        ]

        depth = physics_engine.solve(graph, rules)
        self.assertTrue(graph.check("explained_constant", ["137", "L1"]))
        print(f"Symbolic test passed with depth {depth}")

    def test_rule_parsing(self):
        rules_path = os.path.join(os.path.dirname(__file__), "physics_rules.txt")
        rules = physics_engine.parse_rules(rules_path)
        self.assertGreater(len(rules), 0)
        print(f"Successfully parsed {len(rules)} rules.")

if __name__ == "__main__":
    unittest.main()
