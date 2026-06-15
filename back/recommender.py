INTEREST_PROFILES = {
    "데이터분석": {
        "field_label": "데이터분석",
        "focus": "데이터 수집, 정제, 시각화, 간단한 예측 모델링",
        "skills": ["Python", "Pandas", "Matplotlib", "Seaborn", "Scikit-learn", "Streamlit"],
        "base_project": "공공데이터를 활용한 생활 지표 분석 대시보드",
        "practice": "CSV 데이터를 정리하고 핵심 지표를 그래프로 설명하는 실습",
    },
    "AI": {
        "field_label": "AI",
        "focus": "머신러닝 모델링, 딥러닝 기초, HuggingFace 모델 활용",
        "skills": ["Python", "Pandas", "Scikit-learn", "PyTorch", "HuggingFace", "FastAPI"],
        "base_project": "한국어 문장 감정 분석 또는 주제 분류 서비스",
        "practice": "데이터 전처리부터 모델 학습, 평가, 예측 API 제공까지 연결하는 실습",
    },
    "백엔드": {
        "field_label": "백엔드",
        "focus": "REST API 설계, 요청/응답 모델링, 데이터 처리, 서버 실행",
        "skills": ["Python", "FastAPI", "Pydantic", "REST API", "Uvicorn", "Docker"],
        "base_project": "사용자 입력을 받아 맞춤형 결과를 반환하는 추천 API 서버",
        "practice": "Pydantic 모델과 라우터를 분리하고 Swagger 문서로 검증하는 실습",
    },
    "클라우드": {
        "field_label": "클라우드",
        "focus": "Linux 명령어, Docker 컨테이너, Docker Compose, AWS EC2 배포",
        "skills": ["Linux", "Git", "Docker", "Docker Compose", "AWS EC2", "Nginx"],
        "base_project": "Docker Compose 기반 웹 서비스를 AWS EC2에 배포하는 프로젝트",
        "practice": "EC2 보안 그룹, 포트 설정, 컨테이너 로그 확인까지 포함한 배포 실습",
    },
    "웹개발": {
        "field_label": "웹개발",
        "focus": "사용자 입력 화면, API 연동, 결과 화면 구성, 배포 가능한 웹 UI",
        "skills": ["Streamlit", "Requests", "HTML/CSS 기초", "FastAPI 연동", "Docker"],
        "base_project": "사용자 선택값에 따라 결과 카드가 바뀌는 인터랙티브 추천 웹앱",
        "practice": "입력 위젯, 버튼 이벤트, API 응답 출력, 오류 메시지 처리를 연결하는 실습",
    },
}

GRADE_PROFILES = {
    "1학년": {
        "label": "1학년",
        "depth": "기초 개념과 쉬운 실습 중심",
        "step_style": "용어와 기본 흐름을 먼저 익히고 작은 예제를 따라 만드는 방식",
        "output": "짧은 실습 기록과 개념 정리 노트",
    },
    "2학년": {
        "label": "2학년",
        "depth": "전공 기초와 작은 프로젝트 중심",
        "step_style": "핵심 개념을 익힌 뒤 기능이 분명한 미니 프로젝트로 연결하는 방식",
        "output": "작동하는 미니 프로젝트와 간단한 README",
    },
    "3학년": {
        "label": "3학년",
        "depth": "실전 프로젝트와 배포/모델링 중심",
        "step_style": "실제 데이터나 API를 사용해 결과물을 만들고 배포까지 경험하는 방식",
        "output": "배포 가능한 프로젝트와 실험/개발 기록",
    },
    "4학년": {
        "label": "4학년",
        "depth": "포트폴리오 완성과 취업/연구 산출물 중심",
        "step_style": "완성도, 문서화, 재현성, 발표 가능성을 높이는 방식",
        "output": "제출 가능한 포트폴리오, 연구 요약, 또는 면접 설명 자료",
    },
}

