class Treino:
    def __init__(self, id, data_treino, distancia, tempo):
        self._id = id
        self._data_treino = data_treino
        self._distancia = distancia  
        self._tempo = tempo 

    def get_id(self):
        return self._id

    def get_data_treino(self):
        return self._data_treino

    def get_distancia(self):
        return self._distancia

    def get_tempo(self):
        return self._tempo

    # Setters
    def set_id(self, id):
        self._id = id

    def set_data_treino(self, data_treino):
        self._data_treino = data_treino

    def set_distancia(self, distancia):
        self._distancia = distancia

    def set_tempo(self, tempo):
        self._tempo = tempo

    def velocidade_media(self):
        if self._tempo > 0:
            return self._distancia / (self._tempo / 60)  # km/h
        return 0

    def __str__(self):
        return (f"ID: {self._id}, Data: {self._data_treino}, "
                f"Distância: {self._distancia} km, Tempo: {self._tempo} min, "
                f"Velocidade Média: {self.velocidade_media():.2f} km/h")


class TreinoUI:
    def __init__(self):
        self.treinos = []

    def menu(self):
        print("\n--- Menu Treinos de Corrida ---")
        print("1. Inserir novo treino")
        print("2. Listar todos os treinos")
        print("3. Listar treino por ID")
        print("4. Atualizar treino")
        print("5. Excluir treino")
        print("6. Treino mais rápido")
        print("7. Sair")

    def inserir(self):
        try:
            id = int(input("ID do treino: "))
            data = input("Data do treino (DD-MM-YYYY): ")
            distancia = float(input("Distância percorrida (km): "))
            tempo = float(input("Tempo da corrida (min): "))
            treino = Treino(id, data, distancia, tempo)
            self.treinos.append(treino)
            print("Treino inserido com sucesso!")
        except Exception as e:
            print("Erro ao inserir treino:", e)

    def listar(self):
        if not self.treinos:
            print("Nenhum treino cadastrado.")
        for treino in self.treinos:
            print(treino)

    def listar_id(self):
        id = int(input("Informe o ID do treino: "))
        for treino in self.treinos:
            if treino.get_id() == id:
                print(treino)
                return
        print("Treino não encontrado.")

    def atualizar(self):
        id = int(input("Informe o ID do treino a atualizar: "))
        for treino in self.treinos:
            if treino.get_id() == id:
                data = input("Nova data do treino (YYYY-MM-DD): ")
                distancia = float(input("Nova distância percorrida (km): "))
                tempo = float(input("Novo tempo da corrida (min): "))
                treino.set_data_treino(data)
                treino.set_distancia(distancia)
                treino.set_tempo(tempo)
                print("Treino atualizado com sucesso!")
                return
        print("Treino não encontrado.")

    def excluir(self):
        id = int(input("Informe o ID do treino a excluir: "))
        for i, treino in enumerate(self.treinos):
            if treino.get_id() == id:
                del self.treinos[i]
                print("Treino excluído com sucesso!")
                return
        print("Treino não encontrado.")

    def mais_rapido(self):
        if not self.treinos:
            print("Nenhum treino cadastrado.")
            return
        treino_mais_rapido = max(self.treinos, key=lambda t: t.velocidade_media())
        print("Treino mais rápido:")
        print(treino_mais_rapido)

    def main(self):
        while True:
            self.menu()
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.inserir()
            elif opcao == "2":
                self.listar()
            elif opcao == "3":
                self.listar_id()
            elif opcao == "4":
                self.atualizar()
            elif opcao == "5":
                self.excluir()
            elif opcao == "6":
                self.mais_rapido()
            elif opcao == "7":
                print("Saindo...")
                break
            else:
                print("Opção inválida.")


if __name__ == "__main__":
    ui = TreinoUI()
    ui.main()