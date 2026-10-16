# Lei 14.133/2021 — lote L7 parte f (arts. 92 a 125)
Q = []
TAILS=[" Essa disciplina consta da Lei n.º 14.133/2021 e se aplica às licitações e contratações por ela regidas.",
 " Trata-se de regra do regime geral de licitações e contratos da Administração Pública, nos termos da Lei n.º 14.133/2021.",
 " Tal conclusão decorreria, segundo esse entendimento, da sistemática geral da nova Lei de Licitações e Contratos Administrativos.",
 " Essa seria a orientação extraída da lei para o procedimento de licitação de que ela trata."]
def tail(E,C,i):
    if len(E) < 0.97*len(C) and len(C)-len(E) > 60: return E+TAILS[i%len(TAILS)]
    return E
def P(ponto, arts, padC, padE, dif, C, E, com, terro, tag, risco=None):
    ex = {"risco": risco} if risco else {}
    E = tail(E, C, len(Q))
    padC = padE if padC == 'conceito_correto' else padC
    Q.append((ponto, arts, "C", padC, dif, C, com, "", tag, ex))
    Q.append((ponto, arts, "E", padE, dif, E, com, terro, tag, ex))
# T32
P("T32",["92"],"conceito_correto","excecao_omitida",3,
 "São necessárias em todo contrato cláusulas que estabeleçam, entre outros itens, o objeto e seus elementos característicos, a vinculação ao edital e à proposta do vencedor ou ao ato que autorizou a contratação direta, a legislação aplicável à execução do contrato, o regime de execução, o preço e as condições de pagamento, as garantias, a matriz de risco quando for o caso e os casos de extinção.",
 "São necessárias em todo contrato cláusulas que estabeleçam, entre outros itens, o objeto, o preço e a matriz de risco, esta em todos os contratos, dispensadas cláusulas sobre garantias e casos de extinção, que decorrem da lei.",
 "Art. 92, I a XIX (a matriz de risco é exigida quando for o caso).","torna matriz obrigatória e retira cláusulas","t32a")
P("T32",["92"],"conceito_correto","excecao_omitida",4,
 "Os contratos celebrados pela Administração Pública com pessoas físicas ou jurídicas, inclusive as domiciliadas no exterior, deverão conter cláusula que declare competente o foro da sede da Administração para dirimir qualquer questão contratual, ressalvados os casos de licitação internacional financiada por organismo financeiro internacional, compra de equipamentos fabricados e entregues no exterior mediante autorização do Chefe do Poder Executivo e aquisições por unidades administrativas com sede no exterior.",
 "Os contratos celebrados pela Administração Pública com pessoas jurídicas domiciliadas no exterior poderão eleger livremente o foro, sem ressalvas, e os celebrados com pessoas físicas ou jurídicas nacionais deverão eleger o foro do domicílio do contratado.",
 "Art. 92, § 1º.","troca foro","t32b")
P("T32",["92"],"conceito_correto","excecao_omitida",4,
 "Independentemente do prazo de duração, o contrato deverá conter cláusula que estabeleça o índice de reajustamento de preço, com data-base vinculada à data do orçamento estimado; nos contratos de serviços contínuos, observado o interregno mínimo de 1 ano, o reajuste será por reajustamento em sentido estrito quando não houver dedicação exclusiva ou predominância de mão de obra e por repactuação quando houver.",
 "O contrato de duração inferior a 1 ano dispensa cláusula de reajustamento; nos contratos de serviços contínuos com dedicação exclusiva de mão de obra, o critério será o reajustamento em sentido estrito por índices setoriais, e a repactuação aplica-se aos demais.",
 "Art. 92, §§ 3º e 4º.","troca reajuste e repactuação","t32c")
P("T32",["92"],"conceito_correto","troca_numero",4,
 "Nos contratos de obras e serviços de engenharia, sempre que compatível com o regime de execução, a medição será mensal; e, nos contratos de serviços contínuos com dedicação exclusiva de mão de obra, o prazo para resposta ao pedido de repactuação será preferencialmente de 1 mês, contado do fornecimento da documentação.",
 "Nos contratos de obras e serviços de engenharia, a medição será trimestral; e o prazo para resposta ao pedido de repactuação será obrigatoriamente de 3 meses, contado do protocolo do pedido.",
 "Art. 92, §§ 5º e 6º.","troca periodicidade e prazo","t32d")
