from flask import Flask, render_template, request, jsonify,redirect
from flask_cors import CORS
import yaml
import random
import sqlalchemy
from sqlalchemy import func, cast
import logging
import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from datetime import datetime
from dateutil.relativedelta import relativedelta

app = Flask(__name__)
db_config = yaml.safe_load(open('database.yaml'))
app.config['SQLALCHEMY_DATABASE_URI'] = db_config['uri']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

CORS(app)

@app.route('/datasets/<string:dataset_id>/<string:idsite>/<string:period>/')
def getDatasetByIdAndIdSite(dataset_id, idsite, period):
    # GET a specific data by id
    today = datetime.today().strftime('%Y-%m-%d')
    if request.method == 'GET':
        complement_date = ''
        complement_idsite = ''
        if (period == 'monthly'):
            min_date = (datetime.today() + relativedelta(months=-12)).strftime('%Y-%m-%d')
            min_date = min_date[0:7] + '-01'
            scale = 'substring(date,0,8)'
            complement_date = '-01' 
        if (period == 'weekly'):
            min_date = (datetime.today() + relativedelta(months=-1)).strftime('%Y-%m-%d')
            scale = 'date'
        if (period == 'daily'):
            min_date = (datetime.today() + relativedelta(days=-7)).strftime('%Y-%m-%d')
            scale = 'date'
        if idsite != 'all':
            complement_idsite = " and idsite = '" + idsite + "'"
        my_query = "select " + scale + " as month, sum(views) as views from datasets where id = '" + dataset_id + "'" + complement_idsite + " and date >= '" + min_date + "'group by " + scale + ", type;"
        data = db.session.execute(my_query).fetchall()
        records = []
        for i in range(len(data)):
            record = {}
            record['date'] = str(data[i][0])  + complement_date
            record['value'] = str(data[i][1]) 
            records.append(record)
        
        result = {}
        result['nom'] = 'Nombre de visites'
        result['unite'] = 'visites'
        result['date_maj'] = today
        result['values'] = records

        return jsonify(result)


@app.route('/resources/<string:dataset_id>/<string:period>/')
def getTopResources(dataset_id, period):
    # GET a specific data by id
    today = datetime.today().strftime('%Y-%m-%d')
    if request.method == 'GET':
        if (period == 'monthly'):
            min_date = (datetime.today() + relativedelta(months=-12)).strftime('%Y-%m-%d')
            min_date = min_date[0:7] + '-01'
        if (period == 'weekly'):
            min_date = (datetime.today() + relativedelta(months=-1)).strftime('%Y-%m-%d')
        if (period == 'daily'):
            min_date = (datetime.today() + relativedelta(days=-7)).strftime('%Y-%m-%d')

        my_query = "select id, title, sum(views) as views from resources where dataset_id = '" + dataset_id + "' and date >= '" + min_date + "' group by id, title order by views DESC limit 10;"

        data = db.session.execute(my_query).fetchall()
        records = []
        for i in range(len(data)):
            record = {}
            record['url'] = 'https://www.data.gouv.fr/fr/datasets/r/' + str(data[i][0])
            record['name'] = str(data[i][1]) 
            record['value'] = str(int(data[i][2])) 
            records.append(record)
        
        result = {}
        result['nom'] = 'Top ' + str(len(records)) + ' des téléchargements de ressources'
        result['unite'] = 'téléchargements'
        result['date_maj'] = today
        result['values'] = records

        return jsonify(result)


