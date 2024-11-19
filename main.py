from processo import Processo
from computingProcess import Computing_Process
from printingProcess import Printing_Process
from writingProcess import Writing_Process

print('Bem-vindo ao Gerenciador de Processo GB10')

close_sys = False

lista_proc = []

while(not close_sys):
    
    opt = input('Informe a operação que deseja realizar:\n1) Criar Processo\n2) Executar Próximo Processo'+
            '\n3) Executar Processo Específico\n4) Salvar Fila De Processos\n5) Carregar Arquivo De Fila De Processos\n6) Encerrar\n')
    
    match(opt):
        case '1':
            
            #determinando qual será o pid do processo
            proc_id = len(lista_proc)+1 if len(lista_proc) > 0 else 1

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
                    
                    proc = Computing_Process(proc_id, n1, n2, oper)

                    if(tipo_proc == '1'):
                        lista_proc.append(proc)
                        
                    if(tipo_proc == '2'):
                        proc_exp = proc.return_exp()
                        write_proc = Writing_Process(proc_id, proc_exp)
                        lista_proc.append(write_proc)

                case '3':
                    proc = Writing_Process(proc_id, lista_proc)

        case '2':
            if len(lista_proc) > 0:
                lista_proc[0].execute()
                del lista_proc[0]
            else:
                print('Nenhum processo listado!\n')

        case '3':
            print('opt3')

        case '4':
            print('opt4')

        case '5':
            print('opt5')

        case '6':
            close_sys = True
