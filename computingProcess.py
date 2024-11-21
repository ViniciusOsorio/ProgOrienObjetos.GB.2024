from processo import Processo

class Computing_Process(Processo):

    _num1 = 0
    _num2 = 0
    _operacao = ''

    def __init__(self, id, n1, n2, oper):
        super().__init__(id, "Cálculo")
        self._num1 = float(n1) if '.' in n1 else int(n1)
        self._num2 = float(n2) if '.' in n1 else int(n2)
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

    # Retorna a expressão completa
    def return_exp(self):
        res = self.execute()
        return f'{self._num1} {self._operacao} {self._num2} = {res}'

    # Executa a operação 
    def execute(self):
        match self._operacao:
            case '+':
                return self._num1 + self._num2
            case '-':
                return self._num1 - self._num2
            case '*':
                return self._num1 * self._num2
            case '/':
                return self._num1 / self._num2