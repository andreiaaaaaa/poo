def calcular_calorias(peso, altura, idade, sexo, nivel_atividade):
    # Fórmula de Harris-Benedict (BMR)
    if sexo.lower() == 'masculino':
        bmr = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
    else:
        bmr = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)

    # Fatores de atividade física
    fatores = {
        'sedentario': 1.2,
        'levemente_ativo': 1.375,
        'moderadamente_ativo': 1.55,
        'muito_ativo': 1.725,
        'extremamente_ativo': 1.9
    }

    calorias = bmr * fatores.get(nivel_atividade, 1.2)
    return calorias

# Exemplo de uso:
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (cm): "))
idade = int(input("Digite sua idade: "))
sexo = input("Digite seu sexo (masculino/feminino): ")
nivel_atividade = input("Nível de atividade (sedentario, levemente_ativo, moderadamente_ativo, muito_ativo, extremamente_ativo): ")

calorias = calcular_calorias(peso, altura, idade, sexo, nivel_atividade)
print(f"Você deve consumir aproximadamente {calorias:.0f} calorias por dia.")