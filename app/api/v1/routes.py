from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "healthy"}


@router.get("/products")
async def get_products_v1():
    # V1 implementation
    return {"version": "1", "products": [...]}


# Later, in v2:
# /api/v2/routes.py
@router.get("/products")
async def get_products_v2():
    # V2 implementation with breaking changes
    return {"version": "2", "products": {...}}
