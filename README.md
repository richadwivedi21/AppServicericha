MyFlaskApp
Overview
MyFlaskApp is a simple web application built using Flask and deployed on Azure App Services. This project demonstrates how to create a basic Flask web app and enable live metrics using Azure Application Insights.

Features
Simple Flask Web App: A basic web application that returns a "Hello, Azure with Live Metrics!" message.
Azure App Services Deployment: Instructions to deploy the app on Azure App Services.
Live Metrics with Application Insights: Integration with Azure Application Insights to monitor live metrics.
Prerequisites
Python 3.6 or higher
Azure account
Setup
Clone the repository:

git clone https://github.com/yourusername/myflaskapp.git
cd myflaskapp
Create a virtual environment and activate it:

python -m venv myvenv
source venv/bin/activate  # On Windows use `myvenv\Scripts\activate`
Install the dependencies:

pip install -r requirements.txt
Running the App Locally
Set the Flask app environment variable:

export FLASK_APP=app.py  # On Windows use `set FLASK_APP=app.py`
Run the Flask app:

flask run
Open your browser and navigate to http://127.0.0.1:5000 to see the app in action.

Deploying to Azure App Services
Create a new Web App in the Azure portal.
Use the Deployment Center to connect your GitHub repository or upload your code directly.
Ensure the runtime stack is set to Python.
Enabling Live Metrics with Application Insights
Install the necessary packages:

pip install azure-monitor-opentelemetry-exporter --pre
Update app.py to include the OpenTelemetry configuration:

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
    connection_string="InstrumentationKey=YOUR_INSTRUMENTATION_KEY"
)
span_processor = BatchSpanProcessor(exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

@app.route('/')
def home():
    with tracer.start_as_current_span("home"):
        return "Hello, Azure with Live Metrics!"

if __name__ == '__main__':
    app.run(debug=True)
Replace YOUR_INSTRUMENTATION_KEY with your actual Application Insights instrumentation key.

Deploy your updated app to Azure App Services.

Enable live metrics in the Azure portal:

Open your Application Insights resource.
Select Live Metrics under the Investigate section.
License
This project is licensed under the MIT License. See the LICENSE file for details.
