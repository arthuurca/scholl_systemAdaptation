# PADRÃO SINGLETON: Classes abstratas para visualizar desempenho
# Os cursores aqui vêm da conexão Singleton do banco de dados (veja app.py:conectar())
# Isso garancia que todas as consultas usem a MESMA conexão única

from abc import ABC, abstractmethod

# PADRÃO SINGLETON: Classe abstrata que reforça o contrato
class VisualizadorDesempenho(ABC):
    def __init__(self, usuario):
        self.usuario = usuario

    # PADRÃO SINGLETON: Método abstrato - garante que subclasses implementem com Singleton
    @abstractmethod
    def consultar_dados(self, cursor):
        """
        Este é um MÉTODO ABSTRATO. 
        Ele não tem código aqui, serve apenas como uma regra:
        'Toda subclasse é OBRIGADA a implementar este método'.
        O cursor aqui vem da conexão Singleton do banco de dados.
        """
        pass

# PADRÃO SINGLETON: Implementação para aluno - usa cursor da conexão Singleton
class DesempenhoAluno(VisualizadorDesempenho):
    def consultar_dados(self, cursor):
        # PADRÃO SINGLETON: Cursor vem da conexão Singleton
        cursor.execute("""
            SELECT m.nome, n.ab1_1, n.ab1_2, n.ab2_1, n.ab2_2
            FROM notas n
            JOIN materias m ON n.materia_id = m.id
            WHERE n.aluno_id = ?
        """, (self.usuario.id,))
        return cursor.fetchall()

# PADRÃO SINGLETON: Implementação para professor - usa cursor da conexão Singleton
class DesempenhoProfessor(VisualizadorDesempenho):
    def consultar_dados(self, cursor):
        # PADRÃO SINGLETON: Cursor vem da conexão Singleton
        cursor.execute("""
            SELECT 
                u.nome as aluno,
                u.ano_letivo,
                m.nome as materia,
                n.ab1_1, n.ab1_2, n.ab2_1, n.ab2_2
            FROM notas n
            JOIN usuarios u ON n.aluno_id = u.id
            JOIN materias m ON n.materia_id = m.id
        """)
        return cursor.fetchall()