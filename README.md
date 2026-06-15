# 여름방학 맞춤 운동 루틴 추천 앱

Streamlit 프론트엔드와 FastAPI 백엔드를 Docker Compose로 연결한 운동 루틴 추천 웹 애플리케이션입니다. 사용자가 운동 목적, 경험 수준, 운동 가능 횟수, 운동 장소, 어제 운동한 부위, 운동 가능 시간, 선호 운동 방식을 입력하면 FastAPI가 규칙 기반으로 오늘의 운동 루틴과 주간 계획을 JSON으로 반환하고 Streamlit이 화면에 표시합니다.

추천 로직은 입력 조합에 따라 운동 풀을 다르게 선택합니다. 예를 들어 집에서 처음 시작하는 사용자는 맨몸 전신 루틴을 받고, 헬스장에서 근비대를 목표로 하는 중급자는 등/하체 중심 분할 루틴을 받으며, 어제 전신을 운동한 사용자는 회복 루틴을 우선 추천받습니다.

이 앱은 일반적인 운동 루틴 추천을 제공하는 학습용 웹앱이며, 의학적 진단이나 치료 목적이 아닙니다. 통증, 질환, 부상 이력이 있는 경우 전문가와 상담해야 합니다.

## 기술 스택

- Frontend: Streamlit
- Backend: FastAPI, Pydantic
- HTTP Client: requests
- Container: Docker, Docker Compose
- Deployment target: AWS EC2

## 프로젝트 구조

```text
ds-roadmap-recommender/
├─ back/
│  ├─ main.py
│  ├─ model.py
│  ├─ recommender.py
│  ├─ requirements.txt
│  └─ Dockerfile
├─ front/
│  ├─ app.py
│  ├─ requirements.txt
│  └─ Dockerfile
├─ docker-compose.yml
└─ README.md
```

## 입력값 설명

- `fitness_goal`: 체력 향상, 근비대, 체지방 감량, 근력 향상, 자세 교정/건강 관리
- `experience_level`: 처음 시작, 초급자, 중급자, 상급자
- `days_per_week`: 2회, 3회, 4회, 5회 이상
- `workout_place`: 헬스장, 집, 야외, 기구 거의 없음
- `yesterday_workout`: 운동 안 함, 가슴, 등, 하체, 어깨, 팔, 전신, 유산소
- `available_time`: 30분 이하, 30~60분, 60~90분, 90분 이상
- `preference`: 기초부터 천천히, 짧고 효율적으로, 강도 높게, 체계적인 분할 루틴, 유산소와 근력 병행

## FastAPI 응답 JSON 예시

```json
{
  "user_type": "초급자을 위한 전신 루틴 추천형",
  "routine_type": "전신 3회 루틴",
  "main_recommendation": "운동 목적과 경험 수준, 장소, 운동 시간을 반영한 추천 설명입니다.",
  "today_focus": "오늘 추천 부위는 상체 또는 가벼운 유산소입니다.",
  "recommended_exercises": [
    {
      "name": "맨몸 스쿼트",
      "sets": "3세트",
      "reps": "8~12회",
      "rest": "60~90초",
      "description": "전신 활동량과 기본 체력을 함께 높이는 데 도움이 되는 운동입니다."
    }
  ],
  "weekly_plan": [
    "1일차: 전신 근력 또는 Push",
    "2일차: Pull 또는 전신 보완",
    "3일차: Legs + 코어 또는 가벼운 유산소"
  ],
  "intensity_guide": "RPE 기준으로 무리하지 않는 강도를 안내합니다.",
  "recovery_tip": "어제 운동한 부위와 오늘 운동 부위를 고려한 회복 팁입니다.",
  "caution": "일반적인 운동 안내이며 통증이나 부상 이력이 있으면 전문가와 상담해야 합니다.",
  "debug_info": {
    "selected_goal": "체력 향상",
    "selected_experience": "초급자",
    "selected_days": "3회",
    "selected_place": "집",
    "selected_yesterday": "운동 안 함",
    "selected_time": "30~60분",
    "selected_preference": "기초부터 천천히",
    "selected_exercise_pool": "beginner_fullbody",
    "selected_today_focus": "정상 루틴"
  }
}
```

## 로컬 실행 방법

```bash
docker compose down
docker compose up --build
```

실행 후 브라우저에서 접속합니다.

- Streamlit: http://localhost:8501
- FastAPI docs: http://localhost:8000/docs

## EC2 실행 방법

```bash
git clone https://github.com/IMHOGYUN/ds-roadmap-recommender.git
cd ds-roadmap-recommender
docker compose up --build -d
docker ps
```

AWS EC2 보안 그룹 인바운드 규칙에서 Streamlit 접속용 `8501` 포트를 허용한 뒤 접속합니다.

```text
http://EC2_PUBLIC_IP:8501
```

FastAPI 문서를 외부에서 확인하려면 `8000` 포트도 허용한 뒤 접속합니다.

```text
http://EC2_PUBLIC_IP:8000/docs
```
