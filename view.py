from tracemalloc import stop
from turtle import goto
import controller
import model
from models.linkedlist import LinkedList
from colorama import Fore

# sala default usado para todas as salas dos eventos, copiada.
sala = ["K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8", "K9", "K10", "K11", "K12", "K13", "K14",
        "J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J9", "J10", "J11", "J12", "J13", "J14",
        "I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9", "I10", "I11", "I12", "I13", "I14",
        "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", "H14",
        "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10", "G11", "G12", "G13", "G14",
        "F1", "F2", "F13", "F14",
        "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10", "E11", "E12", "E13", "E14 ",
        "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "D11", "D12", "D13", "D14",
        "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14",
        "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10", "B11", "B12", "B13", "B14",
        "A1", "A2", "A13", "A14", ["A6", "A7", "A8", "A9", "F6", "F7", "F8", "F9"]]

#Lista de bilheteira 2022
bilheteira_janeiro_2022 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]# 31
bilheteira_fevereiro_2022 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_marco_2022 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_abril_2022 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_maio_2022 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_junho_2022 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_julho_2022 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_agosto_2022 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_setembro_2022 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_outubro_2022 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_novembro_2022 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_dezembro_2022 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

bilheteira_anual_2022 = [bilheteira_janeiro_2022, bilheteira_fevereiro_2022, bilheteira_marco_2022,
                         bilheteira_abril_2022,
                         bilheteira_maio_2022, bilheteira_junho_2022, bilheteira_julho_2022, bilheteira_agosto_2022,
                         bilheteira_setembro_2022,
                         bilheteira_outubro_2022, bilheteira_novembro_2022, bilheteira_dezembro_2022]

#Lista de bilheteira 2023
bilheteira_janeiro_2023 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]# 31
bilheteira_fevereiro_2023 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_marco_2023 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_abril_2023 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_maio_2023 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_junho_2023 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_julho_2023 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_agosto_2023 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_setembro_2023 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_outubro_2023 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_novembro_2023 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_dezembro_2023 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_anual_2023 = [bilheteira_janeiro_2023, bilheteira_fevereiro_2023, bilheteira_marco_2023,
                         bilheteira_abril_2023,
                         bilheteira_maio_2023, bilheteira_junho_2023, bilheteira_julho_2023, bilheteira_agosto_2023,
                         bilheteira_setembro_2023,
                         bilheteira_outubro_2023, bilheteira_novembro_2023, bilheteira_dezembro_2023]

# Lista dos eventosque têm reservas com pop() das que foram reservadas
lista_lugares_reservados = []

# Lista dos eventos que têm reservas e que vão ser printados
lista_todos_eventos_print = []

lista_clientes_registados = []
lista_usernames = []
lista_sessao_iniciada = []
lista_reservas = []
lista_reservas_total = []


