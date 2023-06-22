from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "tasks" DROP CONSTRAINT "tasks_user_id_id_fkey";
        ALTER TABLE "tasks" RENAME COLUMN "user_id_id" TO "user_id";
        ALTER TABLE "tasks" ADD CONSTRAINT "tasks_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "users" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "tasks" DROP CONSTRAINT "tasks_user_id_fkey";
        ALTER TABLE "tasks" RENAME COLUMN "user_id" TO "user_id_id";
        ALTER TABLE "tasks" ADD CONSTRAINT "tasks_user_id_id_fkey" FOREIGN KEY ("user_id_id") REFERENCES "users" ("id") ON DELETE CASCADE;"""
