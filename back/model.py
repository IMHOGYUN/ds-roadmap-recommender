from pydantic import BaseModel


class RecommendRequest(BaseModel):
    fitness_goal: str
    experience_level: str
    days_per_week: str
    workout_place: str
    yesterday_workout: str
    available_time: str
    preference: str


class Exercise(BaseModel):
    name: str
    sets: str
    reps: str
    rest: str
    description: str


class RecommendResponse(BaseModel):
    user_type: str
    routine_type: str
    main_recommendation: str
    today_focus: str
    recommended_exercises: list[Exercise]
    weekly_plan: list[str]
    intensity_guide: str
    recovery_tip: str
    caution: str
    debug_info: dict[str, str]
