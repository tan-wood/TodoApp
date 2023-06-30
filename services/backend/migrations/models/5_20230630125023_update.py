from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "tasks" ALTER COLUMN "title" TYPE VARCHAR(300) USING "title"::VARCHAR(300);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "tasks" ALTER COLUMN "title" TYPE VARCHAR(225) USING "title"::VARCHAR(225);"""
