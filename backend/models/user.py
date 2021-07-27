from typing import List
from pydantic import BaseModel
from models import db
from .skill import SkillSchema

users_skills = db.Table('users_skills',
                        db.Column('skill_id', db.Integer, db.ForeignKey(
                            'skill.id'), primary_key=True),
                        db.Column('user_id', db.Integer, db.ForeignKey(
                            'user.id'), primary_key=True)
                        )


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    skills = db.relationship('Skill', secondary=users_skills, lazy='subquery',
                             backref=db.backref('users', lazy=True))

    def __repr__(self):
        return "<User %r>" % self.name


class UserSchema(BaseModel):
    id: int
    name: str
    skills: List[SkillSchema]

    class Config:
        orm_mode = True


class UsersResponse(BaseModel):
    items: List[UserSchema]
