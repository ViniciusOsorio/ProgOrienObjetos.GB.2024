from processo import Processo
from computingProcess import Computing_Process

class Reading_Process(Processo):
    _read_target = ''

    def __init__(self, id):
        super().__init__(id, "Leitura")
        self._read_target = 'computation.txt'

    def execute(self):
        content = []
        read = open(self._read_target, 'r')
        linha = read.readline()
        while(linha != ''):
            linha_sep = linha.split(" ")
            content.append()
            linha = read.readline()