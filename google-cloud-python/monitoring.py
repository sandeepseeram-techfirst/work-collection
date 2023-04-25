import google.auth
from google.cloud import monitoring_v3

# Use ADC to authenticate
credentials, project_id = google.auth.default()

# Create a client for the Cloud Monitoring API
client = monitoring_v3.MetricServiceClient(credentials=credentials)

# Define the resource type and metric for the Cloud Composer DAGs
resource_type = 'composer_environment'
metric_type = 'composer.googleapis.com/environment/dag_run_count'

# Query the Cloud Monitoring API for the DAG metrics
results = client.list_time_series(
    'projects/{}/'.format(project_id),
    'metric.type="{}"'.format(metric_type),
    interval_seconds=3600,
    view=monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL
)

# Parse the results into a dictionary of DAG names and last successful run times
dags = {}
for result in results:
    dag_name = result.resource.labels['environment_name']
    last_successful_run = None
    for point in result.points[::-1]:
        if point.value.int_value > 0:
            last_successful_run = point.interval.end_time.ToJsonString()
            break
    dags[dag_name] = last_successful_run

# Output the results as JSON
import json
print(json.dumps(dags, indent=4))