AIRFLOW EXAMPLE
---------------


# Installation

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



