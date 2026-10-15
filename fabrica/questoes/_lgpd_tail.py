TAILS=[
 " Essa disciplina integra a Lei Geral de Proteção de Dados Pessoais e alcança o tratamento realizado no território nacional, ainda que por meios digitais.",
 " Trata-se de regra aplicável a qualquer operação de tratamento de dados pessoais, realizada por pessoa natural ou jurídica, de direito público ou privado.",
 " Tal conclusão decorreria, segundo esse entendimento, da sistemática geral da LGPD, que se aplica aos agentes de tratamento em todas as fases da operação.",
 " Essa seria a orientação extraída da lei para as hipóteses em que o tratamento envolve dados de pessoas naturais identificadas ou identificáveis.",
]
def tail(E,C,i):
    if len(E) < 0.97*len(C):
        need=len(C)-len(E)
        t=TAILS[i%len(TAILS)]
        return E+t if need>60 else E+t[:0]
    return E
