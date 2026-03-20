import random

def ordenar_pessoas(pessoas, role):
    """
    Ordena pessoas baseado na estratégia:
    - NC → prioriza quem tem menos NC
    - CM/CV → prioriza menor carga
    """

    if role == 'NC':
        return sorted(
            pessoas,
            key=lambda p: (
                p.role_counts['NC'],
                p.score,
                random.random()
            )
        )
    else:
        return sorted(
            pessoas,
            key=lambda p: (
                p.score,
                p.role_counts[role],
                random.random()
            )
        )