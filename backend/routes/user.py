import random
from flask import request, Blueprint, current_app
from models.user import User, UsersResponse
from models.skill import Skill
from models import db
from helpers import skill_helper, user_helper

user_bp = Blueprint('user_bp', __name__)


@user_bp.route("/users", methods=["POST"])
def create_users_batch():
    '''create dummy users'''
    with current_app._get_current_object().app_context():
        user_helper.create_dummy(n=10)
        db.session.commit()
    return "Users created", 201


@user_bp.route("/users", methods=["DELETE"])
def delete_all_users():
    '''delete all users'''
    with current_app._get_current_object().app_context():
        user_helper.delete_all()
        db.session.commit()
    return "Users deleted"


@user_bp.route("/users", methods=["GET"])
def get_users():
    '''get all users'''
    with current_app._get_current_object().app_context():
        results = User.query.all()
    return UsersResponse(items=results).json()


@user_bp.route("/users/<id>/setskills", methods=["POST"])
def set_skills(id):
    '''attach skills to a user

    parameters:
    id: user id

    body(json):
        {skills_names:["skill_name_1","skill_name_2","skill_name_3"]}

    responses:
    400: user id not found in db or skills_names not in body
    204: updated
    '''
    with current_app._get_current_object().app_context():
        user = User.query.get(id)
        if not user:
            return "Bad Request", 400
        skills_names = request.get_json().get('skills_names')
        if not skills_names:
            return "Bad Request", 400
        db_skills = skill_helper.db_skills(skills_names, do_insert=True)
        user.skills = db_skills
        db.session.commit()
    return "Skills set to user", 204


@user_bp.route("/userswithskill", methods=["GET"])
def have_skill():
    '''find users with a specific skill

    query parameters:
    skill_name(str): skill name 

    responses:
    400: skill_name not in query parameters
    404: skill_name not found
    200: OK
    '''
    with current_app._get_current_object().app_context():
        skill_name = request.args.get('skill_name')
        if not skill_name:
            return "Bad Request", 400
        db_skill = skill_helper.db_skill(skill_name)
        if not db_skill:
            return "Skill Not Found", 404
        result = db_skill.users
        return UsersResponse(items=result).json()
