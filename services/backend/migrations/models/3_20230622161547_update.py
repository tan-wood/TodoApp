from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "tasks" ADD "priority_level" INT NOT NULL;
        ALTER TABLE "tasks" ADD "due_date" TIMESTAMPTZ NOT NULL;
        ALTER TABLE "tasks" ALTER COLUMN "comments" DROP NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "tasks" DROP COLUMN "priority_level";
        ALTER TABLE "tasks" DROP COLUMN "due_date";
        ALTER TABLE "tasks" ALTER COLUMN "comments" SET NOT NULL;"""
