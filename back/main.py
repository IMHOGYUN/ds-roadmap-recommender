from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import RecommendRequest, RecommendResponse
from recommender import recommend

app = FastAPI(
    title="Workout Routine Recommendation API",
    description="여름방학 맞춤 운동 루틴을 추천하는 FastAPI 백엔드입니다.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    return {"message": "Workout routine recommendation server is running"}


@app.post("/recommend", response_model=RecommendResponse)
def get_recommendation(request: RecommendRequest):
    result = recommend(request)
    return result
