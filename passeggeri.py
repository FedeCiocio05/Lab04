class Passeggero:
    def __init__(self, codPasseggero, nome, cognome):
        self.codPasseggero = codPasseggero
        self.nome = nome
        self.cognome = cognome

    def __str__(self):
        return f'Passeggero {self.codPasseggero}: {self.nome} {self.cognome}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.codPasseggero == other.codPasseggero
