from db.run_sql import run_sql
from models.project import Project
from repositories import company_db


def save(project):
    query = 'INSERT INTO projects (name, company_id) VALUES (%s, %s) RETURNING id'
    values = [project.name, project.company.id]
    result = run_sql(query, values)
    project.id = result[0]['id']

def get_all():
    projects = []
    query = 'SELECT * FROM projects'
    results = run_sql(query)
    for row in results:
        project = Project(name=row['name'], id=row['id'], company=row['company_id'])
        projects.append(project)

    return projects

def get(project_id):
    query = 'SELECT * FROM projects WHERE id = %s'
    rs = run_sql(query, [project_id])[0]
    company = company_db.get(rs['company_id'])
    project = Project(name=rs['name'], id=rs['id'], company=company)
    return project

def delete(project):
    run_sql('DELETE FROM projects WHERE id = %s', [project.id])

def update(project):
    query = 'UPDATE projects SET (name, company_id) = (%s, %s) WHERE id = %s'
    run_sql(query, [project.name, project.company_id, project.id])

def delete_all():
    run_sql('DELETE FROM projects')

def get_company_projects(company):
    projects = []
    query = 'SELECT * FROM projects WHERE company_id = %s'
    results = run_sql(query, [company.id])

    for row in results:
        project = Project(row['name'], company, row['id'])
        projects.append(project)
    return projects