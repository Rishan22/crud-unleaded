import re,yaml,json,os
from logo import gen

txt=open("README.md").read()
block=re.search(r"```yaml(.*?)```",txt,re.S).group(1)
spec=yaml.safe_load(block)
themes=yaml.safe_load(open("themes.yaml"))
cfg=json.load(open("config.json"))

theme=themes[cfg["industry"]]
os.makedirs("dist",exist_ok=True)

items=[]
for role in spec["entities"]:
    items.append(f"<li>{theme.get(role,role)}</li>")

logo=gen(cfg["brand"])

html = f"""<html><body>
<h1>{cfg['brand']}</h1>
{logo}
<ul>{''.join(items)}</ul>
</body></html>"""

open("dist/index.html","w").write(html)
