def frecuencia_relativa(clases_sorted, fa_sorted):
    frecu_total = sum(fa_sorted)
    frelativa = [fa / frecu_total * 100 for fa in fa_sorted]
    return frelativa  

