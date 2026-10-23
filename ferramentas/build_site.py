"""Monta site/index.html a partir de site/app.tpl.html, embutindo motor/engine.js."""
import os, json
raiz = os.path.join(os.path.dirname(__file__), "..")
t = open(f"{raiz}/site/app.tpl.html", encoding="utf-8").read()
m = open(f"{raiz}/motor/engine.js", encoding="utf-8").read()
assert "<!--MOTOR-->" in t
esp = {x["t"]: x["esp"] for x in json.load(open(f"{raiz}/dados/mapa_cobertura.json", encoding="utf-8")) if "esp" in x}
m += "\nMotor.setPesos(" + json.dumps(esp, separators=(",", ":")) + ");\n"
open(f"{raiz}/site/index.html", "w", encoding="utf-8").write(t.replace("<!--MOTOR-->", m))
print("ok", os.path.getsize(f"{raiz}/site/index.html"))
