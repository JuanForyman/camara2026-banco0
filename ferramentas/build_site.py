"""Monta site/index.html a partir de site/app.tpl.html, embutindo motor/engine.js."""
import os
raiz = os.path.join(os.path.dirname(__file__), "..")
t = open(f"{raiz}/site/app.tpl.html", encoding="utf-8").read()
m = open(f"{raiz}/motor/engine.js", encoding="utf-8").read()
assert "<!--MOTOR-->" in t
open(f"{raiz}/site/index.html", "w", encoding="utf-8").write(t.replace("<!--MOTOR-->", m))
print("ok", os.path.getsize(f"{raiz}/site/index.html"))
