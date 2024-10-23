import time
from datetime import datetime

biblioteca = {}
banco_clientes = {}
reserva_de_livro = {}

def adicionar_livro():
    nome_livro = input("Digite o nome do livro: ")
    quantidade = int(input("Digite a quantidade: "))

    if nome_livro in biblioteca:
        print(f"O livro {nome_livro} já existe na biblioteca, estoque atual do livro: {biblioteca[quantidade]}")

        desejacontinuar = input("Deseja atualizar a quantidade? (S/N)").upper()

        if desejacontinuar == 'S':
            biblioteca[nome_livro] += quantidade
        else:
            pass

    else:
        biblioteca[nome_livro] = quantidade
        print(f"Livro {nome_livro} adicionado com sucesso!")

def remover_livro():
    nome_remover = input("Digite o nome do livro que deseja remover: ")
    quantidade_remover = int(input("Digite a quantidade que deseja remover: "))

    if nome_remover in biblioteca:
        biblioteca[nome_remover] -= quantidade_remover
        print(f"Livro removido, quantidade atual do livro {nome_remover} é {biblioteca[nome_remover]} unidades!")

    elif quantidade_remover < 0:
        print("Número inválido, corrija e tente novamente!")

    elif quantidade_remover == 0:
        del biblioteca[nome_remover]
        print(f"O livro {nome_remover} foi removido da biblioteca!")

    else:
        print(f"O livro {nome_remover} não existe na biblioteca!!")

def visualizar_biblioteca():
    if biblioteca:
        for livro, quantidade in biblioteca.items():
            print(f"Livro: {livro} | Quantidade: {quantidade} ")

    else:
        print("Biblioteca vázia!")

def atualizar_livro():
    nome_atualizar = input("Digite o nome do livro que deseja atualizar: ")
    quantidade_atualizar = int(input("Digite a quantidade que deseja atualizar: "))

    if nome_atualizar in biblioteca:
        biblioteca[nome_atualizar] = quantidade_atualizar
        print(f"Quantidade atualizada, estoque atual do livro {nome_atualizar} é {biblioteca[nome_atualizar]} unidades!")

    elif quantidade_atualizar == biblioteca[nome_atualizar]:
        print(f"Já existe essa quantidade no estoque, estoque atual do livro {nome_atualizar} é {biblioteca[nome_atualizar]} unidades")

    elif quantidade_atualizar < 0:
        print("Não é possível atualizar unidades com números negativos!")

    else:
        print(f"O livro {nome_atualizar} não existe na biblioteca!")

def Cliente():
    while True:
        nome_cliente = input(f"Digite o nome do cliente: ")
        cpf_cliente = input("Digite o CPF do cliente: ")
        telefone_cliente = input("Digite o número de telefone do cliente: ")
        endereco_cliente = str(input("Digite o endereço do cliente: "))

        if nome_cliente in banco_clientes:
            if cpf_cliente in banco_clientes[nome_cliente]:
                print(f"O {nome_cliente} já possuí cadastro na biblioteca! ")

        elif len(cpf_cliente) != 11:
            print("CPF inválido, digite novamente!")

        elif len(telefone_cliente) < 10:
            print("Número de telefone inválido, tente novamente")

                
        else:
            banco_clientes[nome_cliente] = {
                'cpf': cpf_cliente,
                'telefone': telefone_cliente,
                'endereco': endereco_cliente
            }
            print(f"Cliente {nome_cliente} cadastrado com sucesso!")
            break

