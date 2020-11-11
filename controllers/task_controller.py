from flask import Blueprint, Flask, redirect, render_template, request

from models.task import Task
import repositories.task_db as task_db
import controllers.employee_controller as emp_control
from repositories import project_db, employee_db

tasks_blueprint = Blueprint('tasks', __name__)

@tasks_blueprint.route('/tasks')
def all_tasks():
    tasks = task_sql.get_all()
    return tasks

        ##### Add new task - by user #####
# @tasks_blueprint.route('tasks/new/<emp_id>/<pro_id>')
# def add_task():


        ##### When employee makes changes to a task #####
@tasks_blueprint.route('/tasks/update/<emp_id>/<pro_id>/<task_id>', methods=['POST'])
def update_task(emp_id, pro_id, task_id):
    task = task_db.get(task_id)
    task.completed = request.form['completed']
    task.completed_amount = request.form['completed_amount']
    task.description = request.form['description']
    task_db.update(task)
    print("Hello")
    # return emp_control.company(emp_id, task.project.company.id) # Couldn't redirect to a blueprint that isn't in this file
    return redirect(f'/employee_home/{emp_id}/{task.project.company.id}')

@tasks_blueprint.route('/task/new/<pro_id>/<emp_id>')
def new_task_form(pro_id, emp_id):
    return render_template('tasks/new.html', pro_id=pro_id, emp_id=emp_id)

@tasks_blueprint.route('/task/new/<pro_id>/<emp_id>', methods=['POST'])
def add_task(pro_id, emp_id):
    project = project_db.get(pro_id)
    task = Task(name=request.form['name'], description=request.form['description'],
                project=project, completed_amount=request.form['completed_amount'],
                )
    task_db.save(task)
    # print(request.form['assign_to_project'])
    # print(bool(request.form['completed']))
    employee = employee_db.get(emp_id)
    return redirect(f'/employee_home/{emp_id}/{employee.company.id}')