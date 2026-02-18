from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List  # ← ДОБАВИТЬ
from app.core.database import get_db
from app.models.category import Category
from app.models.post import Post
from app.schemas.category import CategoryOut
from app.schemas.post import PostOut

router = APIRouter()

@router.get("/", response_model=List[CategoryOut])
def get_categories(db: Session = Depends(get_db)):
    categories = db.query(Category).all()
    return categories

@router.get("/{slug}/posts", response_model=List[PostOut])
def get_category_posts(slug: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.slug == slug).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    posts = db.query(Post).filter(Post.category_id == category.id).offset(skip).limit(limit).all()
    return posts
