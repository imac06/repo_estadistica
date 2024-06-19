def facumulada_frs(frelativa):
    facumulada = []
    acumulada = 0
    for r in frelativa:
        acumulada += r
        facumulada.append(acumulada)
    return facumulada