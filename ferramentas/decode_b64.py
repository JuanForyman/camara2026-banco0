"""Decodifica o campo `content` (base64) de um JSON de download do Drive para um arquivo.
Uso: python3 -I decode_b64.py <entrada.json> <saida>"""
import base64
import json
import sys

src, dst = sys.argv[1], sys.argv[2]
with open(src, encoding="utf-8") as f:
    d = json.load(f)
raw = base64.b64decode(d["content"])
with open(dst, "wb") as f:
    f.write(raw)
print(d.get("title"), d.get("mimeType"), len(raw), "bytes", raw[:5])
