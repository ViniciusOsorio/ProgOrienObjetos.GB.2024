# Lorenzo Zardo Danzmann e Vinícius Panato Osório

from computingProcess import Computing_Process
from printingProcess import Printing_Process
from writingProcess import Writing_Process
from readingProcess import Reading_Process

if __name__ == "__main__":
    print('\nBem-vindo ao Gerenciador de Processo GB10')

    close_sys = False

    lista_proc = []    

    prox_pid = 1

    while not close_sys:
        opt = input('1) Criar Processo\n2) Executar Próximo Processo' +
                    '\n3) Executar Processo Específico\n4) Salvar Fila De Processos\n5) Carregar Arquivo De Fila De Processos\n6) Encerrar\n\nInforme a operação que deseja realizar: ')

        match opt:
            case '1':
                # Testa se é possível adicionar outro processo sem passar do limite estipulado de 100 processos
                if(len(lista_proc) + 1 <= 100):
                    # Ler e validar o tipo de processo a ser criado
                    valid_proc = False
                    while not valid_proc:
                        tipo_proc = input(
                            '\n1) Processo de Cálculo\n'
                            '2) Processo de Gravação\n'
                            '3) Processo de Leitura\n'
                            '4) Processo de Impressão\n'
                            'Informe que tipo de processo desejar criar: '
                        )
                        if tipo_proc.isnumeric() and 1 <= int(tipo_proc) <= 4:
                            valid_proc = True
                        else:
                            print('Opção inválida. Tente novamente.\n')

                    match tipo_proc:
                        # Processo de cálculo
                        case '1':
                            n1 = input('Informe o primeiro número: ')
                            while not n1.isnumeric():
                                n1 = input('Dado inválido!\nFavor, informar um número válido: ')
                            n2 = input('Informe o segundo número: ')
                            while not n2.isnumeric():
                                n2 = input('Dado inválido!\nFavor, informar um número válido: ')
                            oper = input(
                                '( + ) Adição\n'
                                '( - ) Subtração\n'
                                '( * ) Multiplicação\n'
                                '( / ) Divisão\n'
                                'Informe o símbolo da operação desejada: '
                            )
                            if oper not in {'+', '-', '*', '/'}:
                                print('Operação inválida.\n')
                            else:
                                process = Computing_Process(prox_pid, n1, n2, oper)
                                lista_proc.append(process)
                                prox_pid += 1
                                print('Processo de cálculo criado!\n')

                        # Processo de gravação
                        case '2':
                            if lista_proc and isinstance(lista_proc[-1], Computing_Process):
                                expr = lista_proc[-1].return_exp()
                                process = Writing_Process(prox_pid, expr)
                                lista_proc.append(process)
                                prox_pid += 1
                                print("\nProcesso de gravação criado com sucesso!\n")
                            else:
                                print("\nNenhum processo de cálculo encontrado na fila\n")

                        # Processo de leitura
                        case '3':
                            process = Reading_Process(prox_pid, lista_proc)
                            lista_proc.append(process)
                            prox_pid += 1
                            print('\nProcesso de leitura criado!\n')

                        # Processo de impressão
                        case '4':
                            process = Printing_Process(prox_pid, lista_proc)
                            lista_proc.append(process.execute())
                            prox_pid += 1
                            print('Processo de impressão criado!\n')
                else:
                    print("Adicionar um processo irá exceder o limite de 100 processos! Operação cancelada!")

            case '2':
                if len(lista_proc) > 0:
                    if(isinstance(lista_proc[0], Reading_Process)):
                        read_procs = lista_proc[0].execute(prox_pid)
                        for r in read_procs:
                            lista_proc.append(r)
                        prox_pid += len(read_procs)
                        print('Leitura Concluída!')
                    else:
                        print(f'\nProcesso executado e removido da fila! Retorno do Processo: {lista_proc[0].execute()}\n')
                    del lista_proc[0]
                else:
                    print('Nenhum processo listado!\n')

            case '3':
                print('\n')
                valid_id = False
                end_opt = False
                if(len(lista_proc) > 0):
                    while (not end_opt):
                        exec_proc = input('Informe o pid do processo que deseja executar:\n')
                        if exec_proc.isnumeric():
                            for proc in lista_proc:
                                if proc.id == int(exec_proc):
                                    print(f'Executando processo PID: {proc.id}')
                                    proc.execute()
                                    lista_proc.remove(proc)
                                    end_opt = True
                                    break
                            else:
                                print("Processo não encontrado.")
                        else:
                            print("PID inválido.")
                else:
                    print('Nenhum processo listado!\n')

            case '4':
                # Salvar a fila de processos
                with open('process_queue.txt', 'w') as file:
                    for process in lista_proc:
                        file.write(f"{process.tipo}|{process.id}\n")
                print("Fila de processos salva com sucesso!")

            case '5':
                try:
                    with open('process_queue.txt', 'r') as file:
                        for line in file:
                            tipo, pid = line.strip().split('|')
                            if tipo == "Cálculo":
                                process = Computing_Process(int(pid), 0, 0, "+")
                            elif tipo == "Gravação":
                                process = Writing_Process(int(pid), "")
                            elif tipo == "Leitura":
                                process = Reading_Process(int(pid), lista_proc)
                            elif tipo == "Impressão":
                                process = Printing_Process(int(pid), lista_proc)
                            lista_proc.append(process)
                    print("Fila de processos carregada com sucesso!")
                except FileNotFoundError:
                    print("Arquivo de fila de processos não encontrado.")

            case '6':
                close_sys = True
                print("Encerrando o programa.")

            case _:
                print("Opção inválida.")