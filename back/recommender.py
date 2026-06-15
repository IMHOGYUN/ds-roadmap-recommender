GOAL_PROFILES = {
    "체력 향상": {
        "focus": "전신 근력과 유산소를 함께 늘리는 방향",
        "routine_hint": "전신 루틴",
        "exercise_style": "서킷, 걷기, 가벼운 인터벌, 코어 운동",
        "caution": "처음부터 숨이 턱 막히는 강도보다 대화가 가능한 강도에서 꾸준히 반복하는 것이 좋습니다.",
    },
    "근비대": {
        "focus": "8~12회 반복과 부위별 운동량을 활용해 근육 성장을 노리는 방향",
        "routine_hint": "분할 루틴",
        "exercise_style": "복합 운동과 보조 운동을 조합한 점진적 과부하",
        "caution": "무게를 빠르게 올리기보다 같은 자세로 반복 수와 세트를 안정적으로 채운 뒤 조금씩 증량하세요.",
    },
    "체지방 감량": {
        "focus": "큰 근육 근력 운동과 유산소를 병행해 활동량을 높이는 방향",
        "routine_hint": "체지방 감량 순환 루틴",
        "exercise_style": "짧은 휴식, 전신 순환 운동, 걷기나 조깅",
        "caution": "식단을 극단적으로 제한하기보다 수면, 활동량, 규칙적인 식사를 함께 관리하는 것이 좋습니다.",
    },
    "근력 향상": {
        "focus": "스쿼트, 프레스, 로우 같은 복합 다관절 운동의 힘을 키우는 방향",
        "routine_hint": "근력 중심 루틴",
        "exercise_style": "낮은 반복 수, 충분한 휴식, 정확한 자세",
        "caution": "고중량은 자세가 안정된 뒤에 다뤄야 하며, 초보자는 무리한 1회 최대 중량 테스트를 피하세요.",
    },
    "자세 교정/건강 관리": {
        "focus": "코어, 둔근, 등, 가동성, 스트레칭을 통해 몸의 균형을 회복하는 방향",
        "routine_hint": "건강 관리 회복 루틴",
        "exercise_style": "가동성, 코어 안정화, 가벼운 등/둔근 운동",
        "caution": "통증이 있거나 부상 이력이 있다면 운동 강도를 낮추고 전문가 상담을 우선하세요.",
    },
}

EXPERIENCE_PROFILES = {
    "처음 시작": {
        "label": "운동 처음 시작자",
        "default_routine": "전신 기초 루틴",
        "guide": "운동 습관 형성, 자세 익히기, 무리하지 않기",
        "rpe": "RPE 5~6 정도로 여유를 남기고 마무리하세요.",
    },
    "초급자": {
        "label": "초급자",
        "default_routine": "전신 루틴 또는 상하체 2분할",
        "guide": "스쿼트, 힌지, 푸시, 풀, 코어 패턴을 반복 가능한 루틴으로 익히기",
        "rpe": "RPE 6~7 정도로 마지막 2~4회는 힘들지만 자세가 무너지지 않게 진행하세요.",
    },
    "중급자": {
        "label": "중급자",
        "default_routine": "상하체 2분할 또는 Push/Pull/Legs 3분할",
        "guide": "운동 볼륨과 점진적 과부하를 기록하며 부위별 자극을 구체화하기",
        "rpe": "RPE 7~8 정도로 주요 운동은 집중해서 수행하고 보조 운동은 안정적으로 볼륨을 채우세요.",
    },
    "상급자": {
        "label": "상급자",
        "default_routine": "3분할 또는 4분할 고강도 루틴",
        "guide": "약점 부위 보완, 볼륨 관리, 회복 전략까지 함께 설계하기",
        "rpe": "RPE 8 이상도 가능하지만 모든 세트를 한계까지 밀기보다 고강도일수록 회복일을 계획하세요.",
    },
}

