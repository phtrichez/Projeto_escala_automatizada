def pode_trabalhar(valor_restricao, role):
    """
    valor_restricao:
    - 0 → livre
    - R → não pode trabalhar
    - CM_R → só pode CM
    - CV_R → só pode CV
    """

    # Normaliza (caso venha float ou NaN)
    if str(valor_restricao) in ['0', '0.0', 'nan']:
        return True

    valor_restricao = str(valor_restricao)

    if valor_restricao == 'R':
        return False

    if valor_restricao == 'CM_R' and role != 'CM':
        return False

    if valor_restricao == 'CV_R' and role != 'CV':
        return False

    return True