AIRFLOW EXAMPLE
---------------


# Installation and running airflow

- Install python, pip and set up virtual env

- Install apache airflow ( with celery configurations)

          pip3 install apache-airflow[celery]


- Install mysql create db with name airflow , create user airflow with password airflow
	- or any db with any name, update airflow.cfg accordingly

- Change AIRFLOW_HOME to current project directory

          export AIRFLOW=`pwd`

- Initialize airflow setup and db files

          airflow initdb

- Update airflow.cfg

          line 57 : executor = CeleryExecutor
          line 62 : sql_alchemy_conn = mysql://airflow:airflow@localhost:3306/airflow  (or whatever db and connection you created earlier)
          line 374 : broker_url = sqla+mysql://airflow:airflow@localhost:3306/airflow  
          line 382 : result_backend = db+mysql://airflow:airflow@localhost:3306/airflow


- Initialize airflowdb
	
          source {venv}/bin/activate
          export AIRFLOW_HOME=`pwd`  # setting airflow project directory to current working directory
          airflow initdb


- Start airflow scheduler, worker and webserver

         terminal 1:
         >> source {venv}/bin/activate
         >> export AIRFLOW_HOME=`pwd`
         >> airflow scheduler

         terminal 2:
         >> source {venv}/bin/activate
         >> export AIRFLOW_HOME=`pwd`
         >> airflow worker

        terminal 3:
         >> source {venv}/bin/activate
         >> export AIRFLOW_HOME=`pwd`
         >> airflow webserver


- Open web interface and start the scheduler for DAG - file_operations_pipeline


# Editing and updating dag

- Dag is saved under dags folder








	     