# T33
P("T33",["93"],"conceito_correto","excecao_omitida",4,
 "Nas contratações de projetos ou de serviços técnicos especializados, inclusive de software, o autor deverá ceder todos os direitos patrimoniais à Administração, que poderá utilizá-los e alterá-los livremente em outras ocasiões; a Administração poderá deixar de exigir a cessão quando o objeto envolver atividade de pesquisa e desenvolvimento de caráter científico, tecnológico ou de inovação.",
 "Nas contratações de projetos ou de serviços técnicos especializados, inclusive de software, o autor conservará os direitos patrimoniais, cabendo à Administração obter nova autorização do autor para utilizar ou alterar o projeto em outras ocasiões, sem exceções.",
 "Art. 93, caput e § 2º.","mantém direitos com o autor","t33a")
P("T33",["94"],"conceito_correto","troca_numero",4,
 "A divulgação no PNCP é condição indispensável para a eficácia do contrato e de seus aditamentos e deverá ocorrer em até 20 dias úteis, no caso de licitação, e em até 10 dias úteis, no caso de contratação direta, contados da data de assinatura.",
 "A divulgação no PNCP é condição de mera publicidade, sem efeito sobre a eficácia do contrato, e deverá ocorrer em até 10 dias úteis, no caso de licitação, e em até 20 dias úteis, no caso de contratação direta, contados da data de assinatura.",
 "Art. 94, caput, I e II.","troca prazos e efeito","t33b")
P("T33",["94"],"conceito_correto","troca_efeito",5,
 "Os contratos celebrados em caso de urgência terão eficácia a partir de sua assinatura e deverão ser publicados nos prazos legais, sob pena de nulidade; a divulgação da contratação de profissional do setor artístico por inexigibilidade deverá identificar os custos do cachê, do transporte, da hospedagem, da infraestrutura e da logística do evento.",
 "Os contratos celebrados em caso de urgência só terão eficácia após a publicação no PNCP, e a divulgação da contratação de profissional do setor artístico por inexigibilidade dispensa a identificação dos custos do cachê e das demais despesas.",
 "Art. 94, §§ 1º e 2º.","inverte urgência e dispensa custos","t33c")
P("T33",["94"],"conceito_correto","troca_numero",5,
 "No caso de obras, a Administração divulgará em sítio eletrônico oficial, em até 25 dias úteis após a assinatura do contrato, os quantitativos e preços unitários e totais que contratar e, em até 45 dias úteis após a conclusão do contrato, os quantitativos executados e os preços praticados.",
 "No caso de obras, a Administração divulgará em sítio eletrônico oficial, em até 45 dias úteis após a assinatura do contrato, os quantitativos e preços contratados e, em até 25 dias úteis após a conclusão do contrato, os quantitativos executados e os preços praticados.",
 "Art. 94, § 3º.","inverte prazos","t33d")
# T34
P("T34",["95"],"conceito_correto","excecao_omitida",3,
 "O instrumento de contrato é obrigatório, salvo nas hipóteses de dispensa de licitação em razão de valor e de compras com entrega imediata e integral dos bens adquiridos, das quais não resultem obrigações futuras, independentemente do valor, em que a Administração poderá substituí-lo por carta-contrato, nota de empenho, autorização de compra ou ordem de execução de serviço.",
 "O instrumento de contrato é dispensável em qualquer contratação direta, e sua substituição por nota de empenho só é admitida para compras de valor inferior ao limite da dispensa em razão de valor.",
 "Art. 95, I e II.","amplia dispensa do instrumento","t34a")
P("T34",["95"],"conceito_correto","troca_numero",4,
 "É nulo e de nenhum efeito o contrato verbal com a Administração, salvo o de pequenas compras ou o de prestação de serviços de pronto pagamento, assim entendidos aqueles de valor não superior ao limite legal, que na redação original era de R$ 10.000,00.",
 "É válido o contrato verbal com a Administração, salvo se de valor superior a R$ 50.000,00, caso em que será anulável.",
 "Art. 95, § 2º. Valor atualizado por decreto.","admite verbal em geral","t34b",["valor_atualizado_por_decreto"])
