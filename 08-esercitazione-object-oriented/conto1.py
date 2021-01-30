class Conto:

    conto = 0

    def __init__(self, nome, conto = None):
        self.nome = nome
        if not conto:
            Conto.conto += 1
            conto = Conto.conto

        self.conto = f'{conto:02d}'


class ContoCorrente(Conto):
    # conto = 0

    def __init__(self, nome, saldo=0, conto=None):

        super().__init__(nome, conto)
        # self.nome = nome
        # ContoCorrente.conto += 1
        # self.conto = f'{ContoCorrente.conto:02d}'
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


class GestoreContiCorrenti:
    @staticmethod
    def bonifico(
                    sorgente:       ContoCorrente,  # test
                    destinazione:   ContoCorrente,
                    importo
                ):
        sorgente.preleva(importo)
        destinazione.deposita(importo)


c1 = ContoCorrente("rob", 1000)
c1.descrizione()

c2 = ContoCorrente("fab", 1500)
c2.descrizione()

GestoreContiCorrenti.bonifico(c1, c2, 1000)
c1.descrizione()
c2.descrizione()
