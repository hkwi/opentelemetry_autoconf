import os
import logging
import pkg_resources
import opentelemetry
import opentelemetry.exporter.jaeger
import opentelemetry.sdk.trace.export

logger = logging.getLogger(__name__)
do_instrument = False
provider = opentelemetry.trace.get_tracer_provider()

if provider and "OTEL_AUTO_JAEGER_SERVICE_NAME" in os.environ:
	exporter = opentelemetry.exporter.jaeger.JaegerSpanExporter(
		service_name=os.environ["OTEL_AUTO_JAEGER_SERVICE_NAME"],
		agent_host_name=os.environ.get("OTEL_AUTO_JAEGER_AGENT_HOST", "localhost"),
		agent_port=int(os.environ.get("OTEL_AUTO_JAEGER_AGENT_PORT", "6831"))
	)
	provider.add_span_processor(
		opentelemetry.sdk.trace.export.BatchExportSpanProcessor(exporter)
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


