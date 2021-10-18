class Banco():

	def __init__(self, nome, aagencia):
		self.nome = nome
		self.aagencia = aagencia
		self.contas = []

	def adicionar_conta(self, conta):
		nao_existe = True
		for conta_ativa in self.contas:
			if conta.numero == conta_ativa.numero:
				nao_existe = False
		if nao_existe:
			self.contas.append(conta)
		return nao_existe

	def buscar_conta(self, numero):
		for conta_ativa in self.contas:
			if numero == conta_ativa.numero:
				return conta_ativa
		return None

	def listar_contas(self):
		return self.contas

	@property
	def agencia(self):
		return self.agencia






