
opentelemetry already has some configuration mechanism.
- `OTEL_TRACER_PROVIDER` configures opentelemetry configuration module.
- `opentelemetry-instrument` automatically loads instrumentation code.

This module provides out-of-box automatic configuration.
Just install, and lauch target program normally with configuration
environment variables.

```
$ OTEL_TRACER_PROVIDER=sdk_tracer_provider \
  OTEL_AUTO_JAEGER_SERVICE_NAME=foo \
  python foo.py
```

