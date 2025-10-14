class Passeggero:
    def __init__(self, codPasseggero, nome, cognome):
        self.codPasseggero = codPasseggero
        self.nome = nome
        self.cognome = cognome

    def __str__(self):
        return f'Passeggero: {self.codPasseggero}, {self.nome} {self.cognome}'
