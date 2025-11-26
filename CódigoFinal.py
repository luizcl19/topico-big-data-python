import pandas as pd

arquivo = r"C:\Users\Evellyn\Downloads\Trabalhobigdata\Tabelas\Tabela1.xlsx"

# Lê o arquivo inteiro
df = pd.read_excel(arquivo, header=None)

# Remove as 9 primeiras linhas (enunciado)
df = df.drop(index=range(0, 9))

# Reinicia o índice
df = df.reset_index(drop=True)

# Remove as colunas C, E, F e H (índices 2, 4, 5, 7)
df = df.drop(df.columns[[1, 2, 4, 5, 7]], axis=1)

# Remove a última linha
df = df.iloc[:-1]

# 🔹 Mostra todas as linhas e colunas sem cortes
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Mostra as 200 primeiras (ou todas, se tiver menos)
print(df)

# Salva o resultado limpo
df.to_excel(r"C:\Users\Evellyn\Downloads\Trabalhobigdata\Tabelas\Tabelanova.xlsx", index=False, header=False)
