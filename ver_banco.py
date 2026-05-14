# PADRÃO SINGLETON: Importação do gerenciador de banco de dados
from singleton_database import get_database

def ver_tabela(nome_tabela):
    # PADRÃO SINGLETON: Obtém a instância única do banco de dados
    db = get_database()
    conn = db.get_connection()
    cursor = conn.cursor()

    print(f"\nTABELA: {nome_tabela.upper()}")
    print("-" * 40)

    try:
        cursor.execute(f"SELECT * FROM {nome_tabela}")
        dados = cursor.fetchall()

        if not dados:
            print("⚠️ Nenhum registro encontrado.")
        else:
            for linha in dados:
                print(linha)

    except Exception as e:
        print("Erro:", e)

    conn.close()


# 🔥 visualizar várias tabelas
ver_tabela("usuarios")
ver_tabela("materias")
ver_tabela("notas")
ver_tabela("professor_materias")
ver_tabela("feedbacks")
ver_tabela("presenca")