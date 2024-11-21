# Lorenzo Zardo Danzmann e Vinícius Panato Osório

from processo import Processo

class Writing_Process(Processo):
    _write_target = ''
    _expressao = ''

    def __init__(self, id, exp):
        super().__init__(id, "Gravação")
        self._write_target = 'computation.txt'
        self._expressao = exp

    # Executa a gravação do arquivo
    def execute(self):
        with open(self._write_target, 'a') as arquivo:
            arquivo.write(self._expressao + '\n')
        print(f"Expressão gravada no arquivo {self._write_target}: {self._expressao}\n")