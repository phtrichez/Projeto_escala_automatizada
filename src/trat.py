import pandas as pd
from pathlib import Path


class Tratamento:
    def __init__(self, df):
        if type(df) == pd.DataFrame:
            if df is None or df.empty:
                raise ValueError("DataFrame vazio ou inválido")

            self.df = df.copy()

        else:
            base = Path(__file__).resolve().parent
            arquivo = base.parent / df

            self.df = pd.read_excel(arquivo)

        # valida coluna
        if 'TOTAL 12 HORAS' not in self.df.columns:
            raise ValueError("Coluna 'TOTAL 12 HORAS' não encontrada")

        # corta até a coluna (inclusive)
        col_final = self.df.columns.get_loc('TOTAL 12 HORAS')
        self.df = self.df.iloc[:, :col_final + 1]

    def df_nomes(self, lista_nomes=None):
        if lista_nomes is None:
            lista_nomes = [
                "CAETANO DA ROSA VIEGAS",
                "MATHEUS VIDAL DE SOUZA",
                "BRUNO AUGUSTO AMATO BORGES",
                "PEDRO GUIDI PEREIRA",
                "ELIAS PIRES JUNIOR",
                "LEANDRO DE OLIVEIRA ACCORDI",
                "MAYA KURJAN CUNHA",
                "CAROLINA COUCEIRO",
                "LUAN GOMES CARVALHO",
                "RAFAEL PEDRO BITENCOURT",
                "PEDRO MAGNAGO BARCELOS",
                "DANTE CORD DA COSTA",
                "BRUNO BAUMEL FERREIRA",
                "PEDRO HENRIQUE TRICHEZ",
                "ALYSSON GARCIA"
            ]

        # encontra linha NC
        mask_nc = self.df['NOME COMPLETO'] == 'NC'
        idx_nc = mask_nc.idxmax() if mask_nc.any() else len(self.df)

        df_antes_nc = self.df.iloc[:idx_nc].copy()
        df_antes_nc = df_antes_nc.fillna(0)

        # filtro opcional por nomes
        if lista_nomes:
            df_antes_nc = df_antes_nc[df_antes_nc['NOME COMPLETO'].isin(lista_nomes)]

        df_antes_nc.to_csv('io_nomes.csv', index=False)

        return df_antes_nc

    def df_qtd_dia(self):
        # encontra Planejamento
        mask_plan = self.df['NOME COMPLETO'].astype(str).str.startswith('Planejamento')
        idx_plan = mask_plan.idxmax() if mask_plan.any() else len(self.df)

        df_planejamento = self.df.iloc[idx_plan + 1:].copy()
        df_planejamento = df_planejamento.fillna(0)

        df_planejamento = self.dividir_cruz(df_planejamento)

        # transformação
        df_planejamento = df_planejamento.transpose().reset_index(drop=True)

        # usa primeira linha como header
        df_planejamento.columns = df_planejamento.iloc[0]
        df_planejamento = df_planejamento[1:].reset_index(drop=True)

        df_planejamento.to_csv('io_planejamento.csv', index=False)

        return df_planejamento

    def dividir_cruz(self, df):
        df = df.copy()

        mask_cruz = df['NOME COMPLETO'] == 'Cruz'

        if not mask_cruz.any():
            print("⚠️ Linha 'Cruz' não encontrada")
            return df

        linha_cruz = df.loc[mask_cruz].copy()

        valores = linha_cruz.drop(columns=['NOME COMPLETO'])

        # garante numérico
        valores = valores.apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

        cm = valores // 2
        cv = valores - cm

        df_cm = cm.copy()
        df_cm.insert(0, 'NOME COMPLETO', 'CM')

        df_cv = cv.copy()
        df_cv.insert(0, 'NOME COMPLETO', 'CV')

        # remove Cruz
        df = df.loc[~mask_cruz]

        # adiciona novas linhas
        df_final = pd.concat([df, df_cm, df_cv], ignore_index=True)

        return df_final


if __name__ == "__main__":
    t = Tratamento()
    df1 = t.df_nomes()
    df2 = t.df_qtd_dia()