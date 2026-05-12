from agents.planner_agent import PlannerAgent
from agents.simulation_agent import SimulationAgent
from agents.analysis_agent import AnalysisAgent
from agents.critic_agent import CriticAgent
from agents.optimization_agent import OptimizationAgent

from memory.trajectory_memory import TrajectoryMemory


class CFDOrchestrator:

    def __init__(self):

        self.planner = PlannerAgent()
        self.simulator = SimulationAgent()
        self.analysis = AnalysisAgent()
        self.critic = CriticAgent()
        self.optimizer = OptimizationAgent()

        self.memory = TrajectoryMemory()

    def run(self, goal, iterations=10):

        params = self.planner.plan(goal)

        for i in range(iterations):

            print(f"\n========== ITERATION {i+1} ==========")

            result = self.simulator.run_case(params)

            analysis = self.analysis.evaluate(result)

            record = {
                "params": params,
                "result": result,
                "score": analysis["score"],
                "status": analysis["status"]
            }

            self.memory.add(record)

            print(f"[Analysis] score = {analysis['score']:.3f}")

            params = self.critic.reflect(result, params)

            params = self.optimizer.optimize(params, self.memory)

        print("\n========== BEST RESULT ==========")
        print(self.memory.get_best())
