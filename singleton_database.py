
import sqlite3
from threading import Lock


class Database:
    """
    Classe que implementa o padrão Singleton para gerenciar a conexão com o banco de dados.
    Garante que apenas uma instância de conexão seja criada durante toda execução da aplicação.
    
    PADRÃO SINGLETON: Uso recomendado:
        db = get_database()  # ou Database()
        cursor = db.get_cursor()
        cursor.execute("SELECT * FROM usuarios")
    """
    
    # PADRÃO SINGLETON: Variável privada para armazenar a instância única
    _instance = None
    # PADRÃO SINGLETON: Lock para garantir thread-safety (segurança em múltiplas threads)
    _lock = Lock()
    
    def __new__(cls):
        """
        PADRÃO SINGLETON: Sobrescreve o método __new__ para controlar a criação de instâncias.
        Garante que apenas uma instância seja criada, mesmo com múltiplas chamadas.
        
        O padrão 'Double-Checked Locking' garante thread-safety:
        1. Primeira verificação (rápida): Se já existe instância, retorna
        2. Lock adquirido: Se múltiplas threads tentam criar, apenas uma consegue
        3. Segunda verificação (dentro do lock): Confirma que ainda precisa criar
        4. Instância criada e retornada
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    # PADRÃO SINGLETON: Cria a única instância
                    cls._instance = super(Database, cls).__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        """
        PADRÃO SINGLETON: Inicializa a conexão apenas uma vez.
        Mesmo sendo chamado múltiplas vezes, a inicialização só ocorre na primeira vez.
        """
        # PADRÃO SINGLETON: Verifica se já foi inicializado para evitar reinicializar a conexão
        if self._initialized:
            return
        
        self._initialized = True
        self.connection = None
        self.connect()
    
    def connect(self):
        """
        PADRÃO SINGLETON: Estabelece a conexão com o banco de dados SQLite.
        Esta conexão é única e compartilhada por toda a aplicação.
        """
        try:
            # PADRÃO SINGLETON: check_same_thread=False permite usar em múltiplas threads
            self.connection = sqlite3.connect("escola.db", check_same_thread=False)
            print("✅ Conexão com banco de dados estabelecida (Singleton)")
        except sqlite3.Error as e:
            print(f"❌ Erro ao conectar ao banco de dados: {e}")
            self.connection = None
    
    def get_connection(self):
        """
        PADRÃO SINGLETON: Retorna a instância única da conexão com o banco de dados.
        
        Exemplo:
            conn = db.get_connection()
        """
        return self.connection
    
    def get_cursor(self):
        """
        PADRÃO SINGLETON: Retorna um cursor para execução de comandos SQL.
        Este cursor usa a conexão Singleton única.
        
        Exemplo:
            cursor = db.get_cursor()
            cursor.execute("SELECT * FROM usuarios")
        """
        if self.connection:
            return self.connection.cursor()
        return None
    
    def close(self):
        """
        PADRÃO SINGLETON: Fecha a conexão com o banco de dados.
        Isso encerra a instância única e libera recursos.
        """
        if self.connection:
            self.connection.close()
            print("❌ Conexão com banco de dados fechada")


# PADRÃO SINGLETON: Função auxiliar para obter a instância única do Database
def get_database():
    """
    PADRÃO SINGLETON: Função que retorna a instância única da classe Database.
    Use esta função em vez de instanciar Database() diretamente.
    
    RECOMENDADO: Use esta função como ponto de entrada padrão para obter a conexão.
    
    Exemplo de uso:
        from singleton_database import get_database
        
        db = get_database()
        cursor = db.get_cursor()
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
    
    Vantagens de usar get_database():
    ✅ Clareza no código (deixa explícito que você quer o Singleton)
    ✅ Fácil manutenção (se quiser mudar a implementação depois)
    ✅ Encapsulamento melhor
    """
    return Database()
