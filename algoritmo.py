def triagem_buble_s(fila):
    #ordena fila por prioridade( 1 mais urgente que 3 )
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j]['prioridade'] == fila[j+1]['prioridade']:
                # Se a prioridades forem iguas , ordena por idade(mais velho)
                if fila[j]['idade'] < fila[j+1]['idade']:
                    #
                    fila[j],fila[j+1] = fila[j+1],fila[j]
            elif fila[j]['prioridade'] > fila[j+1]['prioridade']:
                fila[j], fila[j+1] = fila[j+1],fila[j]
    return fila
def busca_paciente(fila, nome):
    for paciente in fila:
        if paciente ['nome'].lower().strip() == nome.lower().strip():
            return paciente
    return None