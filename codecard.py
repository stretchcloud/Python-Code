import json
def codecardjson():
    x = {"template": "template4", "title": "Prasenjit Sarkar", "subtitle": "Cloud Native Evangelist", "bodytext": "Ask me anything on Cloud Native Application World! I run blog.kube-mesh.io", "icon": "microservices", "backgroundColor": "white"}
    y = json.dumps(x)
    print(y)
codecardjson()
