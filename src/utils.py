import random


def total_trabalhos(p):
    return sum(p.role_counts.values())


def diferenca_nc(p):
    return p.role_counts['NC'] - (p.role_counts['CM'] + p.role_counts['CV'])


def diferenca_cm_cv(p):
    return (p.role_counts['CM'] + p.role_counts['CV']) - p.role_counts['NC']


def ordenar_pessoas(pessoas, role):
    """
    Estratégia de priorização:

    1️⃣ Quem trabalhou menos (quantidade total)
    2️⃣ Equilíbrio entre funções
    3️⃣ Aleatoriedade (desempate) pode ser mudado para a nota
    """

    if role == 'NC':
        return sorted(
            pessoas,
            key=lambda p: (
                total_trabalhos(p),   # prioridade principal
                diferenca_nc(p),      # equilíbrio NC vs CM/CV
                random.random()       # desempate
            )
        )
    else:
        return sorted(
            pessoas,
            key=lambda p: (
                total_trabalhos(p),   # prioridade principal
                diferenca_cm_cv(p),   # equilíbrio inverso
                random.random()
            )
        )