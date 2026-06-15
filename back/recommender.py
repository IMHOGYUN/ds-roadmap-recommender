GOAL_RULES = {
    "체력 향상": {
        "label": "체력 향상",
        "rule": "전신 근력과 유산소를 함께 구성",
        "reps": "12-15회 또는 30-45초",
        "rest": "30-60초",
        "guide": "대화가 가능한 강도에서 심박수를 올리고 기본 체력을 쌓습니다.",
    },
    "근비대": {
        "label": "근비대",
        "rule": "부위별 볼륨과 8-12회 반복 중심",
        "reps": "8-12회",
        "rest": "60-90초",
        "guide": "반복 수, 세트 수, 무게를 기록하며 점진적 과부하를 적용합니다.",
    },
    "체지방 감량": {
        "label": "체지방 감량",
        "rule": "큰 근육 운동과 유산소를 병행",
        "reps": "12-20회 또는 30-45초",
        "rest": "30-60초",
        "guide": "짧은 휴식과 꾸준한 활동량을 활용하되 극단적인 식단 처방은 피합니다.",
    },
    "근력 향상": {
        "label": "근력 향상",
        "rule": "복합 다관절 운동과 낮은 반복 수 중심",
        "reps": "3-6회",
        "rest": "120-180초",
        "guide": "자세가 안정된 범위에서 충분히 쉬고 강한 반복을 수행합니다.",
    },
    "자세 교정/건강 관리": {
        "label": "자세 교정",
        "rule": "코어, 둔근, 등, 가동성 중심",
        "reps": "8-12회 또는 20-30초",
        "rest": "30-60초",
        "guide": "통증 없이 가능한 범위에서 정렬과 움직임 질을 우선합니다.",
    },
}

LEVEL_RULES = {
    "처음 시작": {
        "label": "운동 처음 시작자",
        "sets": "2세트",
        "count": 4,
        "rpe": "RPE 5-6",
        "rule": "습관 형성과 자세 익히기 우선",
    },
    "초급자": {
        "label": "초급자",
        "sets": "3세트",
        "count": 5,
        "rpe": "RPE 6-7",
        "rule": "스쿼트, 힌지, 푸시, 풀, 코어 패턴 반복",
    },
    "중급자": {
        "label": "중급자",
        "sets": "3-4세트",
        "count": 6,
        "rpe": "RPE 7-8",
        "rule": "점진적 과부하와 부위별 볼륨 관리",
    },
    "상급자": {
        "label": "상급자",
        "sets": "4-5세트",
        "count": 7,
        "rpe": "RPE 8 전후",
        "rule": "복합 운동, 보조 운동, 약점 보완, 회복 관리",
    },
}

TIME_RULES = {
    "30분 이하": {"count": 4, "rule": "핵심 운동만 고르는 압축 루틴"},
    "30-60분": {"count": 5, "rule": "준비 운동과 본운동을 균형 있게 구성"},
    "60-90분": {"count": 6, "rule": "주요 운동과 보조 운동을 함께 포함"},
    "90분 이상": {"count": 7, "rule": "워밍업, 본운동, 보조 운동, 마무리까지 포함"},
}

TODAY_RULES = {
    "운동 안 함": ("정상 루틴", "어제 운동을 쉬었으므로 목적과 경험 수준에 맞춘 정상 루틴을 진행합니다."),
    "가슴": ("등 중심", "어제 가슴을 운동했으므로 오늘은 등 중심으로 균형을 맞춥니다."),
    "등": ("가슴/하체 중심", "어제 등을 운동했으므로 오늘은 가슴 또는 하체 중심으로 피로를 분산합니다."),
    "하체": ("상체/코어 중심", "어제 하체를 운동했으므로 오늘은 상체, 코어, 가벼운 유산소 위주로 진행합니다."),
    "어깨": ("하체/등 중심", "어제 어깨를 운동했으므로 오늘은 하체 또는 등 중심으로 어깨 부담을 줄입니다."),
    "팔": ("하체/전신 가벼운 루틴", "어제 팔을 운동했으므로 오늘은 하체나 가벼운 전신 루틴을 추천합니다."),
    "전신": ("회복 루틴", "어제 전신을 운동했으므로 오늘은 회복, 가벼운 유산소, 스트레칭 중심이 좋습니다."),
    "유산소": ("근력 루틴", "어제 유산소를 했으므로 오늘은 근력 운동으로 자극을 바꿉니다."),
}

