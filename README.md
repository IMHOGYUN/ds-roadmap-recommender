# 여름방학 맞춤 운동 루틴 추천 앱

Streamlit 프론트엔드와 FastAPI 백엔드를 Docker Compose로 연결한 운동 루틴 추천 웹 애플리케이션입니다. 사용자가 추천 기능, 운동 목적, 경험 수준, 주당 운동 가능 횟수, 운동 장소, 어제 운동한 부위를 입력하면 FastAPI가 규칙 기반으로 오늘의 운동 루틴과 주간 계획을 JSON으로 반환하고 Streamlit이 화면에 표시합니다.

이 앱은 일반적인 운동 루틴 추천을 제공하는 학습용 웹앱이며, 의학적 진단이나 치료 목적이 아닙니다. 통증, 질환, 부상 이력이 있는 경우 전문가와 상담해야 합니다.

## 기술 스택

- Frontend: Streamlit
- Backend: FastAPI, Pydantic
- HTTP Client: requests
- Container: Docker, Docker Compose
- Deployment target: AWS EC2

## 주요 기능

- 처음 시작 루틴 추천
- 오늘 운동 부위 추천
- 주간 분할 루틴 추천
- 목적별 집중 루틴 추천
- 회복/스트레칭 루틴 추천

Streamlit은 추천을 직접 계산하지 않고 `/recommend` API에 요청을 보냅니다. 추천 로직은 FastAPI 백엔드의 `back/recommender.py`에서 처리합니다.

## 입력값

- `recommendation_mode`: 처음 시작 루틴 추천, 오늘 운동 부위 추천, 주간 분할 루틴 추천, 목적별 집중 루틴 추천, 회복/스트레칭 루틴 추천
- `fitness_goal`: 근비대 및 근력 향상, 체지방 감량
- `experience_level`: 처음 시작, 초급자, 중급자, 상급자
- `days_per_week`: 2회, 3회, 4회, 5회 이상
- `workout_place`: 헬스장, 집, 야외, 기구 거의 없음
- `yesterday_workout`: 운동 안 함, 가슴, 등, 하체, 어깨, 팔, 전신, 유산소

## FastAPI 응답 JSON 예시

```json
{
  "user_type": "중급자 오늘 부위 조절 루틴형",
  "routine_type": "오늘 등 중심 루틴",
  "main_recommendation": "오늘 운동 부위 추천 모드에서는 어제 운동한 부위인 가슴을 가장 중요하게 봅니다.",
  "today_focus": "오늘 추천 방향: 등 중심. 어제 가슴을 운동했으므로 오늘은 등 중심으로 균형을 맞춥니다.",
  "recommended_exercises": [
    {
      "name": "랫풀다운",
      "sets": "3-4세트",
      "reps": "8-12회",
      "rest": "60-90초",
      "description": "광배근과 등 너비를 만드는 운동입니다."
    }
  ],
  "weekly_plan": [
    "1일차: 상체 - 밀기와 당기기 균형",
    "2일차: 하체 - 스쿼트와 힌지 패턴"
  ],
  "intensity_guide": "RPE 7-8 기준으로 진행하세요.",
  "recovery_tip": "어제 운동 부위가 가슴이므로 오늘은 등 중심으로 피로를 분산합니다.",
  "caution": "이 앱은 일반적인 운동 루틴 추천을 제공하는 학습용 웹앱이며 의학적 진단이나 치료 목적이 아닙니다.",
  "debug_info": {
    "recommendation_mode": "오늘 운동 부위 추천",
    "selected_exercise_pool": "gym_hypertrophy_pull",
    "selected_today_focus": "등 중심",
    "place_rule": "헬스장 환경에 맞는 운동 풀 사용",
    "goal_rule": "근육량 증가와 힘 향상을 함께 노리는 근력 중심 구성",
    "level_rule": "점진적 과부하와 부위별 볼륨 관리",
    "days_rule": "주 4회 기준 주간 계획 생성"
  }
}
```

## 로컬 실행 방법

```bash
docker compose down --rmi all
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
