class ContoCorrente:
    conto = 0

    def __init__(self, nome, saldo=0):
        self.nome = nome
        ContoCorrente.conto +=1
        self.conto = f'{ContoCorrente.conto:02d}'
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, importo):
        self.preleva(self.__saldo)
        self.deposita(importo)

    def preleva(self, importo):
        self.__saldo -= importo

    def deposita(self, importo):
        self.__saldo += importo

    def descrizione(self):
        print(self.nome, self.conto, self.saldo)


c1 = ContoCorrente("rob", 1000)
c1.descrizione()

c2 = ContoCorrente("fab", 1500)
c2.descrizione()

c1.saldo = 10000
c1.descrizione()
