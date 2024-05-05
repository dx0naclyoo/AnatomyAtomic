import asyncio
from abc import ABC, abstractmethod

import redis
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from anatomic.settings import settings


class DatabaseSQL(ABC):

    @abstractmethod
    async def get_session(self) -> AsyncSession:
        pass


class Postgresql(DatabaseSQL):
    def __init__(self, url: str, echo: bool = False) -> None:
        self.engine = create_async_engine(url, echo=echo)
        self.session_factory = async_sessionmaker(
            bind=self.engine, autoflush=False, autocommit=False, expire_on_commit=False
        )

    async def get_session(self) -> AsyncSession:
        async with self.session_factory() as session:
            yield session


postgresql = Postgresql(url=settings.database.postgres_url, echo=settings.database.echo)


class RedisTools:  # Изменить на URL
    __redis = redis.from_url(settings.database.redis_url)
    default_expire = settings.database.redis_default_expire

    @classmethod
    def set(cls, key: str, value: str):
        try:
            cls.__redis.set(key, value)
            cls.expire(key, cls.default_expire)
        except Exception as e:
            print("Error:", e)

    @classmethod
    def get(cls, key: str) -> str:
        item: bytes = cls.__redis.get(key)
        if item:
            return item.decode("utf-8")

    @classmethod
    def delete(cls, key):
        cls.__redis.delete(key)

    @classmethod
    def get_keys(cls):
        return cls.__redis.keys(pattern="*")

    @classmethod
    def expire(cls, key: str, seconds: int) -> None:
        cls.__redis.expire(key, seconds)


