"""
Simple dag that has tasks to zip a file, move the zipped file and unzip in a new location and print first and last 10 lines of the file
"""

import os

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator


# dag options 
dag_args = {
    'owner': 'user',
    'depends_on_past': False,
    'start_date': (datetime.now() - timedelta(days=1) ),  # if start day is datetime.now() the scheduler will start the dag from tomorrow
    'email': ['satish.kumar@marketale.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 4,
    'retry_delay': timedelta(minutes=2)
}

tar_command_formatter = '''tar -cf {output_file} {input_file}'''
untar = ''' tar -xf {input_file} -C {output_location}'''

def zip_files():
    ''' zips the file '''
    cmd = tar_command_formatter.format(input_file='source_dir/AB_NYC_2019.csv', output_file='source_dir/AB_NYC_2019.tar')
    os.system(cmd)


def move_files():
    ''' moves file from source dir to target dir '''
    os.system('mv source_dir/AB_NYC_2019.tar target_dir/AB_NYC_2019.tar')


def unzip_files():
    ''' unzips the file '''
    cmd = untar.format(input_file='target_dir/AB_NYC_2019.tar', output_location='target_dir/')
    os.system(cmd)


first_10_lines = 'head -n 10 ' + os.getcwd() + '/target_dir/source_dir/AB_NYC_2019.csv'  # prints first 10 lines
last_10_lines = 'tail -n 10 ' + os.getcwd() + '/target_dir/source_dir/AB_NYC_2019.csv'  # prints last 10 lines


# creating DAG object
dag = DAG('file_operations_pipeline', description='dag to perform file operations', catchup=False, default_args=dag_args, schedule_interval='*/5 * * * *')

# schedule_interval = '*/5 * * * *' runs the dag every 5 minutes
# schedule_interval='@daily' or schedule_interval = '0 0 * * *' runs dag every day at midnight 
# refer http://airflow.apache.org/scheduler.html for more details on scheduling

# defining tasks
zip_task = PythonOperator(task_id='zip_target', python_callable=zip_files, dag=dag)
move_task = PythonOperator(task_id='move_target_to_source', python_callable=move_files, dag=dag)
unzip_task = PythonOperator(task_id='unzip_source', python_callable=unzip_files, dag=dag)
sleep = BashOperator(task_id='sleep', bash_command='sleep 5', dag=dag)
print_head = BashOperator(task_id='print_first_ten_lines', bash_command=first_10_lines, dag=dag)
print_tail = BashOperator(task_id='print_last_ten_lines', bash_command=last_10_lines, dag=dag)

# creating the dag order 
zip_task >> move_task >> unzip_task >> print_head >> print_tail
