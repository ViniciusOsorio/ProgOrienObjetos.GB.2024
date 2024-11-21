# Lorenzo Zardo Danzmann e Vinícius Panato Osório

from abc import ABC, abstractmethod

class Processo:

    _pid = 0
    _tipo = ""

    def __init__(self, id, tipo):
        self._pid = id
        self._tipo = tipo

    @property
    def id(self):
        return self._pid
    
    @id.setter
    def id(self, id):
        self._pid = id

    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @abstractmethod
    def execute(self):
        pass