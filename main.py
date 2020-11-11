from flask import Flask, render_template
from controllers.employee_project_controller import employee_projects_blueprint
from controllers.employee_task_controller import employee_tasks_blueprint
from controllers.company_controller import companies_blueprint
from controllers.employee_controller import employee_blueprint
from controllers.project_controller import project_blueprint
from controllers.task_controller import tasks_blueprint

app = Flask(__name__)

app.register_blueprint(employee_projects_blueprint)
app.register_blueprint(employee_tasks_blueprint)
app.register_blueprint(companies_blueprint)
app.register_blueprint(employee_blueprint)
app.register_blueprint(project_blueprint)
app.register_blueprint(tasks_blueprint)


@app.route('/')
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