P("T34",["96"],"conceito_correto","troca_autoridade",3,
 "A critério da autoridade competente, em cada caso, poderá ser exigida, mediante previsão no edital, prestação de garantia nas contratações de obras, serviços e fornecimentos, cabendo ao contratado optar entre caução em dinheiro ou títulos da dívida pública, seguro-garantia e fiança bancária.",
 "A garantia nas contratações de obras, serviços e fornecimentos será sempre obrigatória, e a Administração escolherá a modalidade entre caução, seguro-garantia e fiança bancária.",
 "Art. 96, caput e § 1º.","torna obrigatória e troca quem escolhe","t34c")
P("T34",["96"],"conceito_correto","troca_numero",4,
 "Na suspensão do contrato por ordem ou inadimplemento da Administração, o contratado fica desobrigado de renovar a garantia ou de endossar a apólice até a ordem de reinício da execução ou o adimplemento pela Administração; e o edital fixará prazo mínimo de 1 mês, contado da homologação e anterior à assinatura do contrato, para a prestação da garantia na modalidade seguro-garantia.",
 "Na suspensão do contrato por ordem da Administração, o contratado continua obrigado a renovar a garantia; e o edital fixará prazo máximo de 1 mês, contado da assinatura do contrato, para a prestação da garantia na modalidade seguro-garantia.",
 "Art. 96, §§ 2º e 3º.","inverte renovação e prazo","t34d")
P("T34",["97"],"conceito_correto","excecao_omitida",4,
 "O seguro-garantia visa a garantir o fiel cumprimento das obrigações do contratado, inclusive multas, prejuízos e indenizações; o prazo de vigência da apólice será igual ou superior ao do contrato principal, e o seguro continuará em vigor mesmo se o contratado não tiver pago o prêmio nas datas convencionadas.",
 "No seguro-garantia, a apólice terá vigência de 1 ano, independentemente do prazo do contrato, e perderá a eficácia se o contratado deixar de pagar o prêmio nas datas convencionadas.",
 "Art. 97, I e II.","troca vigência e inadimplência do prêmio","t34e")
P("T34",["98"],"conceito_correto","troca_numero",4,
 "Nas contratações de obras, serviços e fornecimentos, a garantia poderá ser de até 5% do valor inicial do contrato, autorizada a majoração desse percentual para até 10%, desde que justificada mediante análise da complexidade técnica e dos riscos envolvidos.",
 "Nas contratações de obras, serviços e fornecimentos, a garantia poderá ser de até 10% do valor inicial do contrato, autorizada a majoração desse percentual para até 30%, independentemente de justificativa.",
 "Art. 98.","troca percentuais","t34f")
P("T34",["99"],"conceito_correto","troca_numero",4,
 "Nas contratações de obras e serviços de engenharia de grande vulto, poderá ser exigida a prestação de garantia, na modalidade seguro-garantia com cláusula de retomada, em percentual equivalente a até 30% do valor inicial do contrato.",
 "Nas contratações de obras e serviços de engenharia de grande vulto, poderá ser exigida a prestação de garantia, na modalidade fiança bancária com cláusula de retomada, em percentual equivalente a até 50% do valor inicial do contrato.",
 "Art. 99.","troca modalidade e percentual","t34g")
P("T34",["100","101"],"conceito_correto","troca_efeito",3,
 "A garantia prestada pelo contratado será liberada ou restituída após a fiel execução do contrato ou após a sua extinção por culpa exclusiva da Administração e, quando em dinheiro, atualizada monetariamente; nos contratos em que o contratado ficar depositário de bens entregues pela Administração, o valor desses bens será acrescido ao valor da garantia.",
 "A garantia prestada pelo contratado será liberada após a fiel execução do contrato, sendo retida em caso de extinção por culpa exclusiva da Administração; e, quando em dinheiro, será devolvida sem atualização monetária.",
 "Arts. 100 e 101.","retém garantia e nega correção","t34h")
