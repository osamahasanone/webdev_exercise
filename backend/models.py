from typing import List

from flask_sqlalchemy import SQLAlchemy
from pydantic import BaseModel

db = SQLAlchemy()


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return "<Skill %r>" % self.name


class SkillSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class SkillsResponse(BaseModel):
    items: List[SkillSchema]


skills = db.Table('skills',
                  db.Column('skill_id', db.Integer, db.ForeignKey(
                      'skill.id'), primary_key=True),
                  db.Column('user_id', db.Integer, db.ForeignKey(
                      'user.id'), primary_key=True)
                  )


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    skills = db.relationship('Skill', secondary=skills, lazy='subquery',
                             backref=db.backref('users', lazy=True))

    def __repr__(self):
        return "<User %r>" % self.name


class UserSchema(BaseModel):
    id: int
    name: str
    # skills: List[Skill]

    class Config:
        orm_mode = True


class UsersResponse(BaseModel):
    items: List[UserSchema]