@app.route('/organizations/<string:organization_id>/<string:period>/')
def getOrganizationById(organization_id, period):
    # GET a specific data by id
    today = datetime.today().strftime('%Y-%m-%d')
    if request.method == 'GET':
        complement_date = ''
        complement_idsite = ''
        if (period == 'monthly'):
            min_date = (datetime.today() + relativedelta(months=-12)).strftime('%Y-%m-%d')
            min_date = min_date[0:7] + '-01'
            scale = 'substring(date,0,8)'
            complement_date = '-01' 
        if (period == 'weekly'):
            min_date = (datetime.today() + relativedelta(months=-1)).strftime('%Y-%m-%d')
            scale = 'date'
        if (period == 'daily'):
            min_date = (datetime.today() + relativedelta(days=-7)).strftime('%Y-%m-%d')
            scale = 'date'
        my_query = "select " + scale + " as month, sum(views) as views from organizations where id = '" + organization_id + "'" + complement_idsite + " and date >= '" + min_date + "'group by " + scale + ", type;"
        data = db.session.execute(my_query).fetchall()
        records = []
        for i in range(len(data)):
            record = {}
            record['date'] = str(data[i][0])  + complement_date
            record['value'] = str(data[i][1]) 
            records.append(record)
        
        result = {}
        result['nom'] = 'Nombre de visites'
        result['unite'] = 'visites'
        result['date_maj'] = today
        result['values'] = records

        return jsonify(result)


@app.route('/datasets/organizations/<string:organization_id>/<string:period>/')
def getDatasetsFromOrganizationById(organization_id, period):
    # GET a specific data by id
    today = datetime.today().strftime('%Y-%m-%d')
    if request.method == 'GET':
        complement_date = ''
        complement_idsite = ''
        if (period == 'monthly'):
            min_date = (datetime.today() + relativedelta(months=-12)).strftime('%Y-%m-%d')
            min_date = min_date[0:7] + '-01'
            scale = 'substring(date,0,8)'
            complement_date = '-01' 
        if (period == 'weekly'):
            min_date = (datetime.today() + relativedelta(months=-1)).strftime('%Y-%m-%d')
            scale = 'date'
        if (period == 'daily'):
            min_date = (datetime.today() + relativedelta(days=-7)).strftime('%Y-%m-%d')
            scale = 'date'
        my_query = "select " + scale + " as month, sum(views) as views from datasets where organization_id = '" + organization_id + "'" + complement_idsite + " and date >= '" + min_date + "'group by " + scale + ", type;"
        data = db.session.execute(my_query).fetchall()
        records = []
        for i in range(len(data)):
            record = {}
            record['date'] = str(data[i][0])  + complement_date
            record['value'] = str(data[i][1]) 
            records.append(record)
        
        result = {}
        result['nom'] = 'Nombre de visites'
        result['unite'] = 'visites'
        result['date_maj'] = today
        result['values'] = records

        return jsonify(result)



@app.route('/organizations/datasets/<string:organization_id>/<string:period>/')
def getTopDatasets(organization_id, period):
    # GET a specific data by id
    today = datetime.today().strftime('%Y-%m-%d')
    if request.method == 'GET':
        if (period == 'monthly'):
            min_date = (datetime.today() + relativedelta(months=-12)).strftime('%Y-%m-%d')
            min_date = min_date[0:7] + '-01'
        if (period == 'weekly'):
            min_date = (datetime.today() + relativedelta(months=-1)).strftime('%Y-%m-%d')
        if (period == 'daily'):
            min_date = (datetime.today() + relativedelta(days=-7)).strftime('%Y-%m-%d')

        my_query = "select id, slug, sum(views) as views from datasets where organization_id = '" + organization_id + "' and date >= '" + min_date + "' group by id, slug order by views DESC limit 10;"

        data = db.session.execute(my_query).fetchall()
        records = []
        for i in range(len(data)):
            record = {}
            record['url'] = 'https://www.data.gouv.fr/fr/datasets/' + str(data[i][0])
            record['name'] = str(data[i][1]) 
            record['value'] = str(int(data[i][2])) 
            records.append(record)
        
        result = {}
        result['nom'] = 'Top ' + str(len(records)) + ' des visites sur les jeux de données de l\'organisation'
        result['unite'] = 'téléchargements'
        result['date_maj'] = today
        result['values'] = records

        return jsonify(result)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=80)