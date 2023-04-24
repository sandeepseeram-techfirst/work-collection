import os
import io
import sys
from google.cloud import monitoring_v3
from google.auth.default import get_default_credentials

# Get the ADC credentials
adc_credentials = get_default_credentials()

# Create a monitoring client
monitoring_client = monitoring_v3.MonitoringClient(adc_credentials)

# Get the list of DAGs
dags = monitoring_client.list_dags()

# For each DAG, get the last successful job run
for dag in dags:
    last_successful_job_run = monitoring_client.list_job_runs(
        project_id=os.environ["PROJECT_ID"],
        job_type="dag",
        job_id=dag.name,
        filter="status=" + monitoring_v3.JobRun.Status.SUCCESS,
        order_by="start_time desc",
        limit=1,
    ).job_runs[0]

    print("DAG:", dag.name)
    print("Last successful job run:", last_successful_job_run.start_time)
