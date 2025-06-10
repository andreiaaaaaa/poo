N = int(input())
eventos = []
for _ in range(N):
    linha = input().split()
    eventos.append((linha[0], int(linha[1])))

tempo_atual = 0
mensagens = {} 
respostas = {} 
pendentes = {}

for evento, x in eventos:
    if evento == 'T':
        tempo_atual += x
    elif evento == 'R':
        tempo_atual += 1
        if x not in mensagens:
            mensagens[x] = []
            respostas[x] = 0
            pendentes[x] = 0
        mensagens[x].append(tempo_atual)
        pendentes[x] += 1
    elif evento == 'E':
        tempo_atual += 1
        if x in mensagens and mensagens[x]:
            tempo_recebido = mensagens[x].pop(0)
            respostas[x] += tempo_atual - tempo_recebido
            pendentes[x] -= 1

for amigo in sorted(respostas.keys()):
    if pendentes[amigo] == 0:
        print(f"{amigo} {respostas[amigo]}")
    else:
        print(f"{amigo} -1")