from db.run_sql import run_sql
import repositories.employee_db as employee_db
import repositories.project_db as project_db
from models.employee_project import EmployeeProject
from models.project import Project
from repositories import company_db


def save(employee_project):
    query = 'INSERT INTO employee_projects (employee_id, project_id) ' \
            'VALUES (%s, %s) RETURNING id'
    values = [employee_project.employee.id, employee_project.project.id]
    results = run_sql(query, values)
    employee_project.id = results[0]['id']


def get_all():
    employee_projects = []
    query = 'SELECT * FROM employee_projects'
    results = run_sql(query)
    for row in results:
        project = project_db.get(row['project_id'])
        employee = employee_db.get(row['employee_id'])
        employee_project = EmployeeProject(project=project, employee=employee)
        employee_projects.append(employee_project)

    return employee_projects


def select(id):
    query = 'SELECT * FROM employee_projects WHERE id = %s'
    result = run_sql(query, [id])[0]
    project = project_db.get(result['project_id'])
    employee = employee_db.get(result['employee_id'])
    employee_project = EmployeeProject(employee=employee, project=project)

    return employee_project


def delete(id):
    query = "DELETE FROM employee_projects WHERE id = %s"
    run_sql(query, id)


def update(employee_project):
    query = 'UPDATE employee_projects SET (employee_id, project_id) = (%s, %s) ' \
            'WHERE id = %s'
    values = [employee_project.employee.id, employee_project.project.id, employee_project.id]
    run_sql(query, values)


def delete_all():
    run_sql('DELETE FROM employee_projects')


def get_employees_projects(employee):
    emp_projects = []
    query = 'SELECT * FROM projects ' \
            'INNER JOIN employee_projects ON employee_projects.project_id = projects.id ' \
            'WHERE employee_id = %s'
    results = run_sql(query, [employee.id])

    for row in results:
        company = company_db.get(row['company_id'])
        project = Project(row['name'], company, row['project_id'])
        emp_pro = EmployeeProject(employee, project, row['id'])
        emp_projects.append(emp_pro)
    return emp_projects


def get_projects_employee_not_have(employee, company):
    projects = []
    emp_projects = get_employees_projects(employee)
    query = 'SELECT * FROM projects WHERE company_id = %s'
    results = run_sql(query, [company.id])
    for row in results:
        current_project = False
        for project in emp_projects:
            if row['id'] == project.project.id:
                current_project = True
        if not current_project:
            project = Project(row['name'], company, row['id'])
            projects.append(project)
    return projects