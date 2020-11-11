from flask import Blueprint, Flask, redirect, render_template, request

from models.task import Task
import repositories.task_db as task_db
import controllers.employee_controller as emp_control

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
    return emp_control.company(emp_id, task.project.company.id) # Couldn't redirect to a blueprint that isn't in this file