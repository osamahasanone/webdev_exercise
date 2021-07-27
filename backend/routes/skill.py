from flask import Blueprint, current_app
from models.skill import Skill, SkillsResponse
from models import db

skill_bp = Blueprint('skill_bp', __name__)


@skill_bp.route("/skills", methods=["POST"])
def create_skills_batch():
    skill_names = ['Python', 'Flask', 'Bottle', 'FastAPI',
                   'SQL', 'HTML5', 'CSS3', 'Javascript', 'React', 'Angular', 'Vue.Js']
    with current_app._get_current_object().app_context():
        for skill_name in skill_names:
            db.session.add(Skill(name=skill_name))
        db.session.commit()
    return "Skills created", 201


@skill_bp.route("/skills", methods=["GET"])
def skills():
    with current_app._get_current_object().app_context():
        results = Skill.query.all()
    return SkillsResponse(items=results).json()
