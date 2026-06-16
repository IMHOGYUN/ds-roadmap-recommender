GOAL_RULES = {
    "근비대 및 근력 향상": {
        "label": "근비대 및 근력 향상",
        "rule": "근육량 증가와 힘 향상을 함께 노리는 근력 중심 구성",
        "beginner_reps": "8-12회",
        "advanced_reps": "4-8회",
        "rest": "60-120초",
        "guide": "자세가 안정된 범위에서 반복 수와 무게를 조금씩 높이는 방식이 좋습니다.",
    },
    "체지방 감량": {
        "label": "체지방 감량",
        "rule": "큰 근육 운동과 유산소성 움직임을 섞어 활동량을 높이는 구성",
        "beginner_reps": "12-15회 또는 30초",
        "advanced_reps": "12-20회 또는 40초",
        "rest": "30-60초",
        "guide": "짧은 휴식과 꾸준한 활동량을 활용하되 식단 처방처럼 보이는 안내는 피합니다.",
    },
}

LEVEL_RULES = {
    "처음 시작": {
        "label": "운동 처음 시작자",
        "sets": "2세트",
        "count": 4,
        "rpe": "RPE 5-6",
        "rule": "운동 습관 형성, 쉬운 동작, 자세 익히기",
        "routine_suffix": "기초 적응형",
    },
    "초급자": {
        "label": "초급자",
        "sets": "3세트",
        "count": 5,
        "rpe": "RPE 6-7",
        "rule": "기본 패턴 반복, 전신 루틴, 안정적인 수행",
        "routine_suffix": "기본 패턴 반복형",
    },
    "중급자": {
        "label": "중급자",
        "sets": "3-4세트",
        "count": 6,
        "rpe": "RPE 7-8",
        "rule": "분할 루틴, 점진적 과부하, 부위별 볼륨 관리",
        "routine_suffix": "분할 볼륨 관리형",
    },
    "상급자": {
        "label": "상급자",
        "sets": "4-5세트",
        "count": 7,
        "rpe": "RPE 8 전후",
        "rule": "고강도 분할, 약점 보완, 회복 전략",
        "routine_suffix": "고강도 약점 보완형",
    },
}

TODAY_RULES = {
    "운동 안 함": ("정상 루틴", "어제 운동을 쉬었으므로 목적과 경험 수준에 맞춘 정상 루틴을 진행합니다."),
    "가슴": ("등 중심", "어제 가슴을 운동했으므로 오늘은 등 중심으로 균형을 맞춥니다."),
    "등": ("가슴/하체 중심", "어제 등을 운동했으므로 오늘은 가슴 또는 하체 중심으로 피로를 분산합니다."),
    "하체": ("상체/코어 중심", "어제 하체를 운동했으므로 오늘은 상체, 코어, 가벼운 유산소 위주로 진행합니다."),
    "어깨": ("하체/등 중심", "어제 어깨를 운동했으므로 하체 또는 등 중심으로 어깨 부담을 줄입니다."),
    "팔": ("하체/전신 가벼운 루틴", "어제 팔을 운동했으므로 하체나 가벼운 전신 루틴을 추천합니다."),
    "전신": ("회복 루틴", "어제 전신을 운동했으므로 오늘은 회복, 가벼운 유산소, 스트레칭 중심이 좋습니다."),
    "유산소": ("근력 루틴", "어제 유산소를 했으므로 오늘은 근력 운동으로 자극을 바꿉니다."),
}

