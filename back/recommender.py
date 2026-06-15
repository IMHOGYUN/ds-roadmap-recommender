GOAL_GUIDES = {
    "체력 향상": {
        "label": "체력 향상",
        "focus": "전신 근력과 유산소를 함께 늘리는 방향",
        "reps": "12~15회 또는 30~45초",
        "rest": "30~60초",
        "note": "숨이 차더라도 자세가 무너지지 않는 강도에서 반복하는 것이 핵심입니다.",
    },
    "근비대": {
        "label": "근비대",
        "focus": "부위별 운동량과 8~12회 반복을 확보하는 방향",
        "reps": "8~12회",
        "rest": "60~90초",
        "note": "운동 기록을 남기고 반복 수나 무게를 조금씩 올리는 점진적 과부하가 중요합니다.",
    },
    "체지방 감량": {
        "label": "체지방 감량",
        "focus": "큰 근육 근력 운동과 유산소를 병행해 활동량을 높이는 방향",
        "reps": "12~20회 또는 30~45초",
        "rest": "30~60초",
        "note": "극단적인 식단 처방보다 수면, 규칙적인 식사, 꾸준한 활동량을 함께 관리하세요.",
    },
    "근력 향상": {
        "label": "근력 향상",
        "focus": "복합 다관절 운동을 정확한 자세로 수행하며 힘을 키우는 방향",
        "reps": "3~6회",
        "rest": "120~180초",
        "note": "초보자는 고중량보다 자세 안정이 먼저이며, 무게는 천천히 올리는 것이 안전합니다.",
    },
    "자세 교정/건강 관리": {
        "label": "자세 교정",
        "focus": "코어, 둔근, 등, 가동성, 스트레칭으로 몸의 균형을 회복하는 방향",
        "reps": "8~12회 또는 20~30초",
        "rest": "30~60초",
        "note": "통증이 있으면 강도를 낮추고 필요한 경우 전문가 상담을 받는 것이 좋습니다.",
    },
}

EXPERIENCE_GUIDES = {
    "처음 시작": {
        "label": "운동 처음 시작자",
        "sets": "2~3세트",
        "count": 4,
        "rpe": "RPE 5~6",
        "style": "습관 형성, 자세 익히기, 무리하지 않기",
    },
    "초급자": {
        "label": "초급자",
        "sets": "3세트",
        "count": 5,
        "rpe": "RPE 6~7",
        "style": "스쿼트, 힌지, 푸시, 풀, 코어 패턴 반복",
    },
    "중급자": {
        "label": "중급자",
        "sets": "3~4세트",
        "count": 6,
        "rpe": "RPE 7~8",
        "style": "점진적 과부하와 부위별 볼륨 관리",
    },
    "상급자": {
        "label": "상급자",
        "sets": "4~5세트",
        "count": 7,
        "rpe": "RPE 8 전후",
        "style": "복합 운동, 보조 운동, 약점 보완, 회복 관리",
    },
}

TIME_LIMITS = {
    "30분 이하": {"count": 4, "rest_adjust": "짧은 휴식", "pace": "핵심 운동만 고르는 압축 루틴"},
    "30~60분": {"count": 5, "rest_adjust": "표준 휴식", "pace": "가장 일반적인 본운동 중심 루틴"},
    "60~90분": {"count": 6, "rest_adjust": "충분한 휴식", "pace": "보조 운동까지 포함하는 확장 루틴"},
    "90분 이상": {"count": 7, "rest_adjust": "긴 휴식", "pace": "워밍업, 본운동, 보조 운동, 마무리까지 포함하는 긴 루틴"},
}

TODAY_FOCUS = {
    "운동 안 함": ("정상 루틴", "어제 운동을 쉬었으므로 목적과 경험 수준에 맞춘 정상 루틴을 진행합니다."),
    "가슴": ("등 또는 하체", "어제 가슴을 운동했으므로 오늘은 등 또는 하체 중심으로 피로를 분산합니다."),
    "등": ("가슴/어깨 또는 하체", "어제 등을 운동했으므로 오늘은 가슴, 어깨, 하체 중심으로 구성합니다."),
    "하체": ("상체/코어와 가벼운 유산소", "어제 하체를 운동했으므로 무릎과 둔근 피로를 고려해 상체와 코어 위주로 진행합니다."),
    "어깨": ("하체 또는 등", "어제 어깨를 운동했으므로 어깨 관절 부담을 줄이고 하체 또는 등 중심으로 진행합니다."),
    "팔": ("하체 또는 전신 가벼운 루틴", "어제 팔을 운동했으므로 팔 보조근 사용을 줄이고 하체나 가벼운 전신 루틴을 추천합니다."),
    "전신": ("회복 루틴", "어제 전신을 운동했으므로 오늘은 회복, 가벼운 유산소, 코어, 스트레칭 중심이 좋습니다."),
    "유산소": ("근력 운동", "어제 유산소를 했으므로 오늘은 근력 운동으로 자극을 바꿉니다."),
}

