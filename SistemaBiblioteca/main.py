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
            biblioteca[nome_livro] = {
                'quantidade': quantidade
            }
        else:
            pass

    else:
        biblioteca[nome_livro] = {
            'quantidade': quantidade
        }
        print(f"Livro {nome_livro} adicionado com sucesso!")

def remover_livro():
    nome_remover = input("Digite o nome do livro que deseja remover: ")
    quantidade_remover = int(input("Digite a quantidade que deseja remover: "))

    if nome_remover in biblioteca:
        if biblioteca[nome_remover]['quantidade'] >= quantidade_remover:
            biblioteca[nome_remover]['quantidade'] -= quantidade_remover
            print(f"Quantidade atual do livro {nome_remover} é {biblioteca[nome_remover]['quantidade']} unidades.")
            if biblioteca[nome_remover] == 0:
                del biblioteca[nome_remover]
                print(f"O livro {nome_remover} foi removido da biblioteca.")
        else:
            print(f"Você está tentando remover mais do que o disponível. Temos {biblioteca[nome_remover]} unidades.")
    else:
        print(f"O livro {nome_remover} não existe na biblioteca!")

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
        cpf_cliente = input("Digite o CPF do cliente (11 dígitos): ")
        telefone_cliente = input("Digite o número de telefone (mínimo 10 dígitos): ")
        endereco_cliente = input("Digite o endereço do cliente: ")

        if len(cpf_cliente) != 11:
            print("CPF inválido, digite novamente! Deve conter 11 dígitos.")
            continue

        if len(telefone_cliente) < 10:
            print("Número de telefone inválido, tente novamente!")
            continue

        if nome_cliente in banco_clientes and banco_clientes[nome_cliente]['cpf'] == cpf_cliente:
            print(f"O cliente {nome_cliente} já possui cadastro na biblioteca!")
            break

        banco_clientes[nome_cliente] = {
            'cpf': cpf_cliente,
            'telefone': telefone_cliente,
            'endereco': endereco_cliente
        }
        print(f"Cliente {nome_cliente} cadastrado com sucesso!")
        break

def atualizar_cliente():
    while True:
        cliente_que_vai_atualizar = input("Digite o nome do cliente que deseja atualizar: ")

        if cliente_que_vai_atualizar in banco_clientes:
            print("....buscando")
            time.sleep(1)
            print("-----------------------------------------------")
            print("O que deseja atualizar?\n1 - Nome do Cliente | 2 - CPF do Cliente | 3 - Telefone do Cliente | 4 - Endereço do Cliente | 5 - Apagar Cliente | 6 - Voltar")
            
            try:
                resposta_do_cliente_atualizar = int(input("Digite a opção que deseja: "))
            except ValueError:
                print("Por favor, digite uma opção válida!")
                continue

            if resposta_do_cliente_atualizar == 1:
                print(f"Nome atual do cliente: {cliente_que_vai_atualizar}")
                novo_nome_cliente = input("Digite o novo nome do cliente: ")

                if novo_nome_cliente.strip():  
                    banco_clientes[novo_nome_cliente] = banco_clientes.pop(cliente_que_vai_atualizar)
                    print(f"Nome do cliente atualizado com sucesso! Novo nome: {novo_nome_cliente}.")
                    break
                else:
                    print("O novo nome do cliente não pode estar vazio!")

            elif resposta_do_cliente_atualizar == 2:
                novo_cpf = input("Digite o novo CPF do cliente: ")

                if len(novo_cpf) == 11 and novo_cpf.isdigit():  
                    banco_clientes[cliente_que_vai_atualizar]['cpf'] = novo_cpf
                    print(f"CPF do cliente {cliente_que_vai_atualizar} atualizado com sucesso!")
                else:
                    print("CPF inválido! O CPF deve ter 11 dígitos numéricos.")

            elif resposta_do_cliente_atualizar == 3:
                novo_telefone = input("Digite o novo número de telefone do cliente: ")

                if len(novo_telefone) >= 10 and novo_telefone.isdigit():  
                    banco_clientes[cliente_que_vai_atualizar]['telefone'] = novo_telefone
                    print(f"O telefone do cliente {cliente_que_vai_atualizar} foi atualizado com sucesso!")
                else:
                    print("Número de telefone inválido! Deve conter pelo menos 10 dígitos numéricos.")

            elif resposta_do_cliente_atualizar == 4:
                novo_endereco = input("Digite o novo endereço do cliente: ")

                if novo_endereco.strip():  
                    banco_clientes[cliente_que_vai_atualizar]['endereco'] = novo_endereco
                    print(f"Endereço do cliente {cliente_que_vai_atualizar} foi atualizado com sucesso!")
                else:
                    print("O endereço não pode estar vazio!")

            
            elif resposta_do_cliente_atualizar == 5:
                resposta_para_apagar_o_cliente = input("Deseja deletar o cadastro do cliente? (S/N)").upper()
                if resposta_para_apagar_o_cliente == 'S':
                    del banco_clientes[cliente_que_vai_atualizar]
                    print(f"O cadastro do cliente {cliente_que_vai_atualizar} foi apagado com sucesso!")
                    break
                else:
                    print("O cadastro do cliente não foi removido!")

            elif resposta_do_cliente_atualizar == 6:
                break

            else:
                print("Opção inválida! Por favor, escolha uma opção de 1 a 6.")

        else:
            print("Cliente não encontrado, verifique e tente novamente!")
                

