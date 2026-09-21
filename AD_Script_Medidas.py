import numpy as np
import pandas as pd

# 1. Entrada dos dados coletados (n = 24)
tempos = pd.Series([
    18, 19, 19, 20, 20, 21, 22, 22, 23, 23, 24, 24,
    25, 25, 26, 27, 28, 28, 30, 31, 33, 35, 41, 44
], name='tempo_minutos')

# 2. Medidas de tendência central
media = tempos.mean()
mediana = tempos.median()
modas = tempos.mode().tolist()

print("=" * 55)
print("ETAPA 1: MEDIDAS DE TENDÊNCIA CENTRAL")
print("=" * 55)
print(f"Tamanho da amostra (n) : {len(tempos)}")
print(f"Média Aritmética       : {media:.2f} minutos")
print(f"Mediana                : {mediana:.2f} minutos")
print(f"Moda(s)                : {modas} minutos")

# ==============================================================================
# ETAPA 2: MEDIDAS DE DISPERSÃO E VARIABILIDADE
# Foco analítico: Variância Amostral, Desvio Padrão Amostral e Coeficiente de Variação
# ==============================================================================

# 1. Variância amostral (utiliza ddof=1 para o divisor n - 1, conforme Anderson et al.)
variancia_amostral = tempos.var(ddof=1)

# 2. Desvio padrão amostral (raiz quadrada da variância amostral)
desvio_padrao_amostral = tempos.std(ddof=1)

# 3. Coeficiente de variação (medida relativa de dispersão)
coeficiente_variacao = (desvio_padrao_amostral / media) * 100

# Exibição do relatório de dispersão
print("=" * 60)
print("RELATÓRIO DE DISPERSÃO E ESTABILIDADE OPERACIONAL")
print("=" * 60)
print(f"Variância Amostral (s²)     : {variancia_amostral:.2f} minutos²")
print(f"Desvio Padrão Amostral (s)  : {desvio_padrao_amostral:.2f} minutos")
print(f"Coeficiente de Variação (CV): {coeficiente_variacao:.2f}%")
print("=" * 60)

# ==============================================================================
# ETAPA 3: DIAGNÓSTICO EXPLORATÓRIO COM BOXPLOT E REGRA DO IQR
# ==============================================================================
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração visual profissional
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

# 1. Determinação dos quartis e da amplitude interquartil
q1 = tempos.quantile(0.25)
q2 = tempos.quantile(0.50)  # Mediana
q3 = tempos.quantile(0.75)
iqr = q3 - q1

# 2. Determinação dos limites formais para detecção de outliers
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

# 3. Identificação de valores atípicos
outliers_identificados = tempos[(tempos < limite_inferior) | (tempos > limite_superior)].tolist()

print("=" * 60)
print("ETAPA 3: PARÂMETROS DO BOXPLOT E IDENTIFICAÇÃO DE ANOMALIAS")
print("=" * 60)
print(f"Primeiro Quartil (Q1 - 25%)   : {q1:.2f} minutos")
print(f"Segundo Quartil (Q2 - Mediana): {q2:.2f} minutos")
print(f"Terceiro Quartil (Q3 - 75%)   : {q3:.2f} minutos")
print(f"Amplitude Interquartil (IQR)  : {iqr:.2f} minutos")
print(f"Limite Superior (LS)          : {limite_superior:.2f} minutos")
print(f"Outliers Detectados (> LS)    : {outliers_identificados}")
print("=" * 60)

# 4. Construção gráfica do Boxplot com marcadores comparativos
plt.figure(figsize=(9, 4))
sns.boxplot(
    x=tempos, 
    color='#A1C9F4', 
    width=0.35,
    flierprops=dict(marker='o', markerfacecolor='#D32F2F', markersize=8, markeredgecolor='black', alpha=0.9)
)

# Linhas de referência para confronto visual
plt.axvline(media, color='#003366', linestyle='--', linewidth=2.0, label=f'Média ({media:.2f} min)')
plt.axvline(mediana, color='#2E7D32', linestyle='-', linewidth=2.2, label=f'Mediana ({mediana:.2f} min)')
plt.axvline(limite_superior, color='#D32F2F', linestyle=':', linewidth=2.0, label=f'Limite Superior ({limite_superior:.2f} min)')

plt.title('Boxplot dos Tempos de Atendimento — Identificação de Gargalos Ocultos', fontsize=12, fontweight='bold')
plt.xlabel('Tempo de Atendimento (minutos)', fontsize=10)
plt.legend(loc='upper right', frameon=True)
plt.tight_layout()
plt.show()

# ==============================================================================
# ETAPA 4: MODELAGEM DE DECISÃO E POLÍTICA DE NÍVEL DE SERVIÇO (SLA)
# ==============================================================================

# 1. Percentual de pacientes insatisfeitos com a promessa pela média
pacientes_atrasados = (tempos > media).sum()
percentual_atraso_media = (pacientes_atrasados / len(tempos)) * 100

# 2. Capacidade produtiva horária baseada na mediana
capacidade_horaria_mediana = 60.0 / mediana

# 3. Definição do SLA seguro baseado no Terceiro Quartil (Q3)
sla_recomendado = np.ceil(q3)  # Arredondamento para o próximo minuto inteiro

# 4. Aderência da amostra ao SLA do Terceiro Quartil
pacientes_no_sla = (tempos <= sla_recomendado).sum()
taxa_sucesso_sla = (pacientes_no_sla / len(tempos)) * 100

print("=" * 65)
print("PAINEL DECISÓRIO DE OPERAÇÕES E NÍVEL DE SERVIÇO")
print("=" * 65)
print(f"Inadimplência com SLA baseado % de Atraso Médio : {percentual_atraso_media:.1f}% dos pacientes")
print(f"Produtividade Mediana Padrão por Atendente     : {capacidade_horaria_mediana:.2f} atendimentos/hora")
print(f"SLA Contratual Recomendado (Teto Q3)   : {sla_recomendado:.0f} minutos")
print(f"Taxa Efetiva de Cumprimento do SLA     : {taxa_sucesso_sla:.1f}% da demanda")
print("=" * 65)