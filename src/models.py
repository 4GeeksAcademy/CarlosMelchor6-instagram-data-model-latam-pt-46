from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()

class Follow(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    follower_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    followed_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    # USER RELATIONSHIP
    follower: Mapped["User"] = relationship(
        foreign_keys=[follower_id], back_populates="following")
    followed: Mapped["User"] = relationship(
        foreign_keys=[followed_id], back_populates="followers")

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    user_name: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(
        String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(
        String(50),nullable=False)

    # One to many relationship
    followers: Mapped[List["Follow"]] = relationship(
        foreign_keys=[Follow.followed_id], back_populates="followed")
    
    following: Mapped[List["Follow"]] = relationship(
        foreign_keys=[Follow.follower_id], back_populates="follower")

    posts: Mapped[List["Post"]] = relationship(back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }




class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(
        String(250), unique=True, nullable=False)

    # USER RELATIONSHIP
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="posts")

    # Comment relationship
    comments: Mapped["Comment"] = relationship(back_populates="post")


class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(
        String(150), unique=True, nullable=False)

    author_id:  Mapped[int] = mapped_column(ForeignKey("user.id"))
    author: Mapped["User"] = relationship(back_populates="comments")

    # Post relationship
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    post: Mapped["Post"] = relationship(back_populates="comments")
