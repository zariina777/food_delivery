from sqlalchemy import Column, Integer
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker, declared_attr
from app.core.config import settings


class PreBase:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase) #создали баз класс от которого будем наслед и создавать модели
engine = create_async_engine(settings.DATABASE_URL, echo=False, future=True) # движок с котоорым подкд к БД
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, autocommit=False, autoflush=False, expire_on_commit=False)


async def get_async_session(): # функция вызывваем чтобы подкл к БД
    async with AsyncSessionLocal() as async_session:
        yield async_session