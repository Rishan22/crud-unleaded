# ◆ CRUD Site Generator 

Template site generation w/ labels and themes. 

Clone into repository
and run:

```
chmod +x setup.sh
./setup.sh
```

That's all 🎉

----
### Blueprint:

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
