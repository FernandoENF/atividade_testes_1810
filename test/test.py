import unittest
from model.Banco import Banco
from model.Conta import Conta


class MyTestCase(unittest.TestCase):

    def test_criar_conta(self):
        banco = Banco('FEBank', '171')
        conta = Conta('2890', 'Fernando', 0, 500)
        self.assertEqual(banco.adicionar_conta(conta), True)

    def test_criar_varias_contas(self):
        banco = Banco('FEBank', '171')
        contas = [Conta('2890', 'Fernando', 0, 500), Conta('7000', 'Fernando', 0, 500), Conta('8000', 'Fernando', 0,
                                                                                              500)]
        for conta in contas:
            banco.adicionar_conta(conta)
        self.assertEqual(banco.listar_contas(), contas)

    def test_criar_com_numero_que_existe(self):
        banco = Banco('FEBank', '171')
        conta = Conta('9000', 'José', 0, 500)
        banco.adicionar_conta(conta)
        conta2 = Conta('9000', 'Fernando', 0, 500)
        self.assertEqual(banco.adicionar_conta(conta2), False)

    def test_verificar_extrato_apos_criar(self):
        banco = Banco('FEBank', '171')
        conta = Conta('9100', 'José', 0, 500)
        banco.adicionar_conta(conta)
        extrato = "Saldo de 0 do titular José"
        self.assertEqual(conta.extrato(), extrato)

    def test_verificar_extrato_apos_depositar(self):
        banco = Banco('FEBank', '171')
        conta = Conta('9200', 'José', 0, 500)
        banco.adicionar_conta('conta')
        conta.deposita(789)
        extrato = "Saldo de 789 do titular José"
        self.assertEqual(conta.extrato(), extrato)

    def test_realizar_saque_satisfazendo_limite(self):
        banco = Banco('FEBank', '171')
        conta = Conta('9300', 'José', 0, 1000)
        valor = 897
        banco.adicionar_conta(conta)
        conta.saca(valor)
        self.assertEqual(conta.saldo, -897)

    def test_saque_valor_acima_do_limite(self):
        banco = Banco('FEBank', '171')
        conta = Conta('9400', 'José', 0, 1200)
        valor = 1500
        banco.adicionar_conta(conta)
        self.assertEqual(conta.saca(valor), "O valor {} passou o limite".format(valor))

    def test_extrato_apos_saque(self):
        banco = Banco('FEBank', '171')
        valor = 1200
        conta = Conta('9500', 'José', valor, 1500)
        banco.adicionar_conta(conta)
        conta.saca(valor)
        resultado_esperado = "Saldo de {} do titular {}".format(0, 'José')
        self.assertEqual(conta.extrato(), resultado_esperado)

    def test_transferir_com_saldo(self):
        banco = Banco('FEBank', '171')
        valor = 1200
        conta = Conta('9600', 'José', valor, 0)
        conta2 = Conta('9700', 'Fernando', 0, 0)
        banco.adicionar_conta(conta)
        banco.adicionar_conta(conta2)
        conta.transfere(valor, conta2)
        resultado_esperado = False
        if conta.saldo == 0:
            if conta2.saldo == valor:
                resultado_esperado = True
        self.assertEqual(resultado_esperado, True)

    def test_verificar_extrato_apos_transferencia(self):
        banco = Banco('FEBank', '171')
        valor = 1200
        conta = Conta('9600', 'José', valor, 0)
        conta2 = Conta('9700', 'Fernando', 0, 0)
        banco.adicionar_conta(conta)
        banco.adicionar_conta(conta2)
        conta.transfere(valor, conta2)
        resultado_esperado = False
        extrato = "Saldo de {} do titular {}"
        if conta.extrato() == extrato.format(0, 'José'):
            if conta2.extrato() == extrato.format(valor, 'Fernando'):
                resultado_esperado = True
        self.assertEqual(resultado_esperado, True)

    def test_transferir_valor_acima_do_limite(self):
        banco = Banco('FEBank', '171')
        valor = 1200
        conta = Conta('9600', 'José', 0, 1100)
        conta2 = Conta('9700', 'Fernando', 0, 0)
        banco.adicionar_conta(conta)
        banco.adicionar_conta(conta2)
        resultado_esperado = "O valor {} passou o limite".format(valor)
        self.assertEqual(conta.transfere(valor, conta2), resultado_esperado)

    def test_verificar_extrato_apos_transferencia_cancelada(self):
        banco = Banco('FEBank', '171')
        valor = 1200
        conta = Conta('9600', 'José', 50, 1100)
        conta2 = Conta('9700', 'Fernando', 0, 0)
        banco.adicionar_conta(conta)
        banco.adicionar_conta(conta2)
        conta.transfere(valor, conta2)
        resultado_esperado = "Saldo de {} do titular {}".format(50, 'José')
        self.assertEqual(conta.extrato(), resultado_esperado)


if __name__ == '__main__':
    unittest.main()
