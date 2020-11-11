from flask import Blueprint, Flask, redirect, render_template, request
from models.project import Project
import repositories.project_db as project_db
from repositories import company_db
import controllers.employee_controller as emp_control

project_blueprint = Blueprint('projects', __name__)


            ##### Project Home Page #####

@project_blueprint.route('/projects', methods=['GET'])
def projects():
    projects = project_db.get_all()
    return render_template('projects/index.html', projects=projects)



@project_blueprint.route('/projects/new/<com_id>/<emp_id>')
def add_project_form(com_id, emp_id):
    return render_template('projects/new.html', com_id=com_id, emp_id=emp_id)\

@project_blueprint.route('/projects/new/<com_id>/<emp_id>', methods=['POST'])
def add_project(com_id, emp_id):
    company = company_db.get(com_id)
    project = Project(request.form['project_name'], company)
    project_db.save(project)
    return emp_control.route_from_project_to_employee_home(emp_id, com_id)

@project_blueprint.route('/project/<emp_id>/<pro_id>')
def project_home_page(emp_id, pro_id):
    # get tasks for employee
    # get tasks for the project which employee does now own
    # show tasks for employee
    # show tasks that employee can take on
    pass