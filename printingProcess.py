from processo import Processo

class Printing_Process(Processo):

    def __init__(self, id, process_queue):
        super().__init__(id, "Impressão")
        self._process_queue = process_queue

    def execute(self):
        print("Processos na fila:")
        for process in self._process_queue:
            print(f"PID: {process.id}, Tipo: {process.tipo}")