from flask import Blueprint, Flask, redirect, render_template, request

from models.task import Task
import repositories.task_db as task_sql

tasks_blueprint = Blueprint("tasks", __name__)

@tasks_blueprint.route("/tasks")
def all_tasks():
    tasks = task_sql.get_all()
    return tasks