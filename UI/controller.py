import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None


# POPOLA DROPDOWN
    def popola_dropdown(self):
        self._view.dd_biblioteca.options.clear()
        self._view.dd_genere.options.clear()

        self._view.dd_biblioteca.options.append(ft.dropdown.Option(key="", text="Nessun filtro"))
        for b in self._model.get_biblioteche():
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(key=str(b.id), text=b.nome))

        self._view.dd_genere.options.append(ft.dropdown.Option(key="", text="Nessun filtro"))
        for g in self._model.get_generi():
            self._view.dd_genere.options.append(ft.dropdown.Option(key=g, text=g))

        self._view.dd_biblioteca.value = ""
        self._view.dd_genere.value = ""
        self._view.update()
# CALLBACKS DROPDOWN
    def handle_biblioteca_selezionata(self, e):
        valore = self._view.dd_biblioteca.value
        if valore is None or valore == "":
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = int(valore)

    def handle_genere_selezionato(self, e):
        valore = self._view.dd_genere.value
        if valore is None or valore == "":
            self.genere_selezionato = None
        else:
            self.genere_selezionato = valore
# AZIONE: MOSTRA LIBRI
    def handle_mostra_libri(self, e):
        libri = self._model.get_libri_filtrati(
            self.biblioteca_selezionata,
            self.genere_selezionato,
        )
        self._view.lv_libri.controls.clear()

        if not libri:
            self._view.show_alert("Nessun libro trovato con i filtri selezionati.")
            self._view.update()
            return

        for libro in libri:
            self._view.lv_libri.controls.append(
                ft.Text(f"{libro.titolo} - {libro.autore} ({libro.genere}, {libro.anno_pubblicazione})")
            )
        self._view.update()
    



