# PADRÃO SINGLETON: A classe Nota trabalha com dados imutáveis
# Quando usada com cursores, esses cursores vêm da conexão Singleton do banco de dados

class Nota:
    CAMPOS_VALIDOS = {"ab1_1", "ab1_2", "ab2_1", "ab2_2"}

    def __init__(self):
        # PADRÃO SINGLETON: Encapsulamento - dados privados protegidos
        self.__dados = {
            "ab1_1": None,
            "ab1_2": None,
            "ab2_1": None,
            "ab2_2": None
        }

    # PADRÃO SINGLETON: Encapsulamento seguro com validação
    def atualizar(self, campo, valor):
        # valida campo
        if campo not in self.CAMPOS_VALIDOS:
            raise ValueError("Campo inválido")

        # valida valor
        if valor is not None and (valor < 0 or valor > 10):
            raise ValueError("Nota deve estar entre 0 e 10")

        self.__dados[campo] = valor

    # PADRÃO SINGLETON: Getter encapsulado
    def get_valor(self, campo):
        return self.__dados.get(campo)