#!/usr/bin/env python3
"""
미래역산법 (FORWARD FROM THE FUTURE) Neurosymbolic AGI System
============================================================
Master CLI & Entry Point
"""

import sys
import os
import argparse
import json

# Ensure UTF-8 output encoding for Windows terminal
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

from neurosymbolic_engine import NeurosymbolicEngine
from future_backcasting_db import init_db

def main():
    parser = argparse.ArgumentParser(description="미래역산법 (FORWARD FROM THE FUTURE) Neurosymbolic Engine")
    parser.add_argument("--mode", choices=["init", "consult", "ontology"], default="consult", help="실행 모드 (init: DB초기화, consult: 경영처방, ontology: 온톨로지조회)")
    parser.add_argument("--problem", type=str, default="병원 수지 적자 및 과제 병렬 추진으로 인한 조직 마비", help="경영 위기 문제 현상")
    parser.add_argument("--goal", type=str, default="1년 내 수지개선 +35억원 목표상수 확정", help="미래 목표상수 (C_Goal)")
    parser.add_argument("--d", type=float, default=95.0, help="Direction (1/0 선택 최적화율)")
    parser.add_argument("--s", type=float, default=90.0, help="Speed (4M 자원 농축률)")
    parser.add_argument("--q", type=float, default=88.0, help="Quality (실패원인 수술률)")

    args = parser.parse_args()

    if args.mode == "init":
        init_db()
        print("[SUCCESS] 미래역산법 온톨로지 SQLite DB가 성공적으로 초기화되었습니다.")
    elif args.mode == "ontology":
        engine = NeurosymbolicEngine()
        ontology = engine.query_symbolic_ontology()
        print(json.dumps(ontology, ensure_ascii=False, indent=2))
    elif args.mode == "consult":
        engine = NeurosymbolicEngine()
        prescription = engine.generate_neurosymbolic_prescription(
            problem_description=args.problem,
            target_goal=args.goal,
            d=args.d,
            s=args.s,
            q=args.q
        )
        print("\n=======================================================")
        print("[FORWARD FROM THE FUTURE] 미래역산법 AGI 경영 처방전")
        print("=======================================================\n")
        print(json.dumps(prescription, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
