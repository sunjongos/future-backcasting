import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "future_backcasting.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS backcasting_nodes')
    cursor.execute('DROP TABLE IF EXISTS problem_solving_and_learning')
    cursor.execute('DROP TABLE IF EXISTS dsq_optimization_rules')

    # 1. 7단계 온톨로지 테이블
    cursor.execute('''
        CREATE TABLE backcasting_nodes (
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

    # 2. 문제해결 & 피드백 학습 온톨로지 테이블
    cursor.execute('''
        CREATE TABLE problem_solving_and_learning (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            stage_name TEXT,
            vector_direction TEXT,
            core_definition TEXT,
            methodology TEXT,
            outcome TEXT
        )
    ''')

    # 3. DSQ 최적화 수리 규칙 테이블
    cursor.execute('''
        CREATE TABLE dsq_optimization_rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            axis_name TEXT,
            weight REAL,
            formula TEXT,
            description TEXT
        )
    ''')

    nodes_data = [
        ("step1_go", 1, "F", "Find the real problem", "1. F - Find the real problem (顧)", "顧 (돌아볼 고)", "tag-soil", "표면적 요구 너머의 미충족 니즈(Unmet Needs) 파악", "미래역산법 1단계: 이해관계자 정의 및 진짜 문제 발견"),
        ("step2_bi", 2, "O", "Objective definition via SMART", "2. O - Objective definition via SMART (飛)", "飛 (날 비)", "tag-root", "Specific, Measurable, Achievable, Relevant, Time-bound 확정", "미래역산법 2단계: SMART 상수로 확정 후 0/1 선택 역산"),
        ("step3_gyeol", 3, "R", "Realize final outcome", "3. R - Realize final outcome (結)", "結 (맺을 결)", "tag-fruit", "기획 초기 최종 산출물 형태와 KPI 잠정 결론 선제 정립", "미래역산법 3단계: 불필요 분석 소거 및 최단 속도 달성"),
        ("step4_jeon", 4, "W", "Work from highest ground", "4. W - Work from highest ground (前)", "前 (앞 전)", "tag-branch", "최고 성공사례 및 타 산업 벤치마킹 전진기지화", "미래역산법 4단계: 맨땅 헤딩 금지 및 시행착오 차단"),
        ("step5_ja", 5, "A", "Assemble all resources", "5. A - Assemble all resources (資)", "資 (재물 자)", "tag-nutrient", "4M 근육 및 외부/고수 지혜 자원 총집결", "미래역산법 5단계: 내 예산 한계를 넘어선 자원 농축 배분"),
        ("step6_yeok", 6, "R", "Reverse-test your plan", "6. R - Reverse-test your plan (逆)", "逆 (거스를 역)", "tag-storm", "'이 프로젝트가 실패한다면?' 사전 질문으로 맹점 수술", "미래역산법 6단계: 사전 실패 역분석 및 반대자 시각 흡수"),
        ("step7_haeng", 7, "D", "Deploy action plan", "7. D - Deploy action plan with 100-day (行)", "行 (다닐 행)", "tag-trunk", "첫 3개월 100일 마일스톤 및 정밀 실행", "미래역산법 7단계: 사전 저항 예방책 마련 및 100일 쾌속 집행")
    ]

    cursor.executemany('''
        INSERT INTO backcasting_nodes (id, step_order, acrostic_letter, code_name, korean_name, hanja_name, tag_class, summary, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', nodes_data)

    ps_learning_data = [
        ("1단계 역산: 문제 해결 (Problem Solving)", "Future -> Present", "미래 상수를 결정하여 현재의 문제를 해결하는 과정", "0/1 이진 선택 (Focus 1 / Eliminate 0) & DSQ 최적화", "불확실성 차단 및 최적 성과 달성"),
        ("2단계 역산: 학습 (Feedback Learning)", "Present -> Past", "현재의 도출된 결과를 가지고 과거를 역산하여 학습하는 과정", "과거 원인, 실패 패턴, 인과 관계 역추적 피드백", "인과관계 통제 및 시스템 학습 완결"),
        ("순방향 예측: 분석 마비 (Analysis Paralysis)", "Past -> Future", "과거 한계에서 미래를 예측할 때 경우의 수가 폭발하는 과정", "기하급수적 경우의 수 팽창 및 의사결정 정체", "미래역산법을 통한 무한 경우의 수 차단 필요")
    ]

    cursor.executemany('''
        INSERT INTO problem_solving_and_learning (stage_name, vector_direction, core_definition, methodology, outcome)
        VALUES (?, ?, ?, ?, ?)
    ''', ps_learning_data)

    dsq_rules = [
        ("D_Direction", 1.0, "Focus(1) / Eliminate(0)", "사명에 직결된 핵심 과제 선택 및 비본질 배제"),
        ("S_Speed", 1.0, "Assemble 4M Resources", "내 예산 한계를 넘어 외부/고수 자원 총동원 쾌속 실행"),
        ("Q_Quality", 1.0, "Reverse Failure Test", "'실패 이유' 사전 질문으로 리스크 맹점 완벽 제거")
    ]

    cursor.executemany('''
        INSERT INTO dsq_optimization_rules (axis_name, weight, formula, description)
        VALUES (?, ?, ?, ?)
    ''', dsq_rules)

    conn.commit()
    conn.close()
    print(f"[SQLite Ontology] Successfully initialized Future Backcasting DB at: {DB_PATH}")

def get_all_nodes():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM backcasting_nodes ORDER BY step_order ASC')
    rows = cursor.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    init_db()
