from typing import Optional

from pydantic import BaseModel


class RecommendRequest(BaseModel):
    recommendation_mode: str
    fitness_goal: str
    experience_level: str
    days_per_week: str
    workout_place: str
    yesterday_workout: str


class Exercise(BaseModel):
    name: str
    sets: str
    reps: str
    rest: str
    description: str


class DebugInfo(BaseModel):
    recommendation_mode: str
    selected_exercise_pool: str
    selected_today_focus: str
    place_rule: str
    goal_rule: str
    level_rule: str
    days_rule: str


class RecommendResponse(BaseModel):
    user_type: str
    routine_type: str
    mode_summary: str
    experience_highlight: str
    main_recommendation: str
    today_focus: str
    recommended_exercises: list[Exercise]
    weekly_plan: list[str]
    intensity_guide: str
    recovery_tip: str
    caution: str
    debug_info: Optional[DebugInfo] = None
