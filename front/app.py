import os
import requests
import streamlit as st

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.set_page_config(
    page_title="데이터사이언스 학습 로드맵 추천 앱",
    page_icon="📚",
    layout="centered",
)

st.title("📚 데이터사이언스 학습 로드맵 추천 앱")
st.write(
    "관심 분야와 학습 상황을 입력하면 FastAPI 서버가 맞춤형 학습 로드맵을 추천합니다."
)

with st.sidebar:
    st.header("서비스 연결 정보")
    st.caption("Streamlit 화면은 추천을 직접 계산하지 않고 FastAPI API를 호출합니다.")
    st.code(API_URL, language="text")

st.divider()

interest = st.selectbox(
    "관심 분야를 선택하세요",
    ["데이터분석", "AI", "백엔드", "클라우드", "웹개발"],
)

grade = st.selectbox(
    "현재 학년을 선택하세요",
    ["1학년", "2학년", "3학년", "4학년"],
)

difficulty = st.radio(
    "선호하는 난이도를 선택하세요",
    ["쉬움", "보통", "도전"],
    horizontal=True,
)

study_time = st.selectbox(
    "하루 평균 학습 시간을 선택하세요",
    ["1시간 미만", "1~2시간", "3시간 이상"],
)

goal = st.selectbox(
    "학습 목표를 선택하세요",
    ["취업 포트폴리오", "자격증", "프로젝트", "논문/연구"],
)

st.divider()

if st.button("추천 받기", type="primary"):
    payload = {
        "interest": interest,
        "grade": grade,
        "difficulty": difficulty,
        "study_time": study_time,
        "goal": goal,
    }

    try:
        with st.spinner("FastAPI 서버에 추천을 요청하는 중입니다..."):
            response = requests.post(f"{API_URL}/recommend", json=payload, timeout=10)

        if response.status_code == 200:
            result = response.json()

            st.success("추천 결과를 받았습니다!")

            st.subheader("추천 유형")
            st.info(result["user_type"])

            st.subheader("핵심 추천")
            st.write(result["main_recommendation"])

            st.subheader("추천 학습 기술")
            st.write(" · ".join(result["skills"]))

            st.subheader("추천 프로젝트")
            st.write(result["project_idea"])

            st.subheader("단계별 학습 계획")
            for step in result["study_plan"]:
                st.write(f"- {step}")

            st.subheader("주의할 점")
            st.warning(result["caution"])

            with st.expander("FastAPI에서 받은 원본 JSON 보기"):
                st.json(result)
        else:
            st.error(f"FastAPI 서버 오류: {response.status_code}")
            st.text(response.text)

    except requests.exceptions.RequestException as e:
        st.error("FastAPI 서버에 연결할 수 없습니다.")
        st.exception(e)
