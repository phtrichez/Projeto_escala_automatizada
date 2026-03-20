import pandas as pd
from src.models import Pessoa
from src.config import PESOS, ROLES
from src.utils import ordenar_pessoas
from src.restrictions import pode_trabalhar


class Scheduler:

    def __init__(self, escala_path, qtd_path):
        self.escala_df = pd.read_csv(escala_path)
        self.qtd_df = pd.read_csv(qtd_path)

        # Ajuste tipo
        for col in self.escala_df.columns[1:]:
            self.escala_df[col] = self.escala_df[col].astype(object)

        self.pessoas = {
            nome: Pessoa(nome)
            for nome in self.escala_df['NOME COMPLETO']
        }

        self.days = [
            col for col in self.escala_df.columns
            if col != 'NOME COMPLETO'
        ]

        self.ordem_original = list(self.pessoas.keys())

    def get_restricao(self, nome, day):
        return self.escala_df.loc[
            self.escala_df['NOME COMPLETO'] == nome, day
        ].values[0]

    def ja_escalado(self, nome, day):
        valor = self.get_restricao(nome, day)
        return valor in ['NC', 'CM', 'CV']


    def set_trabalho(self, nome, day, role):
        self.escala_df.loc[
            self.escala_df['NOME COMPLETO'] == nome, day
        ] = role

        pessoa = self.pessoas[nome]
        pessoa.add_trabalho(role, PESOS[role])

    def distribuir_dia(self, day, row_qtd):

        for role in ROLES:

            needed = int(row_qtd[role])
            assigned = 0

            pessoas_ordenadas = ordenar_pessoas(
                list(self.pessoas.values()),
                role
            )

            # =====================
            # PASSAGEM NORMAL
            # =====================
            for pessoa in pessoas_ordenadas:

                if assigned >= needed:
                    break

                nome = pessoa.nome
                restricao = self.get_restricao(nome, day)

                if (
                    not self.ja_escalado(nome, day)
                    and pode_trabalhar(restricao, role)
                ):
                    self.set_trabalho(nome, day, role)
                    assigned += 1

            # =====================
            # FALLBACK (ignora restrição e usa ordem original)
            # =====================
            if assigned < needed:

                for nome in reversed(self.ordem_original):

                    if assigned >= needed:
                        break

                    if not self.ja_escalado(nome, day):
                        self.set_trabalho(nome, day, role)
                        assigned += 1

    def run(self):

        for i, day in enumerate(self.days):

            if i >= len(self.qtd_df):
                break

            row_qtd = self.qtd_df.iloc[i]

            self.distribuir_dia(day, row_qtd)

        return self.escala_df

    def save(self, path):
        self.escala_df.to_csv(path, index=False)