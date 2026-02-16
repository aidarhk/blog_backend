from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.core.security import get_current_active_admin
from app.models.user import User
from app.models.post import Post
from app.models.category import Category
from app.schemas.post import PostCreate, PostOut
from app.schemas.category import CategoryCreate, CategoryOut

router = APIRouter(prefix="/admin", tags=["admin"])

@router.post("/posts", response_model=PostOut, status_code=status.HTTP_201_CREATED)
def create_post(
    post: PostCreate, 
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_active_admin)
):
    # Проверяем уникальность slug
    db_post = db.query(Post).filter(Post.slug == post.slug).first()
    if db_post:
        raise HTTPException(status_code=400, detail="Slug already exists")
    
    new_post = Post(**post.dict(), author_id=current_admin.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/posts", response_model=List[PostOut])
def list_admin_posts(
    skip: int = 0, 
    limit: int = 10, 
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_active_admin)
):
    posts = db.query(Post).offset(skip).limit(limit).all()
    return posts

@router.post("/categories", response_model=CategoryOut, status_code=status.HTTP_201_CREATED)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_active_admin)
):
    # Проверяем уникальность slug
    db_category = db.query(Category).filter(Category.slug == category.slug).first()
    if db_category:
        raise HTTPException(status_code=400, detail="Slug already exists")
    
    new_category = Category(**category.dict())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

@router.get("/categories", response_model=List[CategoryOut])
def list_categories(
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_active_admin)
):
    categories = db.query(Category).all()
    return categories

# UPDATE поста
@router.put("/posts/{post_id}", response_model=PostOut)
def update_post(post_id: int, post: PostCreate, db: Session = Depends(get_db), current_admin: User = Depends(get_current_active_admin)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if not db_post: raise HTTPException(404, "Post not found")
    for field, value in post.dict(exclude_unset=True).items():
        setattr(db_post, field, value)
    db.commit()
    db.refresh(db_post)
    return db_post

# DELETE поста  
@router.delete("/posts/{post_id}", status_code=204)
def delete_post(post_id: int, db: Session = Depends(get_db), current_admin: User = Depends(get_current_active_admin)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if not db_post: raise HTTPException(404, "Post not found")
    db.delete(db_post)
    db.commit()

