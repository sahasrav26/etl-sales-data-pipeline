from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="etl_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    extract = BashOperator(
        task_id="extract",
        bash_command="python /opt/airflow/dags/scripts/extract.py"
    )

    transform = BashOperator(
        task_id="transform",
        bash_command="python /opt/airflow/dags/scripts/transform.py"
    )
    
    validate = BashOperator(
    task_id="validate",
    bash_command="python /opt/airflow/dags/scripts/validate.py"
    )

    load = BashOperator(
        task_id="load",
        bash_command="python /opt/airflow/dags/scripts/load.py"
    )

    extract >> transform >> validate >> load
