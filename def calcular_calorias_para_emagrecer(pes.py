# Programa simples para calcular calorias diárias para emagrecer
# e sugerir alimentos saudáveis

def calcular_calorias(peso, altura, idade, sexo, nivel_atividade):
    # Fórmula de Harris-Benedict (BMR)
    if sexo.lower() == 'masculino':
        bmr = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
    else:
        bmr = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)
    
    # Fatores de atividade física
    fatores = {
        'sedentario': 1.2,
        'leve': 1.375,
        'moderado': 1.55,
        'ativo': 1.725,
        'muito ativo': 1.9
    }
    tmb = bmr * fatores.get(nivel_atividade, 1.2)
    # Para emagrecer, recomenda-se consumir ~500 kcal a menos por dia
    calorias_para_emagrecer = tmb - 500
    return round(calorias_para_emagrecer)

def sugestao_alimentos():
    return [
        "Peito de frango grelhado",
        "Peixes (salmão, tilápia)",
        "Ovos cozidos",
        "Arroz integral",
        "Batata doce",
        "Aveia",
        "Legumes variados (brócolis, cenoura, abobrinha)",
        "Frutas (maçã, banana, morango)",
        "Oleaginosas (castanha, nozes, amêndoas)",
        "Iogurte natural"
    ]

# Exemplo de uso
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (cm): "))
idade = int(input("Digite sua idade: "))
sexo = input("Digite seu sexo (masculino/feminino): ")
nivel_atividade = input("Nível de atividade (sedentario, leve, moderado, ativo, muito ativo): ")

calorias = calcular_calorias(peso, altura, idade, sexo, nivel_atividade)
print(f"\nVocê deve consumir aproximadamente {calorias} calorias por dia para emagrecer.")

print("\nSugestão de alimentos saudáveis para incluir na dieta:")
for alimento in sugestao_alimentos():
    print(f"- {alimento}")