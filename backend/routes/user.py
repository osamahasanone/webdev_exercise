import random
from flask import request, Blueprint, current_app
from faker import Faker
from models.user import User, UsersResponse
from models.skill import Skill
from models import db

user_bp = Blueprint('user_bp', __name__)
fake = Faker()


@user_bp.route("/users", methods=["POST"])
def create_users_batch():
    with current_app._get_current_object().app_context():
        for x in range(10):
            user = User(name=fake.name())
            db.session.add(user)
        db.session.commit()
    return "Users created", 201


@user_bp.route("/users", methods=["DELETE"])
def delete_all_users():
    with current_app._get_current_object().app_context():
        User.query.delete()
        db.session.commit()
    return "Users deleted"


@user_bp.route("/users", methods=["GET"])
def users():
    with current_app._get_current_object().app_context():
        results = User.query.all()
    return UsersResponse(items=results).json()


@user_bp.route("/users/<id>/setskills", methods=["POST"])
def set_skill(id):
    with current_app._get_current_object().app_context():
        user = User.query.get(id)
        skills_data = request.get_json().get('skills')
        skills = [skill for skill in Skill.query.all()
                  if skill.name in skills_data]
        user.skills = skills
        db.session.commit()
    return "Skills set to user", 200


@user_bp.route("/userswithskill", methods=["GET"])
def have_skill():
    with current_app._get_current_object().app_context():
        skill_name = request.args.get('skill_name')
        skill = Skill.query.filter_by(name=skill_name).first()
        result = skill.users
        return UsersResponse(items=result).json()
