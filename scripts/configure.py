import json

industries = ["banking","ecommerce","healthcare","logistics","identity"]

print("Select industry:")
for i,x in enumerate(industries,1): print(i,x)
ind = industries[int(input("> "))-1]

mode = ["solo","team"][int(input("1 solo, 2 team: "))-1]
brand = input("Brand name: ")
ux = ["mono","palette"][int(input("1 mono, 2 palette: "))-1]

cfg = {"industry":ind,"mode":mode,"brand":brand,"ux":ux}
open("config.json","w").write(json.dumps(cfg))
