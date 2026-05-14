# PADRÃO SINGLETON: Esta classe é usada em conjunto com o padrão Singleton
# O Singleton garante que apenas uma conexão com o banco de dados exista
# Portanto, os cursores obtidos aqui utilizam essa conexão única

class Usuario:
    def __init__(self, id, nome, email, tipo):
        self.id = id
        self.nome = nome
        self.email = email
        self.tipo = tipo

    def eh_aluno(self):
        return self.tipo == "aluno"

    def eh_professor(self):
        return self.tipo == "professor"
    
    # PADRÃO SINGLETON: Contrato abstrato - subclasses implementam com a conexão Singleton
    def get_dashboard_url(self):
        raise NotImplementedError("A subclasse deve implementar este método")