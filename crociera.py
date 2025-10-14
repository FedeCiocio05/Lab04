import csv
from passeggeri import Passeggero
from cabine import Cabina, CabinaAnimali, CabinaDeluxe


class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.lista_passeggeri = []
        self.lista_cabine = []
        # TODO

    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as infile:
                reader = csv.reader(infile, delimiter=',')
                for row in reader:  # per ogni riga nel file
                    try:
                        if row[0].startswith('P'):
                            codPasseggero = row[0]
                            nome = row[1]
                            cognome = row[2]
                            #oggetto passeggero
                            passeggero = Passeggero(codPasseggero,nome,cognome)
                            #aggiungo in lista
                            self.lista_passeggeri.append(passeggero)
                        elif row[0].startswith('C'):
                            codCabina = row[0]
                            letti = int(row[1])
                            ponte = int(row[2])
                            prezzoBase = float(row[3])
                            if row[4] is int:
                                numAnimali = row[4]
                                cab_animali = CabinaAnimali(codCabina, letti, ponte, prezzoBase, numAnimali)
                                self.lista_cabine.append(cab_animali)
                            else:
                                stile = row[4]
                                cab_deluxe = CabinaDeluxe(codCabina, letti, ponte, prezzoBase, stile)
                                self.lista_cabine.append(cab_deluxe)
                    except IndexError:
                        # errore se la riga ha meno colonne del previsto
                        print(f"Attenzione errore sugli indici,riga incompleta")  # gestione errore sugli indici
                    except ValueError:
                        # errore se i valori non sono convertibili nel formato corretto
                        print(f"Attenzione: riga contiene valori non validi")  # gestione errore sui valori
        except FileNotFoundError:
            # nel caso il file non esiste
            print(f"Errore: il file {file_path} non esiste.")
        except Exception:
            # altro errore non previsto
            print(f"Errore imprevisto")
        # restituisce comunque la lista aggiornata (anche se vuota)
        return self.lista_passeggeri, self.lista_cabine
        # TODO

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO

    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

