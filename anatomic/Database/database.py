import asyncio
from abc import ABC, abstractmethod

from fastapi import Depends
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


postgresql = Postgresql(url=settings.database.url, echo=settings.database.echo)


