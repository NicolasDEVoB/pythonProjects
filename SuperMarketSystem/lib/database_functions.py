from os.path import exists, getsize
from pandas import DataFrame, read_csv, concat

CAMINHO = 'database.csv'

# 🛠️ Garante que o arquivo CSV está pronto
def init_db(cols: list):
    if not exists(CAMINHO) or getsize(CAMINHO) == 0:
        DataFrame(columns=cols).to_csv(CAMINHO, index=False)


# 🔍 Função para aplicar filtro estilo {key: value}
def aplicar_filtro(df, filtro: dict):
    for chave, valor in filtro.items():
        df = df[df[chave] == valor]

    return df


# 🟩 CREATE - adiciona novos registros
def create(registros: list[dict]):
    df_existente = read_csv(CAMINHO)
    novos = DataFrame(registros)
    df_final = concat([df_existente, novos], ignore_index=True)
    df_final.to_csv(CAMINHO, index=False)


# 🟦 READ - retorna dados filtrados (ou todos)
def read(filtro: dict = None):
    df = read_csv(CAMINHO)
    if filtro:
        df = aplicar_filtro(df, filtro)
    return df


# 🟨 UPDATE - atualiza registros conforme filtro
def update(filtro: dict, novos_dados: dict):
    df = read_csv(CAMINHO)
    mask = aplicar_filtro(df.copy(), filtro).index
    for col, val in novos_dados.items():
        df.loc[mask, col] = val
    df.to_csv(CAMINHO, index=False)


# 🟥 DELETE - remove registros conforme filtro
def delete(filtro: dict):
    df = read_csv(CAMINHO)
    df_filtrado = aplicar_filtro(df.copy(), filtro)
    df = df.drop(df_filtrado.index)
    df.to_csv(CAMINHO, index=False)
