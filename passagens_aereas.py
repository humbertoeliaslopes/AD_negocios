# Código para Resolução do Exercício em Sala de Aula sobre Preço das Passagens Aéreas

# Importa as bibliotecas necessárias para resolver o exercício

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Cria as variáveis com os dados fornecidos no exercício

passagem_atlanta = pd.Series(
	[
		340.1,
		321.6,
		291.6,
		339.6,
		359.6,
		384.6,
		309.6,
		415.6,
		293.6,
		249.6,
		539.6,
		455.6,
		359.6,
		333.9,
	],
	index=[
		"Cincinatti",
		"Nova York",
		"Chicago",
		"Denver",
		"Los Angeles",
		"Seatlle",
		"Detroit",
		"Filadélfia",
		"Washington, Dc",
		"Miami",
		"São Francisco",
		"Las Vegas",
		"Phoenix",
		"Dallas",
	],
	name="Preço Passagem Atlanta",
)
print(passagem_atlanta) # Exibe os dados da variável passagem_atlanta

passagem_salt = pd.Series(
    [
        570.1,
        354.6,
        465.6,
        219.6,
        311.6,
        297.6,
        471.6,
        618.4,
        513.6,
        523.2,
        381.6,
        159.6,
        267.6,
        458.6
    ],
    index=[
        "Cincinatti",
        "Nova York",
        "Chicago",
        "Denver",
        "Los Angeles",
        "Seatlle",
        "Detroit",
        "Filadélfia",
        "Washington, Dc",
        "Miami",
        "São Francisco",
        "Las Vegas",
        "Phoenix",
        "Dallas",
    ],
    name="Preço Passagem Salt Lake City",
)
print(passagem_salt) # Exibe os dados da variável passagem_salt

# Une as duas variáveis em um DataFrame para facilitar a análise e visualização dos dados

dados_passagens = pd.DataFrame({
    "Preço Passagem Atlanta": passagem_atlanta,
    "Preço Passagem Salt Lake City": passagem_salt
})

print(dados_passagens)

# Calcula as medidas de tendência central para cada cidade e exibe os resultados em uma tabela

# Medidas para Atlanta

media_atlanta = passagem_atlanta.mean()
mediana_atlanta = passagem_atlanta.median()
modas_atlanta = passagem_atlanta.mode().tolist()

# Exibição das medidas de tendência central para Atlanta

print("=" * 55)
print("MEDIDAS DE TENDÊNCIA CENTRAL - ATLANTA")
print("=" * 55)
print(f"Tamanho da amostra (n) : {len(passagem_atlanta)}")
print(f"Média Aritmética       : {media_atlanta:.2f} dólares")
print(f"Mediana                : {mediana_atlanta:.2f} dólares")
print(f"Moda(s)                : {modas_atlanta} dólares")

# Medidas para Salt Lake City

media_salt = passagem_salt.mean()
mediana_salt = passagem_salt.median()
modas_salt = passagem_salt.mode().tolist()

# Exibição das medidas de tendência central para Salt Lake City

print("=" * 55)
print("MEDIDAS DE TENDÊNCIA CENTRAL - SALT LAKE CITY")
print("=" * 55)
print(f"Tamanho da amostra (n) : {len(passagem_salt)}")
print(f"Média Aritmética       : {media_salt:.2f} dólares")
print(f"Mediana                : {mediana_salt:.2f} dólares")
print(f"Moda(s)                : {modas_salt} dólares")

# Calculando as medidas de dispersão e variabilidade para cada cidade

# Medidas para Atlanta

desvio_padrao_atlanta = passagem_atlanta.std()
variancia_atlanta = passagem_atlanta.var()
coeficiente_variacao_atlanta = (desvio_padrao_atlanta / media_atlanta) * 100

#  Exibição das medidas de dispersão e variabilidade para Atlanta

print("=" * 60)
print("MEDIDAS DE DISPERSÃO E VARIABILIDADE - ATLANTA")
print("=" * 60)
print(f"Desvio Padrão (s)  : {desvio_padrao_atlanta:.2f} dólares")
print(f"Variância (s²)     : {variancia_atlanta:.2f} dólares²")
print(f"Coeficiente de Variação (CV): {coeficiente_variacao_atlanta:.2f}%")

# Medidas para Salt Lake City

desvio_padrao_salt = passagem_salt.std()
variancia_salt = passagem_salt.var()
coeficiente_variacao_salt = (desvio_padrao_salt / media_salt) * 100 

