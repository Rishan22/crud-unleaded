# ◆ CRUD Site Generator 

Generic CRUD site w/ themes. 

Clone into repository, run setup.sh. That's all🎉

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
