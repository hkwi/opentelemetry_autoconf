import os
import logging
import pkg_resources
import opentelemetry
import opentelemetry.sdk.trace.export

logger = logging.getLogger(__name__)
do_instrument = False
provider = opentelemetry.trace.get_tracer_provider()

if provider and "OTEL_AUTO_JAEGER_SERVICE_NAME" in os.environ:
	opts = dict(
		service_name=os.environ["OTEL_AUTO_JAEGER_SERVICE_NAME"]
	)
	if "OTEL_AUTO_JAEGER_AGENT_HOST" in os.environ:
		opts["agent_host_name"] = os.environ["OTEL_AUTO_JAEGER_AGENT_HOST"]
	
	if "OTEL_AUTO_JAEGER_AGENT_PORT" in os.environ:
		opts["agent_port"] = int(os.environ["OTEL_AUTO_JAEGER_AGENT_PORT"])
	
	if "OTEL_AUTO_JAEGER_COLLECTOR_HOST" in os.environ:
		opts["collector_host_name"] = os.environ["OTEL_AUTO_JAEGER_COLLECTOR_HOST"]
	
	if "OTEL_AUTO_JAEGER_COLLECTOR_PORT" in os.environ:
		opts["collector_port"] = int(os.environ["OTEL_AUTO_JAEGER_COLLECTOR_PORT"])
	
	if "OTEL_AUTO_JAEGER_COLLECTOR_ENDPOINT" in os.environ:
		opts["collector_endpoint"] = os.environ["OTEL_AUTO_JAEGER_COLLECTOR_ENDPOINT"]
	
	if "OTEL_AUTO_JAEGER_COLLECTOR_PROTOCOL" in os.environ:
		opts["collector_protocol"] = os.environ["OTEL_AUTO_JAEGER_COLLECTOR_PROTOCOL"]
	
	if "OTEL_AUTO_JAEGER_USERNAME" in os.environ:
		opts["username"] = os.environ["OTEL_AUTO_JAEGER_USERNAME"]
	
	if "OTEL_AUTO_JAEGER_PASSWORD" in os.environ:
		opts["password"] = os.environ["OTEL_AUTO_JAEGER_PASSWORD"]
	
	import opentelemetry.exporter.jaeger
	provider.add_span_processor(
		opentelemetry.sdk.trace.export.BatchExportSpanProcessor(
			opentelemetry.exporter.jaeger.JaegerSpanExporter(**opts)
		)
	)
	do_instrument = True

# auto-instrumentation
if do_instrument:
	for entry_point in pkg_resources.iter_entry_points("opentelemetry_instrumentor"):
		try:
			entry_point.load()().instrument()
			logger.debug("Instrumented %s", entry_point.name)
		except Exception:
			logger.exception("Instrumenting of %s failed", entry_point.name)


