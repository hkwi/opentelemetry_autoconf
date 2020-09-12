# What is this?

This module provides out-of-box automatic opentelemetry configuration.
Just install this module, and lauch target program normally 
with configuration environment variables, WITHOUT ANY CHANGES 
to the target program, like this:

```
$ OTEL_TRACER_PROVIDER=sdk_tracer_provider \
  OTEL_AUTO_JAEGER_SERVICE_NAME=foo \
  python foo.py
```

There's no `import opentelemetry_autoconf`.

opentelemetry already has some configuration mechanism.
- `OTEL_TRACER_PROVIDER` configures opentelemetry configuration module.
- `opentelemetry-instrument` automatically loads instrumentation code.

`opentelemetry_autoconf` does auto-instrumentation, so you don't have to
wrap with `opentelemetry-instrument`.

Current supported configurations:

- `OTEL_AUTO_JAEGER_SERVICE_NAME` enables jaeger exporter.
- `OTEL_AUTO_JAEGER_AGENT_HOST` jaeger agent host
- `OTEL_AUTO_JAEGER_AGENT_PORT` jaeger agent port
- `OTEL_AUTO_JAEGER_COLLECTOR_HOST` jaeger collector host, useful when you want to use TCP.
- `OTEL_AUTO_JAEGER_COLLECTOR_PORT` jaeger collector port, this MUST be set with collector.
- `OTEL_AUTO_JAEGER_COLLECTOR_ENDPOINT` see [jaeger API doc](https://opentelemetry-python.readthedocs.io/en/stable/exporter/jaeger/jaeger.html#opentelemetry.exporter.jaeger.JaegerSpanExporter)
- `OTEL_AUTO_JAEGER_COLLECTOR_PROTOCOL` see [jaeger API doc](https://opentelemetry-python.readthedocs.io/en/stable/exporter/jaeger/jaeger.html#opentelemetry.exporter.jaeger.JaegerSpanExporter)
- `OTEL_AUTO_JAEGER_USERNAME`
- `OTEL_AUTO_JAEGER_PASSWORD`

Following environment variables are from `opentelemetry.configuration`.

- `OTEL_TRACER_PROVIDER` takes `opentelemetry_tracer_provider` entry_point name.
- `OTEL_METER_PROVIDER` takes `opentelemetry_meter_provider` entry_point name.
