def recommend(data):
    score = 0

    if data.difficulty == "도전":
        score += 2
    elif data.difficulty == "보통":
        score += 1

    if data.study_time == "3시간 이상":
        score += 2
    elif data.study_time == "1~2시간":
        score += 1

    if data.grade in ["3학년", "4학년"]:
        score += 1

    goal_tips = {
        "취업 포트폴리오": "GitHub에 결과물과 실행 방법을 정리해 포트폴리오로 보여주는 것을 목표로 잡으세요.",
        "자격증": "기초 개념을 정리하면서 작은 실습을 함께 진행하면 자격증 공부가 더 오래 남습니다.",
        "프로젝트": "처음부터 큰 서비스를 만들기보다 입력, 처리, 출력이 분명한 작은 프로젝트를 완성해 보세요.",
        "논문/연구": "데이터셋, 실험 조건, 평가 지표를 기록하면서 재현 가능한 형태로 공부하는 것이 좋습니다.",
    }

    level = "심화" if score >= 4 else "기초-응용" if score >= 2 else "기초"

    profiles = {
        "데이터분석": {
            "user_type": f"{level} 데이터 분석 로드맵형",
            "main_recommendation": "Python과 Pandas로 데이터를 정리하고, 시각화와 간단한 모델링까지 연결하는 학습 경로를 추천합니다.",
            "skills": ["Python", "Pandas", "Matplotlib", "Seaborn", "Scikit-learn", "Streamlit"],
            "project_idea": "공공데이터를 활용한 지역별 생활 지표 분석 대시보드 만들기",
            "study_plan": [
                "1단계: CSV 데이터를 불러오고 결측치와 이상치를 정리하기",
                "2단계: Pandas groupby와 pivot_table로 핵심 지표 만들기",
                "3단계: Matplotlib/Seaborn으로 비교 그래프 작성하기",
                "4단계: Streamlit 대시보드로 분석 결과를 설명하기",
            ],
            "caution": "그래프를 많이 만드는 것보다 사용자가 이해할 수 있는 질문과 결론을 먼저 정하는 것이 중요합니다.",
        },
        "AI": {
            "user_type": f"{level} AI 모델 실습형",
            "main_recommendation": "Python 기초를 다진 뒤 머신러닝, 딥러닝, HuggingFace 활용 순서로 학습하는 경로를 추천합니다.",
            "skills": ["Python", "Pandas", "Scikit-learn", "PyTorch", "HuggingFace"],
            "project_idea": "한국어 문장 데이터를 활용한 감정 분석 또는 주제 분류 서비스 만들기",
            "study_plan": [
                "1단계: Python 문법과 데이터 전처리 복습하기",
                "2단계: Scikit-learn으로 분류 모델 실습하기",
                "3단계: HuggingFace 모델로 텍스트 분류 실험하기",
                "4단계: FastAPI와 Streamlit으로 예측 결과 보여주기",
            ],
            "caution": "모델 성능만 보지 말고 데이터 전처리, 평가 지표, 오류 사례 분석을 함께 학습해야 합니다.",
        },
        "백엔드": {
            "user_type": f"{level} API 개발 성장형",
            "main_recommendation": "FastAPI의 라우팅, 요청 바디, 응답 JSON, 예외 처리를 중심으로 백엔드 기본기를 쌓는 경로를 추천합니다.",
            "skills": ["FastAPI", "Pydantic", "REST API", "Uvicorn", "Docker"],
            "project_idea": "사용자 입력을 받아 맞춤형 추천 결과를 JSON으로 반환하는 API 서버 만들기",
            "study_plan": [
                "1단계: GET/POST 요청과 HTTP 상태 코드 이해하기",
                "2단계: Pydantic 모델로 요청과 응답 구조 정의하기",
                "3단계: 추천 로직을 별도 함수로 분리하기",
                "4단계: Swagger 문서에서 API를 직접 테스트하기",
            ],
            "caution": "추천 결과를 프론트엔드에서 계산하지 않고 반드시 API 응답으로 받아오는 구조를 유지해야 합니다.",
        },
        "클라우드": {
            "user_type": f"{level} 클라우드 배포 실습형",
            "main_recommendation": "Linux 명령어, Docker, docker compose, AWS EC2 보안 그룹과 배포 흐름을 함께 학습하는 경로를 추천합니다.",
            "skills": ["Linux", "Git", "Docker", "Docker Compose", "AWS EC2", "FastAPI"],
            "project_idea": "FastAPI 추천 API와 Streamlit 화면을 Docker Compose로 EC2에 배포하기",
            "study_plan": [
                "1단계: Linux에서 프로젝트를 clone하고 파일 구조 확인하기",
                "2단계: Dockerfile을 작성하고 이미지를 빌드하기",
                "3단계: docker compose로 프론트엔드와 백엔드 컨테이너 실행하기",
                "4단계: EC2 보안 그룹에서 8501 포트를 열고 외부 접속 확인하기",
            ],
            "caution": "로컬 실행만으로는 과제 요구사항이 부족하므로 EC2 public 주소에서 Streamlit 접속이 되는 장면을 확인해야 합니다.",
        },
        "프론트엔드": {
            "user_type": f"{level} 사용자 인터페이스 구현형",
            "main_recommendation": "Streamlit으로 입력 화면과 결과 화면을 구성하고, API 응답을 사용자가 이해하기 쉽게 보여주는 경로를 추천합니다.",
            "skills": ["Streamlit", "Requests", "UI 구성", "API 연동", "Docker"],
            "project_idea": "관심 분야와 학습 목표에 따라 학습 카드와 단계별 계획을 보여주는 추천 웹 앱 만들기",
            "study_plan": [
                "1단계: selectbox, radio, button 등 입력 위젯 익히기",
                "2단계: requests.post로 FastAPI 추천 엔드포인트 호출하기",
                "3단계: JSON 응답을 카드, 리스트, expander로 보기 좋게 출력하기",
                "4단계: 오류 상황에서도 안내 메시지가 나오도록 처리하기",
            ],
            "caution": "화면 디자인보다 중요한 것은 Streamlit이 FastAPI와 실제로 통신한다는 점을 명확히 보여주는 것입니다.",
        },
    }

    result = profiles.get(data.interest, profiles["데이터분석"]).copy()
    result["study_plan"] = result["study_plan"] + [f"목표 보완: {goal_tips.get(data.goal, '학습 목표에 맞게 결과물을 정리하세요')}"]
    return result
