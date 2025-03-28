from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.api.deps import get_db_session
from app.models.user import User
from app.models.product import Product

router = APIRouter()


@router.get("/users/{user_id}")
async def get_user(user_id: int, db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/users")
async def list_users(db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(select(User).order_by(User.name))
    users = result.scalars().all()
    return users


@router.post("/users")
async def create_user(
    email: str, name: str, db: AsyncSession = Depends(get_db_session)
):
    user = User(email=email, name=name)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


@router.get("/products")
async def list_products(db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(select(Product).order_by(Product.name))
    products = result.scalars().all()
    return products


@router.get("/health")
async def health_check():
    return {"status": "healthy"}


@router.get("/db-test")
async def test_db(db: AsyncSession = Depends(get_db_session)):
    try:
        # Test query
        result = await db.execute(select(User).limit(1))
        user = result.scalar_one_or_none()
        return {"status": "database connected", "test": user.id if user else None}
    except Exception as e:
        return {"status": "database error", "detail": str(e)}


# Later, in v2:
# /api/v2/routes.py
@router.get("/products")
async def get_products_v2():
    # V2 implementation with breaking changes
    return {"version": "2", "products": {...}}