EXERCISE_POOLS = {
    "beginner_home_fullbody": [
        ("맨몸 스쿼트", "하체와 기본 움직임을 익히는 쉬운 전신 운동입니다."),
        ("무릎 푸시업", "상체 밀기 패턴을 부담 낮게 연습합니다."),
        ("힙브릿지", "둔근과 허리 주변 안정성을 기릅니다."),
        ("버드독", "코어 안정성과 균형 감각을 안전하게 훈련합니다."),
        ("플랭크", "몸통을 버티는 기본 코어 운동입니다."),
    ],
    "beginner_gym_machine": [
        ("레그프레스", "머신으로 하체 기본 힘을 안전하게 익힙니다."),
        ("체스트프레스 머신", "가슴과 팔 밀기 동작을 안정적으로 연습합니다."),
        ("랫풀다운", "등 당기기 패턴을 쉽게 익힙니다."),
        ("시티드 로우", "등 중앙부와 자세 안정성을 함께 훈련합니다."),
        ("트레드밀 걷기", "부담 낮은 유산소로 운동 습관을 만듭니다."),
    ],
    "gym_hypertrophy_push": [
        ("벤치프레스", "가슴과 삼두 볼륨을 확보하는 대표 운동입니다."),
        ("인클라인 덤벨프레스", "상부 가슴을 보완합니다."),
        ("숄더프레스 머신", "어깨를 안정적으로 자극합니다."),
        ("케이블 플라이", "가슴 수축감을 집중적으로 느끼기 좋습니다."),
        ("트라이셉스 푸시다운", "삼두 보조 볼륨을 채웁니다."),
    ],
    "gym_hypertrophy_pull": [
        ("랫풀다운", "광배근과 등 너비를 만드는 운동입니다."),
        ("바벨 로우", "등 두께와 당기는 힘을 키웁니다."),
        ("케이블 로우", "등 중앙부를 안정적으로 자극합니다."),
        ("페이스풀", "후면 어깨와 상부 등 안정성에 좋습니다."),
        ("덤벨 컬", "이두 보조 운동으로 팔 볼륨을 더합니다."),
    ],
    "gym_hypertrophy_legs": [
        ("스쿼트", "하체와 코어를 함께 사용하는 대표 운동입니다."),
        ("레그프레스", "하체 볼륨을 안정적으로 채웁니다."),
        ("루마니안 데드리프트", "햄스트링과 둔근을 강화합니다."),
        ("레그컬", "햄스트링을 집중적으로 보완합니다."),
        ("카프레이즈", "종아리를 마무리로 자극합니다."),
    ],
    "gym_strength_compound": [
        ("스쿼트", "하체와 전신 힘을 기르는 핵심 복합 운동입니다."),
        ("벤치프레스", "상체 밀기 근력을 키웁니다."),
        ("데드리프트", "후면 사슬과 전신 힘을 기릅니다."),
        ("오버헤드프레스", "어깨와 코어 안정성을 함께 훈련합니다."),
        ("바벨 로우", "등과 견갑 안정성을 강화합니다."),
    ],
    "outdoor_fat_loss": [
        ("빠르게 걷기", "강도 조절이 쉬운 기본 유산소입니다."),
        ("계단 오르기", "짧은 시간에 활동량을 높입니다."),
        ("가벼운 조깅", "심박수를 부드럽게 올립니다."),
        ("워킹 런지", "하체와 균형 감각을 함께 사용합니다."),
        ("벤치 스텝업", "야외 구조물을 활용한 하체 운동입니다."),
    ],
    "home_fat_loss_circuit": [
        ("점핑잭", "짧은 시간에 심박수를 올리는 전신 운동입니다."),
        ("맨몸 스쿼트", "큰 근육을 사용해 활동량을 높입니다."),
        ("마운틴 클라이머", "코어와 유산소 자극을 함께 줍니다."),
        ("런지", "하체 근력과 균형을 기릅니다."),
        ("플랭크", "순환 루틴 중 코어를 안정화합니다."),
    ],
    "posture_mobility": [
        ("데드버그", "허리 부담을 줄이며 코어를 안정화합니다."),
        ("버드독", "몸통 균형과 척추 안정성을 기릅니다."),
        ("힙브릿지", "둔근 활성화와 골반 안정성을 돕습니다."),
        ("흉추 회전", "등과 어깨 가동성을 회복합니다."),
        ("월슬라이드", "어깨와 등 정렬을 연습합니다."),
    ],
    "recovery_stretching": [
        ("가벼운 걷기", "혈류를 높이고 피로 회복을 돕습니다."),
        ("고양이-소 자세", "척추 주변 긴장을 부드럽게 낮춥니다."),
        ("햄스트링 스트레칭", "하체 뒤쪽 긴장을 완화합니다."),
        ("고관절 스트레칭", "골반과 하체 가동성을 회복합니다."),
        ("복식호흡", "운동 강도를 낮추고 회복을 돕습니다."),
    ],
    "no_equipment_strength": [
        ("월싯", "기구 없이 하체 버티는 힘을 기릅니다."),
        ("푸시업", "상체 밀기 힘을 키웁니다."),
        ("런지", "하체 균형과 근지구력을 기릅니다."),
        ("슈퍼맨", "등과 둔근 후면을 가볍게 강화합니다."),
        ("사이드 플랭크", "옆구리와 코어 안정성을 기릅니다."),
    ],
    "upper_body_home": [
        ("푸시업", "상체 밀기 기본 운동입니다."),
        ("파이크 푸시업", "어깨와 상체를 함께 자극합니다."),
        ("밴드 로우 또는 수건 로우", "집에서 가능한 당기기 운동입니다."),
        ("플랭크 숄더탭", "코어와 어깨 안정성을 함께 훈련합니다."),
        ("딥스 변형", "삼두와 가슴 보조 운동입니다."),
    ],
    "lower_body_home": [
        ("스쿼트", "하체 기본 움직임을 강화합니다."),
        ("런지", "하체 균형과 둔근 자극을 만듭니다."),
        ("힙브릿지", "둔근과 골반 안정성을 기릅니다."),
        ("카프레이즈", "종아리 근지구력을 높입니다."),
        ("월싯", "하체 버티는 힘을 기릅니다."),
    ],
    "core_cardio_light": [
        ("제자리 걷기", "부담 낮은 유산소로 몸을 깨웁니다."),
        ("데드버그", "허리 부담이 적은 코어 운동입니다."),
        ("사이드 플랭크", "측면 코어 안정성을 기릅니다."),
        ("버드독", "균형과 코어 조절을 연습합니다."),
        ("가벼운 스트레칭", "운동 후 긴장을 낮춥니다."),
    ],
}


