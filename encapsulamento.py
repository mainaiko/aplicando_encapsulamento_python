class conta:
    def __init__(self, saldo=0):
        self._saldo = saldo

    def depositar(self,valor):
        self._saldo+= valor
        pass

    def sacar(self, valor):
        self._saldo -= valor
        pass

    def mostrar_saldo(self):
        return self._saldo

conta = conta(100)
conta.depositar(100)
print (conta.mostrar_saldo())
