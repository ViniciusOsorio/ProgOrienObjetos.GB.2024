from processo import Processo
from computingProcess import Computing_Process
from printingProcess import Printing_Process
from writingProcess import Writing_Process
from readingProcess import Reading_Process

print('Bem-vindo ao Gerenciador de Processo GB10')

close_sys = False

lista_proc = []

ind_lista = 1

while(not close_sys):
    
    opt = input('Informe a operação que deseja realizar:\n1) Criar Processo\n2) Executar Próximo Processo'+
            '\n3) Executar Processo Específico\n4) Salvar Fila De Processos\n5) Carregar Arquivo De Fila De Processos\n6) Encerrar\n')
    
    match(opt):
        case '1':

            #ler e validar o tipo de processo a ser criado
            valid_proc = False
            while(not valid_proc):
                tipo_proc = input('Informe que tipo de processo desejar criar:\n1) Processo de Cálculo\n2) Processo de Gravação\n3) Processo de Leitura\n4) Processo de Impressão')
                if(tipo_proc.isnumeric() and not ('.' in oper)):
                    if(int(tipo_proc) > 0 and int(tipo_proc) < 5):
                        valid_proc = True
                if(not valid_proc):\
                    print('Opção Inválida! Informe uma opção válida para prosseguir.')
            
            match(tipo_proc):
                case '1','2':

                    #variáveis para loops de validação
                    n1NaN = True
                    n2NaN = True
                    oper_invalida = True

                    #Informar e validar primeiro número
                    while(n1NaN):
                        n1 = input('Informe o primeiro número da operação:\n')
                        if(n1.isnumeric()):
                            if '.' in n1:
                                n1 = float(n1)
                            else:
                                n1 = int(n1)
                            n1NaN = False
                        else:
                            print('Não foi informado número válido! Favor, tente novamente.')

                    #Informar e validar segundo número        
                    while(n2NaN):
                        n2 = input('Informe o segundo número da operação:\n')
                        if(n2.isnumeric()):
                            if '.' in n2:
                                n2 = float(n2)
                            else:
                                n2 = int(n2)
                            n2NaN = False
                        else:
                            print('Não foi informado número válido! Favor, tente novamente.')            

                    while(oper_invalida):
                        oper = input('Informe qual a operação que deseja realizar:\n1) Adição\n2) Subtração\n3) Multiplicação\n4) Divisão\n')
                        if(oper.isnumeric() and not ('.' in oper)):
                            if(int(oper) > 0 and int(oper) < 5):
                                oper_invalida = False
                            else:
                                print('1')
                                print('Operação Informada É Inválida! Tente Novamente')
                        else:
                            print('2')
                            print('Operação Informada É Inválida! Tente Novamente')
                    
                    proc = Computing_Process(ind_lista, n1, n2, oper)

                    if(tipo_proc == '1'):
                        lista_proc.append(proc)
                        ind_lista += 1

                    if(tipo_proc == '2'):
                        proc_exp = proc.return_exp()
                        write_proc = Writing_Process(ind_lista, proc_exp)
                        lista_proc.append(write_proc)
                        ind_lista += 1

                case '3':
                    proc = Reading_Process(ind_lista)
                    lista_proc.append(proc)
                    ind_lista += 1

                case '4':
                    proc = Printing_Process(ind_lista)
                    ind_lista += 1
                    lista_proc.append(proc)

        case '2':
            if len(lista_proc) > 0:
                if(isinstance(lista_proc[0], Reading_Process)):
                    read_procs = lista_proc[0].execute(ind_lista)
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
                    exec_proc = input('Informe o ID do processo que deseja executar:\n')
                    if(not ('.' in exec_proc) and exec_proc.isnumeric()):
                        valid_id = True

                for proc in lista_proc:
                    if proc.id == exec_proc:
                        p = proc
                        end_opt = True

                if(isinstance(p, Reading_Process)):
                    comp_procs = p.execute(ind_lista)
                else:
                    p.execute()

                if(p == None):
                    cont = input('ID informado não pertence a um processo existente!\nFavor, pressione X para encerrar o processo ou qualquer outra tecla para informar novo ID de Processo\n')
                    match(cont):
                        case 'X','x':
                            end_opt = True
                            input('Encerrando Processo\nPressione ENTER para continuar')
                        case _:
                            None


        case '4':
            print('opt4')

        case '5':
            print('opt5')

        case '6':
            close_sys = True