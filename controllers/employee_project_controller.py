from flask import Blueprint, Flask, redirect, render_template, request
from models.employee_project import EmployeeProject

import repositories.employee_projects_db as emp_pro_db
from repositories import employee_db, project_db

employee_projects_blueprint = Blueprint('employee_projects', __name__)

            ##### Employees Projects Home Page #####

@employee_projects_blueprint.route('/project')
def emp_pro():
    emp_pro = emp_pro_db.get_all()
    return render_template('employee_projects/index.html', emp_pro=emp_pro)

@employee_projects_blueprint.route('/employee_projects/add/<emp_id>/<pro_id>')
def add_employee_to_project(emp_id, pro_id):
    employee = employee_db.get(emp_id)
    project = project_db.get(pro_id)
    employee_project = EmployeeProject(employee, project)
    emp_pro_db.save(employee_project)
    # return emp_control.route_from_project_to_employee_home(emp_id, project.company.id)
    return redirect(f'/employee_home/{emp_id}/{project.company.id}')