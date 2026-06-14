# 데이터사이언스 학습 로드맵 추천 앱

Streamlit 프론트엔드와 FastAPI 백엔드를 Docker Compose로 연결한 추천 웹 애플리케이션입니다. 사용자가 관심 분야, 학년, 선호 난이도, 학습 시간, 목표를 입력하면 FastAPI가 규칙 기반 추천 결과를 JSON으로 반환하고 Streamlit이 화면에 표시합니다.

## 프로젝트 구조

```text
ds-roadmap-recommender/
├─ back/
│  ├─ main.py              # FastAPI 앱과 /recommend API
│  ├─ model.py             # 요청/응답 Pydantic 모델
│  ├─ recommender.py       # 추천 로직
│  ├─ requirements.txt
│  └─ Dockerfile
├─ front/
│  ├─ app.py               # Streamlit 화면과 FastAPI 호출
│  ├─ requirements.txt
│  └─ Dockerfile
├─ docker-compose.yml
├─ .gitignore
└─ README.md
```

## 주요 기능

- Streamlit에서 사용자 입력 받기
- `requests.post()`로 FastAPI `/recommend` 엔드포인트 호출
- FastAPI에서 입력값을 바탕으로 추천 유형, 기술, 프로젝트, 학습 계획 생성
- 추천 결과를 JSON으로 반환
- Docker Compose로 프론트엔드와 백엔드를 각각 다른 컨테이너로 실행

## 로컬 실행 방법

```bash
docker compose up --build
```

실행 후 브라우저에서 접속합니다.

- Streamlit: http://localhost:8501
- FastAPI 문서: http://localhost:8000/docs

## EC2 실행 방법

1. EC2 인스턴스에 Docker와 Docker Compose를 설치합니다.
2. GitHub 저장소를 clone합니다.
3. 프로젝트 폴더로 이동합니다.
4. 다음 명령어를 실행합니다.

```bash
docker compose up --build -d
```

5. 실행 상태를 확인합니다.

```bash
docker ps
```

6. EC2 보안 그룹 인바운드 규칙에서 Streamlit 접속용 `8501` 포트를 허용합니다.
7. 브라우저에서 아래 주소로 접속합니다.

```text
http://EC2_PUBLIC_IP:8501
```

FastAPI는 Docker 내부 네트워크에서 `http://backend:8000` 주소로 Streamlit과 연결됩니다. 외부에서 API 문서까지 확인하려면 보안 그룹에서 `8000` 포트도 허용한 뒤 `http://EC2_PUBLIC_IP:8000/docs`로 접속할 수 있습니다.

## 데모 영상 체크리스트

- EC2 public 주소로 Streamlit 앱 접속
- 입력 항목 선택
- `추천 받기` 버튼 클릭
- 추천 결과 표시 확인
- `FastAPI에서 받은 원본 JSON 보기` expander로 API 응답 확인
- EC2 터미널에서 `docker ps` 실행 상태 확인
- 필요하면 FastAPI 문서 `/docs` 또는 로그로 백엔드 연결 확인