TIME_PROFILES = {
    "30분 이하": {
        "sets": "2~3세트",
        "reps": "10~15회",
        "rest": "30~60초",
        "pace": "짧은 시간 안에 핵심 운동만 고르는 압축 루틴",
    },
    "30~60분": {
        "sets": "3세트",
        "reps": "8~12회",
        "rest": "60~90초",
        "pace": "준비 운동, 본운동, 마무리 운동을 균형 있게 넣는 표준 루틴",
    },
    "60~90분": {
        "sets": "3~4세트",
        "reps": "8~12회",
        "rest": "60~120초",
        "pace": "주요 운동과 보조 운동을 충분히 구성하는 확장 루틴",
    },
    "90분 이상": {
        "sets": "4~5세트",
        "reps": "3~10회",
        "rest": "90~180초",
        "pace": "고강도 복합 운동, 보조 운동, 회복 운동까지 포함하는 긴 루틴",
    },
}

PLACE_EXERCISES = {
    "헬스장": {
        "push": ["벤치프레스", "덤벨 숄더프레스", "케이블 푸시다운"],
        "pull": ["랫풀다운", "케이블 로우", "페이스풀"],
        "legs": ["스쿼트", "레그프레스", "레그컬"],
        "core": ["케이블 크런치", "플랭크"],
        "cardio": ["트레드밀 빠르게 걷기", "사이클 인터벌"],
    },
    "집": {
        "push": ["무릎 푸시업", "푸시업", "파이크 푸시업"],
        "pull": ["밴드 로우", "슈퍼맨", "수건 로우"],
        "legs": ["맨몸 스쿼트", "런지", "힙브릿지"],
        "core": ["버드독", "데드버그", "플랭크"],
        "cardio": ["제자리 걷기", "마운틴 클라이머"],
    },
    "야외": {
        "push": ["벤치 딥스", "인클라인 푸시업"],
        "pull": ["철봉 매달리기", "철봉 보조 풀업"],
        "legs": ["계단 오르기", "워킹 런지", "스텝업"],
        "core": ["플랭크", "사이드 플랭크"],
        "cardio": ["빠르게 걷기", "인터벌 조깅"],
    },
    "기구 거의 없음": {
        "push": ["벽 푸시업", "무릎 푸시업"],
        "pull": ["슈퍼맨", "엎드려 Y 레이즈"],
        "legs": ["의자 스쿼트", "스플릿 스쿼트", "힙브릿지"],
        "core": ["버드독", "데드버그", "플랭크"],
        "cardio": ["제자리 걷기", "팔 벌려 뛰기 낮은 강도"],
    },
}

BODY_PART_GUIDE = {
    "운동 안 함": ("전신", "어제 운동을 쉬었으므로 목적과 경험 수준에 맞춘 정상 루틴을 진행해도 좋습니다."),
    "가슴": ("등 또는 하체", "어제 가슴을 사용했으므로 오늘은 당기는 동작이나 하체 중심으로 균형을 맞추는 것이 좋습니다."),
    "등": ("가슴/어깨 또는 하체", "어제 등을 사용했으므로 오늘은 밀기 동작이나 하체 운동으로 피로 부위를 분산하세요."),
    "하체": ("상체 또는 가벼운 유산소", "어제 하체 피로가 남아 있을 수 있으므로 상체와 코어 중심으로 진행하세요."),
    "어깨": ("하체 또는 등", "어깨 관절 피로를 줄이기 위해 하체나 가벼운 등 운동을 추천합니다."),
    "팔": ("하체 또는 전신 가벼운 루틴", "팔 보조근 피로를 고려해 하체와 코어 중심으로 부담을 낮추세요."),
    "전신": ("회복 루틴", "어제 전신을 사용했다면 오늘은 가벼운 유산소, 코어, 가동성 위주가 안전합니다."),
    "유산소": ("근력 운동", "어제 유산소를 했다면 오늘은 근력 운동으로 자극을 바꾸는 것이 좋습니다."),
}


def _pick_routine(goal, experience, days, preference, yesterday):
    if yesterday == "전신":
        return "회복 루틴"
    if goal == "체지방 감량" and preference in ["짧고 효율적으로", "유산소와 근력 병행"]:
        return "체지방 감량 순환 루틴"
    if experience == "처음 시작":
        return "전신 기초 루틴"
    if days == "2회":
        return "전신 루틴" if experience in ["처음 시작", "초급자"] else "상하체 2분할"
    if days == "3회":
        return "전신 3회 루틴" if experience in ["처음 시작", "초급자"] else "Push/Pull/Legs 3분할"
    if days == "4회":
        return "상하체 2분할 반복" if goal != "근비대" else "근비대 중심 상하체 2분할"
    if experience == "상급자" or preference in ["강도 높게", "체계적인 분할 루틴"]:
        return "3분할 또는 4분할 고강도 루틴"
    return "Push/Pull/Legs 3분할"


