from flask import Blueprint, Flask, redirect, render_template, request
from models.employee_project import EmployeeProject

import repositories.employee_projects_db as emp_pro_db

employee_projects_blueprint = Blueprint('employee_projects', __name__)

            ##### Employees Projects Home Page #####

@employee_projects_blueprint.route('/project')
def emp_pro():
    emp_pro = emp_pro_db.get_all()
    return render_template('employee_projects/index.html', emp_pro=emp_pro)