EXERCISE_POOLS = {
    "gym_hypertrophy_push": [
        ("벤치프레스", "가슴과 삼두를 함께 사용하는 대표적인 근비대 운동입니다."),
        ("인클라인 덤벨프레스", "상부 가슴과 어깨 전면을 안정적으로 자극합니다."),
        ("덤벨 숄더프레스", "어깨 근육과 상체 밀기 힘을 함께 기릅니다."),
        ("케이블 플라이", "가슴 수축감을 집중적으로 느끼기 좋은 보조 운동입니다."),
        ("케이블 푸시다운", "삼두 보조 볼륨을 채우기 좋은 운동입니다."),
    ],
    "gym_hypertrophy_pull": [
        ("랫풀다운", "등 너비와 광배근 자극을 만들기 좋은 운동입니다."),
        ("케이블로우", "등 중앙부와 견갑 움직임을 안정적으로 훈련합니다."),
        ("시티드 로우", "허리 부담을 줄이며 등 볼륨을 채우기 좋습니다."),
        ("페이스풀", "후면 어깨와 상부 등 안정성에 도움이 됩니다."),
        ("덤벨 컬", "팔 보조 운동으로 이두 볼륨을 더합니다."),
    ],
    "gym_hypertrophy_legs": [
        ("레그프레스", "하체 전반에 충분한 볼륨을 주기 좋은 머신 운동입니다."),
        ("루마니안 데드리프트", "햄스트링과 둔근을 중심으로 힌지 패턴을 훈련합니다."),
        ("레그컬", "햄스트링을 집중적으로 보완합니다."),
        ("레그익스텐션", "대퇴사두근을 보조적으로 자극합니다."),
        ("카프레이즈", "종아리 근육을 마무리로 자극합니다."),
    ],
    "gym_strength": [
        ("스쿼트", "하체와 코어를 함께 사용하는 대표적인 복합 운동입니다."),
        ("벤치프레스", "상체 밀기 근력을 키우는 핵심 운동입니다."),
        ("데드리프트", "후면 사슬과 전신 힘을 기르는 고강도 복합 운동입니다."),
        ("오버헤드프레스", "어깨와 코어 안정성을 함께 요구하는 근력 운동입니다."),
        ("바벨로우", "등과 견갑 안정성을 강화하는 당기기 운동입니다."),
        ("파머스 캐리", "악력, 코어, 전신 안정성을 함께 기릅니다."),
    ],
    "home_beginner_fullbody": [
        ("맨몸 스쿼트", "하체와 기본 움직임을 익히는 쉬운 전신 운동입니다."),
        ("무릎 푸시업", "상체 밀기 패턴을 부담 낮게 익힙니다."),
        ("힙브릿지", "둔근과 허리 주변 안정성을 기릅니다."),
        ("버드독", "코어 안정성과 균형 감각을 안전하게 훈련합니다."),
        ("플랭크", "몸통을 버티는 기본 코어 운동입니다."),
    ],
    "home_fat_loss": [
        ("맨몸 스쿼트", "큰 근육을 사용해 짧은 시간에 활동량을 높입니다."),
        ("마운틴 클라이머", "코어와 심박수 상승을 함께 노릴 수 있습니다."),
        ("런지", "하체 근력과 균형 감각을 함께 기릅니다."),
        ("푸시업", "상체 근력과 전신 긴장 유지에 도움이 됩니다."),
        ("제자리 걷기", "초보자도 부담 없이 심박수를 올릴 수 있습니다."),
    ],
    "outdoor_fat_loss": [
        ("빠르게 걷기", "하체 피로가 있어도 강도를 조절하기 쉬운 유산소입니다."),
        ("벤치 딥스", "야외 벤치를 활용한 상체 보조 운동입니다."),
        ("플랭크", "장소 제약이 적은 코어 운동입니다."),
        ("가벼운 조깅", "심박수를 올리되 무리하지 않게 진행합니다."),
        ("계단 오르기", "하체 상태가 괜찮은 날에 활동량을 높이기 좋습니다."),
    ],
    "no_equipment_mobility": [
        ("의자 스쿼트", "무릎 부담을 줄이며 앉고 일어나는 패턴을 익힙니다."),
        ("월싯", "기구 없이 하체와 코어 버티는 힘을 기릅니다."),
        ("슈퍼맨", "등과 둔근 후면 근육을 가볍게 깨웁니다."),
        ("데드버그", "허리 부담을 줄이며 코어를 안정화합니다."),
        ("흉추 회전", "굽은 자세와 등 가동성 개선에 도움이 됩니다."),
    ],
    "posture_health": [
        ("버드독", "허리 부담을 낮추며 코어 안정성을 기릅니다."),
        ("데드버그", "복부 조절과 골반 안정성에 도움이 됩니다."),
        ("힙브릿지", "둔근 활성화와 골반 안정성을 돕습니다."),
        ("흉추 회전", "상체 회전 가동성을 부드럽게 회복합니다."),
        ("벽 천사 운동", "어깨와 등 정렬을 가볍게 연습합니다."),
        ("가벼운 스트레칭", "운동 후 긴장을 낮추는 마무리 동작입니다."),
    ],
    "recovery_routine": [
        ("가볍게 걷기", "전신 피로를 풀고 혈류를 높이는 회복 운동입니다."),
        ("버드독", "부담 없이 코어 안정성을 유지합니다."),
        ("데드버그", "허리 부담이 적은 회복형 코어 운동입니다."),
        ("고양이 소 자세", "척추 주변 긴장을 부드럽게 낮춥니다."),
        ("흉추 회전", "등과 어깨 주변 가동성을 회복합니다."),
        ("호흡 스트레칭", "운동 강도를 낮추고 회복을 돕습니다."),
    ],
    "beginner_fullbody": [
        ("고블릿 스쿼트", "가벼운 덤벨이나 물건으로 하체 패턴을 익힙니다."),
        ("인클라인 푸시업", "상체 밀기 동작을 쉬운 각도로 연습합니다."),
        ("밴드 로우", "등 당기기 패턴을 안전하게 익힙니다."),
        ("힙힌지 연습", "허리 대신 엉덩이를 쓰는 움직임을 배웁니다."),
        ("플랭크", "코어 버티는 힘을 기릅니다."),
    ],
    "intermediate_upper": [
        ("벤치프레스", "상체 밀기 힘과 가슴 볼륨을 확보합니다."),
        ("랫풀다운", "등 너비와 당기기 패턴을 강화합니다."),
        ("덤벨 숄더프레스", "어깨 근력과 안정성을 함께 기릅니다."),
        ("케이블로우", "등 중앙부 볼륨을 보완합니다."),
        ("페이스풀", "후면 어깨와 자세 안정성을 챙깁니다."),
    ],
    "intermediate_lower": [
        ("스쿼트", "하체 전반과 코어 안정성을 함께 기릅니다."),
        ("레그프레스", "하체 볼륨을 안정적으로 채웁니다."),
        ("루마니안 데드리프트", "햄스트링과 둔근을 강화합니다."),
        ("레그컬", "햄스트링 보조 볼륨을 더합니다."),
        ("플랭크", "하체 운동 후 코어 안정성을 마무리합니다."),
    ],
    "advanced_split": [
        ("벤치프레스", "고강도 상체 밀기 메인 운동입니다."),
        ("스쿼트", "하체와 전신 근력의 핵심 운동입니다."),
        ("오버헤드프레스", "어깨와 코어 안정성을 함께 요구합니다."),
        ("바벨로우", "등 두께와 당기기 힘을 강화합니다."),
        ("딥스", "가슴과 삼두를 보조적으로 강하게 자극합니다."),
        ("행잉 레그레이즈", "고강도 루틴 후 코어를 보완합니다."),
        ("가벼운 사이클", "긴 운동 후 회복을 돕는 마무리 유산소입니다."),
    ],
}


