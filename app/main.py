from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine, Base
from app.routers.auth import router as auth_router
from app.routers import auth, users, posts, categories, admin

# ✅ КРИТИЧНО: Импортируем модели, чтобы SQLAlchemy их увидел
from app.models.user import User
from app.models.post import Post
from app.models.category import Category

app = FastAPI(title="FastAPI Blog Backend")

app.include_router(auth_router, prefix="/api/v1", tags=["auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(posts.router, prefix="/api/v1/posts", tags=["posts"])
app.include_router(categories.router, prefix="/api/v1/categories", tags=["categories"])
app.include_router(admin.router, prefix="/api/v1", tags=["admin"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Теперь создаст все таблицы
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "FastAPI Blog Backend"}
