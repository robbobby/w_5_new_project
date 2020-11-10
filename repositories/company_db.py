from db.run_sql import run_sql
import repositories.project_db as project_db
from models.company import Company


def save(company):
    query = 'INSERT INTO companies (name) VALUES (%s) RETURNING *;'
    values = [company.name]
    results = run_sql(query, values)
    company.id = results[0]['id']

def get_all():
    companies = []
    query = 'SELECT * FROM companies'
    results = run_sql(query)
    for company in results:
        company_to_add = Company(company['name'], company['id'])
        companies.append(company_to_add)

    return companies

def get(company_id):
    query = "SELECT * FROM companies WHERE id = %s"
    result = run_sql(query, [company_id])[0]
    company = Company(result['name'], result['id'])
    return company


def delete(company):
    query = 'DELETE FROM companies WHERE id = %s'
    values = [company.id]
    run_sql(query, values)

def update(company):
    query = 'UPDATE companies SET name = %s WHERE id = %s'
    values = [company.name, company.id]
    run_sql(query, values)

def delete_all():
    run_sql('DELETE FROM companies')

def get_projects(company):
    return project_db.get_company_projects(company)