def _routine_type(data):
    if data.yesterday_workout == "전신":
        return "회복 루틴"
    if data.preference == "체계적인 분할 루틴":
        if data.days_per_week == "4회":
            return "상하체 2분할 반복"
        if data.days_per_week == "5회 이상":
            return "고급 4분할 루틴"
        if data.days_per_week == "3회":
            return "Push/Pull/Legs 3분할"
    if data.fitness_goal == "체지방 감량":
        return "유산소와 근력 병행 순환 루틴"
    if data.fitness_goal == "근력 향상" and data.experience_level in ["중급자", "상급자"]:
        return "근력 중심 분할 루틴"
    if data.experience_level == "처음 시작":
        return "전신 기초 루틴"
    if data.days_per_week == "2회":
        return "전신 A/B 루틴" if data.experience_level == "초급자" else "상체/하체 2분할"
    if data.days_per_week == "3회":
        return "전신 3회 루틴" if data.experience_level == "초급자" else "Push/Pull/Legs 기초형"
    if data.days_per_week == "4회":
        return "상하체 2분할 반복"
    return "PPL과 약점 보완 루틴"


def _select_pool(data, today_label):
    if data.yesterday_workout == "전신":
        return "recovery_routine"
    if data.fitness_goal == "자세 교정/건강 관리":
        return "posture_health" if data.workout_place != "기구 거의 없음" else "no_equipment_mobility"
    if data.fitness_goal == "체지방 감량" and data.workout_place == "야외":
        return "outdoor_fat_loss"
    if data.fitness_goal == "체지방 감량" and data.workout_place == "집":
        return "home_fat_loss"
    if data.experience_level == "처음 시작" and data.workout_place == "집":
        return "home_beginner_fullbody"
    if data.experience_level in ["처음 시작", "초급자"] and data.workout_place != "헬스장":
        return "beginner_fullbody"
    if data.fitness_goal == "근력 향상" and data.workout_place == "헬스장":
        return "gym_strength"
    if data.fitness_goal == "근비대" and data.workout_place == "헬스장":
        if "등" in today_label:
            return "gym_hypertrophy_pull"
        if "하체" in today_label:
            return "gym_hypertrophy_legs"
        return "gym_hypertrophy_push"
    if data.experience_level == "상급자":
        return "advanced_split"
    if "하체" in today_label:
        return "intermediate_lower"
    if "상체" in today_label or "가슴" in today_label or "등" in today_label:
        return "intermediate_upper"
    return "beginner_fullbody"


