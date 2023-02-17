class Privet_Pupsik:
    privet = "Privet"
    _privet = "_Privet"
    __privet = "__Privet"
    def __init__(self):
        self.pupsik = "Pupsik"
        self._pupsik = "_Pupsik"
        self.__pupsik = "__Pupsik"
class Pr(Privet_Pupsik):
    def printer(self):
        print(self.privet+self.pupsik)
        print(self._privet+self._pupsik)
        # print(self.__privet+self.__pupsik)

# я закоментировал этe две строчкe потому-что там модификатор доступа прайват и она будет вызывать ошибки
pr = Pr()
pr.printer()

