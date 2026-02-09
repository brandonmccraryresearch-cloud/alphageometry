# physics_engine.py
import re

class PhysicsRule:
    def __init__(self, premise, conclusion, name=None):
        self.premise = premise # List of (pred_name, args)
        self.conclusion = conclusion # (pred_name, args)
        self.name = name

    def __repr__(self):
        return f"Rule({self.name}: {self.premise} => {self.conclusion})"

def parse_rules(filepath):
    rules = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=>' not in line:
                continue

            premise_str, conclusion_str = line.split('=>')

            # Simple parser for "pred(args), pred(args) => pred(args)"
            def parse_preds(s):
                preds = []
                # Match name(args)
                matches = re.findall(r'(\w+)\s*\(([^)]+)\)', s)
                for name, args_str in matches:
                    args = [a.strip().strip('"') for a in args_str.split(',')]
                    preds.append((name, args))
                return preds

            premise = parse_preds(premise_str)
            conclusion_preds = parse_preds(conclusion_str)
            if not conclusion_preds:
                # Or log a warning about the malformed rule
                continue
            conclusion = conclusion_preds[0]
            rules.append(PhysicsRule(premise, conclusion, name=line))
    return rules

def solve(graph, rules, max_depth=10):
    added_any = True
    depth = 0
    while added_any and depth < max_depth:
        added_any = False
        depth += 1
        for rule in rules:
            # Simple unification
            mappings = [{}] # List of possible variable mappings

            for pred_name, pred_args in rule.premise:
                new_mappings = []
                for mapping in mappings:
                    # Find matching predicates in graph
                    for g_name, g_args in graph.get_predicates(pred_name):
                        if len(g_args) != len(pred_args):
                            continue

                        m_copy = mapping.copy()
                        match = True
                        for p_arg, g_arg in zip(pred_args, g_args):
                            if p_arg.isupper(): # Variable
                                if p_arg in m_copy:
                                    if m_copy[p_arg] != g_arg:
                                        match = False
                                        break
                                else:
                                    m_copy[p_arg] = g_arg
                            else: # Constant
                                if p_arg != g_arg:
                                    match = False
                                    break

                        if match:
                            new_mappings.append(m_copy)
                mappings = new_mappings
                if not mappings:
                    break

            for mapping in mappings:
                # Apply conclusion
                c_name, c_args = rule.conclusion
                actual_args = [mapping.get(a, a) for a in c_args]
                if graph.add_predicate(c_name, actual_args):
                    added_any = True
    return depth