def _limit_count(data):
    time_count = TIME_LIMITS[data.available_time]["count"]
    exp_count = EXPERIENCE_GUIDES[data.experience_level]["count"]
    if data.experience_level == "처음 시작":
        return min(time_count, 5)
    if data.experience_level == "상급자" and data.available_time in ["60~90분", "90분 이상"]:
        return max(time_count, 6)
    return min(time_count, exp_count)


def _build_exercises(data, pool_name):
    goal = GOAL_GUIDES[data.fitness_goal]
    experience = EXPERIENCE_GUIDES[data.experience_level]
    count = _limit_count(data)
    pool = EXERCISE_POOLS[pool_name][:count]
    exercises = []

    for name, description in pool:
        reps = goal["reps"]
        rest = goal["rest"]
        sets = experience["sets"]

        if data.available_time == "30분 이하":
            sets = "2세트" if data.experience_level == "처음 시작" else "2~3세트"
            rest = "30~45초"
        if data.fitness_goal == "근력 향상" and data.experience_level in ["처음 시작", "초급자"]:
            reps = "6~8회"
            rest = "90~120초"

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


def _weekly_plan(data):
    if data.days_per_week == "2회":
        if data.experience_level in ["처음 시작", "초급자"]:
            return [
                "1일차: 전신 A - 스쿼트, 푸시, 풀, 코어 중심",
                "2일차: 전신 B - 힌지, 런지, 상체 보완, 가벼운 유산소",
                "나머지 날: 20분 걷기, 가벼운 스트레칭, 충분한 휴식",
            ]
        return [
            "1일차: 상체 - 가슴, 등, 어깨 중심",
            "2일차: 하체 - 스쿼트, 힌지, 코어 중심",
            "나머지 날: 회복 걷기와 관절 가동성 운동",
        ]
    if data.days_per_week == "3회":
        if data.experience_level in ["처음 시작", "초급자"]:
            return [
                "1일차: 전신 기초 루틴",
                "2일차: 전신 기초 루틴과 코어",
                "3일차: 전신 루틴과 가벼운 유산소",
                "운동 사이 하루 이상 휴식하거나 걷기 위주로 회복",
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
            "5일차: 약점 부위 보완 또는 기술 연습",
            "주 5회 이상은 수면, 식사, 관절 피로를 확인하며 휴식일을 조정",
        ]
    return [
        "1일차: Push",
        "2일차: Pull",
        "3일차: Legs",
        "4일차: 전신 순환 또는 약점 보완",
        "5일차: 가벼운 유산소와 코어",
        "피로가 누적되면 하루는 완전 휴식으로 바꾸기",
    ]


