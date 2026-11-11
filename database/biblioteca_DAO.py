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
    def get_biblioteche() -> list[Biblioteca] | None:
        """
        Restituisce tutte le biblioteche nel database.
        :return: lista di oggetti Biblioteca oppure None
        """
        cnx = DBConnect.get_connection()
        result = []

        if cnx is None:
            print("❌ Errore di connessione al database (get_biblioteche).")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT * FROM  biblioteca """

        try:
            cursor.execute(query)
            for row in cursor:
                biblioteca = Biblioteca(
                    id=row["id"],
                    nome=row["nome"],
                    indirizzo=row["indirizzo"]
                )
                result.append(biblioteca)
        except Exception as e:
            print(f"Errore durante la query get_biblioteche: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()

        return result
