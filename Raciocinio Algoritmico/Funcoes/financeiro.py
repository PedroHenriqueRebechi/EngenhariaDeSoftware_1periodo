def juros_simples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo

def juros_compostos(capital, taxa, tempo):
    return capital * ((1 + taxa / 100) ** tempo - 1)