def clean_text(value):
    if isinstance(value, str):
        value = value.replace("~~", "")
        value = value.replace("~", "-")
        for token in ["<s>", "</s>", "<del>", "</del>", "text-decoration", "line-through"]:
            value = value.replace(token, "")
        return " ".join(value.split())
    if isinstance(value, list):
        return [clean_text(item) for item in value]
    if isinstance(value, dict):
        return {key: clean_text(item) for key, item in value.items()}
    return value


def get_today_focus(yesterday_workout, fitness_goal, experience_level):
    focus, reason = TODAY_RULES.get(yesterday_workout, TODAY_RULES["운동 안 함"])
    if fitness_goal == "자세 교정/건강 관리" and yesterday_workout != "전신":
        reason += " 자세 관리 목적이므로 코어와 가동성 운동을 함께 넣습니다."
    if experience_level == "처음 시작":
        reason += " 처음 시작 단계이므로 강도보다 자세와 반복 가능한 습관을 우선합니다."
    return focus, reason


def get_routine_type(data):
    if data.recommendation_mode == "처음 시작 루틴 추천":
        return "전신 기초 루틴"
    if data.recommendation_mode == "회복/스트레칭 루틴 추천":
        return "회복 및 가동성 루틴"
    if data.recommendation_mode == "오늘 운동 부위 추천":
        focus, _ = get_today_focus(data.yesterday_workout, data.fitness_goal, data.experience_level)
        return f"오늘 {focus} 루틴"
    if data.recommendation_mode == "주간 분할 루틴 추천":
        if data.days_per_week == "2회":
            return "전신 A/B 루틴" if data.experience_level in ["처음 시작", "초급자"] else "상하체 2분할 루틴"
        if data.days_per_week == "3회":
            return "전신 3회 루틴" if data.experience_level in ["처음 시작", "초급자"] else "Push/Pull/Legs 3분할 루틴"
        if data.days_per_week == "4회":
            return "상하체 2분할 반복 루틴"
        return "4분할 약점 보완 루틴" if data.experience_level == "상급자" else "PPL과 약점 보완 루틴"
    if data.fitness_goal == "체지방 감량":
        return "유산소와 근력 병행 순환 루틴"
    if data.fitness_goal == "근력 향상":
        return "복합 다관절 근력 루틴"
    if data.fitness_goal == "근비대":
        return "부위별 볼륨 근비대 루틴"
    if data.fitness_goal == "자세 교정/건강 관리":
        return "자세 교정 및 코어 안정화 루틴"
    return "전신 체력 향상 루틴"


