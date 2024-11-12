from processo import Processo

class Computing_Process(Processo):

    _num1 = 0
    _num2 = 0
    _operacao = ''

    def __init__(self, id, n1, n2, oper):
        super().__init__(id)
        self._num1 = int(n1) if isinstance(int(n1), int) else float(n1)
        self._num2 = int(n2) if isinstance(int(n2), int) else float(n2)
        self._operacao = oper

    @property
    def n1(self):
        return self._num1
    
    @n1.setter
    def n1(self, n1):
        self._num1 = n1
    
    @property
    def n2(self):
        return self._num2
    
    @n2.setter
    def n2(self, n2):
        self._num2 = n2

    @property
    def oper(self):
        return self._operacao
    
    @oper.setter
    def oper(self, oper):
        self._operacao = oper

    def execute(self):

        match(int(self._operacao)):
            case 1:
                return self._num1 + self._num2
            case 2:
                return self._num1 - self._num2
            case 3:
                return self._num1 * self._num2
            case 4:
                return self._num1 / self._num2
    
    


