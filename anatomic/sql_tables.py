from typing import List

from sqlalchemy import Integer, String, ForeignKey, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
    progress: Mapped[list] = mapped_column(ARRAY(String), nullable=True)

    def __str__(self) -> str:
        return f"User( {self.id=} {self.username=} {self.email=} {self.progress=} )"


class Section(Base):  # Разделы
    __tablename__ = "section"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    topic_list: Mapped[List["Topic"]] = relationship("Topic", back_populates="section")
    keywords: Mapped[list] = mapped_column(ARRAY(String))

    def __str__(self) -> str:
        return f"Section( {self.id=} {self.name=} {self.topic_list=} {self.keywords=} )"


class Topic(Base):  # Темы
    __tablename__ = "topic"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)
    content: Mapped[str] = mapped_column(String)

    section: Mapped[Section] = relationship("Section", back_populates="topic_list")
    section_id: Mapped[int] = mapped_column(Integer, ForeignKey("section.id"))

    keywords: Mapped[list] = mapped_column(ARRAY(String))

    def __str__(self) -> str:
        return f"Topic( {self.id=} {self.name=} {self.content=} {self.section_id=} {self.keywords=} )"