P("T34",["102"],"conceito_correto","excecao_omitida",5,
 "Na contratação de obras e serviços de engenharia, o edital poderá exigir seguro-garantia com cláusula de retomada, em que, havendo inadimplemento do contratado, a seguradora assume a execução e conclui o objeto; se concluir, ficará isenta de pagar a importância segurada, e se não assumir a execução, pagará a integralidade da importância segurada indicada na apólice.",
 "Na contratação de obras e serviços de engenharia, o edital poderá exigir seguro-garantia com cláusula de retomada, em que, havendo inadimplemento do contratado, a seguradora assume a execução e, mesmo que a conclua, deverá pagar a importância segurada, sendo vedada a subcontratação da conclusão.",
 "Art. 102 e parágrafo único.","exige pagamento mesmo concluindo","t34i")
# T35
P("T35",["103"],"conceito_correto","excecao_omitida",4,
 "O contrato poderá prever matriz de alocação de riscos, que considerará a natureza do risco, o beneficiário das prestações e a capacidade de cada setor para melhor gerenciá-lo; os riscos que tenham cobertura oferecida por seguradoras serão preferencialmente transferidos ao contratado, e a matriz definirá o equilíbrio econômico-financeiro inicial em relação a eventos supervenientes.",
 "O contrato deverá, em qualquer caso, prever matriz de alocação de riscos, e os riscos que tenham cobertura oferecida por seguradoras serão preferencialmente assumidos pela Administração.",
 "Art. 103, caput e §§ 1º, 2º e 4º.","torna obrigatória e inverte seguro","t35a")
P("T35",["103"],"conceito_correto","excecao_omitida",5,
 "Atendidas as condições do contrato e da matriz de alocação de riscos, considera-se mantido o equilíbrio econômico-financeiro, renunciando as partes aos pedidos de restabelecimento relacionados aos riscos assumidos, exceto quanto às alterações unilaterais determinadas pela Administração e ao aumento ou redução, por legislação superveniente, dos tributos diretamente pagos pelo contratado em decorrência do contrato.",
 "Mesmo atendidas as condições da matriz de alocação de riscos, as partes poderão pleitear o restabelecimento do equilíbrio econômico-financeiro em relação a qualquer risco assumido, e a legislação tributária superveniente não afeta o equilíbrio do contrato.",
 "Art. 103, § 5º, I e II.","nega renúncia e exceções","t35b")
P("T35",["104"],"conceito_correto","excecao_omitida",3,
 "O regime jurídico dos contratos confere à Administração as prerrogativas de modificá-los unilateralmente, extingui-los unilateralmente nos casos legais, fiscalizar sua execução, aplicar sanções motivadas pela inexecução e ocupar provisoriamente bens e utilizar pessoal e serviços vinculados ao objeto em caso de risco à prestação de serviços essenciais ou de necessidade de acautelar apuração administrativa de faltas contratuais.",
 "O regime jurídico dos contratos confere à Administração as prerrogativas de modificá-los e extingui-los unilateralmente sem observância dos direitos do contratado, e de ocupar provisoriamente bens do contratado em qualquer hipótese de inadimplemento.",
 "Art. 104, I a V.","amplia prerrogativas","t35c")
P("T35",["104"],"conceito_correto","troca_efeito",4,
 "As cláusulas econômico-financeiras e monetárias dos contratos não poderão ser alteradas sem prévia concordância do contratado; na modificação unilateral para melhor adequação às finalidades de interesse público, as cláusulas econômico-financeiras deverão ser revistas para que se mantenha o equilíbrio contratual.",
 "As cláusulas econômico-financeiras e monetárias dos contratos poderão ser alteradas unilateralmente pela Administração, sem necessidade de revisão do equilíbrio contratual na modificação por interesse público.",
 "Art. 104, §§ 1º e 2º.","permite alteração unilateral das cláusulas econômicas","t35d")
# T36
P("T36",["105"],"conceito_correto","excecao_omitida",3,
 "A duração dos contratos será a prevista em edital, e deverão ser observadas, no momento da contratação e a cada exercício financeiro, a disponibilidade de créditos orçamentários, bem como a previsão no plano plurianual, quando ultrapassar 1 exercício financeiro.",
 "A duração dos contratos ficará limitada à vigência dos respectivos créditos orçamentários, de 1 exercício financeiro, vedada a celebração de contratos plurianuais.",
 "Art. 105.","limita ao exercício","t36a")
