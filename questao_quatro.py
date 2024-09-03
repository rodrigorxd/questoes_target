# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

faturamento_sp = 67836.43
faturamento_rj = 36678.66
faturamento_mg = 29229.88
faturamento_es = 27165.48
faturamento_outros = 19849.53

faturamento_total = faturamento_sp + faturamento_rj + faturamento_mg + faturamento_es + faturamento_outros

porcentagem_sp = (faturamento_sp * 100) / faturamento_total

porcentagem_rj = (faturamento_rj * 100) / faturamento_total

porcentagem_mg = (faturamento_mg * 100) / faturamento_total

porcentagem_es = (faturamento_es * 100) / faturamento_total

porcentagem_outros = (faturamento_outros * 100) / faturamento_total


print(f"-----DISTRIBUIÇÃO DO FATURAMENTO-----\nSP: {porcentagem_sp:.1f}%\nRJ: {porcentagem_rj:.1f}%\nES: {porcentagem_es:.1f}%\nMG: {porcentagem_mg:.1f}%\nOutros: {porcentagem_outros:.1f}%")