import json
ind="banking"
cfg={"industry":ind,"mode":"solo","brand":"Demo","ux":"mono"}
open("config.json","w").write(json.dumps(cfg))