P("T36",["106"],"conceito_correto","troca_numero",4,
 "A Administração poderá celebrar contratos com prazo de até 5 anos nas hipóteses de serviços e fornecimentos contínuos, desde que a autoridade competente ateste a maior vantagem econômica da contratação plurianual e a Administração ateste, no início da contratação e de cada exercício, a existência de créditos orçamentários e a vantagem em sua manutenção.",
 "A Administração poderá celebrar contratos com prazo de até 10 anos nas hipóteses de serviços e fornecimentos contínuos, dispensada a atestação da vantagem econômica e da existência de créditos orçamentários a cada exercício.",
 "Art. 106, I e II.","troca prazo e dispensa atestações","t36b")
P("T36",["106"],"conceito_correto","troca_numero",5,
 "Nos contratos plurianuais de serviços e fornecimentos contínuos de até 5 anos, a Administração terá a opção de extinguir o contrato, sem ônus, quando não dispuser de créditos orçamentários ou entender que o contrato não mais lhe oferece vantagem; a extinção ocorrerá apenas na próxima data de aniversário do contrato e não poderá ocorrer em prazo inferior a 2 meses, contado dessa data.",
 "Nos contratos plurianuais de serviços e fornecimentos contínuos de até 5 anos, a Administração poderá extinguir o contrato, sem ônus, a qualquer tempo, ainda que sem prazo mínimo, quando entender que o contrato não mais lhe oferece vantagem.",
 "Art. 106, III e § 1º.","permite extinção a qualquer tempo","t36c")
P("T36",["107"],"conceito_correto","excecao_omitida",4,
 "Os contratos de serviços e fornecimentos contínuos poderão ser prorrogados sucessivamente, respeitada a vigência máxima decenal, desde que haja previsão em edital e que a autoridade competente ateste que as condições e os preços permanecem vantajosos, permitida a negociação com o contratado ou a extinção contratual sem ônus para qualquer das partes.",
 "Os contratos de serviços e fornecimentos contínuos poderão ser prorrogados sucessivamente, respeitada a vigência máxima de 5 anos, independentemente de previsão em edital, desde que o contratado concorde com a prorrogação.",
 "Art. 107.","troca limite e dispensa edital","t36d")
P("T36",["108"],"conceito_correto","troca_numero",5,
 "A Administração poderá celebrar contratos com prazo de até 10 anos nas hipóteses de dispensa para bens ou serviços de alta complexidade tecnológica e defesa nacional, materiais de uso das Forças Armadas, transferência de tecnologia e contratações que possam acarretar comprometimento da segurança nacional, entre outras previstas nos incisos do art. 75.",
 "A Administração poderá celebrar contratos com prazo de até 5 anos nas hipóteses de dispensa para bens ou serviços de alta complexidade tecnológica e defesa nacional, vedada prazo superior em qualquer hipótese do art. 75.",
 "Art. 108.","troca prazo","t36e")
P("T36",["109","110"],"conceito_correto","troca_numero",5,
 "Nos contratos que gerem receita e nos contratos de eficiência que gerem economia para a Administração, os prazos serão de até 10 anos nos contratos sem investimento e de até 35 anos nos contratos com investimento, assim considerados os que impliquem benfeitorias permanentes realizadas exclusivamente a expensas do contratado, revertidas ao patrimônio da Administração ao término do contrato.",
 "Nos contratos que gerem receita e nos contratos de eficiência que gerem economia para a Administração, os prazos serão de até 5 anos nos contratos sem investimento e de até 20 anos nos contratos com investimento, sem reversão de benfeitorias ao término do contrato.",
 "Art. 110, I e II.","troca prazos","t36f")
P("T36",["109"],"conceito_correto","excecao_omitida",4,
 "A Administração poderá estabelecer a vigência por prazo indeterminado nos contratos em que seja usuária de serviço público oferecido em regime de monopólio, desde que comprovada, a cada exercício financeiro, a existência de créditos orçamentários vinculados à contratação.",
 "A Administração poderá estabelecer a vigência por prazo indeterminado em qualquer contrato de serviço contínuo, desde que haja previsão no edital, dispensada a comprovação anual de créditos orçamentários.",
 "Art. 109.","generaliza prazo indeterminado","t36g")
