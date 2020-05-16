def regra_simples(x,y,z):      # regra de três simples
    return (y/x)*z

def regra_composta(a,x,y,z):   # regra de três composta
    return (a*z)*(y/(a*x))

q1 = """
    Suponha que 4 funcionários públicos sejam capazes de atender, 
    em média, a 54 pessoas por hora. Espera-se que 6 funcionários públicos, 
    com a mesma capacidade operacional dos primeiros, sejam capazes de atender, por hora,
    a quantas pessoas?
"""

q2 = """
    Em um mesmo plano, a sombra de uma árvore, 
    projetada pelo sol, sobre um chão plano, mede 16m, 
    enquanto a sobra de um hidrante de 0,8m de altura mede 0,4m. 
    Qual a altura da árvore?
"""
q3 = """
    O processamento de 300 toneladas de lixo é realizado em 28 horas por 5 máquinas.
    Se uma das máquinas quebrar, 
    quantas horas as demais levarão para fazer o mesmo processamento?

"""
print('\n')
print(f'QUESTÃO 1: {q1} \nRESPOSTA: {regra_simples(4,54,6)}\n')
print(f'QUESTÃO 2: {q2} \nRESPOSTA: {regra_simples(0.4,0.8,16)}\n')
print(f'QUESTÃO 3: {q3} \nRESPOSTA: {regra_composta(300,4,28,5)}\n')
