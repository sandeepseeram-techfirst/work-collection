# import the API in your service code.
from opentelemetry import trace, metrics
 
# other code removed for clarity
 
if __name__ == "__main__": 
    service_name = must_map_env('OTEL_SERVICE_NAME')
  
    # now, we can call the tracing and metrics providers to hook into the SDK being configured by our agent.
    tracer = trace.get_tracer_provider().get_tracer(service_name)
    meter = metrics.get_meter_provider().get_meter(service_name)
    rec_svc_metrics = init_metrics(meter)
# metrics.py
def init_metrics(meter):
 
    # we can create a counter and then use it to create a metric for some interesting business metric, such as the number of recommendations the service provides per request.
    app_recommendations_counter = meter.create_counter(
        'app_recommendations_counter', unit='recommendations', description="Counts the total number of given recommendations"
    )
 
    rec_svc_metrics = {
        "app_recommendations_counter": app_recommendations_counter,
    }
 
    return rec_svc_metrics