def _categories_for_today(goal, today_part):
    if "회복" in today_part:
        return ["cardio", "core", "pull"]
    if "등" in today_part:
        return ["pull", "legs", "core"]
    if "가슴" in today_part or "어깨" in today_part:
        return ["push", "legs", "core"]
    if "하체" in today_part:
        return ["legs", "pull", "core"]
    if "상체" in today_part:
        return ["push", "pull", "core"]
    if goal == "체지방 감량":
        return ["legs", "push", "core", "cardio"]
    if goal == "자세 교정/건강 관리":
        return ["core", "pull", "legs"]
    if goal == "근력 향상":
        return ["legs", "push", "pull"]
    return ["legs", "push", "pull", "core"]


def _exercise_description(name, goal):
    descriptions = {
        "체력 향상": f"{name}은 전신 활동량과 기본 체력을 함께 높이는 데 도움이 되는 운동입니다.",
        "근비대": f"{name}은 목표 근육에 충분한 반복과 자극을 주기 좋은 운동입니다.",
        "체지방 감량": f"{name}은 큰 근육 사용과 심박수 상승을 통해 운동 밀도를 높이는 데 적합합니다.",
        "근력 향상": f"{name}은 안정적인 자세에서 힘을 쓰는 능력을 기르는 데 도움이 됩니다.",
        "자세 교정/건강 관리": f"{name}은 코어 안정성과 바른 움직임을 익히는 데 적합한 운동입니다.",
    }
    return descriptions.get(goal, f"{name}을 현재 루틴에 맞게 안전한 자세로 수행하세요.")


def _build_exercises(goal, place, today_part, available_time):
    place_table = PLACE_EXERCISES.get(place, PLACE_EXERCISES["집"])
    time_profile = TIME_PROFILES.get(available_time, TIME_PROFILES["30~60분"])
    categories = _categories_for_today(goal, today_part)

    names = []
    for category in categories:
        names.extend(place_table[category][:2])

    if available_time == "30분 이하":
        names = names[:5]
    elif available_time == "90분 이상":
        names = names[:8]
    else:
        names = names[:6]

    exercises = []
    for name in names:
        reps = time_profile["reps"]
        rest = time_profile["rest"]
        if goal == "근력 향상" and available_time in ["60~90분", "90분 이상"]:
            reps = "3~6회"
            rest = "120~180초"
        elif goal == "체지방 감량":
            reps = "12~20회 또는 30~45초"
            rest = "30~60초"

        exercises.append(
            {
                "name": name,
                "sets": time_profile["sets"],
                "reps": reps,
                "rest": rest,
                "description": _exercise_description(name, goal),
            }
        )
    return exercises


def _weekly_plan(days, routine_type, goal, experience):
    plans = {
        "2회": [
            f"1일차: {routine_type} - 큰 근육 위주의 전신 운동",
            "2일차: 전신 또는 상하체 보완 루틴 - 부족한 부위와 코어 추가",
            "나머지 날: 가벼운 걷기와 스트레칭으로 회복",
        ],
        "3회": [
            "1일차: 전신 근력 또는 Push",
            "2일차: Pull 또는 전신 보완",
            "3일차: Legs + 코어 또는 가벼운 유산소",
            "초보자는 세 날 모두 전신 루틴으로 반복해도 좋습니다.",
        ],
        "4회": [
            "1일차: 상체 또는 Push",
            "2일차: 하체 + 코어",
            "3일차: 상체 또는 Pull",
            "4일차: 하체 보완 + 유산소",
        ],
        "5회 이상": [
            "1일차: Push 또는 가슴/어깨",
            "2일차: Pull 또는 등/팔",
            "3일차: Legs",
            "4일차: 약점 부위 보완 또는 전신 순환",
            "5일차: 목표에 따라 유산소, 코어, 추가 분할 루틴 진행",
            "고빈도 루틴은 수면과 피로도를 확인하며 휴식일을 반드시 조정하세요.",
        ],
    }
    result = plans.get(days, plans["3회"])
    if goal == "근비대":
        result = result + ["근비대 목적이므로 같은 부위를 주 2회 정도 자극하되 총 세트 수를 기록하세요."]
    if goal == "체지방 감량":
        result = result + ["체지방 감량 목적이므로 쉬는 날에도 20~30분 가벼운 걷기를 추가하면 좋습니다."]
    if experience == "상급자":
        result = result + ["상급자는 고강도일수록 약점 부위 보완일과 완전 휴식일을 함께 설계하세요."]
    return result


