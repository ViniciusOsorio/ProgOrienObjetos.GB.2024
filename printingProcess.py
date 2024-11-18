from processo import Processo

class Printing_Process(Processo):
    print_target = ''

    def __init__(self, id):
        super().__init__(id)