def recommend(data):
    goal = GOAL_GUIDES[data.fitness_goal]
    experience = EXPERIENCE_GUIDES[data.experience_level]
    time_guide = TIME_LIMITS[data.available_time]
    today_label, today_reason = TODAY_FOCUS[data.yesterday_workout]
    routine = _routine_type(data)
    pool_name = _select_pool(data, today_label)
    exercises = _build_exercises(data, pool_name)

    if data.fitness_goal == "근비대" and data.experience_level == "중급자":
        user_type = "중급자 근비대 분할 루틴형"
    elif data.experience_level == "처음 시작":
        user_type = "운동 처음 시작자를 위한 기초 적응형 루틴"
    elif data.experience_level == "상급자":
        user_type = f"상급자 {goal['label']} 고강도 관리형 루틴"
    else:
        user_type = f"{experience['label']} {goal['label']} 맞춤 루틴"

    main_recommendation = (
        f"현재 목표가 '{data.fitness_goal}'이고 운동 경험이 '{data.experience_level}'이므로 "
        f"{goal['focus']}의 {routine}을 추천합니다. "
        f"주 {data.days_per_week} 운동이 가능하고 장소가 '{data.workout_place}'이므로 "
        f"{time_guide['pace']}으로 구성했습니다. "
        f"어제 운동은 '{data.yesterday_workout}'이어서 오늘은 {today_label} 중심으로 진행합니다."
    )

    today_focus = f"오늘 추천 방향: {today_label}. {today_reason}"
    intensity_guide = (
        f"{experience['rpe']}를 기준으로 진행하세요. "
        f"{data.preference} 선호를 반영하되, {experience['style']}을 우선합니다. "
        f"{goal['note']}"
    )
    recovery_tip = (
        f"어제 운동 부위가 '{data.yesterday_workout}'이므로 오늘 루틴 후에는 해당 부위의 피로를 확인하세요. "
        "운동 후 5~10분 정리 운동, 가벼운 스트레칭, 충분한 수분 섭취와 수면을 권장합니다."
    )
    if data.yesterday_workout == "하체":
        recovery_tip += " 하체 피로가 남아 있으면 달리기나 계단 운동 강도를 낮추세요."
    if data.days_per_week == "5회 이상":
        recovery_tip += " 주 5회 이상 운동은 과훈련을 피하기 위해 휴식일을 계획적으로 넣어야 합니다."

    caution = (
        "이 앱은 일반적인 운동 루틴 추천을 제공하는 학습용 웹앱이며 의학적 진단이나 치료 목적이 아닙니다. "
        "날카로운 통증, 어지러움, 질환, 부상 이력이 있는 경우 운동을 중단하고 전문가와 상담하세요. "
        "모든 운동은 정확한 자세와 안전한 범위가 우선입니다."
    )

    return {
        "user_type": user_type,
        "routine_type": routine,
        "main_recommendation": main_recommendation,
        "today_focus": today_focus,
        "recommended_exercises": exercises,
        "weekly_plan": _weekly_plan(data),
        "intensity_guide": intensity_guide,
        "recovery_tip": recovery_tip,
        "caution": caution,
        "debug_info": {
            "selected_goal": data.fitness_goal,
            "selected_experience": data.experience_level,
            "selected_days": data.days_per_week,
            "selected_place": data.workout_place,
            "selected_yesterday": data.yesterday_workout,
            "selected_time": data.available_time,
            "selected_preference": data.preference,
            "selected_exercise_pool": pool_name,
            "selected_today_focus": today_label,
        },
    }
