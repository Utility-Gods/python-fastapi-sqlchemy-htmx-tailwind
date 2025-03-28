from typing import Optional, List
from datetime import datetime
from decimal import Decimal

class Queries:
    def __init__(self, pool):
        self.pool = pool

    # Users
    async def get_user(self, user_id: int):
        async with self.pool.acquire() as conn:
            return await conn.fetchrow(
                """
                SELECT * FROM users
                WHERE id = $1
                """, 
                user_id
            )

    async def list_users(self) -> List[dict]:
        async with self.pool.acquire() as conn:
            return await conn.fetch(
                """
                SELECT * FROM users
                ORDER BY name
                """
            )

    async def create_user(self, email: str, name: str):
        async with self.pool.acquire() as conn:
            return await conn.fetchrow(
                """
                INSERT INTO users (email, name)
                VALUES ($1, $2)
                RETURNING *
                """,
                email, name
            )

    # Products
    async def get_product(self, product_id: int):
        async with self.pool.acquire() as conn:
            return await conn.fetchrow(
                """
                SELECT * FROM products
                WHERE id = $1
                """,
                product_id
            )

    async def create_product(self, name: str, description: Optional[str], price: Decimal):
        async with self.pool.acquire() as conn:
            return await conn.fetchrow(
                """
                INSERT INTO products (name, description, price)
                VALUES ($1, $2, $3)
                RETURNING *
                """,
                name, description, price
            ) 