# Exibição das medidas de dispersão e variabilidade para Salt Lake City

print("=" * 60)
print("MEDIDAS DE DISPERSÃO E VARIABILIDADE - SALT LAKE CITY")
print("=" * 60)
print(f"Desvio Padrão (s)  : {desvio_padrao_salt:.2f} dólares")
print(f"Variância (s²)     : {variancia_salt:.2f} dólares²")
print(f"Coeficiente de Variação (CV): {coeficiente_variacao_salt:.2f}%")

# Cálculo das Separatrizes

# Cálculo dos Quartis para Atlanta

quartis = dados_passagens['Preço Passagem Atlanta'].quantile([0.25, 0.50, 0.75])

# Exibição dos Quartis para Atlanta

print("=" * 60)
print("QUARTIS - ATLANTA")
print("=" * 60)
print(f"1º Quartil (Q1) : {quartis[0.25]:.2f} dólares")
print(f"2º Quartil (Q2) : {quartis[0.50]:.2f} dólares")
print(f"3º Quartil (Q3) : {quartis[0.75]:.2f} dólares") 

# Cálculo dos Quartis para Salt Lake City

quartis = dados_passagens['Preço Passagem Salt Lake City'].quantile([0.25, 0.50, 0.75])

# Exibição dos Quartis para Salt Lake City

print("=" * 60)
print("QUARTIS - SALT LAKE CITY")
print("=" * 60)
print(f"1º Quartil (Q1) : {quartis[0.25]:.2f} dólares")
print(f"2º Quartil (Q2) : {quartis[0.50]:.2f} dólares")
print(f"3º Quartil (Q3) : {quartis[0.75]:.2f} dólares") 

# Cria um boxplot para identificação de outliers

# =============================================================================
# CONSTRUÇÃO DOS BOXPLOTS COMPARATIVOS
# =============================================================================

# Configuração da figura para exibição gráfica
plt.figure(figsize=(9, 6))

# Propriedades visuais para destacar os outliers de forma didática
marcador_outlier = dict(
    marker="o", markerfacecolor="firebrick", markersize=8, linestyle="none"
)
linha_mediana = dict(color="darkblue", linewidth=1.8)

# Geração dos boxplots pareados
dados_passagens.boxplot(
    column=["Preço Passagem Atlanta", "Preço Passagem Salt Lake City"],
    flierprops=marcador_outlier,
    medianprops=linha_mediana,
    patch_artist=False,
    grid=True,
)

# Ajustes de formatação gráfica e titulação
plt.title(
    "Comparação da Distribuição de Tarifas Aéreas: Atlanta vs. Salt Lake City",
    fontsize=12,
    fontweight="bold",
    pad=15,
)
plt.ylabel("Preço da Passagem (US$)", fontsize=11)
plt.xticks(
    [1, 2], ["Destino: Atlanta", "Destino: Salt Lake City"], fontsize=10
)
plt.tight_layout()
plt.show()

# =============================================================================
# IDENTIFICAÇÃO ANALÍTICA DE OUTLIERS (REGRA DO INTERVALO INTERQUARTIL - IQR)
# =============================================================================

print("\n" + "=" * 65)
print("IDENTIFICAÇÃO DE OUTLIERS PELO CRITÉRIO 1,5 x IQR (ANDERSON ET AL.)")
print("=" * 65)

for coluna in dados_passagens.columns:
    q1 = dados_passagens[coluna].quantile(0.25)
    q3 = dados_passagens[coluna].quantile(0.75)
    iqr = q3 - q1

    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    # Filtragem das cidades consideradas outliers
    outliers = dados_passagens[
        (dados_passagens[coluna] < limite_inferior)
        | (dados_passagens[coluna] > limite_superior)
    ][coluna]

    cidade = "Atlanta" if "Atlanta" in coluna else "Salt Lake City"

    print(f"\nDestino: {cidade}")
    print(f"Amplitude Interquartil (IQR) : {iqr:.2f} dólares")
    print(f"Limite Inferior             : {limite_inferior:.2f} dólares")
    print(f"Limite Superior             : {limite_superior:.2f} dólares")

    if not outliers.empty:
        print("Outliers identificados:")
        for origem, valor in outliers.items():
            print(f"  * Origem: {origem} | Tarifa: US$ {valor:.2f}")
    else:
        print("Nenhum outlier identificado nesta variável.")