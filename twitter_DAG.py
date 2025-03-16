from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from twitter_ETL import run_twitter_etl  # Ensure this file is in the correct location.

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Define the DAG
dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='DAG for running a Twitter ETL process!',
    schedule_interval='@daily',  # Schedule to run daily
    start_date=days_ago(1),  # Start from one day ago
    catchup=False,  # Prevent backfilling
)

# Task to execute the ETL function
run_etl = PythonOperator(
    task_id='complete_twitter_etl',
    python_callable=run_twitter_etl,  # Function from twitter_ETL.py
    dag=dag, 
)

# Set task dependencies (if there are multiple tasks, you can chain them)
run_etl
