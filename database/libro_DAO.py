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
    def get_libri_filtrati(biblioteca: str, genere: str) -> list[Libro] | None:
        """
        Restituisce tutti i libri appartenenti a una data biblioteca e/o di un dato genere (filtri opzionali).
        :return: lista di oggetti Libro oppure None
        """
        cnx = DBConnect.get_connection()
        result = []

        if cnx is None:
            print("❌ Errore di connessione al database (get_libri_filtrati).")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """
                    SELECT l.*
                    FROM libro l, biblioteca b
                    WHERE b.nome = COALESCE(%s,b.nome) and l.genere = COALESCE(%s,l.genere) and l.id_biblioteca = b.id
                    """
        try:
            cursor.execute(query, (biblioteca, genere,))
            for row in cursor:
                libro = Libro(
                    id=row["id"],
                    titolo=row["titolo"],
                    autore=row["autore"],
                    genere=row["genere"],
                    anno_pubblicazione=row["anno_pubblicazione"],
                    id_biblioteca=row["id_biblioteca"],
                )
                result.append(libro)
        except Exception as e:
            print(f"Errore durante la query get_libri_filtrati: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()

        return result

    @staticmethod
    def get_generi() -> list[str] | None:
        """
        Restituisce tutti i generi presenti nel database.
        :return: lista di generi (stringhe) oppure None
        """
        cnx = DBConnect.get_connection()
        result = []

        if cnx is None:
            print("❌ Errore di connessione al database (get_generi).")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """
                    SELECT DISTINCT genere
                    FROM libro
                    """
        try:
            cursor.execute(query)
            for row in cursor:
                result.append(row["genere"])

        except Exception as e:
            print(f"Errore durante la query get_generi: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()

        return result
