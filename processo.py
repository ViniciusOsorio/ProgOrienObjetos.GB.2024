class Processo:

    _pid = 0

    def __init__(self, id):
        self._pid = id

    @property
    def id(self):
        return self._pid
    
    @id.setter
    def id(self, id):
        self._pid = id