EXERCISE_POOLS = {
    "beginner_home_strength": [
        ("맨몸 스쿼트", "하체 기본 움직임을 안전하게 익힙니다."),
        ("무릎 푸시업", "상체 밀기 패턴을 부담 낮게 연습합니다."),
        ("힙브릿지", "둔근과 허리 주변 안정성을 기릅니다."),
        ("버드독", "코어 안정성과 균형 감각을 훈련합니다."),
        ("플랭크", "몸통을 버티는 기본 코어 운동입니다."),
    ],
    "beginner_gym_strength": [
        ("레그프레스", "머신으로 하체 기본 힘을 안전하게 익힙니다."),
        ("체스트프레스 머신", "가슴과 팔 밀기 동작을 안정적으로 연습합니다."),
        ("랫풀다운", "등 당기기 패턴을 쉽게 익힙니다."),
        ("시티드 로우", "등 중앙부와 자세 안정성을 함께 훈련합니다."),
        ("트레드밀 걷기", "부담 낮은 유산소로 운동 습관을 만듭니다."),
    ],
    "novice_pattern_strength": [
        ("고블릿 스쿼트", "가벼운 중량으로 스쿼트 패턴을 익힙니다."),
        ("인클라인 푸시업", "상체 밀기 동작을 쉬운 각도로 연습합니다."),
        ("밴드 로우", "등 당기기 패턴을 반복하기 좋은 운동입니다."),
        ("덤벨 루마니안 데드리프트", "힙힌지 동작을 안전하게 익힙니다."),
        ("데드버그", "허리 부담이 적은 코어 안정화 운동입니다."),
    ],
    "intermediate_strength_split": [
        ("벤치프레스", "상체 밀기 근력과 가슴 볼륨을 확보합니다."),
        ("랫풀다운", "등 너비와 당기기 힘을 강화합니다."),
        ("레그프레스", "하체 볼륨을 안정적으로 채웁니다."),
        ("루마니안 데드리프트", "햄스트링과 둔근을 강화합니다."),
        ("덤벨 숄더프레스", "어깨와 코어 안정성을 함께 기릅니다."),
        ("케이블 로우", "등 중앙부를 안정적으로 자극합니다."),
    ],
    "advanced_strength_split": [
        ("스쿼트", "하체와 전신 힘을 기르는 핵심 복합 운동입니다."),
        ("벤치프레스", "상체 밀기 근력을 키웁니다."),
        ("데드리프트", "후면 사슬과 전신 힘을 기릅니다."),
        ("오버헤드프레스", "어깨와 코어 안정성을 함께 훈련합니다."),
        ("바벨 로우", "등과 견갑 안정성을 강화합니다."),
        ("딥스", "가슴과 삼두를 강하게 자극합니다."),
        ("페이스풀", "후면 어깨와 상부 등 안정성을 챙깁니다."),
    ],
    "home_fat_loss": [
        ("점핑잭", "짧은 시간에 심박수를 올리는 전신 운동입니다."),
        ("맨몸 스쿼트", "큰 근육을 사용해 활동량을 높입니다."),
        ("마운틴 클라이머", "코어와 유산소 자극을 함께 줍니다."),
        ("런지", "하체 근력과 균형을 기릅니다."),
        ("플랭크", "순환 루틴 중 코어를 안정화합니다."),
    ],
    "outdoor_fat_loss": [
        ("빠르게 걷기", "강도 조절이 쉬운 기본 유산소입니다."),
        ("계단 오르기", "짧은 시간에 활동량을 높입니다."),
        ("가벼운 조깅", "심박수를 부드럽게 올립니다."),
        ("워킹 런지", "하체와 균형 감각을 함께 사용합니다."),
        ("벤치 스텝업", "야외 구조물을 활용한 하체 운동입니다."),
    ],
    "gym_fat_loss": [
        ("트레드밀 빠르게 걷기", "관절 부담을 조절하며 심박수를 올립니다."),
        ("레그프레스", "큰 근육을 사용해 에너지 소비를 높입니다."),
        ("랫풀다운", "등 운동으로 상체 활동량을 더합니다."),
        ("케틀벨 데드리프트", "전신 후면 근육을 함께 사용합니다."),
        ("사이클 인터벌", "짧은 유산소 자극을 추가합니다."),
    ],
    "recovery": [
        ("가벼운 걷기", "혈류를 높이고 피로 회복을 돕습니다."),
        ("고양이-소 자세", "척추 주변 긴장을 부드럽게 낮춥니다."),
        ("햄스트링 스트레칭", "하체 뒤쪽 긴장을 완화합니다."),
        ("고관절 스트레칭", "골반과 하체 가동성을 회복합니다."),
        ("복식호흡", "운동 강도를 낮추고 회복을 돕습니다."),
    ],
    "today_upper_recovery": [
        ("인클라인 푸시업", "하체 피로가 있을 때 상체를 가볍게 자극합니다."),
        ("밴드 로우 또는 수건 로우", "장소 제약을 줄인 상체 당기기 운동입니다."),
        ("데드버그", "하체 부담 없이 코어를 안정화합니다."),
        ("사이드 플랭크", "측면 코어와 몸통 안정성을 기릅니다."),
        ("가벼운 걷기", "하체 피로를 확인하며 회복을 돕습니다."),
    ],
}


def clean_text(value):
    if isinstance(value, str):
        value = value.replace("~~", "").replace("~", "-")
        for token in ["<s>", "</s>", "<del>", "</del>", "text-decoration", "line-through"]:
            value = value.replace(token, "")
        return " ".join(value.split())
    if isinstance(value, list):
        return [clean_text(item) for item in value]
    if isinstance(value, dict):
        return {key: clean_text(item) for key, item in value.items()}
    return value


def get_today_focus(yesterday_workout, experience_level):
    focus, reason = TODAY_RULES.get(yesterday_workout, TODAY_RULES["운동 안 함"])
    if experience_level == "처음 시작":
        reason += " 처음 시작 단계이므로 강도보다 자세와 습관 형성을 우선합니다."
    elif experience_level == "상급자":
        reason += " 상급자는 피로 누적을 확인하며 볼륨을 조절하세요."
    return focus, reason


