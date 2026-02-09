# AlphaPhysics: Neuro-Symbolic Frontier Physics Solver

AlphaPhysics is an advanced reasoning system designed to solve frontier physics problems using a neuro-symbolic approach. It combines a rigorous symbolic deduction engine with a generative LLM layer, specifically tailored for the **Hyper-Literal Reverse Engineering (HLRE)** methodology.

## Methodology: Hyper-Literal Reverse Engineering (HLRE)

HLRE treats the physical universe as a "found object"—a machine of unknown origin whose operating specifications are visible in the fundamental constants.

### Core Axioms:
1.  **The Semantic Axiom (Ban on Metaphor)**: Replaces abstract labels (e.g., "color", "flavor") with precise mechanical descriptions (e.g., "geometric orientation", "lattice stress").
2.  **The Geometric Axiom (Substrate Requirement)**: Dimensionless constants (like 1/137) are treated as structural properties (degrees of freedom) of a discrete vacuum substrate (lattice).
3.  **The Mechanical Axiom (Mechanism over Magic)**: "Intrinsic properties" are redefined as extrinsic results of interaction between an object and the lattice (e.g., mass as lattice resistance).

## System Architecture

The AlphaPhysics system consists of three primary layers:

1.  **Symbolic Engine (`physics_engine.py`)**: A Breadth-First Search (BFS) deduction engine that applies formal HLRE rules to a graph state.
2.  **Graph Representation (`physics_graph.py`)**: A state-tracking mechanism that stores predicates and ensures logical consistency.
3.  **Architect of Axiomatic Rigor (`llm_client.py`)**: A generative layer utilizing Google Gemini (via `google-genai`) to provide Nobel-level discourse, mechanical reconstructions, and meta-theoretical validation when symbolic deduction reaches saturation.

## Quick Start (Automation)

The system is automated for use by Jules or other AI coding agents.

### 1. Prerequisites

Ensure you have Python 3.10+ installed.

### 2. Set Up API Key

AlphaPhysics requires a Gemini API key. The system prioritizes the `JULES_API_KEY` environment variable.

```bash
export JULES_API_KEY="your_api_key_here"
```

*Note: `GEMINI_API_KEY` is also supported as a fallback.*

### 3. Run AlphaPhysics

Use the `automate.py` script to run the system. It handles dependency installation (`google-genai`) and execution.

```bash
# Run with a custom problem
./automate.py "Explain the mechanical origin of the Fine Structure Constant"

# Run with a pre-defined problem
./automate.py --list
./automate.py "Problem 2"
```

## Detailed Step-by-Step Setup

### Manual Installation
If you prefer not to use the automation script:

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements_physics.txt
    ```

2.  **Run Tests**:
    ```bash
    python3 test_alphaphysics.py
    ```

3.  **Execute Main Program**:
    ```bash
    python3 alphaphysics.py "Your problem statement here"
    ```

## Project Structure

-   `alphaphysics.py`: Main entry point and orchestration logic.
-   `automate.py`: Automation script for setup and execution.
-   `physics_engine.py`: Symbolic deduction logic.
-   `physics_graph.py`: State management for derived predicates.
-   `llm_client.py`: Interface for the Gemini Architect.
-   `physics_rules.txt`: Formalized HLRE deduction rules.
-   `physics_problems.txt`: A collection of frontier physics challenges.
-   `system_instruction.txt`: Detailed personas and logical protocols for the LLM.

## Deducting the Fine Structure Constant (Example)

When solving the Fine Structure Constant problem:
1.  The **Symbolic Engine** identifies the "137" integer as a degree of freedom.
2.  It matches this to the **D4 Lattice** (SO(8) group) scattering channels.
3.  The **Gemini Architect** then provides a detailed mechanical reconstruction of why the vacuum lattice necessitates 137 degrees of freedom, performing a Meta-Theoretical Validation of the result.

---
*AlphaPhysics: Decoding the Blueprints of Reality.*
