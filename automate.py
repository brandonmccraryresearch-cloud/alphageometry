#!/usr/bin/env python3
import os
import sys
import subprocess
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def install_dependencies():
    logging.info("Checking and installing AlphaPhysics dependencies...")
    try:
        import google.genai
        logging.info("google-genai already installed.")
    except ImportError:
        logging.info("Installing google-genai...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "google-genai"])
        except Exception as e:
            logging.error(f"Failed to install google-genai: {e}")
            sys.exit(1)

def check_env():
    api_key = os.environ.get("JULES_API_KEY") or os.environ.get("GEMINI_API_KEY")
    if not api_key:
        logging.warning("No API key found in environment variables (JULES_API_KEY or GEMINI_API_KEY).")
        logging.warning("Symbolic deduction will still run, but LLM reconstruction will fail.")
        return False
    return True

def list_problems():
    if not os.path.exists("physics_problems.txt"):
        logging.error("physics_problems.txt not found.")
        return

    print("\n=== Pre-defined Physics Problems ===\n")
    with open("physics_problems.txt", "r") as f:
        print(f.read())
    print("===================================\n")

def run_physics(problem):
    logging.info(f"Solving problem: {problem}")
    try:
        from alphaphysics import run_alphaphysics
        run_alphaphysics(problem)
    except ImportError as e:
        logging.error(f"Failed to import AlphaPhysics components: {e}")
        logging.info("Make sure you are in the correct directory.")
    except Exception as e:
        logging.error(f"An error occurred during execution: {e}")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--list":
        list_problems()
        sys.exit(0)

    problem_statement = "Explain the mechanical origin of the Fine Structure Constant (approx. 1/137) using HLRE."
    if len(sys.argv) > 1:
        problem_statement = " ".join(sys.argv[1:])

    install_dependencies()
    check_env()
    run_physics(problem_statement)

if __name__ == "__main__":
    main()
