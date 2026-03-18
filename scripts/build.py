import re,yaml,json,os
from logo import gen

txt=open("README.md").read()
block=re.search(r"```yaml(.*?)```",txt,re.S).group(1)
spec=yaml.safe_load(block)
themes=yaml.safe_load(open("themes.yaml"))
cfg=json.load(open("config.json"))

theme=themes[cfg["industry"]]

os.makedirs("dist",exist_ok=True)
logo=gen(cfg["brand"])

open("dist/index.html","w").write("<html><body><h1>"+cfg["brand"]+"</h1>"+logo+"</body></html>")
