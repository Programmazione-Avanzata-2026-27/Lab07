from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass
    @staticmethod
    def get_biblioteche():
        cnx = DBConnect.get_connection()
        if cnx is None:
            return []
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT id, nome, indirizzo FROM biblioteca ORDER BY nome"
        cursor.execute(query)
        risultato = []
        for row in cursor:
            risultato.append(Biblioteca(row["id"], row["nome"], row["indirizzo"]))
        cursor.close()
        cnx.close()
        return risultato
