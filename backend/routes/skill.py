from flask import Blueprint, current_app
from models.skill import Skill, SkillsResponse
from models import db
from sqlalchemy import exc

skill_bp = Blueprint('skill_bp', __name__)


@skill_bp.route("/skills", methods=["GET"])
def get_skills():
    '''get all skills'''
    with current_app._get_current_object().app_context():
        results = Skill.query.all()
    return SkillsResponse(items=results).json()