def get_weekly_plan(data, routine_type):
    if data.recommendation_mode == "회복/스트레칭 루틴 추천":
        return [
            "1일차: 가벼운 걷기와 전신 스트레칭",
            "2일차: 코어 안정화와 가동성 운동",
            "3일차: 피로가 적으면 짧은 전신 기초 운동, 피로가 크면 휴식",
            "나머지 날: 수면과 수분 섭취를 우선하고 통증이 있으면 운동을 쉬기",
        ]
    if data.days_per_week == "2회":
        return [
            "1일차: 전신 A 또는 상체 중심",
            "2일차: 전신 B 또는 하체 중심",
            "나머지 날: 걷기, 스트레칭, 휴식으로 회복",
        ]
    if data.days_per_week == "3회":
        if data.experience_level in ["처음 시작", "초급자"]:
            return [
                "1일차: 전신 기초 루틴",
                "2일차: 전신 루틴과 코어",
                "3일차: 전신 루틴과 가벼운 유산소",
            ]
        return [
            "1일차: Push - 가슴, 어깨, 삼두",
            "2일차: Pull - 등, 이두, 후면 어깨",
            "3일차: Legs - 하체, 둔근, 코어",
        ]
    if data.days_per_week == "4회":
        return [
            "1일차: 상체 - 밀기와 당기기 균형",
            "2일차: 하체 - 스쿼트와 힌지 패턴",
            "3일차: 휴식 또는 가벼운 걷기",
            "4일차: 상체 - 부족한 부위 보완",
            "5일차: 하체 - 둔근, 햄스트링, 코어 보완",
        ]
    if data.experience_level == "상급자":
        return [
            "1일차: 가슴과 삼두",
            "2일차: 등과 이두",
            "3일차: 하체",
            "4일차: 어깨와 팔",
            "5일차: 약점 부위 보완",
            "주 5회 이상은 피로도에 따라 완전 휴식일을 반드시 조정",
        ]
    return [
        "1일차: Push",
        "2일차: Pull",
        "3일차: Legs",
        "4일차: 전신 순환 또는 약점 보완",
        "5일차: 가벼운 유산소와 코어",
    ]


