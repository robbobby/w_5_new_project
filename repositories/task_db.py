from db.run_sql import run_sql
from models.task import Task
import repositories.project_db as project_db
from models.project import Project

def save(task):
    query = 'INSERT INTO tasks (name, description, completed_amount, completed, project_id) ' \
            'VALUES (%s, %s, %s, %s, %s) RETURNING id'

    result = run_sql(query, [task.name, task.description, task.completed_amount,
                             task.completed, task.project.id])
    task.id = result[0]['id']

def get_all():
    tasks = []
    query = 'SELECT * FROM tasks'
    results = run_sql(query)
    for row in results:
        project = project_db.get(row['project_id'])
        task = Task(name=row['name'], description=row['description'], id=row['id'],
                    project=project, completed_amount=row['completed_amount'],
                    completed=row['completed'])
        tasks.append(task)
    return tasks

def get(task_id):
    query = 'SELECT * FROM tasks WHERE id = %s'
    rs = run_sql(query, [task_id])[0]
    project = project_db.get(rs['project_id'])
    task = Task(name=rs['name'], description=rs['description'], id=task_id,
                project=project, completed_amount=rs['completed_amount'],
                completed=rs['completed'])
    return task

def delete(task):
    run_sql('DELETE FROM tasks WHERE id = %s', [task.id])

def update(task):
    query = 'UPDATE tasks SET (name, description, completed_amount, completed, project_id)' \
            ' = (%s, %s, %s, %s, %s) WHERE id = %s'
    values = [task.name, task.description, task.completed_amount, task.completed,
              task.project.id, task.id]
    run_sql(query, values)

def delete_all():
    run_sql('DELETE FROM tasks')