def _object_particle(text):
    last = text[-1]
    code = ord(last)
    if 0xAC00 <= code <= 0xD7A3:
        return "을" if (code - 0xAC00) % 28 else "를"
    return "을"


def recommend(data):
    goal_profile = GOAL_PROFILES[data.fitness_goal]
    experience_profile = EXPERIENCE_PROFILES[data.experience_level]
    time_profile = TIME_PROFILES[data.available_time]
    today_part, today_reason = BODY_PART_GUIDE[data.yesterday_workout]

    routine_type = _pick_routine(
        data.fitness_goal,
        data.experience_level,
        data.days_per_week,
        data.preference,
        data.yesterday_workout,
    )

    particle = _object_particle(experience_profile["label"])
    user_type = f"{experience_profile['label']}{particle} 위한 {goal_profile['routine_hint']} 추천형"
    main_recommendation = (
        f"운동 목적이 '{data.fitness_goal}'이므로 {goal_profile['focus']}으로 루틴을 구성했습니다. "
        f"현재 경험 수준은 '{data.experience_level}'이어서 {experience_profile['guide']}를 우선하고, "
        f"주 {data.days_per_week} 운동 가능하므로 '{routine_type}' 방식이 적합합니다. "
        f"운동 장소가 '{data.workout_place}'이므로 해당 환경에서 가능한 운동을 중심으로 골랐고, "
        f"1회 운동 시간 '{data.available_time}'에 맞춰 {time_profile['pace']}으로 구성했습니다. "
        f"선호 방식 '{data.preference}'도 반영해 무리하지 않으면서 지속 가능한 흐름을 추천합니다."
    )
    today_focus = f"오늘 추천 부위는 {today_part}입니다. {today_reason}"

    exercises = _build_exercises(
        data.fitness_goal,
        data.workout_place,
        today_part,
        data.available_time,
    )
    weekly_plan = _weekly_plan(
        data.days_per_week,
        routine_type,
        data.fitness_goal,
        data.experience_level,
    )

    intensity_guide = (
        f"{experience_profile['rpe']} 오늘 루틴은 {time_profile['sets']} 기준으로 시작하고, "
        "통증이 아니라 운동 자극으로 느껴지는 범위에서만 강도를 올리세요."
    )
    recovery_tip = (
        f"어제 운동 부위가 '{data.yesterday_workout}'이므로 오늘은 {today_part} 중심으로 피로를 분산합니다. "
        "운동 후에는 5~10분 가벼운 스트레칭, 충분한 수분 섭취, 수면 확보를 권장합니다. "
        "피로가 강하면 세트 수를 줄이거나 가벼운 걷기로 대체해도 됩니다."
    )
    caution = (
        f"{goal_profile['caution']} 이 앱은 일반적인 운동 루틴 추천을 제공하는 학습용 웹앱이며, "
        "의학적 진단이나 치료 목적이 아닙니다. 운동 중 날카로운 통증, 어지러움, 기존 질환이나 부상 이력이 있다면 "
        "운동을 중단하고 전문가와 상담하세요."
    )

    return {
        "user_type": user_type,
        "routine_type": routine_type,
        "main_recommendation": main_recommendation,
        "today_focus": today_focus,
        "recommended_exercises": exercises,
        "weekly_plan": weekly_plan,
        "intensity_guide": intensity_guide,
        "recovery_tip": recovery_tip,
        "caution": caution,
    }