P("T36",["111","112","113","114"],"conceito_correto","troca_numero",5,
 "Na contratação que previr a conclusão de escopo predefinido, o prazo de vigência será automaticamente prorrogado quando o objeto não for concluído no período firmado; no regime de fornecimento e prestação de serviço associado, a vigência é a soma do prazo do fornecimento inicial ou da entrega da obra com o do serviço de operação e manutenção, este limitado a 5 anos; e o contrato de operação continuada de sistemas estruturantes de tecnologia da informação poderá ter vigência máxima de 15 anos.",
 "Na contratação que previr a conclusão de escopo predefinido, o prazo de vigência não será prorrogado automaticamente; no regime de fornecimento e prestação de serviço associado, o serviço de operação e manutenção é limitado a 10 anos; e o contrato de operação continuada de sistemas estruturantes de tecnologia da informação poderá ter vigência máxima de 10 anos.",
 "Arts. 111, 113 e 114.","troca regras de prazo","t36h")
P("T36",["111"],"conceito_correto","excecao_omitida",4,
 "Quando a não conclusão do escopo predefinido decorrer de culpa do contratado, ele será constituído em mora, aplicáveis a ele as respectivas sanções administrativas, e a Administração poderá optar pela extinção do contrato, adotando as medidas admitidas em lei para a continuidade da execução contratual.",
 "Quando a não conclusão do escopo predefinido decorrer de culpa do contratado, a vigência será prorrogada sem sanções, sendo vedada à Administração optar pela extinção do contrato.",
 "Art. 111, parágrafo único.","afasta sanção e extinção","t36i")
# T37
P("T37",["115"],"conceito_correto","excecao_omitida",3,
 "É proibido à Administração retardar imotivadamente a execução de obra ou serviço, ou de suas parcelas, inclusive na hipótese de posse do respectivo chefe do Poder Executivo ou de novo titular no órgão ou entidade contratante; em caso de impedimento, ordem de paralisação ou suspensão do contrato, o cronograma será prorrogado automaticamente pelo tempo correspondente, anotadas as circunstâncias mediante simples apostila.",
 "A Administração poderá retardar a execução de obra ou serviço na hipótese de posse de novo titular no órgão contratante; em caso de paralisação, o cronograma só será prorrogado mediante termo aditivo.",
 "Art. 115, §§ 1º e 5º.","permite retardo e exige aditivo","t37a")
P("T37",["115"],"conceito_correto","troca_numero",4,
 "Nas contratações de obras, verificada a paralisação por mais de 1 mês, a Administração deverá divulgar, em sítio eletrônico oficial e em placa afixada no local da obra, aviso público de obra paralisada, com o motivo, o responsável pela inexecução temporária e a data prevista para o reinício; e, quando a responsabilidade pelo licenciamento ambiental for da Administração, a licença prévia deverá ser obtida antes da divulgação do edital.",
 "Nas contratações de obras, verificada a paralisação por mais de 6 meses, a Administração poderá divulgar aviso público de obra paralisada em sítio eletrônico oficial; e a licença prévia poderá ser obtida após a divulgação do edital, antes da assinatura do contrato.",
 "Art. 115, §§ 4º, 6º e 7º.","troca prazo e momento da licença","t37b")
P("T37",["116","118"],"conceito_correto","excecao_omitida",3,
 "Ao longo de toda a execução do contrato, o contratado deverá cumprir a reserva de cargos prevista em lei para pessoa com deficiência, reabilitado da Previdência Social e aprendiz, e comprovar o cumprimento sempre que solicitado; deverá ainda manter preposto aceito pela Administração no local da obra ou do serviço para representá-lo na execução do contrato.",
 "O contratado deverá cumprir a reserva de cargos para pessoa com deficiência apenas na assinatura do contrato; e a manutenção de preposto no local da obra ou do serviço é facultativa, a critério do contratado.",
 "Arts. 116 e 118.","limita reserva de cargos e preposto","t37c")
