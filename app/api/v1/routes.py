from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db_session

router = APIRouter()


@router.get("/health")
async def health_check():
    return {"status": "healthy"}


@router.get("/db-test")
async def test_db(db: AsyncSession = Depends(get_db_session)):
    try:
        # Test query
        result = await db.execute("SELECT 1")
        return {"status": "database connected", "test": True}
    except Exception as e:
        return {"status": "database error", "detail": str(e)}