def get_routine_type(data):
    if data.recommendation_mode == "회복/스트레칭 루틴 추천":
        return "회복 및 가동성 루틴"
    if data.recommendation_mode == "처음 시작 루틴 추천":
        return "운동 습관 형성 전신 루틴"
    if data.recommendation_mode == "오늘 운동 부위 추천":
        focus, _ = get_today_focus(data.yesterday_workout, data.experience_level)
        return f"어제 운동을 고려한 {focus} 루틴"
    if data.recommendation_mode == "목적별 집중 루틴 추천":
        return "근력 집중 루틴" if data.fitness_goal == "근비대 및 근력 향상" else "체지방 감량 순환 루틴"
    if data.yesterday_workout == "전신":
        return "회복 및 가동성 루틴"
    if data.experience_level == "처음 시작":
        return "전신 기초 루틴"
    if data.experience_level == "초급자":
        return "전신 반복 루틴" if data.days_per_week in ["2회", "3회"] else "상하체 입문 2분할"
    if data.experience_level == "중급자":
        return "상하체 2분할 루틴" if data.days_per_week in ["2회", "4회"] else "Push/Pull/Legs 3분할"
    if data.days_per_week == "5회 이상":
        return "4분할 약점 보완 루틴"
    return "고강도 3분할 루틴"


def get_weekly_plan(data):
    if data.recommendation_mode == "회복/스트레칭 루틴 추천":
        return [
            "1일차: 가벼운 걷기와 전신 스트레칭",
            "2일차: 코어 안정화와 가동성 운동",
            "3일차: 피로가 적으면 짧은 전신 루틴, 피로가 크면 휴식",
            "나머지 날: 수면, 수분 섭취, 가벼운 산책으로 회복",
        ]
    if data.experience_level == "처음 시작":
        return [
            "1일차: 전신 기초 동작과 가벼운 유산소",
            "2일차: 전신 기초 동작 반복과 코어",
            "나머지 날: 걷기, 스트레칭, 휴식으로 운동 습관 만들기",
        ]
    if data.experience_level == "초급자":
        return [
            "1일차: 전신 루틴 A - 스쿼트, 푸시, 풀",
            "2일차: 전신 루틴 B - 힌지, 런지, 코어",
            "3일차: 가능하면 가벼운 유산소와 전신 보완",
            "반복 가능한 루틴을 우선하고 종목 수를 과하게 늘리지 않기",
        ]
    if data.experience_level == "중급자":
        return [
            "1일차: 상체 또는 Push",
            "2일차: 하체 또는 Pull",
            "3일차: 휴식 또는 가벼운 유산소",
            "4일차: 상체 보완",
            "5일차: 하체와 코어 보완",
            "운동 기록을 남기고 점진적 과부하 적용",
        ]
    return [
        "1일차: 가슴과 삼두 또는 Push",
        "2일차: 등과 이두 또는 Pull",
        "3일차: 하체",
        "4일차: 어깨와 팔",
        "5일차: 약점 부위 보완",
        "피로도에 따라 완전 휴식일을 반드시 조정",
    ]


def select_pool(data, today_focus):
    if data.recommendation_mode == "회복/스트레칭 루틴 추천" or today_focus == "회복 루틴":
        return "recovery"
    if data.recommendation_mode == "처음 시작 루틴 추천":
        if data.workout_place == "헬스장":
            return "beginner_gym_strength"
        return "beginner_home_strength"
    if data.recommendation_mode == "오늘 운동 부위 추천":
        if today_focus == "상체/코어 중심":
            return "today_upper_recovery"
        if "등" in today_focus and data.workout_place == "헬스장":
            return "intermediate_strength_split" if data.experience_level in ["중급자", "상급자"] else "beginner_gym_strength"
        if "하체" in today_focus and data.workout_place == "헬스장":
            return "intermediate_strength_split"
    if data.fitness_goal == "체지방 감량":
        if data.workout_place == "야외":
            return "outdoor_fat_loss"
        if data.workout_place == "헬스장":
            return "gym_fat_loss"
        return "home_fat_loss"
    if data.experience_level == "처음 시작":
        return "beginner_gym_strength" if data.workout_place == "헬스장" else "beginner_home_strength"
    if data.experience_level == "초급자":
        return "novice_pattern_strength" if data.workout_place != "헬스장" else "beginner_gym_strength"
    if data.experience_level == "중급자":
        return "intermediate_strength_split"
    return "advanced_strength_split"


def build_exercises(data, pool_name):
    goal = GOAL_RULES[data.fitness_goal]
    level = LEVEL_RULES[data.experience_level]
    reps = goal["advanced_reps"] if data.experience_level in ["중급자", "상급자"] else goal["beginner_reps"]
    rest = goal["rest"]
    if pool_name == "recovery":
        reps, rest = "20-40초", "편안하게"
    selected = EXERCISE_POOLS[pool_name][: level["count"]]
    return [
        {
            "name": name,
            "sets": "1-2세트" if pool_name == "recovery" else level["sets"],
            "reps": reps,
            "rest": rest,
            "description": description,
        }
        for name, description in selected
    ]


