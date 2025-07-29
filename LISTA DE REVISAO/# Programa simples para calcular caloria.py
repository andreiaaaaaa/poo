# Programa simples para calcular calorias, sugerir treinos e dieta

def calcular_calorias(peso, altura, idade, sexo, objetivo):
    # Fórmula de Harris-Benedict
    if sexo.lower() == 'masculino':
        tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
    else:
        tmb = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)
    if objetivo == 'perda':
        return tmb - 500  # déficit calórico
    elif objetivo == 'ganho':
        return tmb + 500  # superávit calórico
    else:
        return tmb

def sugerir_treino(objetivo):
    if objetivo == 'perda':
        return [
            "HIIT 20 minutos",
            "Circuito: agachamento, flexão, burpee, abdominal (3x15 cada)",
            "Pular corda 15 minutos"
        ]
    elif objetivo == 'ganho':
        return [
            "Treino de força: agachamento, flexão, tríceps, abdominal (4x12 cada)",
            "Treino com mochila ou garrafas para resistência",
            "Isometria: prancha 3x30s"
        ]
    else:
        return ["Caminhada leve 30 minutos", "Alongamento"]

def sugerir_dieta(objetivo):
    if objetivo == 'perda':
        return [
            "Café da manhã: ovos mexidos com aveia",
            "Almoço: frango grelhado, arroz integral, salada",
            "Lanche: iogurte natural com frutas",
            "Jantar: peixe assado, legumes cozidos"
        ]
    elif objetivo == 'ganho':
        return [
            "Café da manhã: ovos, pão integral, banana",
            "Almoço: carne vermelha magra, batata doce, salada",
            "Lanche: shake de proteína, castanhas",
            "Jantar: frango, arroz, brócolis"
        ]
    else:
        return ["Alimentação equilibrada com frutas, legumes, proteínas e carboidratos integrais"]

# Exemplo de uso
peso = float(input("Informe seu peso (kg): "))
altura = float(input("Informe sua altura (cm): "))
idade = int(input("Informe sua idade: "))
sexo = input("Informe seu sexo (masculino/feminino): ")
objetivo = input("Objetivo (perda/ganho/manutenção): ").lower()

calorias = calcular_calorias(peso, altura, idade, sexo, objetivo)
treino = sugerir_treino(objetivo)
dieta = sugerir_dieta(objetivo)

print(f"\nCalorias diárias recomendadas: {calorias:.0f} kcal")
print("\nSugestão de treino intenso em casa:")
for t in treino:
    print("-", t)
print("\nSugestão de dieta:")
for d in dieta:
    print("-", d)