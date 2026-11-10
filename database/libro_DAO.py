from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    @staticmethod
    def get_generi():
        cnx = DBConnect.get_connection()
        if cnx is None:
            return []
        cursor = cnx.cursor()
        query = "SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL ORDER BY genere"
        cursor.execute(query)
        risultato = [row[0] for row in cursor]
        cursor.close()
        cnx.close()
        return risultato

    @staticmethod
    def get_libri_filtrati(id_biblioteca, genere):
        cnx = DBConnect.get_connection()
        if cnx is None:
            return []
        cursor = cnx.cursor(dictionary=True)
        query = """
            SELECT id, titolo, autore, genere, anno_pubblicazione, id_biblioteca
            FROM libro
            WHERE id_biblioteca = COALESCE(%s, id_biblioteca)
              AND genere = COALESCE(%s, genere)
            ORDER BY titolo
        """
        cursor.execute(query, (id_biblioteca, genere))
        risultato = []
        for row in cursor:
            risultato.append(Libro(
                row["id"],
                row["titolo"],
                row["autore"],
                row["genere"],
                row["anno_pubblicazione"],
                row["id_biblioteca"],
            ))
        cursor.close()
        cnx.close()
        return risultato
