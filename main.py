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
        
        opt = input('1) Criar Processo\n2) Executar Próximo Processo'+
                '\n3) Executar Processo Específico\n4) Salvar Fila De Processos\n5) Carregar Arquivo De Fila De Processos\n6) Encerrar\n\nInforme a operação que deseja realizar: ')
        
        match opt:
            case '1':

                # ler e validar o tipo de processo a ser criado
                valid_proc = False
                while not valid_proc:
                    tipo_proc = input(
                        '1) Processo de Cálculo\n'
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
                        n1 = float(input('Informe o primeiro número: '))
                        n2 = float(input('Informe o segundo número: '))
                        oper = input(
                            '( + ) Adição\n'
                            '( - ) Subtração\n'
                            '( * ) Multiplicação\n'
                            '( / ) Divisão\n'
                            'Informe a operação desejada: '
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
                        if lista_proc:
                            last_process = lista_proc[-1]
                            if isinstance(last_process, Computing_Process):
                                expr = last_process.execute()
                                process = Writing_Process(prox_pid, expr)
                                lista_proc.append(process)
                                prox_pid += 1
                                print('Processo de gravação criado!\n')
                            else:
                                print('O último processo na fila não é um processo de cálculo.\n')
                        else:
                            print('A fila de processos está vazia.\n')

                    # Processo de leitura
                    case '3':
                        process = Reading_Process(prox_pid, lista_proc)
                        lista_proc.append(process)
                        prox_pid += 1
                        print('Processo de leitura criado!\n')
                    
                    # Processo de impressão
                    case '4':
                        process = Printing_Process(prox_pid, lista_proc)
                        lista_proc.append(process)
                        prox_pid += 1
                        print('Processo de impressão criado!\n')

            case '2':
                if len(lista_proc) > 0:
                    if(isinstance(lista_proc[0], Reading_Process)):
                        read_procs = lista_proc[0].execute(prox_pid)
                        for r in read_procs:
                            lista_proc.append(r)
                    else:
                        lista_proc[0].execute()
                    del lista_proc[0]
                else:
                    print('Nenhum processo listado!\n')

            case '3':
                valid_id = False
                end_opt = False
                p = None

                while (not end_opt):
                    while(not valid_id):
                        exec_proc = input('Informe o pid do processo que deseja executar:\n')
                        if(not ('.' in exec_proc) and exec_proc.isnumeric()):
                            valid_id = True

                    for proc in lista_proc:
                        if proc.id == exec_proc:
                            p = proc
                            end_opt = True

                    if(isinstance(p, Reading_Process)):
                        comp_procs = p.execute(prox_pid)
                    else:
                        p.execute()

                    if(p == None):
                        cont = input('pid informado não pertence a um processo existente!\nFavor, pressione X para encerrar o processo ou qualquer outra tecla para informar novo pid de Processo\n')
                        match(cont):
                            case 'X','x':
                                end_opt = True
                                input('Encerrando Processo\nPressione ENTER para continuar')
                            case _:
                                None


            case '4':
                # Salvar a fila de processos
                with open('process_queue.txt', 'w') as file:
                    for process in lista_proc:
                        file.write(f"{process.tipo}|{process.id}\n")
                print("Fila de processos salva com sucesso!")

            case '5':
                with open('process_queue.txt', 'r') as file:
                    process_queue = []
                    for line in file:
                        tipo, pid = line.strip().split('|')
                        if tipo == "Cálculo":
                            expr = input(f"Insira a expressão para o processo PID {pid}: ")
                            process = Computing_Process(int(pid), expr)
                            process_queue.append(process)
                        elif tipo == "Gravação":
                            expr = input(f"Insira a expressão para gravação no PID {pid}: ")
                            process = Writing_Process(int(pid), expr)
                            process_queue.append(process)
                        elif tipo == "Leitura":
                            process = Reading_Process(int(pid), process_queue)
                            process_queue.append(process)
                        elif tipo == "Impressão":
                            process = Printing_Process(int(pid), process_queue)
                            process_queue.append(process)
                print("Fila de processos carregada com sucesso!")

            case '6':
                close_sys = True
                print("Encerrando o programa")

            case _:
                print("Opção inválida")