def get_intensity_guide(data):
    if data.recommendation_mode == "회복/스트레칭 루틴 추천":
        return "RPE 3-5 수준으로 진행하세요. 땀이 많이 나는 운동보다 몸이 가벼워지는 정도의 회복 강도가 적합합니다."
    level = LEVEL_RULES[data.experience_level]
    goal = GOAL_RULES[data.fitness_goal]
    if data.preference == "강도 높게" and data.experience_level in ["처음 시작", "초급자"]:
        return f"{level['rpe']} 범위에서만 도전 요소를 추가하세요. 초보 단계에서는 고강도보다 정확한 자세가 우선입니다."
    return f"{level['rpe']} 기준으로 진행하세요. {goal['guide']} 선호 방식은 '{data.preference}'이므로 강도보다 지속 가능성을 확인하세요."


def get_recovery_tip(data, today_focus):
    if data.recommendation_mode == "회복/스트레칭 루틴 추천":
        return f"오늘은 {today_focus} 중심입니다. 운동 후 피로가 줄어드는 느낌이 목표이며, 수면과 수분 섭취를 충분히 챙기세요."
    tip = f"어제 운동 부위가 '{data.yesterday_workout}'이므로 오늘은 {today_focus}로 피로를 분산합니다."
    if data.yesterday_workout == "하체":
        tip += " 무릎이나 고관절 피로가 남아 있으면 달리기와 계단 운동은 강도를 낮추세요."
    if data.days_per_week == "5회 이상":
        tip += " 주 5회 이상 운동은 과훈련을 피하기 위해 휴식일을 계획적으로 넣어야 합니다."
    return tip + " 운동 후 5-10분 정리 운동과 가벼운 스트레칭을 권장합니다."


def limit_exercises_by_time(exercises, available_time):
    return exercises[: TIME_RULES[available_time]["count"]]


def _make_exercises(pool_name, data):
    goal = GOAL_RULES[data.fitness_goal]
    level = LEVEL_RULES[data.experience_level]
    exercises = []
    selected = limit_exercises_by_time(EXERCISE_POOLS[pool_name], data.available_time)
    if data.recommendation_mode == "처음 시작 루틴 추천":
        selected = EXERCISE_POOLS[pool_name][:5]

    for name, description in selected:
        reps = goal["reps"]
        rest = goal["rest"]
        sets = level["sets"]
        if data.recommendation_mode == "회복/스트레칭 루틴 추천":
            sets, reps, rest = "1-2세트", "20-40초", "편안하게"
        elif data.recommendation_mode == "처음 시작 루틴 추천":
            sets = "2세트"
            rest = "30-60초"
        exercises.append(
            {
                "name": name,
                "sets": sets,
                "reps": reps,
                "rest": rest,
                "description": description,
            }
        )
    return exercises


def _place_beginner_pool(place):
    return {
        "집": "beginner_home_fullbody",
        "헬스장": "beginner_gym_machine",
        "야외": "outdoor_fat_loss",
        "기구 거의 없음": "posture_mobility",
    }.get(place, "beginner_home_fullbody")


