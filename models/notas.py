# PADRÃO SINGLETON: A classe Nota trabalha com dados imutáveis
# Quando usada com cursores, esses cursores vêm da conexão Singleton do banco de dados
# PADRÃO MEMENTO: Integração com Memento para histórico de mudanças

from models.memento_nota import NotaMemento, NotaCaretaker

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
        
        # PADRÃO MEMENTO: Inicializa o gerenciador de histórico
        self.__caretaker = NotaCaretaker()
        # Salva o estado inicial
        self.__caretaker.guardar_estado(NotaMemento(self.__dados))

    # PADRÃO SINGLETON: Encapsulamento seguro com validação
    # PADRÃO MEMENTO: Captura estado antes de modificar
    def atualizar(self, campo, valor):
        # valida campo
        if campo not in self.CAMPOS_VALIDOS:
            raise ValueError("Campo inválido")

        # valida valor
        if valor is not None and (valor < 0 or valor > 10):
            raise ValueError("Nota deve estar entre 0 e 10")

        self.__dados[campo] = valor
        
        # PADRÃO MEMENTO: Salva o novo estado no histórico
        self.__caretaker.guardar_estado(NotaMemento(self.__dados))

    # PADRÃO SINGLETON: Getter encapsulado
    def get_valor(self, campo):
        return self.__dados.get(campo)
    
    # PADRÃO MEMENTO: Desfaz a última mudança
    def desfazer(self):
        memento = self.__caretaker.desfazer()
        if memento:
            self.__dados = memento.obter_dados()
            return True
        return False
    
    # PADRÃO MEMENTO: Refaz a última mudança desfeita
    def refazer(self):
        memento = self.__caretaker.refazer()
        if memento:
            self.__dados = memento.obter_dados()
            return True
        return False
    
    # PADRÃO MEMENTO: Verifica se pode desfazer
    def pode_desfazer(self):
        return self.__caretaker.pode_desfazer()
    
    # PADRÃO MEMENTO: Verifica se pode refazer
    def pode_refazer(self):
        return self.__caretaker.pode_refazer()
    
    # PADRÃO MEMENTO: Retorna tamanho do histórico
    def obter_tamanho_historico(self):
        return self.__caretaker.obter_tamanho_historico()