from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "tasks" ALTER COLUMN "modified_at" TYPE TIMESTAMPTZ USING "modified_at"::TIMESTAMPTZ;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "tasks" ALTER COLUMN "modified_at" TYPE TIMESTAMPTZ USING "modified_at"::TIMESTAMPTZ;"""
