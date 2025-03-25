from flask import Flask
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter

app = Flask(__name__)

# Set up OpenTelemetry
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# Configure Azure Monitor exporter
exporter = AzureMonitorTraceExporter(
    connection_string="InstrumentationKey=d6ea9e8e-d6c5-40be-8da0-1d10da66e171;IngestionEndpoint=https://centralindia-0.in.applicationinsights.azure.com/;LiveEndpoint=https://centralindia.livediagnostics.monitor.azure.com/;ApplicationId=b1662395-cec3-4793-b3cf-a1fd11088828"
)
span_processor = BatchSpanProcessor(exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

@app.route('/')
def home():
    with tracer.start_as_current_span("home"):
        return "Hello, Azure with Live Metrics!"

if __name__ == '__main__':
    app.run(debug=True)