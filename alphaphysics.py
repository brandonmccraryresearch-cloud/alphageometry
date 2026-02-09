# alphaphysics.py
import sys
import logging
import physics_graph
import physics_engine
import llm_client

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def run_alphaphysics(problem_statement):
    logging.info(f"Solving Frontier Physics Problem: {problem_statement}")

    # 1. Initialize Graph and Load Rules
    graph = physics_graph.PhysicsGraph()
    rules_path = os.path.join(os.path.dirname(__file__), "physics_rules.txt")
    rules = physics_engine.parse_rules(rules_path)

    # 2. Add initial premises to graph (this is a simplified representation)
    # In a real system, we would parse the problem_statement into predicates.
    # For now, let's assume the problem statement might contain some hints or we let the LLM handle it.
    if "Fine Structure Constant" in problem_statement:
        graph.add_predicate("lattice_structure", ["L1", "D4"])
        graph.add_predicate("degree_of_freedom", ["L1", "137"])

    # 3. First attempt: Symbolic Deduction
    logging.info("Attempting symbolic deduction...")
    depth = physics_engine.solve(graph, rules)
    logging.info(f"Symbolic deduction reached depth {depth}")

    # Check if we have an 'explained_constant'
    explained = graph.get_predicates("explained_constant")
    if explained:
        logging.info(f"Symbolic engine successfully explained: {explained}")
        # Even if solved symbolically, we might want the LLM to provide the Nobel-level discourse.
    else:
        logging.info("Symbolic engine reached saturation without full explanation. Calling Architect of Axiomatic Rigor...")

    # 4. Generative Layer: Call LLM
    try:
        client = llm_client.GeminiPhysicsClient()
        # We pass the current graph state and the problem to the LLM
        graph_state = str(graph.get_predicates())
        prompt = f"""
Current Symbolic State: {graph_state}
Problem Statement: {problem_statement}

Based on the Hyper-Literal Reverse Engineering (HLRE) methodology, provide a mechanical reconstruction and perform a Meta-Theoretical Validation.
"""
        response = client.generate_reconstruction(prompt)
        print("\n=== ALPHA-PHYSICS OUTPUT ===\n")
        print(response)
        print("\n============================\n")
    except ValueError as e:
        logging.warning(f"Skipping LLM call due to configuration error: {e}. Ensure GEMINI_API_KEY is set.")
    except Exception as e:
        logging.error(f"LLM Client failed unexpectedly: {e}")

if __name__ == "__main__":
    problem = "Explain the mechanical origin of the Fine Structure Constant (approx. 1/137) using HLRE."
    if len(sys.argv) > 1:
        problem = " ".join(sys.argv[1:])
    run_alphaphysics(problem)