DIFFICULTY_PROFILES = {
    "쉬움": {
        "label": "기초 로드맵형",
        "intensity": "부담을 줄이고 핵심 개념을 천천히 쌓는 학습 강도",
        "action": "예제를 따라 하며 개념을 확인",
    },
    "보통": {
        "label": "기초-응용 연결형",
        "intensity": "개념 학습과 직접 구현을 균형 있게 섞는 학습 강도",
        "action": "개념을 익힌 뒤 작은 기능으로 응용",
    },
    "도전": {
        "label": "심화 실전형",
        "intensity": "프로젝트 완성도와 실제 활용 가능성을 함께 높이는 학습 강도",
        "action": "직접 설계하고 개선하며 결과물을 확장",
    },
}

TIME_PROFILES = {
    "1시간 미만": {
        "pace": "짧은 실습과 핵심 개념 위주",
        "volume": "하루 30~50분 단위로 쪼개서 진행",
        "extra": "큰 기능보다 매일 하나의 개념이나 작은 예제를 끝내는 데 집중하세요.",
    },
    "1~2시간": {
        "pace": "개념과 실습의 균형 중심",
        "volume": "하루 한 개념과 한 가지 구현 과제를 함께 진행",
        "extra": "개념 정리와 코드 실습을 같은 날에 연결하면 학습 흐름이 안정적입니다.",
    },
    "3시간 이상": {
        "pace": "프로젝트 확장, 배포, 문서화까지 포함",
        "volume": "하루 학습을 개념, 구현, 개선, 기록으로 나누어 진행",
        "extra": "기능 추가와 함께 README, 실행 방법, 결과 해석까지 정리해 완성도를 높이세요.",
    },
}

GOAL_PROFILES = {
    "취업 포트폴리오": {
        "label": "포트폴리오 로드맵",
        "main_focus": "GitHub에 설명 가능한 결과물을 남기고 README, 실행 방법, 배포 주소까지 정리하는 방향",
        "project_suffix": "를 GitHub 포트폴리오로 정리하고 EC2 또는 Streamlit 화면에서 시연 가능하게 만들기",
        "plan_focus": [
            "GitHub 저장소 구조를 정리하고 README에 문제 정의와 실행 방법 작성하기",
            "핵심 기능이 한눈에 보이도록 화면, API, 결과 예시를 연결하기",
            "Docker 또는 배포 주소를 포함해 다른 사람이 실행할 수 있는 형태로 마무리하기",
        ],
        "caution": "기능을 많이 넣는 것보다 문제 정의, 실행 방법, 결과 화면, 본인이 맡은 구현 포인트를 명확히 설명하는 것이 중요합니다.",
    },
    "자격증": {
        "label": "자격증 대비 로드맵",
        "main_focus": "개념 정리, 용어 암기, 기출 문제 반복, 작은 실습을 함께 진행하는 방향",
        "project_suffix": "를 자격증 개념 정리 노트와 실습 예제로 나누어 정리하기",
        "plan_focus": [
            "출제 가능성이 높은 핵심 용어와 개념을 표로 정리하기",
            "기출 문제나 예상 문제를 풀며 틀린 개념을 다시 실습으로 확인하기",
            "반복 학습할 수 있도록 요약 노트와 체크리스트 만들기",
        ],
        "caution": "자격증 준비에서는 멋진 프로젝트보다 정확한 용어 이해와 반복 복습이 중요하므로, 실습은 개념을 확인하는 크기로 유지하세요.",
    },
    "프로젝트": {
        "label": "프로젝트 완성 로드맵",
        "main_focus": "기능 구현, API 연결, 화면 구성, 오류 처리, 완성도 있는 흐름을 만드는 방향",
        "project_suffix": "를 입력, 처리, 결과 출력이 분명한 완성형 미니 서비스로 만들기",
        "plan_focus": [
            "사용자 입력, 처리 로직, 결과 출력 흐름을 먼저 설계하기",
            "핵심 기능을 구현한 뒤 예외 처리와 빈 화면 안내를 추가하기",
            "사용자가 실제로 눌러보며 이해할 수 있도록 화면 구성과 결과 문구 다듬기",
        ],
        "caution": "프로젝트 목표라면 주제만 넓히지 말고 사용자가 처음부터 끝까지 완주할 수 있는 기능 흐름을 우선 완성해야 합니다.",
    },
    "논문/연구": {
        "label": "연구 실험 로드맵",
        "main_focus": "데이터셋 선정, 실험 설계, 평가 지표, 결과 해석을 중심으로 재현 가능한 학습을 하는 방향",
        "project_suffix": "를 데이터셋, 실험 조건, 평가 지표, 결과 해석이 포함된 연구형 실험으로 확장하기",
        "plan_focus": [
            "사용할 데이터셋과 비교 기준을 정하고 실험 질문을 명확히 쓰기",
            "평가 지표와 실험 조건을 고정해 결과를 재현할 수 있게 만들기",
            "성공 사례뿐 아니라 실패 사례와 한계까지 정리해 결과를 해석하기",
        ],
        "caution": "연구 목적에서는 결과가 좋아 보이는 것보다 데이터, 조건, 평가 방식이 일관되고 재현 가능하게 기록되는지가 더 중요합니다.",
    },
}


