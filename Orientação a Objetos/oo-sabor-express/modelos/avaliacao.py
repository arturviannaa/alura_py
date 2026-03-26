class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente

        if nota > 5:
            self._nota = 5
        elif nota < 0:
            self._nota = 0
        else:
            self._nota = nota