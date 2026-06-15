import os

import requests
import streamlit as st

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.set_page_config(
    page_title="여름방학 맞춤 운동 루틴 추천 앱",
    page_icon="🏋️",
    layout="centered",
)

st.title("🏋️ 여름방학 맞춤 운동 루틴 추천 앱")
st.write(
    "운동 목적, 경험 수준, 운동 장소, 어제 운동한 부위를 입력하면 "
    "FastAPI 서버가 오늘의 운동 루틴과 주간 계획을 추천합니다."
)

with st.sidebar:
    st.header("서비스 연결 정보")
    st.caption("Streamlit 화면은 추천을 직접 계산하지 않고 FastAPI API를 호출합니다.")
    st.code(API_URL, language="text")

st.divider()

fitness_goal = st.selectbox(
    "운동 목적을 선택하세요",
    ["체력 향상", "근비대", "체지방 감량", "근력 향상", "자세 교정/건강 관리"],
)

experience_level = st.radio(
    "운동 경험을 선택하세요",
    ["처음 시작", "초급자", "중급자", "상급자"],
    horizontal=True,
)

days_per_week = st.selectbox(
    "주당 운동 가능 횟수를 선택하세요",
    ["2회", "3회", "4회", "5회 이상"],
)

workout_place = st.selectbox(
    "운동 장소를 선택하세요",
    ["헬스장", "집", "야외", "기구 거의 없음"],
)

yesterday_workout = st.selectbox(
    "어제 운동한 부위를 선택하세요",
    ["운동 안 함", "가슴", "등", "하체", "어깨", "팔", "전신", "유산소"],
)

available_time = st.radio(
    "1회 운동 가능 시간을 선택하세요",
    ["30분 이하", "30~60분", "60~90분", "90분 이상"],
    horizontal=True,
)

preference = st.selectbox(
    "선호 운동 방식을 선택하세요",
    ["기초부터 천천히", "짧고 효율적으로", "강도 높게", "체계적인 분할 루틴", "유산소와 근력 병행"],
)

st.divider()

if st.button("운동 루틴 추천 받기", type="primary"):
    payload = {
        "fitness_goal": fitness_goal,
        "experience_level": experience_level,
        "days_per_week": days_per_week,
        "workout_place": workout_place,
        "yesterday_workout": yesterday_workout,
        "available_time": available_time,
        "preference": preference,
    }

    try:
        with st.spinner("FastAPI 서버에 운동 루틴 추천을 요청하는 중입니다..."):
            response = requests.post(f"{API_URL}/recommend", json=payload, timeout=10)

        if response.status_code == 200:
            result = response.json()

            st.success("운동 루틴 추천 결과를 받았습니다!")

            st.subheader("추천 유형")
            st.info(result["user_type"])

            st.subheader("추천 루틴 방식")
            st.write(result["routine_type"])

            st.subheader("핵심 추천")
            st.info(result["main_recommendation"])

            st.subheader("오늘 추천 운동 부위")
            st.write(result["today_focus"])

            st.subheader("오늘의 운동 루틴")
            for exercise in result["recommended_exercises"]:
                with st.container(border=True):
                    st.subheader(exercise["name"])
                    st.write(f"세트: {exercise['sets']}")
                    st.write(f"반복: {exercise['reps']}")
                    st.write(f"휴식: {exercise['rest']}")
                    st.caption(exercise["description"])

            st.subheader("주간 운동 계획")
            for idx, plan in enumerate(result["weekly_plan"], start=1):
                st.write(f"{idx}. {plan}")

            st.subheader("강도 조절 가이드")
            st.write(result["intensity_guide"])

            st.subheader("회복 팁")
            st.write(result["recovery_tip"])

            st.subheader("주의사항")
            st.warning(result["caution"])

            with st.expander("전송한 입력값 보기"):
                st.json(payload)

            with st.expander("FastAPI에서 받은 원본 JSON 보기"):
                st.json(result)
        else:
            st.error(f"FastAPI 서버 오류: {response.status_code}")
            st.text(response.text)

    except requests.exceptions.RequestException as e:
        st.error("FastAPI 서버에 연결할 수 없습니다.")
        st.exception(e)