def _pool_for_focus(data, today_focus):
    if today_focus == "회복 루틴":
        return "recovery_stretching"
    if data.workout_place == "기구 거의 없음":
        return "no_equipment_strength" if data.fitness_goal != "자세 교정/건강 관리" else "posture_mobility"
    if data.workout_place == "야외":
        return "outdoor_fat_loss" if data.fitness_goal == "체지방 감량" else "core_cardio_light"
    if data.workout_place == "집":
        if "상체" in today_focus or "가슴" in today_focus or "등" in today_focus:
            return "upper_body_home"
        if "하체" in today_focus:
            return "lower_body_home"
        if data.fitness_goal == "체지방 감량":
            return "home_fat_loss_circuit"
        return "beginner_home_fullbody"
    if "등" in today_focus:
        return "gym_hypertrophy_pull"
    if "하체" in today_focus:
        return "gym_hypertrophy_legs"
    if data.fitness_goal == "근력 향상":
        return "gym_strength_compound"
    return "gym_hypertrophy_push"


def _pool_for_goal(data):
    if data.fitness_goal == "체지방 감량":
        if data.workout_place == "야외":
            return "outdoor_fat_loss"
        return "home_fat_loss_circuit" if data.workout_place != "헬스장" else "gym_hypertrophy_legs"
    if data.fitness_goal == "근비대":
        return "gym_hypertrophy_push" if data.workout_place == "헬스장" else "upper_body_home"
    if data.fitness_goal == "근력 향상":
        return "gym_strength_compound" if data.workout_place == "헬스장" else "no_equipment_strength"
    if data.fitness_goal == "자세 교정/건강 관리":
        return "posture_mobility"
    return "beginner_gym_machine" if data.workout_place == "헬스장" else "beginner_home_fullbody"


def build_context(data):
    today_focus, today_reason = get_today_focus(data.yesterday_workout, data.fitness_goal, data.experience_level)
    routine_type = get_routine_type(data)
    return {
        "today_focus": today_focus,
        "today_reason": today_reason,
        "routine_type": routine_type,
        "goal_rule": GOAL_RULES[data.fitness_goal]["rule"],
        "level_rule": LEVEL_RULES[data.experience_level]["rule"],
        "time_rule": TIME_RULES[data.available_time]["rule"],
        "place_rule": f"{data.workout_place} 환경에 맞는 운동 풀 사용",
    }


def _response(data, context, pool_name, user_type, main_recommendation):
    today_focus_text = f"오늘 추천 방향: {context['today_focus']}. {context['today_reason']}"
    result = {
        "user_type": user_type,
        "routine_type": context["routine_type"],
        "main_recommendation": main_recommendation,
        "today_focus": today_focus_text,
        "recommended_exercises": _make_exercises(pool_name, data),
        "weekly_plan": get_weekly_plan(data, context["routine_type"]),
        "intensity_guide": get_intensity_guide(data),
        "recovery_tip": get_recovery_tip(data, context["today_focus"]),
        "caution": (
            "이 앱은 일반적인 운동 루틴 추천을 제공하는 학습용 웹앱이며 의학적 진단이나 치료 목적이 아닙니다. "
            "날카로운 통증, 어지러움, 질환, 부상 이력이 있는 경우 운동을 중단하고 전문가와 상담하세요."
        ),
        "debug_info": {
            "recommendation_mode": data.recommendation_mode,
            "selected_exercise_pool": pool_name,
            "selected_today_focus": context["today_focus"],
            "place_rule": context["place_rule"],
            "goal_rule": context["goal_rule"],
            "level_rule": context["level_rule"],
            "time_rule": context["time_rule"],
        },
    }
    return clean_text(result)


def recommend_beginner_start(data, context):
    pool_name = _place_beginner_pool(data.workout_place)
    main = (
        f"'{data.recommendation_mode}' 모드이므로 운동 습관 형성과 자세 익히기를 우선합니다. "
        f"장소가 '{data.workout_place}'이고 시간은 '{data.available_time}'이므로 쉬운 전신 운동만 골랐습니다. "
        f"목표가 '{data.fitness_goal}'이어도 처음에는 낮은 강도로 반복 가능한 루틴을 만드는 것이 좋습니다."
    )
    return _response(data, context, pool_name, "운동 습관 형성형 전신 기초 루틴", main)