def main():
    while True:
        try:
            controlos = input().split(" ")
        except EOFError:
            return

        if controlos[0] == "START":
            print()
            print("Bem vindo à sala de espetáculos!\nEscolha uma opção.")
            print()
            model.menu()

        # Tiago Lança
        if controlos[0] == "Registar":
            print() 
            print("Para se registar, introduza o seu Nome, Username e Password.\n")
            controlos = input().split(" ")

            registo = controller.verificar_cliente(lista_clientes_registados, lista_usernames, controlos)
            while registo == True:
                print()
                print("Já existe alguem registado com o username escolhido.\n")
                print("Para se registar, introduza o seu Nome, Username e Password.\n")
                print("Para voltar para o menu principal, digite Menu")
                controlos2 = input().split(" ")

                if len(controlos2) == 1:
                    if controlos2[0] == "Menu":
                        controller.funcao_menu()
                        break
                

                elif len(controlos) == 3:
                    registo_break = controller.verificar_cliente(lista_clientes_registados, lista_usernames, controlos2)
                    if registo_break == False:
                        print()
                        print("Registo efetuado com sucesso.\n")
                        controller.funcao_menu()
                        break

            if registo == False:
                print()
                print("Registo efetuado com sucesso.\n")
                controller.funcao_menu()


        elif controlos[0] == "Login":
            print()
            print("Para fazer login, introduza o seu Username e Password.\n")
            controlos = input().split(" ")
            if model.sessao_iniciada == True:
                model.sessao_iniciada = False
                login = controller.verificar_username(lista_clientes_registados, controlos)
                if login == False:
                    print()
                    print("Não existe registo efetuado com o username selecionado.\n")
                    print("Para fazer login, introduza o seu Username e Password.\n")
                    print("Para voltar para o menu principal, digite Menu")
                    controlos = input().split(" ")
                    if controlos[0] == "Menu":
                        print()
                        controller.funcao_menu()

                else:
                    if login == True:
                        username = controlos[0]
                        model.sessao_iniciada = True
                        print()
                        print("Login efetuado com sucesso.\n")
                        controller.funcao_menu()
            else:
                if model.sessao_iniciada == False:
                    login = controller.verificar_username(lista_clientes_registados, controlos)
                    if login == False:
                        print()
                        print("Não existe registo efetuado com o username selecionado.\n")
                        print("Para fazer login, introduza o seu Username e Password.\n")
                        print("Para voltar para o menu principal, digite Menu")
                        controlos = input().split(" ")
                        if controlos[0] == "Menu":
                            print()
                            controller.funcao_menu()

                    else:
                        if login == True:
                            username = controlos[0]
                            model.sessao_iniciada = True
                            print()
                            print("Login efetuado com sucesso.\n")
                            controller.funcao_menu()

       

        elif controlos[0] == "Eventos":
            print()
            print("Por favor, escolha um evento!\n")
            model.cartaz_eventos()
            controlos = input()
            dia = "NÃO EXISTE"
            dia_existe = "NÃO"
            erro_instrucao = "NÃO"

            # EVENTOS BRODWAY
            if controlos == "Brodway" or "Circo" or "Musical" or "Opera" or "Teatro":
                if controlos == "Circo":
                    evento = controlos
                    lista_reservas.append(evento)
                    print()
                    print(f"Escolha o dia, que pretende assitir ao evento {evento}.\n")
                    print('\n'.join(map(str, model.dias_circo)))
                    controlos = input()
                    if controlos in model.dias_circo:
                        dia_existe = "SIM"
                        reserva_dia = controlos
                        lista_reservas.append(reserva_dia)
                        dia = controlos
                
                elif controlos == "Teatro":
                    evento = controlos
                    lista_reservas.append(evento)
                    print()
                    print(f"Escolha o dia, que pretende assitir ao evento {evento}.\n")
                    print('\n'.join(map(str, model.dias_teatro)))
                    controlos = input()
                    if controlos in model.dias_teatro:
                        dia_existe = "SIM"
                        reserva_dia = controlos
                        lista_reservas.append(reserva_dia)
                        dia = controlos
                
                elif controlos == "Opera":
                    evento = controlos
                    lista_reservas.append(evento)
                    print()
                    print(f"Escolha o dia, que pretende assitir ao evento {evento}.\n")
                    print('\n'.join(map(str, model.dias_opera)))
                    controlos = input()
                    if controlos in model.dias_opera:
                        dia_existe = "SIM"
                        reserva_dia = controlos
                        lista_reservas.append(reserva_dia)
                        dia = controlos
                
                elif controlos == "Musical":
                    evento = controlos
                    lista_reservas.append(evento)
                    print()
                    print(f"Escolha o dia, que pretende assitir ao evento {evento}.\n")
                    print('\n'.join(map(str, model.dias_musical)))
                    controlos = input()
                    if controlos in model.dias_musical:
                        dia_existe = "SIM"
                        reserva_dia = controlos
                        lista_reservas.append(reserva_dia)
                        dia = controlos
                
                elif controlos == "Brodway":
                    evento = controlos
                    lista_reservas.append(evento)
                    print()
                    print(f"Escolha o dia, que pretende assitir ao evento {evento}.\n")
                    print('\n'.join(map(str, model.dias_brodway)))
                    controlos = input()
                    if controlos in model.dias_brodway:
                        dia_existe = "SIM"
                        reserva_dia = controlos
                        lista_reservas.append(reserva_dia)
                        dia = controlos

                if dia_existe == "SIM":
                    if len(controlos) == 8:
                        variavel_dia = int(controller.guardar_dia_1digito(controlos))
                        variavel_mes = int(controller.guardar_mes_1digito(controlos))

                    elif len(controlos) == 9:
                        variavel_teste = controller.guardar_dia_2digitos(controlos)
                        
                        if "/" in variavel_teste:
                            variavel_dia = int(controller.guardar_dia_1digito(variavel_teste))
                            variavel_mes = int(controller.guardar_mes_9elementos_2digitos(controlos))

                        else:
                            variavel_dia = int(controller.guardar_dia_2digitos(controlos))
                            variavel_mes = int(controller.guardar_mes_9elementos(controlos))

                    elif len(controlos) == 10:
                        variavel_dia = int(controller.guardar_dia_2digitos(controlos))
                        variavel_mes = int(controller.guardar_mes_2digitos(controlos))
                else:
                    print(f"{Fore.RED}Instrução não compreendida, voltando ao menu inicial.{Fore.RESET}")
                    model.menu()
                    erro_instrucao = "SIM"

                verificacao_login = controller.verificar_sessao_iniciada()
                if verificacao_login == False and erro_instrucao == "NÃO":
                    print()
                    print(f"Para reservar um bilhete, por favor registe-se na nossa plataforma, na opção {Fore.RED}REGISTAR{Fore.RESET} no Menu.\n")
                    print(f"Se já se encontra registado, por favor faça {Fore.RED}LOGIN{Fore.RESET}.\n")
                    controller.funcao_menu()
                elif verificacao_login == True:
                

                    if dia != 0:
                        print("Que tipo de bilhete pretende?\n")
                        print(model.tabela_precos())
                        controlos = input()

                    if controlos == "Normal":
                        tipo_bilhete = controlos
                        lista_reservas.append(tipo_bilhete)
                        variavel_teste = "Não Reservado"

                        while variavel_teste == "Não Reservado":
                            controller.print_palco_evento(dia)
                            print("Selecione o seu lugar\n")
                            lugar = input()

                            if lugar == "A6" or lugar == "A7" or lugar == "A8" or lugar == "A9" or lugar == "F6" or lugar == "F7" or lugar == "F8" or lugar == "F9":
                                print(f"O lugar introduzido pertence a um lugar {Fore.YELLOW}VIP{Fore.RESET}, se pretende comprar um lugar {Fore.YELLOW}VIP{Fore.RESET}, porfavor, introduza {Fore.GREEN}MENU{Fore.RESET} e selecione o bilhete {Fore.YELLOW}VIP{Fore.RESET}.\n")
                            elif lugar not in sala:
                                print(f"{Fore.RED}Porfavor Introduza um lugar válido{Fore.RESET}\n")
                            else:
                                variavel_teste = controller.criar_reservas_normal(dia, lugar)
                                if variavel_teste == "Não Reservado":
                                    print(f"Este lugar {Fore.RED}{lugar}{Fore.RESET} já se encontra reservado. Por favor, selecione outro lugar.\n")

                            input("Pressione ENTER para continuar\n")

                        valor_bilhete = 4
                        controller.adicionar_valor_bilheteira(variavel_mes, variavel_dia, valor_bilhete, bilheteira_janeiro_2022, bilheteira_fevereiro_2022, bilheteira_marco_2022,
                            bilheteira_abril_2022,
                            bilheteira_maio_2022, bilheteira_junho_2022, bilheteira_julho_2022, bilheteira_agosto_2022,
                            bilheteira_setembro_2022,
                            bilheteira_outubro_2022, bilheteira_novembro_2022, bilheteira_dezembro_2022)
                   
                        controller.print_palco_evento(dia)
                        controller.adicionar_dict(username, evento, reserva_dia, tipo_bilhete, lugar)
                        print()
                        print(f"O lugar {Fore.GREEN}{lugar}{Fore.RESET} está reservado para si.\n")
                        input("Pressione ENTER para continuar\n")
                        model.menu()

                if controlos == "VIP":
                    tipo_bilhete = controlos
                    lista_reservas.append(tipo_bilhete)
                    variavel_teste = "Não Reservado"

                    while variavel_teste == "Não Reservado":
                        controller.print_palco_evento(dia)
                        print("Selecione o seu lugar\n")
                        lugar = input()

                        if lugar in sala:
                            print("O seu bilhete é VIP por favor selecione um dos lugares assinalados a amarelo.\n")
                        elif lugar not in sala[len(sala) - 1]:
                            print(f"{Fore.RED}Por favor Introduza um lugar válido{Fore.RESET}.\n")
                        else:
                            variavel_teste = controller.criar_reservas_vip(dia, lugar)
                            if variavel_teste == "Não Reservado":
                                print(f"Este lugar {Fore.RED}{lugar}{Fore.RESET} já se encontra reservado. Por favor, selecione outro lugar.\n")

                        input("Pressione ENTER para continuar\n")

                    valor_bilhete = 12
                    controller.adicionar_valor_bilheteira(variavel_mes, variavel_dia, valor_bilhete, bilheteira_janeiro_2022, bilheteira_fevereiro_2022, bilheteira_marco_2022,
                            bilheteira_abril_2022,
                            bilheteira_maio_2022, bilheteira_junho_2022, bilheteira_julho_2022, bilheteira_agosto_2022,
                            bilheteira_setembro_2022,
                            bilheteira_outubro_2022, bilheteira_novembro_2022, bilheteira_dezembro_2022)
                   
                    controller.print_palco_evento(dia)
                    controller.adicionar_dict(username, evento, reserva_dia, tipo_bilhete, lugar)
                    print()  # apenas para aparecer separado, é so estetica
                    print(f"O lugar {Fore.GREEN}{lugar}{Fore.RESET} está reservado para si.\n")
                    input("Pressione ENTER para continuar\n")
                    model.menu()

        # Tiago Sousa
        elif controlos[0] == "Bilheteira":
            print()
            print("Selecione uma opção.\n")
            model.bilheteira_menu_opcao()
            controlos = input()
            verificacao = 0

            if controlos == "Dia":
                print("\nSelecione o mês, a que pertence o dia.\n")
                model.bilheteira_menu_meses()
                controlos1 = input()
                temp_mes = controlos1
                if temp_mes in model.meses:
                    print("Selecione o dia.\n")
                    controlos2 = int(input())
                    temp_dia = controlos2
                    print(temp_mes)
                    if temp_mes == "janeiro" or temp_mes == "março" or temp_mes == "maio" or temp_mes == "julho" or temp_mes == "agosto" or temp_mes == "outobro" or temp_mes == "dezembro":
                        if temp_dia in model.dias_mes_31:
                            verificacao = "OK"
                    elif temp_mes == "abril" or temp_mes == "junho" or temp_mes == "setembro" or temp_mes == "novembro":
                        if temp_dia in model.dias_mes_30:
                            verificacao = "OK"
                    elif temp_mes == "fevereiro":
                        if temp_dia in model.dias_fevereiro:
                            verificacao = "OK"
                    
                    if verificacao == "OK":
                        valor_diario = controller.contar_bilheteira_dia(temp_mes, temp_dia, bilheteira_janeiro_2022,
                                                                bilheteira_fevereiro_2022, bilheteira_marco_2022,
                                                                bilheteira_abril_2022,
                                                                bilheteira_maio_2022, bilheteira_junho_2022,
                                                                bilheteira_julho_2022, bilheteira_agosto_2022,
                                                                bilheteira_setembro_2022,
                                                                bilheteira_outubro_2022, bilheteira_novembro_2022,
                                                                bilheteira_dezembro_2022)
                        print(f"Lucro bilheteira no dia {temp_dia}: {Fore.YELLOW}{valor_diario}{Fore.RESET}\n")
                        controller.funcao_menu()
                    else:
                        print(f"{Fore.RED}Dia não reconhecido, voltando ao menu inicial.{Fore.RESET}")
                        controller.funcao_menu()
                else:
                    print(f"{Fore.RED}Mês não reconhecido, voltando ao menu inicial.{Fore.RESET}")
                    controller.funcao_menu()


            elif controlos == "Ano":
                print()
                print("Selecione o ano 2022 ou o ano 2023.\n")
                controlos2 = input()
                print()
                if controlos2 == "2022":
                    valor_ano = controller.contar_bilheteira_anual(bilheteira_anual_2022)
                    print(f"Lucro bilheteira no Ano de 2022: {Fore.YELLOW}{valor_ano}{Fore.RESET}")
                    controller.funcao_menu

                elif controlos2 == "2023":
                    valor_ano_2023 = controller.contar_bilheteira_anual_2023(bilheteira_anual_2023)
                    print(f"Lucro bilheteira no Ano de 2023: {Fore.YELLOW}{valor_ano_2023}{Fore.RESET}")
                    controller.funcao_menu
                
                else:
                    print(f"{Fore.RED}Instrução não compreendida, voltando ao menu inicial.{Fore.RESET}")

            elif controlos == "Mes":
                print()
                print("Selecione o mês.\n")
                model.bilheteira_menu_meses()
                controlos = input()

                if controlos == "janeiro":
                    print()
                    valor_mes = controller.contar_bilheteira_mes(bilheteira_janeiro_2022)
                    print(f"Lucro bilheteira em Janeiro: {Fore.YELLOW}{valor_mes}{Fore.RESET}")
                    controller.funcao_menu()

                elif controlos == "fevereiro":
                    print()
                    valor_mes = controller.contar_bilheteira_mes(bilheteira_fevereiro_2022)
                    print(f"Lucro bilheteira em Fevereiro: {Fore.YELLOW}{valor_mes}{Fore.RESET}")
                    controller.funcao_menu()

                elif controlos == "março":
                    print()
                    valor_mes = controller.contar_bilheteira_mes(bilheteira_marco_2022)
                    print(f"Lucro bilheteira em Março: {Fore.YELLOW}{valor_mes}{Fore.RESET}")
                    controller.funcao_menu()

                elif controlos == "abril":
                    print()
                    valor_mes = controller.contar_bilheteira_mes(bilheteira_abril_2022)
                    print(f"Lucro bilheteira em Abril: {Fore.YELLOW}{valor_mes}{Fore.RESET}")
                    controller.funcao_menu()

                elif controlos == "maio":
                    print()
                    valor_mes = controller.contar_bilheteira_mes(bilheteira_maio_2022)
                    print(f"Lucro bilheteira em Maio: {Fore.YELLOW}{valor_mes}{Fore.RESET}")
                    controller.funcao_menu()

                elif controlos == "junho":
                    print()
                    valor_mes = controller.contar_bilheteira_mes(bilheteira_junho_2022)
                    print(f"Lucro bilheteira em Junho: {Fore.YELLOW}{valor_mes}{Fore.RESET}")
                    controller.funcao_menu()

                elif controlos == "julho":
                    print()
                    valor_mes = controller.contar_bilheteira_mes(bilheteira_julho_2022)
                    print(f"Lucro bilheteira em Julho: {Fore.YELLOW}{valor_mes}{Fore.RESET}")
                    controller.funcao_menu()

                elif controlos == "agosto":
                    print()
                    valor_mes = controller.contar_bilheteira_mes(bilheteira_agosto_2022)
                    print(f"Lucro bilheteira em Agosto: {Fore.YELLOW}{valor_mes}{Fore.RESET}")
                    controller.funcao_menu()

                elif controlos == "setembro":
                    print()
                    valor_mes = controller.contar_bilheteira_mes(bilheteira_setembro_2022)
                    print(f"Lucro bilheteira em Setembro: {Fore.YELLOW}{valor_mes}{Fore.RESET}")
                    controller.funcao_menu()

                elif controlos == "outubro":
                    print()
                    valor_mes = controller.contar_bilheteira_mes(bilheteira_outubro_2022)
                    print(f"Lucro bilheteira em Outubro: {Fore.YELLOW}{valor_mes}{Fore.RESET}")
                    controller.funcao_menu()

                elif controlos == "novembro":
                    print()
                    valor_mes = controller.contar_bilheteira_mes(bilheteira_novembro_2022)
                    print(f"Lucro bilheteira em Novembro: {Fore.YELLOW}{valor_mes}{Fore.RESET}")
                    controller.funcao_menu()

                elif controlos == "dezembro":
                    print()
                    valor_mes = controller.contar_bilheteira_mes(bilheteira_dezembro_2022)
                    print(f"Lucro bilheteira em Dezembro: {Fore.YELLOW}{valor_mes}{Fore.RESET}")
                    controller.funcao_menu()
                
                else:
                    print(f"{Fore.RED}Instrução não compreendida, voltando ao menu inicial.{Fore.RESET}")

        elif controlos[0] == "Reservas":
            print()
            print("Selecione uma opção.")
            print()
            model.reservas_menu()
            controlos = input().split(" ")

            if controlos[0] == "Consultar":
                print()
                print(f"Insira o seu Username e Password")
                controlos = input().split(" ")
                print()
                
                verificar_user_reserva = controller.verificar_username(lista_clientes_registados, controlos)
                if verificar_user_reserva == False:
                    print()
                    print(f"{Fore.RED}Não existe registo efetuado com o username selecionado.{Fore.RESET}\n")
                    print(f"Para fazer {Fore.YELLOW}LOGIN{Fore.RED}, introduza o seu Username e Password.\n")
                    print(f"Para voltar para o menu principal, digite {Fore.YELLOW}Menu{Fore.RESET}")
                    controlos = input().split(" ")

                    if controlos[0] == "Menu":
                        print()
                        controller.funcao_menu()

                else:
                    if verificar_user_reserva == True:
                        controller.consultar_reserva(controlos)
                        print()
                        controller.funcao_menu()
            
            elif controlos[0] == "Alterar":
                print()
                print(f"Insira o seu Username e Password")
                controlos = input().split(" ")
                print()

                verificar_user_reserva = controller.verificar_username(lista_clientes_registados, controlos)
                if verificar_user_reserva == False:
                    print()
                    print(f"{Fore.RED}Não existe registo efetuado com o username selecionado.{Fore.RESET}\n")
                    print(f"Para fazer {Fore.YELLOW}LOGIN{Fore.RED}, introduza o seu Username e Password.\n")
                    print(f"Para voltar para o menu principal, digite {Fore.YELLOW}Menu{Fore.RESET}")
                    controlos = input().split(" ")

                    if controlos[0] == "Menu":
                        print()
                        controller.funcao_menu()

                else:
                    if verificar_user_reserva == True:
                        reservas_referentes_utilizador = controller.alterar_eliminar_reserva(controlos)
                        if len(reservas_referentes_utilizador) == 0:
                            print("Você não tem nenhuma reserva efetuada, voltando para o MENU")
                            controller.funcao_menu()
                        else:
                            controlos = int(input("Introduza o número referente à reserva que deseja alterar:\n"))
                            if 0 < controlos and controlos <= len(reservas_referentes_utilizador):
                                reserva_selecionada = reservas_referentes_utilizador[controlos - 1]
                                tipo_bilhete = reservas_referentes_utilizador[controlos - 1].get("Bilhete")
                                dia = reservas_referentes_utilizador[controlos - 1].get("Dia do evento")
                                lugar_antigo = reservas_referentes_utilizador[controlos - 1].get("Lugar")

                                if len(dia) == 8:
                                    variavel_dia = int(controller.guardar_dia_1digito(dia))
                                    variavel_mes = int(controller.guardar_mes_1digito(dia))

                                elif len(dia) == 9:
                                    variavel_teste = controller.guardar_dia_2digitos(dia)
                                
                                    if "/" in variavel_teste:
                                        variavel_dia = int(controller.guardar_dia_1digito(variavel_teste))
                                        variavel_mes = int(controller.guardar_mes_9elementos_2digitos(dia))

                                    else:
                                        variavel_dia = int(controller.guardar_dia_2digitos(dia))
                                        variavel_mes = int(controller.guardar_mes_9elementos(dia))

                                elif len(dia) == 10:
                                    variavel_dia = int(controller.guardar_dia_2digitos(dia))
                                    variavel_mes = int(controller.guardar_mes_2digitos(dia))

                                controller.print_palco_evento(dia)

                                if tipo_bilhete == "Normal":
                                    variavel_teste = "Não Reservado"

                                    while variavel_teste == "Não Reservado":
                                        controller.print_palco_evento(dia)
                                        print("Selecione o seu lugar\n")
                                        lugar_novo = input()

                                        if lugar_novo == "A6" or lugar_novo == "A7" or lugar_novo == "A8" or lugar_novo == "A9" or lugar_novo == "F6" or lugar_novo == "F7" or lugar_novo == "F8" or lugar_novo == "F9":
                                            print("O lugar introduzido pertence a um lugar VIP e o seu lugar é Normal, se pretende alterar para um lugar VIP, será lhe retirado 8 euros da sua conta.\n")
                                            controlos = input("S para alterar, N para continuar\n(S \ N)\n")
                                            if controlos == "S":
                                                variavel_teste = controller.alterar_reservas_normal_vip(dia, lugar_novo, lugar_antigo)
                                                if variavel_teste == "Reservado":
                                                    valor_bilhete = 8
                                                    tipo_bilhete = "VIP"
                                                    controller.adicionar_valor_bilheteira(variavel_mes, variavel_dia, valor_bilhete, bilheteira_janeiro_2022, bilheteira_fevereiro_2022, bilheteira_marco_2022,
                                                            bilheteira_abril_2022,
                                                            bilheteira_maio_2022, bilheteira_junho_2022, bilheteira_julho_2022, bilheteira_agosto_2022,
                                                            bilheteira_setembro_2022,
                                                            bilheteira_outubro_2022, bilheteira_novembro_2022, bilheteira_dezembro_2022)
                                                else: 
                                                    print(f"Este lugar {lugar_novo} já se encontra reservado. Por favor, selecione outro lugar.\n")
                                        elif lugar_novo not in sala:
                                            print("Porfavor Introduza um lugar válido\n")
                                        else:
                                            variavel_teste = controller.alterar_reservas_normal_normal(dia, lugar_novo, lugar_antigo)
                                            if variavel_teste == "Não Reservado":
                                                print(f"Este lugar {lugar_novo} já se encontra reservado. Por favor, selecione outro lugar.\n")

                                        input("Pressione ENTER para continuar\n")

                                if tipo_bilhete == "VIP":
                                    variavel_teste = "Não Reservado"

                                    while variavel_teste == "Não Reservado":
                                        controller.print_palco_evento(dia)
                                        print("Selecione o seu lugar\n")
                                        lugar_novo = input()

                                        if lugar_novo in sala:
                                            print("O lugar introduzido pertence a um lugar Normal e o seu lugar é VIP, se pretende alterar para um lugar Normal, será lhe devolvido 8 euros para a sua conta.\n")
                                            controlos = input("S para alterar, N para continuar.\n(S \ N)\n")
                                            if controlos == "S":
                                                variavel_teste = controller.alterar_reservas_vip_normal(dia, lugar_novo, lugar_antigo)
                                                if variavel_teste == "Reservado":
                                                    valor_bilhete = -8
                                                    tipo_bilhete = "Normal"
                                                    controller.adicionar_valor_bilheteira(variavel_mes, variavel_dia, valor_bilhete, bilheteira_janeiro_2022, bilheteira_fevereiro_2022, bilheteira_marco_2022,
                                                            bilheteira_abril_2022,
                                                            bilheteira_maio_2022, bilheteira_junho_2022, bilheteira_julho_2022, bilheteira_agosto_2022,
                                                            bilheteira_setembro_2022,
                                                            bilheteira_outubro_2022, bilheteira_novembro_2022, bilheteira_dezembro_2022)
                                                else:
                                                    print(f"Este lugar {lugar_novo} já se encontra reservado. Por favor, selecione outro lugar.\n")
                                        elif lugar_novo not in sala[len(sala) - 1]:
                                            print("Por favor Introduza um lugar válido\n")
                                        else:
                                            variavel_teste = controller.alterar_reservas_vip_vip(dia, lugar_novo, lugar_antigo)
                                            if variavel_teste == "Não Reservado":
                                                print(f"Este lugar {lugar_novo} já se encontra reservado. Por favor, selecione outro lugar.\n")

                                        input("Pressione ENTER para continuar\n")
                                    
                                controller.print_palco_evento(dia)
                                controller.eliminar_antiga_adicionar_nova_reserva(reserva_selecionada, lugar_novo, tipo_bilhete)
                                print("Alteração Efetuada com sucesso!\n")
                                model.menu()

                            else:
                                print(f"{Fore.RED}Instrução não compreendida, voltando ao menu inicial.{Fore.RESET}")
                                controller.funcao_menu


            elif controlos[0] == "Eliminar":
                print()
                print(f"Insira o seu Username e Password")
                controlos = input().split(" ")
                print()

                verificar_user_reserva = controller.verificar_username(lista_clientes_registados, controlos)
                if verificar_user_reserva == False:
                    print()
                    print(f"{Fore.RED}Não existe registo efetuado com o username selecionado.{Fore.RESET}\n")
                    print(f"Para fazer {Fore.YELLOW}LOGIN{Fore.RED}, introduza o seu Username e Password.\n")
                    print(f"Para voltar para o menu principal, digite {Fore.YELLOW}Menu{Fore.RESET}")
                    controlos = input().split(" ")

                    if controlos[0] == "Menu":
                        print()
                        controller.funcao_menu()

                else:
                    if verificar_user_reserva == True:
                        reservas_referentes_utilizador = controller.alterar_eliminar_reserva(controlos)
                        if len(reservas_referentes_utilizador) == 0:
                            print("Você não tem nenhuma reserva efetuada, voltando para o MENU")
                            controller.funcao_menu()
                        else:
                            controlos = int(input(f"Introduza o número referente à reserva que deseja {Fore.RED}ELIMINAR:{Fore.RESET}\n"))
                            if 0 < controlos and controlos <= len(reservas_referentes_utilizador):
                                reserva_selecionada = reservas_referentes_utilizador[controlos - 1]
                                tipo_bilhete = reservas_referentes_utilizador[controlos - 1].get("Bilhete")
                                dia = reservas_referentes_utilizador[controlos - 1].get("Dia do evento")

                                decisao = input((f"\nTem a certeza que deseja apagar a reserva selecionada?\nS para Sim, N para Não\n(S \ N)\n"))
                                if decisao == "S":
                                    controller.eliminar_reserva(reserva_selecionada)
                                    if tipo_bilhete == "Normal":
                                        valor_bilhete = -4
                                    else:
                                        valor_bilhete = -12

                                    if len(dia) == 8:
                                        variavel_dia = int(controller.guardar_dia_1digito(dia))
                                        variavel_mes = int(controller.guardar_mes_1digito(dia))

                                    elif len(dia) == 9:
                                        variavel_teste = controller.guardar_dia_2digitos(dia)
                                    
                                        if "/" in variavel_teste:
                                            variavel_dia = int(controller.guardar_dia_1digito(variavel_teste))
                                            variavel_mes = int(controller.guardar_mes_9elementos_2digitos(dia))

                                        else:
                                            variavel_dia = int(controller.guardar_dia_2digitos(dia))
                                            variavel_mes = int(controller.guardar_mes_9elementos(dia))

                                    elif len(dia) == 10:
                                        variavel_dia = int(controller.guardar_dia_2digitos(dia))
                                        variavel_mes = int(controller.guardar_mes_2digitos(dia))

                                    controller.adicionar_valor_bilheteira(variavel_mes, variavel_dia, valor_bilhete, bilheteira_janeiro_2022, bilheteira_fevereiro_2022, bilheteira_marco_2022,
                                                            bilheteira_abril_2022,
                                                            bilheteira_maio_2022, bilheteira_junho_2022, bilheteira_julho_2022, bilheteira_agosto_2022,
                                                            bilheteira_setembro_2022,
                                                            bilheteira_outubro_2022, bilheteira_novembro_2022, bilheteira_dezembro_2022)

                                    print("A sua reserva foi eliminada com sucesso.")
                                    controller.funcao_menu()
                                elif decisao == "N":
                                    print("Voltando para o MENU")
                                    controller.funcao_menu()
                                else:
                                    print("Instrução não compreendida voltando para o MENU")
                                    controller.funcao_menu()
                            else:
                                print(f"{Fore.RED}Instrução não compreendida, voltando ao menu inicial.{Fore.RESET}")
                                controller.funcao_menu()

        elif controlos[0] == "Eliminar_Evento":                    
            if model.admin_logado == False:
                print("Apenas o administrador pode aceder aqui!")
            else:
                print("Selecione o Evento que pretende alterar para eliminar")
                model.cartaz_eventos()
                controlos = input()
                if controlos == "Brodway":
                    print("Selecione o dia que pretende eliminar")
                    #adicionar dia
                    dia = input()

                    '\n'.join(map(str, model.dias_musical))