P("T37",["117"],"conceito_correto","excecao_omitida",4,
 "A execução do contrato deverá ser acompanhada e fiscalizada por 1 ou mais fiscais, representantes da Administração especialmente designados, permitida a contratação de terceiros para assisti-los; a empresa ou o profissional contratado assumirá responsabilidade civil objetiva pela veracidade das informações prestadas, firmará termo de confidencialidade e não poderá exercer atribuição própria e exclusiva de fiscal, e a contratação de terceiros não eximirá de responsabilidade o fiscal, nos limites das informações recebidas.",
 "A execução do contrato poderá ser fiscalizada por terceiros contratados, que poderão exercer atribuições próprias do fiscal; a contratação de terceiros exime de responsabilidade o fiscal do contrato.",
 "Art. 117, caput e § 4º.","permite terceiro exercer função de fiscal","t37d")
P("T37",["117"],"conceito_correto","troca_autoridade",4,
 "O fiscal do contrato anotará em registro próprio todas as ocorrências relacionadas à execução do contrato, determinando o que for necessário para a regularização das faltas ou defeitos, informará a seus superiores, em tempo hábil, a situação que demandar decisão que ultrapasse sua competência e será auxiliado pelos órgãos de assessoramento jurídico e de controle interno.",
 "O fiscal do contrato decidirá, por si, todas as questões que surgirem na execução, inclusive as que ultrapassem sua competência, e dispensa registro próprio das ocorrências, sendo vedado o auxílio dos órgãos de assessoramento jurídico e de controle interno.",
 "Art. 117, §§ 1º a 3º.","amplia competência do fiscal","t37e")
P("T37",["119","120"],"conceito_correto","troca_efeito",3,
 "O contratado será obrigado a reparar, corrigir, remover, reconstruir ou substituir, a suas expensas, o objeto do contrato em que se verificarem vícios, defeitos ou incorreções, e será responsável pelos danos causados diretamente à Administração ou a terceiros, não excluindo nem reduzindo essa responsabilidade a fiscalização ou o acompanhamento pelo contratante.",
 "O contratado será responsável pelos danos causados à Administração ou a terceiros em razão da execução do contrato, mas essa responsabilidade será excluída ou reduzida quando houver fiscalização ou acompanhamento pelo contratante.",
 "Arts. 119 e 120.","fiscalização exclui responsabilidade","t37f")
P("T37",["121"],"conceito_correto","excecao_omitida",5,
 "Somente o contratado é responsável pelos encargos trabalhistas, previdenciários, fiscais e comerciais resultantes da execução do contrato; exclusivamente nas contratações de serviços contínuos com regime de dedicação exclusiva de mão de obra, a Administração responderá solidariamente pelos encargos previdenciários e subsidiariamente pelos trabalhistas se comprovada falha na fiscalização.",
 "A Administração responde solidariamente pelos encargos trabalhistas e previdenciários resultantes da execução de qualquer contrato, independentemente de falha na fiscalização.",
 "Art. 121, caput e § 2º.","generaliza responsabilidade","t37g")
P("T37",["121"],"conceito_correto","troca_efeito",5,
 "Nos serviços contínuos com dedicação exclusiva de mão de obra, a Administração poderá, mediante disposição em edital ou contrato, exigir caução, fiança bancária ou seguro-garantia para verbas rescisórias, condicionar o pagamento à comprovação de quitação das obrigações trabalhistas, depositar valores em conta vinculada e efetuar diretamente o pagamento das verbas trabalhistas em caso de inadimplemento; os valores da conta vinculada são absolutamente impenhoráveis.",
 "Nos serviços contínuos com dedicação exclusiva de mão de obra, é vedado à Administração condicionar o pagamento à comprovação de quitação trabalhista ou efetuar diretamente o pagamento das verbas, e os valores depositados em conta vinculada são penhoráveis.",
 "Art. 121, §§ 3º e 4º.","veda medidas e torna penhoráveis","t37h")
P("T37",["122"],"conceito_correto","excecao_omitida",4,
 "O contratado poderá subcontratar partes da obra, do serviço ou do fornecimento até o limite autorizado pela Administração, apresentando documentação que comprove a capacidade técnica do subcontratado; regulamento ou edital poderão vedar, restringir ou estabelecer condições para a subcontratação, que é vedada quando houver vínculo com dirigente do órgão contratante ou com agente que atue na licitação, na fiscalização ou na gestão do contrato, ou parentesco até o terceiro grau.",
 "O contratado poderá subcontratar livremente qualquer parte do objeto, sem autorização da Administração, e a subcontratação de pessoa com vínculo com agente público que atue na fiscalização do contrato só será vedada se o parentesco for de primeiro grau.",
 "Art. 122, caput e §§ 1º a 3º.","libera subcontratação e restringe vedação","t37i")
