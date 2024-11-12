from computingProcess import Computing_Process

print('Bem-vindo ao Gerenciador de Processo GB10')

close_sys = False

while(not close_sys):
    
    opt = input('Informe a operação que deseja realizar:\n1) Criar Processo\n2) Executar Próximo Processo'+
            '\n3) Executar Processo Específico\n4) Salvar Fila De Processos\n5) Carregar Arquivo De Fila De Processos\n6) Encerrar\n')
    
    match(opt):
        case '1':
            #tipo_proc = input('Informe que tipo de processo desejar criar:')

            proc_id = 1
            n1NaN = True
            n2NaN = True
            oper_invalida = True
            while(n1NaN):
                n1 = input('Informe o primeiro número da operação:\n')
                if(n1.isnumeric()):
                    n1NaN = False
                else:
                    print('Não foi informado número válido! Favor, tente novamente.')
            while(n2NaN):
                n2 = input('Informe o segundo número da operação:\n')
                if(n2.isnumeric()):
                    n2NaN = False
                else:
                    print('Não foi informado número válido! Favor, tente novamente.')
            

            while(oper_invalida):
                oper = input('Informe qual a operação que deseja realizar:\n1) Adição\n2) Subtração\n3) Multiplicação\n4) Divisão\n')
                if(oper.isnumeric() and isinstance(int(oper), int)):                    
                    if(int(oper) > 0 and int(oper) < 5):
                        oper_invalida = False
                    else:
                        print('1')
                        print('Operação Informada É Inválida! Tente Novamente')
                else:
                    print('2')
                    print('Operação Informada É Inválida! Tente Novamente')

                proc = Computing_Process(proc_id, n1, n2, oper)

                print(f'Retorno do Processo: {proc.execute()}')