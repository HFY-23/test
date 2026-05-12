from orchestrator import CFDOrchestrator

if __name__ == "__main__":

    goal = {
        "target": "low_nox_high_uniformity"
    }

    orchestrator = CFDOrchestrator()

    orchestrator.run(goal, iterations=15)
