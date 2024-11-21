# Lorenzo Zardo Danzmann e Vinícius Panato Osório

from processo import Processo
from computingProcess import Computing_Process

class Reading_Process(Processo):
    _read_target = ''

    def __init__(self, id, process_queue):
        super().__init__(id, "Leitura")
        self._read_target = 'computation.txt'
        self._process_queue = process_queue

    # Executa a leitura do arquivo
    def execute(self, ultimo_id):
        novos_processos = []

        try:
            with open(self._read_target, 'r') as arquivo:
                linhas = arquivo.readlines()
                for linha in linhas:
                    n1, oper, n2 = linha.strip().split(" ")
                    novos_processos.append(Computing_Process(ultimo_id, n1, n2, oper))
                    ultimo_id += 1
            open(self._read_target, 'w').close()
            print("Arquivo lido e processado com sucesso")
        except FileNotFoundError:
            print("Arquivo computation.txt não encontrado")
        return novos_processos