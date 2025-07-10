from enum import Enum
from datetime import date

class Pagamento(Enum):
    EM_ABERTO = "Em Aberto"
    PAGO_PARCIAL = "Pago Parcial"
    PAGO = "Pago"

class Boleto:
    def __init__(self, codigo_barras, data_emissao, data_vencimento, valor_total):
        self.__codigo_barras = codigo_barras
        self.__data_emissao = data_emissao
        self.__data_vencimento = data_vencimento
        self.__valor_total = valor_total
        self.__valor_pago = 0.0

    def pagar(self, valor):
        if valor <= 0:
            print("Valor inválido para pagamento.")
            return
        if self.__valor_pago + valor > self.__valor_total:
            print("Valor excede o total do boleto.")
            return
        self.__valor_pago += valor
        print(f"Pagamento de R${valor:.2f} registrado com sucesso.")

    def situacao(self):
        if self.__valor_pago == 0:
            return Pagamento.EM_ABERTO
        elif self.__valor_pago < self.__valor_total:
            return Pagamento.PAGO_PARCIAL
        else:
            return Pagamento.PAGO

    def __str__(self):
        return (
            f"Código de Barras: {self.__codigo_barras}\n"
            f"Data de Emissão: {self.__data_emissao.strftime('%d/%m/%Y')}\n"
            f"Data de Vencimento: {self.__data_vencimento.strftime('%d/%m/%Y')}\n"
            f"Valor Total: R${self.__valor_total:.2f}\n"
            f"Valor Pago: R${self.__valor_pago:.2f}\n"
            f"Situação: {self.situacao().value}"
        )

    def get_codigo_barras(self):
        return self.__codigo_barras

    def get_valor_total(self):
        return self.__valor_total

    def get_valor_pago(self):
        return self.__valor_pago

    def set_valor_total(self, novo_valor):
        self.__valor_total = novo_valor

    def set_codigo_barras(self, novo_codigo):
        self.__codigo_barras = novo_codigo

def main():
    print("=== Cadastro de Boleto ===")
    codigo = input("Código de Barras: ")
    dia_emissao = int(input("Dia da Emissão: "))
    mes_emissao = int(input("Mês da Emissão: "))
    ano_emissao = int(input("Ano da Emissão: "))
    dia_venc = int(input("Dia do Vencimento: "))
    mes_venc = int(input("Mês do Vencimento: "))
    ano_venc = int(input("Ano do Vencimento: "))
    valor = float(input("Valor do Boleto: R$"))

    emissao = date(ano_emissao, mes_emissao, dia_emissao)
    vencimento = date(ano_venc, mes_venc, dia_venc)

    boleto = Boleto(codigo, emissao, vencimento, valor)

    while True:
        print("\n--- Menu ---")
        print("1 - Ver dados do boleto")
        print("2 - Fazer um pagamento")
        print("3 - Ver situação")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n" + str(boleto))
        elif opcao == "2":
            valor_pago = float(input("Valor a pagar: R$"))
            boleto.pagar(valor_pago)
        elif opcao == "3":
            print(f"Situação do boleto: {boleto.situacao().value}")
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
