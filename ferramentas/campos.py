"""Atribui a cada questão do banco o 'campo' (q.f): grupo de átomos vizinhos que o motor trata como um mesmo terreno
(acertar em um reduz a urgência dos irmãos; uma questão por campo por bloco; campo dominado é revisado espaçado).
Uso: python3 -I campos.py <banco.json> <campos.json>   (idempotente). Regimentos: sem agrupamento (campo = átomo)."""
import json, re, sys
ROM = {"I":1,"V":5,"X":10,"L":50,"C":100}
def rom(s):
    n = 0
    for i, c in enumerate(s):
        v = ROM[c]; n += -v if i+1 < len(s) and ROM[s[i+1]] > v else v
    return n
# (art_ini, art_fim, id, nome)
CF = [(1,4,"CF-princ","Princípios fundamentais (arts. 1º a 4º)"),(6,11,"CF-sociais","Direitos sociais e sindicais (arts. 6º a 11)"),
 (12,13,"CF-nac","Nacionalidade (arts. 12 e 13)"),(14,16,"CF-polit","Direitos políticos (arts. 14 a 16)"),(17,17,"CF-partidos","Partidos políticos (art. 17)"),
 (18,19,"CF-fed","Entes federativos e vedações (arts. 18 e 19)"),(20,24,"CF-comp","Bens e competências (arts. 20 a 24)"),
 (25,33,"CF-estmun","Estados, Municípios e DF (arts. 25 a 33)"),(34,36,"CF-interv","Intervenção (arts. 34 a 36)"),
 (37,38,"CF-adm","Princípios e regras da administração pública (arts. 37 e 38)"),(41,41,"CF-estab","Estabilidade do servidor (art. 41)"),
 (44,48,"CF-congresso","Estrutura do Congresso Nacional (arts. 44 a 48)"),(49,52,"CF-compcasas","Competências do Congresso, da Câmara e do Senado (arts. 49 a 52)"),
 (53,56,"CF-parl","Estatuto dos parlamentares (arts. 53 a 56)"),(57,58,"CF-func","Funcionamento e comissões (arts. 57 e 58)"),
 (59,59,"CF-pl-esp","Espécies normativas (art. 59)"),(60,60,"CF-emenda","Emendas à Constituição (art. 60)"),(61,67,"CF-pl","Processo legislativo: iniciativa, MP, sanção e veto (arts. 61 a 67)"),
 (68,69,"CF-deleg","Leis delegadas e complementares (arts. 68 e 69)"),(70,75,"CF-controle","Fiscalização e controle externo (arts. 70 a 75)")]
# art. 5º por intervalos de inciso
C5 = [(1,15,"CF5-liberd","Art. 5º: igualdade, liberdades e intimidade (I a XV)"),(16,21,"CF5-assoc","Art. 5º: reunião e associação (XVI a XXI)"),
 (22,31,"CF5-prop","Art. 5º: propriedade (XXII a XXXI)"),(32,40,"CF5-garant","Art. 5º: garantias gerais e legalidade penal (XXXII a XL)"),
 (41,52,"CF5-penal","Art. 5º: crimes, penas e extradição (XLI a LII)"),(53,68,"CF5-proc","Art. 5º: devido processo e prisão (LIII a LXVIII)"),
 (69,73,"CF5-remedios","Art. 5º: remédios constitucionais (LXIX a LXXIII)"),(74,78,"CF5-acesso","Art. 5º: assistência, indenização e duração do processo (LXXIV a LXXVIII)")]
def campo(atom):
    m = re.match(r"A-CF-(\d+)(?:\.([IVXLC]+))?$", atom)
    if not m: return None
    a = int(m.group(1))
    if a == 5:
        if not m.group(2): return ("CF5-par", "Art. 5º: caput e parágrafos")
        i = rom(m.group(2))
        for lo, hi, cid, nm in C5:
            if lo <= i <= hi: return (cid, nm)
    for lo, hi, cid, nm in CF:
        if lo <= a <= hi: return (cid, nm)
    return None
B = json.load(open(sys.argv[1], encoding="utf-8")); names = {}
for q in B:
    q.pop("f", None)
    cs = {campo(a) for a in q.get("a", []) if campo(a)}
    if len(cs) == 1:
        cid, nm = next(iter(cs)); q["f"] = cid; names[cid] = nm
json.dump(B, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
json.dump(names, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(sum("f" in q for q in B), "questões com campo;", len(names), "campos")
