from models import db
from models.skill import Skill


def fix_name(name):
    '''prepare skill name to meet db constraints'''
    return name.lower()


def fix_names(names):
    '''prepare list of skill names to meet db constraints'''
    return [fix_name(name) for name in names]


def insert_missing(names):
    '''insert skills if not found'''
    for name in names:
        if not Skill.query.filter_by(name=name).first():
            skill = Skill(name=name)
            db.session.add(skill)


def db_skill(name):
    '''fetch matching skill from db

    parameters:
    name: skill name to find
    '''
    return Skill.query.filter_by(name=fix_name(name)).first()


def db_skills(names, do_insert=False):
    '''fetch matching skills from db

    parameters:
    names: skill names to find
    do_insert: if True, insert missing
    '''
    fixed_names = fix_names(names)
    if do_insert:
        insert_missing(fixed_names)
    return [skill for skill in Skill.query.all()if skill.name in fixed_names]
