# Refinery

Generic site generator w/ themes.

<!-- BEGIN_SPEC -->
```yaml
entities:
  - Actor
  - LifecycleObject
  - Container
  - Definition
  - Event
  - System

paths:
  LifecycleObject:
    GET: ["/{id}", "/template"]
    POST: ["/", "/{id}?command=activate", "/{id}?command=close"]
    PUT: ["/{id}"]
    DELETE: ["/{id}"]

global:
  query: [fields, pretty, template]
```
<!-- END_SPEC -->
