class Cabina:
    def __init__(self, codCabina, letti, ponte, prezzoBase):
        self.codCabina = codCabina
        self.letti = letti
        self.ponte = ponte
        self.prezzoBase = prezzoBase

    def __str__(self):
        return f'Cabina: {self.codCabina}, {self.letti} posti letto, ponte {self.ponte}. Prezzo = {self.prezzoBase}'


#classe figlia CabinaAnimali
class CabinaAnimali(Cabina):
    def __init__(self, codCabina, letti, ponte, prezzoBase, numAnimali):
        super().__init__(codCabina, letti, ponte, prezzoBase)
        self.numAnimali = numAnimali

    def __str__(self):
        return f'Cabina Animali: {self.codCabina}, {self.letti} posti letto, ponte {self.ponte}. Prezzo = {self.prezzoBase}, max {self.numAnimali} animali.'

    def maggiorazione_prezzo(self):
        #prezzofinale = prezzo base × (1 + 0.10 × max_animali)
        self.prezzoBase += self.prezzoBase * (1 + 0.10 * self.numAnimali)
        return self.prezzoBase


# classe figlia CabinaDeluxe
class CabinaDeluxe(Cabina):
    def __init__(self, codCabina, letti, ponte, prezzoBase, stile):
        super().__init__(codCabina, letti, ponte, prezzoBase)
        self.stile = stile

    def __str__(self):
        return f'Cabina Deluxe: {self.codCabina}, {self.letti} posti letto, ponte {self.ponte}. Prezzo = {self.prezzoBase}, stile {self.stile}.'

    def maggiorazione_prezzo(self):
        # prezzo finale = prezzo base × 1.20
        self.prezzoBase += self.prezzoBase * 1.20
        return self.prezzoBase