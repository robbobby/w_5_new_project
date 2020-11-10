import pdb

from models.company import Company
from models.project import Project
from models.employee import Employee
from models.task import Task
from models.employee_project import EmployeeProject
from models.employee_task import EmployeeTasks

import repositories.company_db as company_db
import repositories.project_db as project_db
import repositories.employee_db as employee_db
import repositories.task_db as task_db
import repositories.employee_projects_db as emp_pro_db
import repositories.employee_tasks_db as emp_task_db

                        ##### DELETE ALL ENTRIES ON TABLE #####
emp_task_db.delete_all()
emp_pro_db.delete_all()
task_db.delete_all()
employee_db.delete_all()
project_db.delete_all()
company_db.delete_all()

                        ##### MAKE TEST DATA #####
company = Company("Trump Disaster")
company_db.save(company)

project = Project("Become President", company=company)
project1 = Project("Fail at making money", company=company)
project2 = Project("Win second election", company=company)

project_db.save(project)
project_db.save(project1)
project_db.save(project2)

employee = Employee("Bob", company=company)
employee1 = Employee("Jeff", company=company)
employee2 = Employee("Barb", company=company)
employee3 = Employee("Peggy", company=company)
employee4 = Employee("Ritta", company=company)
employee5 = Employee("George", company=company)
Employee6 = Employee("Donald Trump", company=company)

employee_db.save(employee)
employee_db.save(employee1)
employee_db.save(employee2)
employee_db.save(employee3)
employee_db.save(employee4)
employee_db.save(employee5)

task = Task("Tweet things people appreciate", "Self explanatory", project, 99)
task_db.save(task)

emp_pro = EmployeeProject(employee1, project)
emp_pro_db.save(emp_pro)
emp_pro = EmployeeProject(employee, project)
emp_pro_db.save(emp_pro)
emp_pro = EmployeeProject(employee, project1)
emp_pro_db.save(emp_pro)
emp_pro = EmployeeProject(employee, project2)
emp_pro_db.save(emp_pro)
emp_pro = EmployeeProject(employee2, project)
emp_pro_db.save(emp_pro)
emp_pro = EmployeeProject(employee3, project)
emp_pro_db.save(emp_pro)
emp_pro = EmployeeProject(employee5, project)
emp_pro_db.save(emp_pro)
emp_pro = EmployeeProject(employee1, project1)
emp_pro_db.save(emp_pro)
emp_pro = EmployeeProject(employee1, project2)
emp_pro_db.save(emp_pro)
emp_pro = EmployeeProject(employee2, project2)
emp_pro_db.save(emp_pro)



emp_task = EmployeeTasks(employee, task)
emp_task_db.save(emp_task)