def visualizar_clientes():
    for cliente in banco_clientes.items():
        print(f"{cliente}\n")

def reservar_livro():
    while True:
        print("-------------------------------------------------")
        print("O Cliente tem cadastro na loja?\n 1 - Sim | 2 - Não")
        print("-------------------------------------------------")
        opcao_tem_cadastro_ou_nao = int(input("Escolha uma opção: "))

        if opcao_tem_cadastro_ou_nao == 1:  
            nome_do_cliente_que_vai_reservar = input("Qual o nome do cliente que vai reservar: ")
            cpf_do_cliente_que_vai_reservar_o_livro = input("Qual CPF do cliente que vai reservar: ")

            if nome_do_cliente_que_vai_reservar in banco_clientes:
                if banco_clientes[nome_do_cliente_que_vai_reservar]['cpf'] == cpf_do_cliente_que_vai_reservar_o_livro:
                    livro_que_sera_reservado = input("Qual livro deseja reservar? ")

                    if livro_que_sera_reservado in biblioteca and biblioteca[livro_que_sera_reservado]['quantidade'] > 0:
                        data_que_vai_reservar = input("Data que será reservado: (dd/mm/yy) ")
                        data_que_vai_devolver = input("Data que será devolvido: (dd/mm/yy) ")
                        try:
                            data_reservada = datetime.strptime(data_que_vai_reservar, '%d/%m/%y')
                            data_devolucao = datetime.strptime(data_que_vai_devolver, '%d/%m/%y')

                            reserva_de_livro[livro_que_sera_reservado] = {
                                'cliente_que_reservou': nome_do_cliente_que_vai_reservar,
                                'cpf_do_cliente_que_reservou': cpf_do_cliente_que_vai_reservar_o_livro,
                                'livro_reservado': livro_que_sera_reservado,
                                'data_reservada': data_reservada,  
                                'data_devolucao': data_devolucao 
                            }

                            biblioteca[livro_que_sera_reservado]['quantidade'] -= 1
                            print(f"O livro '{livro_que_sera_reservado}' foi reservado com sucesso!")
                            print(f"Data a ser devolvida: {data_devolucao.strftime('%d/%m/%Y')}")
                            break

                        except ValueError:
                            print("Formato de data inválido. Por favor, insira no formato dd/mm/yy.")
                        
                    elif livro_que_sera_reservado not in biblioteca:
                        print(f"O livro '{livro_que_sera_reservado}' não existe.")
                    else:
                        print(f"O livro '{livro_que_sera_reservado}' está esgotado.")
                else:
                    print("CPF inválido ou cliente não tem cadastro na loja!")
            else:
                print("Cliente não encontrado no cadastro.")

        elif opcao_tem_cadastro_ou_nao == 2:
            print("Cliente não tem cadastro na loja. Por favor, cadastre-se primeiro.")
            break  

        else:
            print("Opção inválida! Por favor, escolha 1 ou 2.")


def cancelar_reserva():
    while True:
        print("--------------------------------")
        nome_cliente_que_vai_cancelar_reserva = input("Digite o nome do cliente que deseja cancelar a reserva: ")
        cpf_cliente_que_vai_cancelar_reserva = input("Digite o CPF do cliente que deseja cancelar a reserva: ")

        
        reserva_encontrada = False

        
        for livro, reserva in reserva_de_livro.items():
            if reserva['cliente_que_reservou'] == nome_cliente_que_vai_cancelar_reserva and reserva['cpf_do_cliente_que_reservou'] == cpf_cliente_que_vai_cancelar_reserva:
                reserva_encontrada = True
                opcao_para_cancelar_reserva = int(input(f"Deseja cancelar a reserva do cliente {nome_cliente_que_vai_cancelar_reserva} para o livro '{livro}'?\n1 - SIM || 2 - NÃO: "))
                
                if opcao_para_cancelar_reserva == 1:
                    del reserva_de_livro[livro]  
                    print("Reserva apagada com sucesso!")
                else:
                    print("Cancelamento de reserva cancelado!")
                break  

        if not reserva_encontrada:
            print("Reserva não encontrada para o cliente informado.")
        
        break 

                    




def livros_reservados():
    print("Livros Reservados:")
    for reserva in reserva_de_livro.values():
        print(f"Livro: {reserva['livro_reservado']}, Cliente: {reserva['cliente_que_reservou']}, CPF: {reserva['cpf_do_cliente_que_reservou']}, Data Reservada: {reserva['data_reservada'].strftime('%d/%m/%Y')}, Data de Devolução: {reserva['data_devolucao'].strftime('%d/%m/%Y')}")





def menu():
    print('---------------------------------------------------')
    print('     Seja bem-vindo ao sistema da biblioteca!      ')
    print('---------------------------------------------------')
    print('             O que você deseja hoje?               ')
    

    while True:
        print("1 - Cadastrar Livro | 2 - Remover Livro | 3 - Visualizar Biblioteca | 4 - Atualizar livro | 5 - Cadastrar Cliente | 6 - Atualizar Cliente| 7 - Visualizar Clientes |8 - Reservar Livro | 9 - Livros Reservados | 10 - Cancelar Reserva | 11 - Sair do Sistema")

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

        elif opcao == 8:
            reservar_livro()
            
        elif opcao == 9:
            livros_reservados()

        elif opcao == 10:
            cancelar_reserva()

        elif opcao == 11:
            print("Sistema encerrado!")
            break
            

menu()

 
