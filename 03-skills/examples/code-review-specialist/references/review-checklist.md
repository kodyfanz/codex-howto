# Risk-focused review checklist

Use only relevant sections.

## Correctness

- Trace changed inputs through outputs and state transitions.
- Check boundary values, empty states, partial failures, and error propagation.
- Look for behavior changes hidden by refactoring or default values.

## Security and privacy

- Verify identity, authorization, validation, and secret-handling boundaries.
- Check whether logs or errors expose sensitive data.
- Treat external input, generated commands, and deserialization as untrusted.

## Reliability and concurrency

- Check retry safety, idempotency, cleanup, timeouts, and cancellation.
- Look for lost updates, races, lock ordering, and stale reads.
- Verify that partial completion leaves recoverable state.

## Compatibility

- Identify public API, schema, configuration, and migration impacts.
- Check rollout order when old and new versions may coexist.
- Confirm failure behavior when a dependency lacks the new capability.

## Tests

- Prefer a test that reproduces the concrete risk.
- Do not request coverage solely to increase a metric.
- Note when the existing suite could not be run.
