import requests

from common import configure_tracer

@tracer.start_as_current_span("browse")

def browse():

    print("visiting the grocery store")

    with tracer.start_as_current_span(

        "web request", kind=trace.SpanKind.CLIENT

    ) as span:

        url = "http://localhost:5000"

        span.set_attributes(

            {

                SpanAttributes.HTTP_METHOD: "GET",

                SpanAttributes.HTTP_FLAVOR: str(HttpFlavorValues.HTTP_1_1),

                SpanAttributes.HTTP_URL: url,

                SpanAttributes.NET_PEER_IP: "127.0.0.1",

            }

        )

        resp = requests.get(url)

        span.set_attribute(SpanAttributes.HTTP_STATUS_CODE, resp.status_code)