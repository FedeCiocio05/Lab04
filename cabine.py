class Cabina:
    def __init__(self, codCabina, letti, ponte, prezzoBase):
        self.codCabina = codCabina
        self.letti = letti
        self.ponte = ponte
        self.prezzoBase = prezzoBase

    def prezzo(self):
        """Prezzo effettivo (cabina base: nessuna maggiorazione)."""
        return float(self.prezzoBase)

    def __str__(self):
        return f'Cabina Base {self.codCabina}: {self.letti} posti letto, ponte {self.ponte}. Prezzo = {self.prezzoBase}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.codCabina == other.codCabina

    def __lt__(self, other):
        return self.prezzo() < other.prezzo()

#classe figlia CabinaAnimali
class CabinaAnimali(Cabina):
    def __init__(self, codCabina, letti, ponte, prezzoBase, numAnimali):
        super().__init__(codCabina, letti, ponte, prezzoBase)
        self.numAnimali = numAnimali

    def prezzo(self):
        # prezzofinale = prezzo base × (1 + 0.10 × max_animali)
        return float(self.prezzoBase) * (1 + 0.10 * int(self.numAnimali))

    def __str__(self):
        return f'Cabina Animali {self.codCabina}: {self.letti} posti letto, ponte {self.ponte}. Prezzo = {self.prezzoBase}, max {self.numAnimali} animali.'

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.prezzo() < other.prezzo()

# classe figlia CabinaDeluxe
class CabinaDeluxe(Cabina):
    def __init__(self, codCabina, letti, ponte, prezzoBase, stile):
        super().__init__(codCabina, letti, ponte, prezzoBase)
        self.stile = stile

    def prezzo(self):
        # prezzo finale = prezzo base × 1.20
        return float(self.prezzoBase) * 1.20

    def __str__(self):
        return f'Cabina Deluxe {self.codCabina}: {self.letti} posti letto, ponte {self.ponte}. Prezzo = {self.prezzoBase}, stile {self.stile}.'

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.prezzo() < other.prezzo()