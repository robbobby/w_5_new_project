from flask import Blueprint, Flask, redirect, render_template, request

from models.company import Company
import repositories.company_db as company_db

companies_blueprint = Blueprint('companies', __name__)


    ##### Companies Home Page #####

@companies_blueprint.route('/companies', methods=['GET'])
def companies():
    companies = company_db.get_all()
    return render_template('companies/index.html', companies=companies)


    ##### Companies Form For Page #####

@companies_blueprint.route('/companies/new', methods=['GET'])
def new_company():
    return render_template('companies/new.html')


    ##### Add New Company and Redirect to 'Company' Home Page #####

@companies_blueprint.route('/companies', methods=['POST'])
def add_company():
    company = Company(request.form['name'])
    company_db.save(company)
    return redirect(f'/company_home/{company.id}')


    ##### Takes info from form to redirect to companies page #####
    ### Try is there if they select the default option ###
    # Bit of a hack #

@companies_blueprint.route('/companies/selected', methods=['POST'])
def reroute_to_company_home():
    try:
        company_id = request.form['company_id']
        return redirect(f'/company_home/{company_id}')
    except:
        return redirect('/companies')


    ##### Route to company page when signed in #####
@companies_blueprint.route('/company_home/<id>', methods=['GET'])
def company(id):
    company = company_db.get(id)
    projects = company_db.get_projects(company)
    return render_template('companies/company.html', company=company, projects=projects)
