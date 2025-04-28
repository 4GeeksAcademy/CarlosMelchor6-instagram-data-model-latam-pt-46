from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    user_name : Mapped[str]= mapped_column(String(50), unique=True, nullable=False)
    first_name : Mapped[str]= mapped_column(String(50), unique=True, nullable=False)
    last_name : Mapped[str]= mapped_column(String(50), unique=True, nullable=False)


    #One to many relationship
    follower: Mapped[List["Follower"]] = relationship(back_populates="user")
    follows: Mapped[List["Follows"]] = relationship(back_populates="user")
    post: Mapped[List["Post"]] = relationship(back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }


class Follower(db.Model):
    id : Mapped[int] = mapped_column(primary_key=True)
    user_name : Mapped[str]= mapped_column(String(50), unique=True, nullable=False)

    #USER RELATIONSHIP
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="follower")

class Follows(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name : Mapped[str]= mapped_column(String(50), unique=True, nullable=False)

    #USER RELATIONSHIP
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="follows")

class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    content : Mapped[str] = mapped_column(String(250), unique=True, nullable=False)

    #USER RELATIONSHIP
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="post")

class comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text : Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    author_id : Mapped[int] = mapped_column(primary_key=True)
    from_post_id : Mapped[int] = mapped_column(primary_key=True)