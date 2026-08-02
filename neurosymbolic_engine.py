"""
Neurosymbolic Model Engine for Future Backcasting (미래역산법)
============================================================
Combines Symbolic Logic (SQLite Ontology + Math Optimization) 
with Neural Perception (Contextual Reasoning & Prescriptions).
"""

import sqlite3
import os
import json

DB_PATH = os.path.join(os.path.dirname(__file__), "future_backcasting.db")

class NeurosymbolicEngine:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        if not os.path.exists(self.db_path):
            from future_backcasting_db import init_db
            init_db()

    def query_symbolic_ontology(self):
        """Extracts Symbolic Knowledge Graph from SQLite DB."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM backcasting_nodes ORDER BY step_order ASC")
        nodes = [dict(row) for row in cursor.fetchall()]

        cursor.execute("SELECT * FROM problem_solving_and_learning")
        mechanisms = [dict(row) for row in cursor.fetchall()]

        cursor.execute("SELECT * FROM dsq_optimization_rules")
        dsq_rules = [dict(row) for row in cursor.fetchall()]

        conn.close()

        return {
            "7_steps": nodes,
            "mechanisms": mechanisms,
            "dsq_rules": dsq_rules
        }

    def calculate_dsq_performance(self, direction: float, speed: float, quality: float, base_profit: float = 48.0):
        """
        Mathematical Optimization Solver:
        Performance = Direction(0/1) * Speed(4M) * Quality(Pre-mortem) * Base_Profit
        """
        d_norm = max(0.0, min(1.0, direction / 100.0))
        s_norm = max(0.0, min(1.0, speed / 100.0))
        q_norm = max(0.0, min(1.0, quality / 100.0))

        delta_pi = d_norm * s_norm * q_norm * base_profit
        return {
            "direction_norm": d_norm,
            "speed_norm": s_norm,
            "quality_norm": q_norm,
            "delta_pi_billion_krw": round(delta_pi, 2)
        }

    def generate_neurosymbolic_prescription(self, problem_description: str, target_goal: str, d: float = 95, s: float = 90, q: float = 88):
        """
        Neurosymbolic Solver:
        Bindings problem context to Symbolic Knowledge Nodes and outputs executable prescription.
        """
        symbolic_data = self.query_symbolic_ontology()
        dsq_result = self.calculate_dsq_performance(d, s, q)

        prescription = {
            "system": "미래역산법 Neurosymbolic AGI Engine 2.5",
            "problem_input": problem_description,
            "target_goal_constant": target_goal,
            "step1_problem_solving": {
                "vector": "Future -> Present",
                "binary_choice": {
                    "focus_1": "사명 및 정량 목표상수(C_Goal) 직결 과제 100% 농축",
                    "eliminate_0": "불필요 권위, 비본질 적자 관행 0 차단"
                },
                "dsq_optimization": dsq_result
            },
            "step2_feedback_learning": {
                "vector": "Present -> Past",
                "causal_tracing": "현재 결과 데이터로 과거 원인 및 패턴 역산 학습"
            },
            "7_steps_roadmap": [
                {
                    "step": node["step_order"],
                    "code": f"{node['acrostic_letter']} · {node['hanja_name']}",
                    "action": node["summary"]
                }
                for node in symbolic_data["7_steps"]
            ]
        }

        return prescription

if __name__ == "__main__":
    engine = NeurosymbolicEngine()
    prescription = engine.generate_neurosymbolic_prescription(
        problem_description="중소병원 검진센터 적자 표류 및 12개 테마 병렬 추진으로 조직 마비",
        target_goal="1년 내 만성질환 외래 환자 비율 35% 증대 및 35억 수지 개선"
    )
    print(json.dumps(prescription, ensure_ascii=False, indent=2))
