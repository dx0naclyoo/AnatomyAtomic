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
        return f'"id": {self.id}, "username": {self.username}, "email": {self.email}, "progress": {self.progress}'


class Section(Base):  # Разделы
    __tablename__ = "section"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    slug: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    keywords: Mapped[list] = mapped_column(ARRAY(String))

    subsection: Mapped[List["SubSection"]] = relationship(
        "SubSection",
        back_populates="section",
        cascade="save-update, merge, delete",
        passive_deletes=True,
    )

    def __repr__(self):
        return f'"id": {self.id}, "name": "{self.name}", "description": "{self.description}", ' \
               f'"keywords": {self.keywords}, "slug": "{self.slug}"'


class SubSection(Base):
    __tablename__ = "subsection"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    slug: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    keywords: Mapped[list] = mapped_column(ARRAY(String))

    section: Mapped[Section] = relationship("Section", back_populates="subsection")
    section_id: Mapped[int] = mapped_column(Integer, ForeignKey("section.id", ondelete="CASCADE"))

    topic_list: Mapped[List["Topic"]] = relationship(
        "Topic",
        back_populates="subsection",
        cascade="save-update, merge, delete",
        passive_deletes=True,
    )

    def __repr__(self):
        return f'"id": {self.id}, "name": "{self.name}", ' \
               f'"description": "{self.description}", ' \
               f'"slug": "{self.slug}", "keywords": {self.keywords}, "section_id": {self.section_id}'


class Topic(Base):  # Темы
    __tablename__ = "topic"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    slug: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    keywords: Mapped[list] = mapped_column(ARRAY(String))

    subsection: Mapped[Section] = relationship("SubSection", back_populates="topic_list")
    subsection_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("subsection.id", ondelete="CASCADE")
    )

    content: Mapped["TopicContent"] = relationship(
        "TopicContent",
        back_populates="topic",
        cascade="save-update, merge, delete",
        passive_deletes=True,
    )

    def __repr__(self):
        return f'"id": {self.id}, "name": "{self.name}", ' \
               f'"slug": "{self.slug}", "keywords": {self.keywords}, ' \
               f'"subsection_id": {self.subsection_id}'


class TopicContent(Base):
    __tablename__ = "topic_content"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column(String)

    topic_id: Mapped[int] = mapped_column(Integer, ForeignKey("topic.id", ondelete="CASCADE"))
    topic: Mapped["Topic"] = relationship(
        "Topic",
        back_populates="content",
    )

    def __repr__(self):
        return f'"id": {self.id}, "content": "{self.content}", "topic_id": {self.topic_id}'
