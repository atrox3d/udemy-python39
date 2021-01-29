class ContoCorrente:
    conto = 0

    def __init__(self, nome, saldo=0):
        self.nome = nome
        ContoCorrente.conto +=1
        self.conto = f'{ContoCorrente.conto:02d}'
        self.saldo = saldo

    def preleva(self, importo):
        self.saldo -= importo

    def deposita(self, importo):
        self.saldo += importo

    def descrizione(self):
        print(self.nome, self.conto, self.saldo)


c1 = ContoCorrente("rob", 1000)
c1.descrizione()

c2 = ContoCorrente("fab", 1500)
c2.descrizione()

c1.preleva(1000)
c2.deposita(1000)

c1.descrizione()
c2.descrizione()
