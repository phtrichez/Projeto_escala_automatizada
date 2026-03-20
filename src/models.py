class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.score = 0
        self.role_counts = {'NC': 0, 'CM': 0, 'CV': 0}

    def add_trabalho(self, role, peso):
        self.score += peso
        self.role_counts[role] += 1