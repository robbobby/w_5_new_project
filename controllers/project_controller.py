from flask import Blueprint, Flask, redirect, render_template, request
from models.project import Project
import repositories.project_db as project_db

project_blueprint = Blueprint('projects', __name__)


            ##### Project Home Page #####

@project_blueprint.route('/projects', methods=['GET'])
def projects():
    projects = project_db.get_all()
    return render_template('projects/index.html', projects=projects)



@project_blueprint.route('/projects/new')
def add_project_form():
    pass

@project_blueprint.route('/project/<emp_id>/<pro_id>')
def project_home_page(emp_id, pro_id):
    # get tasks for employee
    # get tasks for the project which employee does now own
    # show tasks for employee
    # show tasks that employee can take on

    pass