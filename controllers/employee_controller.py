from flask import Blueprint, Flask, redirect, render_template, request

from models.employee import Employee
import repositories.employee_db as employee_db
import repositories.company_db as company_db
import repositories.employee_projects_db as emp_pro_db

employee_blueprint = Blueprint("employees", __name__)


            ##### Employees Home Page #####
@employee_blueprint.route('/employees', methods=['GET'])
def employees():
    employees = employee_db.get_all()
    return render_template('employees/index.html', employees=employees)

@employee_blueprint.route('/employees/new', methods=['GET'])
def new_employee():
    companies = company_db.get_all()
    return render_template('employees/new.html', companies=companies)

@employee_blueprint.route('/employees/new/selected', methods=['POST'])
def reroute_to_employee_home():
    company = company_db.get(request.form['company_id'])
    employee = Employee(request.form['name'], company)
    employee_db.save(employee)
    return redirect(f'/employee_home/{employee.id}/{company.id}')

@employee_blueprint.route('/employees/selected', methods=['POST'])
def user_selected():
    try:
        employee = employee_db.get(request.form['employee_id'])
        return redirect(f'/employee_home/{employee.id}/{employee.company.id}')
    except:
        return redirect('/employees')

@employee_blueprint.route('/employee_home/<emp_id>/<com_id>', methods=['GET'])
def company(emp_id, com_id):
    employee = employee_db.get(emp_id)
    company = company_db.get(com_id)
    employee_projects = emp_pro_db.get_employees_projects(employee)
    not_employee_projects = emp_pro_db.get_projects_employee_not_have(employee, company)

    return render_template('employees/employee.html', employee=employee, employee_projects=employee_projects, com_id=com_id, emp_id=emp_id, not_employee_projects=not_employee_projects)

def route_from_project_to_employee_home(emp_id, com_id):
    return redirect(f'/employee_home/{emp_id}/{com_id}')