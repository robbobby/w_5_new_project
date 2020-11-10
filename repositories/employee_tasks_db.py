from db.run_sql import run_sql
import repositories.employee_db as employee_db
import repositories.task_db as task_db
from models.employee import Employee
from models.employee_task import EmployeeTasks


def save(employee_task):
    query = 'INSERT INTO employee_tasks (employee_id, task_id) VALUES (%s, %s) RETURNING id'
    values = [employee_task.employee.id, employee_task.task.id]
    results = run_sql(query, values)
    employee_task.id = results[0]['id']

def get_all():
    employee_tasks = []
    query = 'SELECT * FROM employee_tasks'
    results = run_sql(query)
    for row in results:
        task = task_db.get(row['task_id'])
        employee = employee_db.get(row['employee_id'])
        employee_task = EmployeeTasks(task=task, employee=employee, id=row['id'])
        employee_tasks.append(employee_task)

    return employee_tasks

def get(id):
    query = 'SELECT * FROM employee_tasks WHERE id = %s'
    result = run_sql(query, [id])[0]
    task = task_db.get(result['task_id'])
    employee = employee_db.get(result['employee_id'])
    employee_task = EmployeeTasks(employee=employee, task=task)

    return employee_task

def delete(id):
    query = "DELETE FROM employee_tasks WHERE id = %s"
    run_sql(query, id)

def update(employee_task):
    query = 'UPDATE employee_tasks SET (employee_id, task_id) = (%s, %s) WHERE id = %s'
    values = [employee_task.employee.id, employee_task.task.id, employee_task.id]
    run_sql(query, values)

def delete_all():
    run_sql('DELETE FROM employee_tasks')

def get_employees_project_tasks(emp_id, pro_id):
    emp_tasks = []
    query = 'SELECT tasks.project_id, employee_tasks.*' \
            'FROM employee_tasks INNER JOIN tasks ON employee_tasks.task_id = tasks.id ' \
            'WHERE (employee_id, project_id) = (%s, %s);'
    values = [emp_id, pro_id]
    results = run_sql(query, values)

    for row in results:
        task = task_db.get(row['task_id'])
        employee = employee_db.get(row['employee_id'])
        emp_task = EmployeeTasks(employee, task, row['id'])
        emp_tasks.append(emp_task)
    return emp_tasks

def get_all_employee_tasks(emp_id):
    emp_tasks = []
    query = 'SELECT employee_tasks.*' \
            'FROM employee_tasks INNER JOIN tasks ON employee_tasks.task_id = tasks.id ' \
            'WHERE employee_id = %s'
    values = [emp_id]
    results = run_sql(query, values)

    for row in results:
        task = task_db.get(row['task_id'])
        employee = employee_db(row['empoyee_id'])
        emp_task = EmployeeTasks(employee, task, row['id'])
        emp_tasks.append(emp_task)
    return emp_tasks