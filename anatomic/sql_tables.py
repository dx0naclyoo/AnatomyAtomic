from typing import List

from sqlalchemy import Integer, String, ForeignKey, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    progress: Mapped[list] = mapped_column(ARRAY(String), nullable=True)

    def __str__(self):
        return f"{self.id=}, {self.username=}, {self.email=}, {self.progress=}"

    def __repr__(self):
        return f'{"id": self.id, "username": self.username, "email": self.email, "progress": self.progress}'


class Section(Base):  # Разделы
    __tablename__ = "section"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    slug: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    topic_list: Mapped[List["Topic"]] = relationship(
        "Topic",
        back_populates="section",
        cascade="save-update, merge, delete",
        passive_deletes=True,
    )
    keywords: Mapped[list] = mapped_column(ARRAY(String))

    def __str__(self):
        return f"{self.id=}, {self.name=}, {self.description=}, {self.keywords=}, {self.slug=}, {self.topic_list=}"

    def __repr__(self):
        return f'{"id": self.id, "name": self.name, "topic_list": self.topic_list, "description": self.description, "keywords": self.keywords, "slug": self.slug}'


class Topic(Base):  # Темы
    __tablename__ = "topic"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    slug: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)

    section: Mapped[Section] = relationship("Section", back_populates="topic_list")
    section_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("section.id", ondelete="CASCADE")
    )

    keywords: Mapped[list] = mapped_column(ARRAY(String))

    # def __str__(self):
    #     return f"{self.id=}, {self.name=}, {self.content=}, {self.section_id=}, {self.keywords=}, {self.slug=}"

    def __repr__(self):
        return f'"id": {self.id}, "name": "{self.name}", "content": "{self.content}", "section_id": {self.section_id}, "keywords": {self.keywords}, "slug": "{self.slug}"'
