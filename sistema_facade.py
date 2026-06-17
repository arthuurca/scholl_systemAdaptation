from singleton_database import get_database

class SistemaFacade:

    def autenticar_usuario(self, cpf, senha):

        db = get_database()

        cursor = db.get_cursor()

        cursor.execute("""
        SELECT *
        FROM usuarios
        WHERE cpf=? AND senha=?
        """, (cpf, senha))

        return cursor.fetchone()