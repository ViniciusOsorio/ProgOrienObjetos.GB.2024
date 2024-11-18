from processo import Processo
import os.path

class Writing_Process(Processo):
    _write_target = ''
    _expressao = ''

    def __init__(self, id, exp):
        super().__init__(id)
        self._write_target = 'computation.txt'
        self._expressao = exp

    def execute(self):
        if os.path.isfile(self._write_target):
            exe = open(self._write_target, 'a')
        else:
            exe = open(self._write_target, 'w')

        exe.write(self._expressao)

        exe.close()