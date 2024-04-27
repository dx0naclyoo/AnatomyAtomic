from typing import List

from sqlalchemy import DeclarativeBase, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
    progress: Mapped[list] = mapped_column(String)


class Section(Base):  # Разделы
    __tablename__ ='section'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    topic_list: Mapped[List["Topic"]] = relationship("Topic", back_populates="section")
    keywords: Mapped[str] = mapped_column(String, default="")


class Topic(Base):  # Темы
    __tablename__ = "topic"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    content: Mapped[str] = mapped_column(String)

    section: Mapped[Section] = relationship("Section", back_populates="topic_list")
    section_id: Mapped[int] = mapped_column(Integer, ForeignKey("section"))

    keywords: Mapped[str] = mapped_column(String, default="")