def recommend_today_focus(data, context):
    pool_name = _pool_for_focus(data, context["today_focus"])
    main = (
        f"'{data.recommendation_mode}' 모드에서는 어제 운동한 부위인 '{data.yesterday_workout}'을 가장 중요하게 봅니다. "
        f"오늘은 {context['today_focus']}로 피로를 분산하고, '{data.workout_place}'에서 가능한 운동으로 구성했습니다. "
        f"목표 '{data.fitness_goal}'와 경험 수준 '{data.experience_level}'에 맞춰 강도를 조절하세요."
    )
    return _response(data, context, pool_name, f"{data.experience_level} 오늘 부위 조절 루틴형", main)


def recommend_weekly_split(data, context):
    if data.experience_level == "상급자" and data.days_per_week == "5회 이상":
        pool_name = "gym_strength_compound" if data.workout_place == "헬스장" else "no_equipment_strength"
    elif data.days_per_week in ["4회", "5회 이상"] and data.workout_place == "헬스장":
        pool_name = "gym_hypertrophy_legs" if data.fitness_goal == "근비대" else "gym_strength_compound"
    else:
        pool_name = _pool_for_focus(data, context["today_focus"])
    main = (
        f"'{data.recommendation_mode}' 모드에서는 주 {data.days_per_week} 가능 여부와 경험 수준 '{data.experience_level}'을 기준으로 나눴습니다. "
        f"추천 방식은 {context['routine_type']}이며, 주간 계획에서 운동일과 회복일을 분리했습니다. "
        f"선호 방식 '{data.preference}'를 반영해 분할 이름과 반복 구조가 명확히 보이도록 구성했습니다."
    )
    return _response(data, context, pool_name, f"{data.experience_level} {data.days_per_week} 주간 분할 루틴형", main)


def recommend_goal_focus(data, context):
    pool_name = _pool_for_goal(data)
    main = (
        f"'{data.recommendation_mode}' 모드에서는 운동 목적 '{data.fitness_goal}'을 가장 크게 반영합니다. "
        f"{GOAL_RULES[data.fitness_goal]['rule']} 원칙에 맞춰 운동 목록과 반복 수를 정했습니다. "
        f"장소 '{data.workout_place}', 시간 '{data.available_time}', 선호 방식 '{data.preference}'도 함께 반영했습니다."
    )
    return _response(data, context, pool_name, f"{data.experience_level} {data.fitness_goal} 집중 루틴형", main)


def recommend_recovery(data, context):
    pool_name = "recovery_stretching" if data.yesterday_workout in ["전신", "하체", "등", "가슴"] else "posture_mobility"
    context = dict(context)
    context["routine_type"] = "회복 및 가동성 루틴"
    context["today_focus"] = "회복/스트레칭"
    main = (
        f"'{data.recommendation_mode}' 모드이므로 오늘은 강한 운동보다 회복과 가동성을 우선합니다. "
        f"어제 운동 부위가 '{data.yesterday_workout}'이므로 피로가 남은 부위를 직접 몰아붙이지 않습니다. "
        f"시간 '{data.available_time}' 안에서 가벼운 호흡, 스트레칭, 코어 안정화 위주로 진행하세요."
    )
    return _response(data, context, pool_name, f"{data.experience_level} 회복 관리 루틴형", main)


def recommend(data):
    context = build_context(data)
    if data.recommendation_mode == "처음 시작 루틴 추천":
        return recommend_beginner_start(data, context)
    if data.recommendation_mode == "오늘 운동 부위 추천":
        return recommend_today_focus(data, context)
    if data.recommendation_mode == "주간 분할 루틴 추천":
        return recommend_weekly_split(data, context)
    if data.recommendation_mode == "목적별 집중 루틴 추천":
        return recommend_goal_focus(data, context)
    if data.recommendation_mode == "회복/스트레칭 루틴 추천":
        return recommend_recovery(data, context)
    return recommend_goal_focus(data, context)
