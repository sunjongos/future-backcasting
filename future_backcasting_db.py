"""
Future Backcasting (미래역산법) SQLite Knowledge Graph Engine 4.0
==================================================================
Fully Ontologized Core Knowledge Architecture:
1. 7 Steps (顧飛結前資逆行 x FORWARD Acrostic)
2. DSQ Optimization Math Model (Direction 1/0, Speed 4M, Quality Pre-mortem)
3. 5 Problem Solving Logic Shifts (Predict->Backcast, Parallel->Serial, etc.)
4. Drucker 5 SMART Goal Constants
5. 3-Axis Timeline Vectors (Future->Present, Present->Past, Forward Analysis Paralysis)
6. Complete RDF Triples Knowledge Graph (20+ Triples)
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "future_backcasting.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Drop existing tables for fresh schema rebuild
    cursor.execute('DROP TABLE IF EXISTS backcasting_7steps')
    cursor.execute('DROP TABLE IF EXISTS dsq_math_ontology')
    cursor.execute('DROP TABLE IF EXISTS problem_solving_5axioms')
    cursor.execute('DROP TABLE IF EXISTS drucker_smart_goals')
    cursor.execute('DROP TABLE IF EXISTS timeline_3axis_mechanism')
    cursor.execute('DROP TABLE IF EXISTS knowledge_graph_triples')

    # 1. 7단계 온톨로지 (FORWARD Acrostic & 顧飛結前資逆行)
    cursor.execute('''
        CREATE TABLE backcasting_7steps (
            id TEXT PRIMARY KEY,
            step_order INTEGER,
            acrostic_letter TEXT,
            code_name TEXT,
            korean_name TEXT,
            hanja_name TEXT,
            tag_class TEXT,
            summary TEXT,
            description TEXT
        )
    ''')

    # 2. DSQ 성과 최적화 온톨로지
    cursor.execute('''
        CREATE TABLE dsq_math_ontology (
            id TEXT PRIMARY KEY,
            axis_symbol TEXT,
            axis_name TEXT,
            formula_role TEXT,
            choice_mechanism TEXT,
            weight REAL,
            description TEXT
        )
    ''')

    # 3. 문제해결 5대 전환 로직 온톨로지
    cursor.execute('''
        CREATE TABLE problem_solving_5axioms (
            axiom_number INTEGER PRIMARY KEY,
            from_paradigm TEXT,
            to_paradigm TEXT,
            core_logic TEXT,
            impact TEXT
        )
    ''')

    # 4. 피터 드러커 5대 SMART 목표상수 온톨로지
    cursor.execute('''
        CREATE TABLE drucker_smart_goals (
            letter TEXT PRIMARY KEY,
            principle_name TEXT,
            concept TEXT,
            backcasting_role TEXT
        )
    ''')

    # 5. 3축 시간역산 메커니즘 온톨로지
    cursor.execute('''
        CREATE TABLE timeline_3axis_mechanism (
            id TEXT PRIMARY KEY,
            phase_name TEXT,
            vector_direction TEXT,
            primary_purpose TEXT,
            result_state TEXT
        )
    ''')

    # 6. RDF Triples 온톨로지 그래프 (Subject-Predicate-Object)
    cursor.execute('''
        CREATE TABLE knowledge_graph_triples (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT,
            predicate TEXT,
            object TEXT,
            category TEXT,
            description TEXT
        )
    ''')

    # Data Insertions:
    # 1. 7단계
    steps_data = [
        ("step1_go", 1, "F", "Find the real problem", "1. F - Find real problem (顧)", "顧 (돌아볼 고)", "tag-soil", "표면적 요구 너머의 미충족 니즈(Unmet Needs) 파악", "미래역산법 1단계: 이해관계자 정의 및 진짜 문제 발견"),
        ("step2_bi", 2, "O", "Objective SMART", "2. O - Objective SMART (飛)", "飛 (날 비)", "tag-root", "SMART 5대 정량 상수로 확정 후 0/1 선택 역산", "미래역산법 2단계: 미래 목표상수 고정"),
        ("step3_gyeol", 3, "R", "Realize final outcome", "3. R - Realize outcome (結)", "結 (맺을 결)", "tag-fruit", "기획 초기 최종 산출물 형태와 KPI 잠정 결론 선제 정립", "미래역산법 3단계: 불필요 분석 소거 및 최단 속도 달성"),
        ("step4_jeon", 4, "W", "Work highest ground", "4. W - Work highest ground (前)", "前 (앞 전)", "tag-branch", "최고 성공사례 및 타 산업 벤치마킹 전진기지화", "미래역산법 4단계: 맨땅 헤딩 금지 및 시행착오 차단"),
        ("step5_ja", 5, "A", "Assemble 4M", "5. A - Assemble 4M (資)", "資 (재물 자)", "tag-nutrient", "4M 근육 및 외부/고수 지혜 자원 총집결", "미래역산법 5단계: 내 예산 한계를 넘어선 자원 농축 배분"),
        ("step6_yeok", 6, "R", "Reverse-test plan", "6. R - Reverse-test plan (逆)", "逆 (거스를 역)", "tag-storm", "'이 프로젝트가 실패한다면?' 사전 질문으로 맹점 수술", "미래역산법 6단계: 사전 실패 역분석 및 반대자 시각 흡수"),
        ("step7_haeng", 7, "D", "Deploy action 100-day", "7. D - Deploy 100-day (行)", "行 (다닐 행)", "tag-trunk", "첫 3개월 100일 마일스톤 및 정밀 실행", "미래역산법 7단계: 사전 저항 예방책 마련 및 100일 쾌속 집행")
    ]
    cursor.executemany("INSERT INTO backcasting_7steps VALUES (?,?,?,?,?,?,?,?,?)", steps_data)

    # 2. DSQ 온톨로지
    dsq_data = [
        ("DSQ_D", "D", "Direction (1/0 선택)", "Performance = D x S x Q 핵심 연산자", "1(Focus 100% 자원농축) / 0(Eliminate 비본질 배제)", 1.0, "목표 상수에 직결된 과제에 자원 농축, 불필요 낭비 0 차단"),
        ("DSQ_S", "S", "Speed (4M 자원농축)", "Performance = D x S x Q 성과 가속도", "내 예산 한계를 넘어 외부/고수 지혜 자원 집결", 1.0, "가용한 4M 자원(Man, Machine, Material, Method) 총동원"),
        ("DSQ_Q", "Q", "Quality (사전 질문 수술)", "Performance = D x S x Q 완성도 디테일", "'실패 원인은?' 역발상 사전 질의로 맹점 제거", 1.0, "기획 허점 사전에 선제 수술하여 실행 저항 제로화")
    ]
    cursor.executemany("INSERT INTO dsq_math_ontology VALUES (?,?,?,?,?,?,?)", dsq_data)

    # 3. 5대 로직 (5 bindings)
    axioms_data = [
        (1, "예측 (Predict)", "역산 (Backcast)", "미래 상수를 우선 고정해 거꾸로 역산", "불확실성 차단 및 정량 달성"),
        (2, "병렬 (Parallel)", "직렬 (Serial)", "1순위 핵심 과제 순차적 직렬 집행", "조직 마비 해소 및 쾌속 집행"),
        (3, "복잡 (Complex)", "단순 (Simple)", "1/0 이진 계산기 수준 단순 연산", "무한 연산 소거 및 빠른 결정"),
        (4, "우연 (Accidental)", "필연 (Causal)", "성공을 인과관계 구조로 통제", "재현 가능한 반복적 성과"),
        (5, "동시성 (Concurrent)", "순차적 (Sequential)", "첫 3개월 100일 마일스톤 순차 집행", "실행 저항 최소화")
    ]
    cursor.executemany("INSERT INTO problem_solving_5axioms VALUES (?,?,?,?,?)", axioms_data)

    # 4. SMART 온톨로지
    smart_data = [
        ("S", "Specific", "구체적 목표상수", "목표의 모호성을 제거하고 대상을 명확히 정의"),
        ("M", "Measurable", "측정가능 정량상수", "+35억 수지개선 등 0과 1로 검증 가능한 수치화"),
        ("A", "Achievable", "4M자원 달성가능", "외부/고수 자원 농축으로 달성 가능성 확보"),
        ("R", "Relevant", "사명부합 본질목표", "조직의 본질 사명에 직결된 핵심 과제 설정"),
        ("T", "Time-bound", "100일/시점 고정", "미래 시점(2029년) 및 첫 100일 마일스톤 고정")
    ]
    cursor.executemany("INSERT INTO drucker_smart_goals VALUES (?,?,?,?)", smart_data)

    # 5. 3축 메커니즘 온톨로지
    timeline_data = [
        ("axis_step1", "1단계 역산: 문제 해결 (Problem Solving)", "Future -> Present", "미래 상수로 현재 선택(0/1)과 DSQ 최적화 해갈", "불확실성 제로화 및 최적 성과"),
        ("axis_step2", "2단계 역산: 과거 피드백 학습 (Feedback Learning)", "Present -> Past", "현재 결과 데이터로 과거 원인 및 패턴 역추적", "인과 피드백 시스템 학습 완결"),
        ("axis_forward", "순방향 예측: 분석 마비 (Analysis Paralysis)", "Past -> Present -> Future", "과거/현재 한계에서 미래 순방향 예측", "경우의 수 2^n 폭발 ➔ 분석 마비")
    ]
    cursor.executemany("INSERT INTO timeline_3axis_mechanism VALUES (?,?,?,?,?)", timeline_data)

    # 6. RDF Knowledge Triples (20개 완전 전수 조인 노드)
    triples_data = [
        ("Future_Backcasting", "uses_methodology", "FORWARD_Acrostic_7Steps", "CORE", "미래역산법은 FORWARD 7자 및 顧飛結前資逆行 7단계를 사용"),
        ("Future_Backcasting", "defines_future_as", "Target_Goal_Constant_C_Goal", "CORE", "미래역산법은 미래를 측정가능한 목표상수로 우선 정의"),
        ("Target_Goal_Constant_C_Goal", "structured_by", "Drucker_SMART_5Principles", "SMART", "목표상수는 피터 드러커 SMART 5대 원칙으로 구조화"),
        ("Future_Backcasting", "solves_present_via", "Binary_Choice_01", "PROBLEM_SOLVING", "1단계 역산(Future->Present)은 현재 문제를 0/1 선택으로 해결"),
        ("Binary_Choice_1", "concentrates_resources_on", "Core_Mission", "CHOICE", "1(선택)은 본질 사명에 자원 100% 농축 투입"),
        ("Binary_Choice_0", "eliminates_waste_of", "Non_Essential_Inertia", "CHOICE", "0(배제)는 낭비성 관행 및 비본질 적자 요소 0 차단"),
        ("Future_Backcasting", "optimizes_performance_via", "DSQ_Equation", "OPTIMIZATION", "Performance = Direction(0/1) x Speed(4M) x Quality(Pre-mortem)"),
        ("DSQ_Direction", "executes_binary", "Choice_1_Focus_0_Eliminate", "OPTIMIZATION", "방향 최적화는 1 선택과 0 배제를 정밀 실행"),
        ("DSQ_Speed", "assembles_resources_via", "Assemble_4M_Resources", "OPTIMIZATION", "속도 최적화는 외부/고수 자원 4M 총집결"),
        ("DSQ_Quality", "eliminates_risks_via", "Reverse_Test_Pre_Mortem", "OPTIMIZATION", "완성도 최적화는 '실패원인 사전질문'으로 맹점 수술"),
        ("Present_Outcome", "traces_back_to", "Past_Causes", "LEARNING", "2단계 역산(Present->Past)은 현재 성과 결과로 과거 원인 역추적"),
        ("Learner_Agent", "completes_learning_via", "Causal_Feedback", "LEARNING", "현재 데이터 기반 과거 피드백 학습 완결"),
        ("Forward_Predictive_Model", "causes_exponential", "Quantum_Case_Explosion", "LIMITATION", "순방향 예측은 과거/현재 한계에서 무한 경우의 수 폭발"),
        ("Quantum_Case_Explosion", "triggers_state_of", "Analysis_Paralysis", "LIMITATION", "무한 경우의 수 폭발은 의사결정 정체 [분석 마비] 발생"),
        ("Future_Backcasting", "eliminates_risk_of", "Analysis_Paralysis", "CORE", "미래역산법으로 미래 상수를 고정하여 분석 마비를 완전 해소"),
        ("Problem_Solving_Logic", "shifts_predict_to", "Backcast", "AXIOM", "1대 전환: 불확실한 예측을 확정된 역산으로 전환"),
        ("Problem_Solving_Logic", "shifts_parallel_to", "Serial", "AXIOM", "2대 전환: 병렬적 혼란을 1순위 과제 직렬 집행으로 전환"),
        ("Problem_Solving_Logic", "shifts_complex_to", "Simple", "AXIOM", "3대 전환: 복잡성을 1/0 이진 계산기 단순 연산으로 전환"),
        ("Problem_Solving_Logic", "shifts_accidental_to", "Causal", "AXIOM", "4대 전환: 우연(운)을 통제된 인과관계 필연으로 전환"),
        ("Problem_Solving_Logic", "shifts_concurrent_to", "Sequential", "AXIOM", "5대 전환: 동시 집행을 100일 마일스톤 순차 집행으로 전환")
    ]
    cursor.executemany("INSERT INTO knowledge_graph_triples (subject, predicate, object, category, description) VALUES (?,?,?,?,?)", triples_data)

    conn.commit()
    conn.close()
    print(f"[SQLite Knowledge Graph 4.0] Full Ontologization Completed at: {DB_PATH}")

if __name__ == "__main__":
    init_db()
