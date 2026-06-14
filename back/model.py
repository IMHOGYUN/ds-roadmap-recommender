from pydantic import BaseModel


class RecommendRequest(BaseModel):
    interest: str
    grade: str
    difficulty: str
    study_time: str
    goal: str


class RecommendResponse(BaseModel):
    user_type: str
    main_recommendation: str
    skills: list[str]
    project_idea: str
    study_plan: list[str]
    caution: str