def atualizar_cliente():
    while True:
        CLientequevaiAtualizar = input("Digite o nome do cliente que deseja atualizar: ")

        if CLientequevaiAtualizar in banco_clientes:
            print("....buscando")
            time.sleep(1)
            print("-----------------------------------------------")
            print("O que deseja atualizar?\n 1 - Nome do Cliente | 2 - CPF do Cliente | 3 - Telefone do Cliente | 4 - Endereço do Cliente | 5 - Apagar Cliente | 6 - Voltar")

            resposta_do_cliente_atualizar = int(input("Digite a opção que deseja: "))

            if resposta_do_cliente_atualizar == 1:
                print(f"Nome atual do cliente: {CLientequevaiAtualizar}")

                novo_nome_cliente = input("Digite o novo nome do cliente: ")
                banco_clientes[novo_nome_cliente] = banco_clientes.pop(CLientequevaiAtualizar)
                print(f"Nome do cliente atualizado com sucesso! Novo nome: {novo_nome_cliente}.")
                break

            elif novo_nome_cliente == CLientequevaiAtualizar:
                print("Esse nome já existe dessa forma no sistema!")

            elif novo_nome_cliente == None:
                print("O novo nome do cliente não pode estar vázio!")


            elif  resposta_do_cliente_atualizar == 2:
                novo_cpf = input("Digite o novo CPF do cliente: ")
                banco_clientes[CLientequevaiAtualizar]['cpf'] = novo_cpf
                print(f"CPF do cliente {CLientequevaiAtualizar} atualizado com sucesso!")

                if len(novo_cpf) != 11:
                    print("CPF inválido, digite novamente!")
            
            elif resposta_do_cliente_atualizar == 3:
                novo_telefone = input("Digite o novo número de telefone do cliente: ")
                banco_clientes[CLientequevaiAtualizar]['telefone'] = novo_telefone
                print(f"O telefone do cliente {CLientequevaiAtualizar} foi atualizado com sucesso!")
                if len(novo_telefone) < 10:
                    print("Número de telefone inválido, tente novamente")

            elif resposta_do_cliente_atualizar == 4:
                novo_endereco = str(input("Digite o novo endereço do cliente: "))
                banco_clientes[CLientequevaiAtualizar]['endereco'] = novo_endereco
                print(f"Endereço do cliente {CLientequevaiAtualizar} foi atualizado com sucesso!")

            elif resposta_do_cliente_atualizar == 5:
                resposta_para_apagar_o_cliente = input("Deseja deletar o cadastro do cliente? (S/N)").upper()
                if resposta_para_apagar_o_cliente == 'S':
                    del banco_clientes[CLientequevaiAtualizar]
                    print(f"O cadastro do cliente foi apagado com sucesso!")

                else:
                    print('O Cadastro do cliente não foi removido!')

            elif resposta_do_cliente_atualizar == 6:
                break


            else:
                print("Cliente não encotrado, verifique e tente novamente!") 
                

def visualizar_clientes():
    for cliente in banco_clientes.items():
        print(f"{cliente}\n")

def reservar_livro():
    while True:
        print("-------------------------------------------------")
        print("O Cliente tem cadastro na loja?\n 1 - Sim | 2 - Não")
        print("-------------------------------------------------")
        opcao_tem_cadastro_ou_nao = input("Escolha uma opção: ")

        if opcao_tem_cadastro_ou_nao == 1:
            nome_do_cliente_que_vai_reservar = input("Qual o nome do cliente que vai reservar: ")
            cpf_do_cliente_que_vai_reservar_o_livro = input("Qual cpf do cliente que vai reservar: ")

            if nome_do_cliente_que_vai_reservar in banco_clientes:
                if cpf_do_cliente_que_vai_reservar_o_livro in banco_clientes[nome_do_cliente_que_vai_reservar]['cpf']:
                    livro_que_sera_reservado = input("Qual livro deseja reservar? ")


                    if livro_que_sera_reservado in biblioteca:
                        if biblioteca[livro_que_sera_reservado]['quantidade'] > 0:
                            data_que_vai_reservar = input("Data que será reservado: (dd/mm/yy)")
                            data_que_vai_devolver = input("Data que será devolvido: (dd/mm/yy) ")
                            try:
                                data_formatada = datetime.strptime(data_que_vai_reservar, '%d/%m/%y')
                                data_formatada = datetime.strptime(data_que_vai_devolver, '%d/%m/%y')
                                print("Data válida:", data_formatada.strftime('%d/%m/%Y'))

    
                                reserva_de_livro[livro_que_sera_reservado] = {
                                    'cliente_que_reservou': nome_do_cliente_que_vai_reservar,
                                    'cpf_do_cliente_que_reservou': cpf_do_cliente_que_vai_reservar_o_livro,
                                    'livro_reservado': livro_que_sera_reservado,
                                    'data_reservada': data_formatada,
                                    'data_devolucao': data_que_vai_devolver
                                }

                                biblioteca[livro_que_sera_reservado]['quantidade'] -= 1
                                print(f"O livro {livro_que_sera_reservado} foi reservado com sucesso! Data a ser devolvida é {data_que_vai_devolver}")

                            except ValueError:
                                print("Formato de data inválido. Por favor, insira no formato dd/mm/yy.")

/





def menu():
    print('---------------------------------------------------')
    print('     Seja bem-vindo ao sistema da biblioteca!      ')
    print('---------------------------------------------------')
    print('             O que você deseja hoje?               ')
    

    while True:
        print("1 - Cadastrar Livro | 2 - Remover Livro | 3 - Visualizar Biblioteca | 4 - Atualizar livro | 5 - Cadastrar Cliente | 6 - Atualizar Cliente| 7 - Visualizar Clientes |8 - Reservar Livro | 9 - Sair do Sistema")

        opcao = int(input("Digite sua escolha: "))
        if opcao == 1:
            adicionar_livro()
        
        elif opcao == 2:
            remover_livro()
        
        elif opcao == 3:
            visualizar_biblioteca()

        elif opcao == 4:
            atualizar_livro()

        elif opcao == 5:
            Cliente()

        elif opcao == 6:
            atualizar_cliente()

        elif opcao == 7:
            visualizar_clientes()

        elif opcao == 9:
            print("Sistema encerrado!")
            break
            

menu()

 



    