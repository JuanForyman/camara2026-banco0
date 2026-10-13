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
CF = [(1,4,"CF-princ","Princípios fundamentais (arts. 1º a 4º)"),(6,6,"CF-sociais","Direitos sociais: rol (art. 6º)"),(7,7,"CF-art7","Direitos dos trabalhadores (art. 7º)"),(8,11,"CF-sindic","Sindicatos, greve e representação (arts. 8º a 11)"),
 (12,13,"CF-nac","Nacionalidade (arts. 12 e 13)"),(14,16,"CF-polit","Direitos políticos (arts. 14 a 16)"),(17,17,"CF-partidos","Partidos políticos (art. 17)"),
 (18,19,"CF-fed","Entes federativos e vedações (arts. 18 e 19)"),(20,20,"CF-bens","Bens da União (art. 20)"),(21,21,"CF-c21","Competência material da União (art. 21)"),(22,22,"CF-c22","Competência legislativa privativa da União (art. 22)"),(23,23,"CF-c23","Competência comum (art. 23)"),(24,24,"CF-c24","Competência legislativa concorrente (art. 24)"),
 (25,28,"CF-estados","Estados federados (arts. 25 a 28)"),(29,31,"CF-municipios","Municípios (arts. 29 a 31)"),(32,33,"CF-dfterr","Distrito Federal e Territórios (arts. 32 e 33)"),(34,36,"CF-interv","Intervenção (arts. 34 a 36)"),
 (37,38,"CF-adm","Princípios e regras da administração pública (arts. 37 e 38)"),(39,40,"CF-servidores","Servidores civis: regime e previdência (arts. 39 e 40)"),(41,41,"CF-estab","Estabilidade do servidor (art. 41)"),(42,42,"CF-militares","Servidores militares (arts. 42, 142 e 143)"),(43,43,"CF-regioes","Regiões (art. 43)"),(142,143,"CF-militares","Servidores militares (arts. 42, 142 e 143)"),
 (44,47,"CF-congresso","Estrutura do Congresso Nacional (arts. 44 a 47)"),(48,48,"CF-art48","Matérias de lei do Congresso com sanção (art. 48)"),(49,52,"CF-compcasas","Competências do Congresso, da Câmara e do Senado (arts. 49 a 52)"),
 (53,56,"CF-parl","Estatuto dos parlamentares (arts. 53 a 56)"),(57,58,"CF-func","Funcionamento e comissões (arts. 57 e 58)"),
 (59,59,"CF-pl-esp","Espécies normativas (art. 59)"),(60,60,"CF-emenda","Emendas à Constituição (art. 60)"),(61,67,"CF-pl","Processo legislativo: iniciativa, MP, sanção e veto (arts. 61 a 67)"),
 (68,69,"CF-deleg","Leis delegadas e complementares (arts. 68 e 69)"),(70,75,"CF-controle","Fiscalização e controle externo (arts. 70 a 75)")]
# art. 5º por intervalos de inciso
C5 = [(1,15,"CF5-liberd","Art. 5º: igualdade, liberdades e intimidade (I a XV)"),(16,21,"CF5-assoc","Art. 5º: reunião e associação (XVI a XXI)"),
 (22,31,"CF5-prop","Art. 5º: propriedade (XXII a XXXI)"),(32,40,"CF5-garant","Art. 5º: garantias gerais e legalidade penal (XXXII a XL)"),
 (41,52,"CF5-penal","Art. 5º: crimes, penas e extradição (XLI a LII)"),(53,68,"CF5-proc","Art. 5º: devido processo e prisão (LIII a LXVIII)"),
 (69,73,"CF5-remedios","Art. 5º: remédios constitucionais (LXIX a LXXIII)"),(74,78,"CF5-acesso","Art. 5º: assistência, indenização e duração do processo (LXXIV a LXXVIII)")]
L9784 = [(1,2,"L9784-disp","Lei 9.784: disposições gerais e princípios (arts. 1º e 2º)"),(3,4,"L9784-dir","Lei 9.784: direitos e deveres do administrado (arts. 3º e 4º)"),(5,8,"L9784-inicio","Lei 9.784: início do processo (arts. 5º a 8º)"),
 (9,10,"L9784-interess","Lei 9.784: interessados (arts. 9º e 10)"),(11,17,"L9784-comp","Lei 9.784: competência (arts. 11 a 17)"),(18,21,"L9784-imped","Lei 9.784: impedimento e suspeição (arts. 18 a 21)"),
 (22,28,"L9784-atos","Lei 9.784: forma, tempo, lugar e comunicação dos atos (arts. 22 a 28)"),(29,47,"L9784-instr","Lei 9.784: instrução (arts. 29 a 47)"),(48,55,"L9784-decisao","Lei 9.784: dever de decidir, motivação, anulação e revogação (arts. 48 a 55)"),
 (56,65,"L9784-recurso","Lei 9.784: recurso administrativo e revisão (arts. 56 a 65)"),(66,69,"L9784-prazos","Lei 9.784: prazos, sanções e disposições finais (arts. 66 a 69)")]
def campo(atom):
    ml = re.match(r"A-L9784-(\d+)", atom)
    if ml:
        a = int(ml.group(1))
        for lo, hi, cid, nm in L9784:
            if lo <= a <= hi: return (cid, nm)
        return None
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
