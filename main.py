import random

# Probabilidades de cada raridade
raridades = {
    'amarelo': 0.0025575,
    'vermelho': 0.0063939,
    'rosa': 0.0319693,
    'roxo': 0.1598465,
    'azul': 0.7992327
}

while True:
    # Pergunta se o usuário quer abrir uma caixa
    resposta = input('Deseja abrir uma caixa? (sim/não) ')
    if resposta.lower() != 'sim':
        break

    # Escolhe um número aleatório entre 0 e 1 para determinar a raridade do item
    numero_aleatorio = random.random()

    # Determina a raridade do item baseado no número aleatório gerado
    raridade = None
    acumulado = 0
    for k, v in raridades.items():
        acumulado += v
        if numero_aleatorio <= acumulado:
            raridade = k
            break

    # Determina o item baseado na raridade
    if raridade == 'amarelo':
        item = 'Luvas excessivamente raras'
    elif raridade == 'vermelho':
        item = random.choice(['AWP | Duality', 'P90 | Neorrainha', 'UMP-45 | Desgarrada'])
    elif raridade == 'rosa':
        item = random.choice(['M4A4 | Temukau', 'AK-47 | Tiro na Cabeça'])
    elif raridade == 'roxo':
        item = random.choice([ 'M4A1-S | Enforossauro-S',
                              'Glock-18 | Coelho Umbrático', 'MAC-10 | Sakkaku', 'Revólver R8 | Bananólver'])
    elif raridade == 'azul':
        item = random.choice(["MAG-7 | Insônia",
"MP9 | Peso-Pena","SCAR-20 | Fragmentos","P250 | Re.feita","MP5-SD | Liquefação","SG 553 | Ciberforça","Tec-9 | Rebelde"])

    # Imprime o item dropado
    print(f'Você ganhou um(a) {item} ({raridade.title()})!')

print('Obrigado por jogar!')
