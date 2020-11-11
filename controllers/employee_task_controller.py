from flask import Blueprint, Flask, redirect, render_template, request
from models.employee_task import EmployeeTasks
import repositories.employee_tasks_db as emp_tasks_db
import repositories.project_db as project_db
import repositories.task_db as task_db

import repositories.employee_tasks_db as emp_task_db
from repositories import employee_db

employee_tasks_blueprint = Blueprint('employee_tasks', __name__)

            ##### Employee Tasks Home Page #####

@employee_tasks_blueprint.route('/emp_tasks/<emp_id>/<pro_id>')
def emp_tasks(emp_id, pro_id):
    project = project_db.get(pro_id)
    new_tasks = emp_task_db.get_new_tasks_available_for_project(project, emp_id)
    emp_tasks = emp_task_db.get_employees_project_tasks(emp_id, pro_id)
    return render_template('employee_tasks/index.html', emp_tasks=emp_tasks, new_tasks=new_tasks,
                           pro_id=pro_id, emp_id=emp_id)

@employee_tasks_blueprint.route('/emp_task/new/<emp_id>/<task_id>')
def add(emp_id, task_id):
    task = task_db.get(task_id)
    employee = employee_db.get(emp_id)
    emp_task = EmployeeTasks(employee, task)
    emp_task_db.save(emp_task)
    return redirect(f'/emp_tasks/{emp_id}/{task.project.id}')