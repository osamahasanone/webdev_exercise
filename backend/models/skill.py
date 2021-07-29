from typing import List
from pydantic import BaseModel
from models import db


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __str__(self):
        return self.name


class SkillSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class SkillsResponse(BaseModel):
    items: List[SkillSchema]
