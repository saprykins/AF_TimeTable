from uneven_intervals_timetable import UnevenIntervalsTimetable
from datetime import timedelta, datetime
from airflow.operators.python_operator import PythonOperator
from airflow import DAG

dag = DAG(
    dag_id="example_timetable_dag",
    start_date=datetime(2021, 10, 9), 
    max_active_runs=1,
    timetable=UnevenIntervalsTimetable(),
    default_args={
        "retries": 1,
        "retry_delay": timedelta(minutes=3),
    },
    catchup=True
)

def workflow():
    print('context')

workflow = PythonOperator(
    task_id='log_out', 
    python_callable=workflow, 
    dag=dag
    )

workflow