P("T37",["123"],"conceito_correto","troca_numero",4,
 "A Administração terá o dever de explicitamente emitir decisão sobre todas as solicitações e reclamações relacionadas à execução dos contratos, ressalvados os requerimentos manifestamente impertinentes, meramente protelatórios ou de nenhum interesse; salvo prazo específico, concluída a instrução, terá o prazo de 1 mês para decidir, admitida a prorrogação motivada por igual período.",
 "A Administração poderá deixar de decidir as solicitações e reclamações relacionadas à execução dos contratos; concluída a instrução, terá o prazo de 3 meses para decidir, vedada a prorrogação.",
 "Art. 123 e parágrafo único.","troca dever e prazo","t37j")
# T38
P("T38",["124"],"conceito_correto","excecao_omitida",3,
 "Os contratos poderão ser alterados, com as devidas justificativas, unilateralmente pela Administração, para modificar o projeto ou as especificações ou quando necessária a modificação do valor contratual em decorrência de acréscimo ou diminuição quantitativa de seu objeto, e por acordo entre as partes, para substituir a garantia, modificar o regime de execução ou a forma de pagamento e restabelecer o equilíbrio econômico-financeiro.",
 "Os contratos poderão ser alterados unilateralmente pela Administração para restabelecer o equilíbrio econômico-financeiro e modificar a forma de pagamento, e por acordo entre as partes para modificar o projeto e acrescer quantitativos do objeto.",
 "Art. 124, I e II.","troca hipóteses unilateral e consensual","t38a")
P("T38",["124"],"conceito_correto","troca_efeito",4,
 "Se decorrentes de falhas de projeto, as alterações de contratos de obras e serviços de engenharia ensejarão apuração de responsabilidade do responsável técnico e adoção das providências para o ressarcimento dos danos causados à Administração; aplica-se o restabelecimento do equilíbrio econômico-financeiro quando a execução for obstada pelo atraso em desapropriação, desocupação, servidão ou licenciamento ambiental por circunstâncias alheias ao contratado.",
 "Se decorrentes de falhas de projeto, as alterações de contratos de obras e serviços de engenharia dispensam apuração de responsabilidade do responsável técnico; o atraso em desapropriação ou licenciamento ambiental por circunstâncias alheias ao contratado não autoriza restabelecimento do equilíbrio econômico-financeiro.",
 "Art. 124, §§ 1º e 2º.","dispensa responsabilização","t38b")
P("T38",["125"],"conceito_correto","troca_numero",4,
 "Nas alterações unilaterais, o contratado será obrigado a aceitar, nas mesmas condições contratuais, acréscimos ou supressões de até 25% do valor inicial atualizado do contrato que se fizerem nas obras, nos serviços ou nas compras e, no caso de reforma de edifício ou de equipamento, o limite para os acréscimos será de 50%.",
 "Nas alterações unilaterais, o contratado será obrigado a aceitar acréscimos ou supressões de até 50% do valor inicial atualizado do contrato nas obras, serviços ou compras e, no caso de reforma de edifício ou de equipamento, o limite para os acréscimos será de 25%.",
 "Art. 125.","inverte percentuais","t38c")
P("T38",["125"],"caso_concreto","caso_concreto",4,
 "Contrato de compra de material de escritório, de valor inicial atualizado de R$ 1.000.000,00, precisa de acréscimo quantitativo unilateral de R$ 200.000,00 determinado pela Administração. O contratado é obrigado a aceitar o acréscimo, nas mesmas condições contratuais, pois ele se mantém dentro do limite de 25%.",
 "Contrato de reforma de edifício, de valor inicial atualizado de R$ 1.000.000,00, precisa de acréscimo quantitativo unilateral de R$ 400.000,00 determinado pela Administração. O contratado é obrigado a aceitar o acréscimo, pois o limite para reforma é de 25%, e o acréscimo é permitido nas mesmas condições contratuais.",
 "Art. 125.","aplica 25% à reforma (é 50%)","t38d")
