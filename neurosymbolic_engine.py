"""
Neurosymbolic Model Engine for Future Backcasting (미래역산법) 3.0
============================================================
Combines Symbolic Logic (SQLite Graph Ontology + Math Optimization Solver) 
with Multi-Agent Harness Loop (Planner, Ontology, Optimization, Learner Agents).
"""

import sqlite3
import os
import json
import math

DB_PATH = os.path.join(os.path.dirname(__file__), "future_backcasting.db")

class PlannerAgent:
    """Agent 1: Determines Target Goal Constant (C_Goal) and Future-to-Present Backcasting Path."""
    def plan_backcasting(self, target_goal_constant: str):
        return {
            "agent": "PlannerAgent (미래역산 기획 에이전트)",
            "vector": "Future -> Present",
            "target_goal_constant": target_goal_constant,
            "action": "미래 상수를 고정하고 현재 0(배제)/1(선택) 직렬 과제 도출"
        }

class OntologyAgent:
    """Agent 2: Queries Knowledge Graph Triples from SQLite DB."""
    def query_graph_triples(self, db_path):
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM ontology_triples")
        triples = [dict(row) for row in cursor.fetchall()]

        cursor.execute("SELECT * FROM backcasting_nodes ORDER BY step_order ASC")
        steps = [dict(row) for row in cursor.fetchall()]

        conn.close()
        return {"triples": triples, "steps": steps}

class OptimizationAgent:
    """Agent 3: Mathematical Solver for DSQ Optimization Model (Gradient & Cost Function)."""
    def solve_dsq(self, d: float, s: float, q: float, target_profit: float = 35.0, base_scale: float = 48.0):
        d_norm = max(0.0, min(1.0, d / 100.0))
        s_norm = max(0.0, min(1.0, s / 100.0))
        q_norm = max(0.0, min(1.0, q / 100.0))

        achieved = d_norm * s_norm * q_norm * base_scale
        loss = (achieved - target_profit) ** 2

        # Sensitivity Analysis (Gradients)
        grad_d = s_norm * q_norm * base_scale
        grad_s = d_norm * q_norm * base_scale
        grad_q = d_norm * s_norm * base_scale

        return {
            "d_norm": round(d_norm, 4),
            "s_norm": round(s_norm, 4),
            "q_norm": round(q_norm, 4),
            "achieved_roi_billion_krw": round(achieved, 2),
            "target_gap": round(achieved - target_profit, 2),
            "loss_cost": round(loss, 4),
            "gradients": {
                "d_direction_gradient": round(grad_d, 2),
                "s_speed_gradient": round(grad_s, 2),
                "q_quality_gradient": round(grad_q, 2)
            }
        }

class LearnerAgent:
    """Agent 4: Traces Present Outcomes back to Past Causal Patterns (Feedback Learning)."""
    def trace_past_learning(self, current_outcome: float, historical_failure_patterns: list):
        return {
            "agent": "LearnerAgent (과거 피드백 학습 에이전트)",
            "vector": "Present -> Past",
            "current_outcome": current_outcome,
            "causal_feedback_insights": [
                f"과거 패착 패턴 '{pattern}' 0으로 완벽 제거" for pattern in historical_failure_patterns
            ],
            "status": "인과 피드백 학습 완결"
        }

class NeurosymbolicEngine:
    """Master Harness Engine Orchestrating 4 Agents & Symbolic Knowledge Graph."""
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        if not os.path.exists(self.db_path):
            from future_backcasting_db import init_db
            init_db()

        self.planner = PlannerAgent()
        self.ontology_agent = OntologyAgent()
        self.optimizer = OptimizationAgent()
        self.learner = LearnerAgent()

    def query_symbolic_ontology(self):
        """Extracts Symbolic Knowledge Graph from SQLite DB."""
        return self.ontology_agent.query_graph_triples(self.db_path)

    def calculate_dsq_performance(self, d: float, s: float, q: float, base_profit: float = 48.0):
        return self.optimizer.solve_dsq(d, s, q, base_scale=base_profit)

    def generate_neurosymbolic_prescription(self, problem_description: str, target_goal: str, d: float = 95, s: float = 90, q: float = 88):
        """Harness Loop execution combining all 4 agents."""
        return self.run_harness_loop(problem_description, target_goal, d, s, q)

    def run_harness_loop(self, problem: str, goal: str, d: float = 95, s: float = 90, q: float = 88):
        # Step 1: Planner Agent
        plan = self.planner.plan_backcasting(goal)

        # Step 2: Ontology Agent
        graph_knowledge = self.ontology_agent.query_graph_triples(self.db_path)

        # Step 3: Optimization Agent
        dsq_sol = self.optimizer.solve_dsq(d, s, q, target_profit=35.0)

        # Step 4: Learner Agent
        learn = self.learner.trace_past_learning(
            current_outcome=dsq_sol["achieved_roi_billion_krw"],
            historical_failure_patterns=["12개 과제 병렬 추진으로 조직 마비", "권위적 문화", "적자 검진센터 표류"]
        )

        return {
            "system": "미래역산법 Neurosymbolic Multi-Agent Harness Engine 3.0",
            "problem": problem,
            "harness_loop_agents": [
                "PlannerAgent", "OntologyAgent", "OptimizationAgent", "LearnerAgent"
            ],
            "step1_problem_solving_plan": plan,
            "step3_dsq_mathematical_solution": dsq_sol,
            "step2_feedback_learning": learn,
            "symbolic_graph": {
                "steps_count": len(graph_knowledge["steps"]),
                "triples_count": len(graph_knowledge["triples"]),
                "sample_triples": graph_knowledge["triples"][:3]
            }
        }

if __name__ == "__main__":
    engine = NeurosymbolicEngine()
    result = engine.run_harness_loop(
        problem="중소병원 수지 적자 및 과제 병렬 추진으로 조직 마비",
        goal="1년 내 수지개선 +35억원 목표상수 확정"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
