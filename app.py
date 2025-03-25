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
    connection_string="InstrumentationKey=c8e43d86-8f8f-471a-85dc-6190346ee095;IngestionEndpoint=https://centralindia-0.in.applicationinsights.azure.com/;LiveEndpoint=https://centralindia.livediagnostics.monitor.azure.com/;ApplicationId=0d62543e-6d26-4250-af89-121fb76a2042"
)
span_processor = BatchSpanProcessor(exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

@app.route('/')
def home():
    with tracer.start_as_current_span("home"):
        return "Hello, Azure with Live Metrics!"

if __name__ == '__main__':
    app.run(debug=True)