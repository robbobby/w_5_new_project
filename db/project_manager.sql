DROP TABLE IF EXISTS employee_tasks;
DROP TABLE IF EXISTS employee_projects;
DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS companies;

CREATE TABLE companies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    company_id INT REFERENCES companies(id)
);

CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    company_id INT REFERENCES companies(id)
);

CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    name  VARCHAR(255),
    description TEXT,
    completed_amount INT,
    completed BOOL,
    project_id INT REFERENCES projects(id)
);

CREATE TABLE employee_projects (
    id SERIAL PRIMARY KEY,
    employee_id INT REFERENCES employees(id),
    project_id INT REFERENCES projects(id)
);

CREATE TABLE employee_tasks (
    id SERIAL PRIMARY KEY,
    employee_id INT REFERENCES employees(id),
    task_id INT REFERENCES tasks(id)
);