from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import RecommendRequest, RecommendResponse
from recommender import recommend

app = FastAPI(title="Data Science Roadmap Recommendation API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    return {"message": "FastAPI recommendation server is running"}


@app.post("/recommend", response_model=RecommendResponse)
def get_recommendation(request: RecommendRequest):
    result = recommend(request)
    return result