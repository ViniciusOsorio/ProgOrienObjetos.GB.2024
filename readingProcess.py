from processo import Processo
from computingProcess import Computing_Process

class Reading_Process(Processo):
    _read_target = ''

    def __init__(self, id):
        super().__init__(id, "Leitura")
        self._read_target = 'computation.txt'

    def execute(self, ultimo_id):
        content = []
        id = ultimo_id + 1
        read = open(self._read_target, 'r')
        linha = read.readline()
        while(linha != ''):
            linha_sep = linha.split(" ")
            content.append(Computing_Process(id, linha_sep[0], linha_sep[2], linha_sep[1]))
            id += 1
            linha = read.readline()
        return content