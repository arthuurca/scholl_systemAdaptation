# PADRÃO BEHAVIORAL: MEMENTO
# Implementação para capturar e restaurar estados das notas do aluno
# Permite desfazer (undo) e refazer (redo) mudanças nas notas

from copy import deepcopy
from datetime import datetime


class NotaMemento:
    """
    Memento: Captura um estado específico das notas em um ponto no tempo.
    Armazena uma cópia imutável do estado interno.
    """
    
    def __init__(self, dados_notas, timestamp=None):
        # Cria uma cópia profunda para evitar mudanças acidentais
        self.__dados = deepcopy(dados_notas)
        self.__timestamp = timestamp or datetime.now()
    
    def obter_dados(self):
        """Retorna os dados capturados (protegidos por cópia)"""
        return deepcopy(self.__dados)
    
    def obter_timestamp(self):
        """Retorna quando este estado foi capturado"""
        return self.__timestamp


class NotaCaretaker:
    """
    Caretaker: Gerencia o histórico de estados (mementos).
    Implementa undo/redo mantendo duas pilhas de estados.
    """
    
    def __init__(self):
        self.__historico_desfazer = []
        self.__historico_refazer = []
    
    def guardar_estado(self, memento):
        """Salva um novo estado. Limpa histórico de redo quando novo estado é criado."""
        self.__historico_desfazer.append(memento)
        self.__historico_refazer.clear()
    
    def pode_desfazer(self):
        """Verifica se há estados anteriores para restaurar"""
        return len(self.__historico_desfazer) > 1
    
    def pode_refazer(self):
        """Verifica se há estados futuros para restaurar"""
        return len(self.__historico_refazer) > 0
    
    def desfazer(self):
        """
        Desfaz a última ação (undo).
        Retorna o estado anterior ou None se não houver histórico.
        """
        if not self.pode_desfazer():
            return None
        
        # Move estado atual para redo
        estado_atual = self.__historico_desfazer.pop()
        self.__historico_refazer.append(estado_atual)
        
        # Retorna o estado anterior
        return self.__historico_desfazer[-1]
    
    def refazer(self):
        """
        Refaz a última ação desfeita (redo).
        Retorna o estado futuro ou None se não houver histórico.
        """
        if not self.pode_refazer():
            return None
        
        # Move estado de redo para desfazer
        estado_futuro = self.__historico_refazer.pop()
        self.__historico_desfazer.append(estado_futuro)
        
        # Retorna o estado restaurado
        return self.__historico_desfazer[-1]
    
    def obter_estado_atual(self):
        """Retorna o estado atual sem modificar o histórico"""
        if not self.__historico_desfazer:
            return None
        return self.__historico_desfazer[-1]
    
    def limpar_historico(self):
        """Limpa todo o histórico (útil para resetar)"""
        self.__historico_desfazer.clear()
        self.__historico_refazer.clear()
    
    def obter_tamanho_historico(self):
        """Retorna quantos estados estão no histórico"""
        return len(self.__historico_desfazer)