def _get_profile(table, key, default_key):
    return table.get(key, table[default_key])


def recommend(data):
    interest = data.interest
    grade = data.grade
    difficulty = data.difficulty
    study_time = data.study_time
    goal = data.goal

    interest_profile = _get_profile(INTEREST_PROFILES, interest, "데이터분석")
    grade_profile = _get_profile(GRADE_PROFILES, grade, "1학년")
    difficulty_profile = _get_profile(DIFFICULTY_PROFILES, difficulty, "쉬움")
    time_profile = _get_profile(TIME_PROFILES, study_time, "1시간 미만")
    goal_profile = _get_profile(GOAL_PROFILES, goal, "프로젝트")

    field_label = interest_profile["field_label"]
    user_type = (
        f"{grade_profile['label']} {difficulty_profile['label']} "
        f"{field_label} {goal_profile['label']}"
    )

    main_recommendation = (
        f"{field_label} 분야를 선택했으므로 {interest_profile['focus']}을 중심으로 학습하는 것이 좋습니다. "
        f"현재 {grade_profile['label']} 단계에는 {grade_profile['depth']}이 적합하고, "
        f"난이도는 '{difficulty}'을 선택했기 때문에 {difficulty_profile['intensity']}로 진행합니다. "
        f"하루 학습 시간이 '{study_time}'이므로 {time_profile['pace']}로 계획을 잡고, "
        f"학습 목표가 '{goal}'인 만큼 {goal_profile['main_focus']}으로 결과물을 만들어 보세요."
    )

    project_idea = (
        f"{interest_profile['base_project']}{goal_profile['project_suffix']}. "
        f"이 프로젝트는 {interest_profile['practice']}을 포함하고, 최종 산출물은 "
        f"{grade_profile['output']} 형태로 정리하는 것을 추천합니다."
    )

    study_plan = [
        (
            f"1단계: {grade_profile['step_style']}으로 시작하세요. "
            f"{field_label} 분야의 핵심 주제인 {interest_profile['focus']}을 먼저 작은 예제로 확인합니다."
        ),
        (
            f"2단계: '{difficulty}' 난이도에 맞춰 {difficulty_profile['action']}합니다. "
            f"이때 {', '.join(interest_profile['skills'][:3])}을 우선 사용해 기본 흐름을 익힙니다."
        ),
        (
            f"3단계: 하루 학습 시간 '{study_time}'에 맞게 {time_profile['volume']}합니다. "
            f"{time_profile['extra']}"
        ),
        (
            f"4단계: 목표가 '{goal}'이므로 {goal_profile['plan_focus'][0]} "
            f"그다음 {goal_profile['plan_focus'][1]}"
        ),
        (
            f"5단계: 마무리 단계에서는 {goal_profile['plan_focus'][2]} "
            f"최종 결과는 {grade_profile['output']}로 정리하세요."
        ),
    ]

    caution = (
        f"{goal_profile['caution']} 또한 {grade_profile['label']} 학습자는 {grade_profile['depth']}이라는 점을 고려해야 합니다. "
        f"'{study_time}' 학습 시간을 선택했다면 무리하게 범위를 넓히기보다 {time_profile['pace']}라는 원칙을 지키는 것이 좋습니다."
    )

    return {
        "user_type": user_type,
        "main_recommendation": main_recommendation,
        "skills": interest_profile["skills"],
        "project_idea": project_idea,
        "study_plan": study_plan,
        "caution": caution,
    }
