import csv
from passeggeri import Passeggero
from cabine import Cabina, CabinaAnimali, CabinaDeluxe


class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self._nome = nome
        self.lista_passeggeri = []
        self.lista_cabine = []
        # Stato interno per gestire assegnazioni e disponibilità
        self.disponibilita_cabine = {}  # {codCabina: True/False}
        self.prenotazioni = {}  # {codPasseggero: codCabina}
        self.cabina_assegnata = {}  # {codCabina: codPasseggero}
        # TODO

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nuovo_nome):
        self._nome = nuovo_nome
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as infile:
                reader = csv.reader(infile, delimiter=',')
                for row in reader:  # per ogni riga nel file
                    # Salta righe vuote o con prima cella vuota
                    if not row or not row[0].strip():
                        continue
                    try:
                        tag = row[0].strip()
                        if tag.startswith('P'):
                            codPasseggero = tag
                            nome = row[1].strip()
                            cognome = row[2].strip()
                            # oggetto passeggero
                            passeggero = Passeggero(codPasseggero, nome, cognome)
                            # aggiungo in lista
                            self.lista_passeggeri.append(passeggero)

                        elif tag.startswith('C'):
                            codCabina = tag
                            letti = int(row[1])
                            ponte = int(row[2])
                            prezzoBase = float(row[3])
                            # 5° campo opzionale: se convertibile a int -> Animali, altrimenti -> Deluxe
                            if len(row) > 4 and row[4].strip() != "":
                                extra = row[4].strip()
                                try:
                                    numAnimali = int(extra)
                                    cab = CabinaAnimali(codCabina, letti, ponte, prezzoBase, numAnimali)
                                except ValueError:
                                    stile = extra
                                    cab = CabinaDeluxe(codCabina, letti, ponte, prezzoBase, stile)
                            else:
                                cab = Cabina(codCabina, letti, ponte, prezzoBase)

                            self.lista_cabine.append(cab)
                            # Imposto la cabina come disponibile: serve per il controllo nel metodo di assegnazione.
                            self.disponibilita_cabine[codCabina] = True #cabina prenotabile
                    except IndexError:
                        # riga con meno colonne del previsto
                        print(f"Attenzione: riga incompleta -> {row}")
                    except ValueError as e:
                        # valori non convertibili (es. letti/ponte/prezzo non numerici)
                        print(f"Attenzione: valori non validi in riga {row} ({e})")
        except FileNotFoundError:
            # faccio gestire l'errore al main/menù
            raise
        except Exception as e:
            # altro errore non previsto (mostro quale)
            print(f"Errore imprevisto: {e}")
        # check sulle liste caricate
        print(f'CABINE:{self.lista_cabine},\nPASSEGGERI:{self.lista_passeggeri}')
        # restituisco comunque la lista aggiornata (anche se vuota)
        return self.lista_passeggeri, self.lista_cabine
        # TODO

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # Validazioni essenziali:
        # 1) cabina/passeggero esistono
        # 2) passeggero non ha già una cabina
        # 3) cabina è disponibile

        # trovo cabina
        cab = next((c for c in self.lista_cabine if c.codCabina == codice_cabina), None)
        if cab is None:
            raise ValueError("Cabina inesistente.")

        # trovo passeggero
        pas = next((p for p in self.lista_passeggeri if p.codPasseggero == codice_passeggero), None)
        if pas is None:
            raise ValueError("Passeggero inesistente.")

        # passeggero già assegnato?
        if codice_passeggero in self.prenotazioni:
            raise ValueError("Passeggero già assegnato a una cabina.")

        # cabina disponibile?
        if not self.disponibilita_cabine.get(codice_cabina, True):
            raise ValueError("Cabina non disponibile.")

        # Aggiorno tutte le strutture coerentemente:
        # - prenotazioni       (passeggero -> cabina)
        # - cabina_assegnata   (cabina -> passeggero)
        # - disponibilita_cabine (da True a False)
        self.prenotazioni[codice_passeggero] = codice_cabina
        self.cabina_assegnata[codice_cabina] = codice_passeggero
        self.disponibilita_cabine[codice_cabina] = False
        # TODO

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO
        #sorted SENZA metodo __lt__()
        #return sorted(self.lista_cabine, key=lambda cab: cab.prezzo)
        # sorted CON metodo __lt__()
        return sorted(self.lista_cabine)

    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        for p in self.lista_passeggeri:
            cod_cab = self.prenotazioni.get(p.codPasseggero)
            if cod_cab:
                print(f"{p} – Cabina assegnata: {cod_cab}")
            else:
                print(f"{p} – Nessuna cabina assegnata")
        # TODO