def get_intensity_guide(data):
    level = LEVEL_RULES[data.experience_level]
    goal = GOAL_RULES[data.fitness_goal]
    if data.recommendation_mode == "회복/스트레칭 루틴 추천":
        return "RPE 3-5 수준으로 진행하세요. 피로가 줄어드는 느낌이 목표이며 강한 자극을 만들 필요는 없습니다."
    return f"{level['rpe']} 기준으로 진행하세요. 경험 수준에 맞게 '{level['rule']}'를 우선합니다. {goal['guide']}"


def get_recovery_tip(data, today_focus):
    tip = f"어제 운동 부위가 '{data.yesterday_workout}'이므로 오늘은 {today_focus} 방향으로 피로를 분산합니다."
    if data.experience_level == "상급자":
        tip += " 상급자는 운동량이 많아지기 쉬우므로 수면과 관절 피로를 꼭 확인하세요."
    elif data.experience_level == "처음 시작":
        tip += " 처음 시작 단계에서는 근육통이 강하면 하루 쉬어도 괜찮습니다."
    return tip + " 운동 후 5-10분 정리 운동과 가벼운 스트레칭을 권장합니다."


def recommend(data):
    today_focus, today_reason = get_today_focus(data.yesterday_workout, data.experience_level)
    routine_type = get_routine_type(data)
    pool_name = select_pool(data, today_focus)
    goal = GOAL_RULES[data.fitness_goal]
    level = LEVEL_RULES[data.experience_level]

    main = (
        f"'{data.recommendation_mode}' 모드에서 목표는 '{data.fitness_goal}'이고 경험 수준은 '{data.experience_level}'입니다. "
        f"{goal['rule']} 원칙에 맞춰 {routine_type}을 추천합니다. "
        f"장소는 '{data.workout_place}', 주당 운동 가능 횟수는 '{data.days_per_week}'이므로 "
        f"{level['rule']}에 맞는 운동 풀을 선택했습니다."
    )

    mode_summary = {
        "처음 시작 루틴 추천": "처음 시작 모드라서 쉬운 전신 운동과 낮은 강도를 우선했습니다.",
        "오늘 운동 부위 추천": f"어제 '{data.yesterday_workout}' 운동을 반영해 오늘은 {today_focus}으로 조정했습니다.",
        "주간 분할 루틴 추천": f"주 {data.days_per_week}와 경험 수준 '{data.experience_level}'에 맞춰 분할 계획을 만들었습니다.",
        "목적별 집중 루틴 추천": f"운동 목적 '{data.fitness_goal}'에 맞춰 운동 종류와 반복 방식을 선택했습니다.",
        "회복/스트레칭 루틴 추천": "회복 모드라서 강한 근력 운동보다 가동성, 스트레칭, 낮은 강도를 우선했습니다.",
    }.get(data.recommendation_mode, "입력 조건을 바탕으로 맞춤 루틴을 구성했습니다.")

    experience_highlight = (
        f"{level['label']} 단계이므로 '{level['routine_suffix']}'으로 분류했습니다. "
        f"운동 수는 최대 {level['count']}개, 세트는 {level['sets']}, 강도는 {level['rpe']} 기준입니다."
    )

    result = {
        "user_type": f"{level['label']} {goal['label']} {level['routine_suffix']} 루틴",
        "routine_type": routine_type,
        "mode_summary": mode_summary,
        "experience_highlight": experience_highlight,
        "main_recommendation": main,
        "today_focus": f"오늘 추천 방향: {today_focus}. {today_reason}",
        "recommended_exercises": build_exercises(data, pool_name),
        "weekly_plan": get_weekly_plan(data),
        "intensity_guide": get_intensity_guide(data),
        "recovery_tip": get_recovery_tip(data, today_focus),
        "caution": (
            "이 앱은 일반적인 운동 루틴 추천을 제공하는 학습용 웹앱이며 의학적 진단이나 치료 목적이 아닙니다. "
            "날카로운 통증, 어지러움, 질환, 부상 이력이 있는 경우 운동을 중단하고 전문가와 상담하세요."
        ),
        "debug_info": {
            "recommendation_mode": data.recommendation_mode,
            "selected_exercise_pool": pool_name,
            "selected_today_focus": today_focus,
            "place_rule": f"{data.workout_place} 환경에 맞는 운동 풀 사용",
            "goal_rule": goal["rule"],
            "level_rule": level["rule"],
            "days_rule": f"주 {data.days_per_week} 기준 주간 계획 생성",
        },
    }
    return clean_text(result)
