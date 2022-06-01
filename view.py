import controller
import model
from models.linkedlist import LinkedList

#sala default usado para todas as salas dos eventos, copiada.
sala = ["k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8", "k9", "k10", "k11", "k12", "k13" "k14", "j1", "j2", "j3", "j4", "j5", "j6", "j7", "j8", "j9", "j10", "j11", "j12", "j13", "j14"
"i1", "i2", "i3", "i4", "i5", "i6", "i7", "i8", "i9", "i10", "i11", "i12", "i13", "i14",
"h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "h11", "h12", "h13", "h14",
"g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9", "g10", "g11", "g12", "g13", "g14",
"f1", "f2", "f13", "f14",
"e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "e9","e10", "e11", "e12", "e13", "e14",
"d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "d11", "d12", "d13", "d14",
"c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13", "c14",
"b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9", "b10", "b11","b12", "b13", "b14",
"a1", "a2", "a13", "a14", ["a6", "a7", "a8", "a9", "f6", "f7", "f8", "f9"]]

#Tiago Sousa: listas para bilheteiras
bilheteira_janeiro_2022 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #31
bilheteira_fevereiro_2022 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_março_2022 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_abril_2022 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_maio_2022 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_junho_2022 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_julho_2022 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_agosto_2022 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_setembro_2022 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_outubro_2022 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_novembro_2022 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bilheteira_dezembro_2022 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

bilheteira_anual_2022 = [bilheteira_janeiro_2022, bilheteira_fevereiro_2022, bilheteira_março_2022, bilheteira_abril_2022,
bilheteira_maio_2022, bilheteira_junho_2022, bilheteira_julho_2022, bilheteira_agosto_2022, bilheteira_setembro_2022,
bilheteira_outubro_2022, bilheteira_novembro_2022, bilheteira_dezembro_2022]

bilheteira_menu_opcoes = ["Dia", "Mes", "Ano"]
bilheteira_menu_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", 
"Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

#Tiago e Rodrigo:
lista_todas_reservas = []
lista_lugares_reservados = []

menu_sala_espetaculos = ["Eventos", "Bilheteira", "Reservas", "SignIn/SignUp"]

cartaz_espetaculos = [
    {"evento_1": "Brodway", "dia": 20, "mês": 1, "ano": 2022},
    {"evento_2": "Circo", "dia": 12, "mês": 2, "ano": 2022},
    {"evento_3": "Musical", "dia": 6, "mês": 3, "ano": 2022},
    {"evento_4": "Opera", "dia": 22, "mês": 4, "ano": 2022},
    {"evento_5": "Teatro", "dia": 14, "mês": 11, "ano": 2022}
    ]
cartaz_espetaculos_user = [
    "Brodway", 
    "Circo", 
    "Musical", 
    "Opera",
    "Teatro"
    ]

dias_brodway = ["3/1/2022", "23/1/2022\n", "3/2/2022", "23/2/2022\n", "3/3/2022", "23/3/2022\n", "3/4/2022", "23/4/2022\n",
"3/5/2022", "23/5/2022\n", "3/6/2022", "23/6/2022\n", "3/7/2022", "23/7/2022\n", "3/9/2022", "23/9/2022\n", "3/10/2022",
"23/10/2022\n", "3/11/2022", "23/11/2022\n", "3/12/2022", "23/12/2022\n"]
dias_musical = ["15/1/2022\n", "6/2/2022\n", "6/3/2022\n", "22/4/2022\n", "17/6/2022\n", "20/7/2022\n", "5/9/2022\n", 
"29/10/2022\n", "4/11/2022\n", "21/12/2022\n"]
dias_opera = ["4/1/2022\n", "22/3/2022\n", "11/6/2022\n", "5/9/2022\n", "9/12/2022\n"]
dias_circo = ["4/1/2022\n", "6/6/2022\n", "12/2/2022\n"]
dias_teatro = ["22/9/2022"]


lista_clientes_registados = controller.criar_lista
lista_usernames = controller.criar_lista

#Tiago Sousa: lista para usar no menu reservas
reserva_opcoes = ["Consultar reserva", "Eliminar reserva", "Alterar reserva"]


def main():

    
    while True:
        try:
            controlos = input().split(" ")
        except EOFError:
            return

        if controlos[0] == "Registar":
            if controller.verificar_cliente(lista_clientes_registados,controlos[2]):
                print("Já existe alguem registado com o username escolhido.")
            else:
                controller.registar_clientes(lista_clientes_registados, controlos[1], controlos[2], controlos[3])
                print("Registo efetuado com sucesso")

        

        elif controlos[0] == "START":
            print() #apenas para aparecer separado, é so estetica
            print("Bem vindo à sala de espetáculos!\nEscolha uma opção.")
            print() #apenas para aparecer separado, é so estetica
            print('\n'.join(map(str, menu_sala_espetaculos)))

        elif controlos[0] == "Eventos":
            print() #apenas para aparecer separado, é so estetica
            print("Por favor, escolha um evento!\n")
            
            print('\n'.join(map(str, cartaz_espetaculos_user)))
            controlos = input()
            dia = "NÃO EXISTE"
            
            #EVENTOS BRODWAY
            if controlos == "Brodway":
                evento = controlos
                print() #apenas para aparecer separado, é so estetica
                print(f"Escolha o dia, que pretende assitir ao evento {evento}.\n" )
                print('\n'.join(map(str, dias_brodway)))
                
                controlos = input()

                if controlos in dias_brodway:
                    dia = dias_brodway[1]

                    if len(controlos) == 8:
                        variavel_dia = int(controller.guardar_dia_1digito(controlos))
                        
                    elif len(controlos) == 9:
                        variavel_dia = int(controller.guardar_dia_2digitos(controlos))
                        
                    elif len(controlos) == 10:
                        variavel_dia = int(controller.guardar_dia_2digitos(controlos))
                        
                
                else:
                    print("Instrução não compreendida!")
            
                if dia != 0:
                    print("Que tipo de bilhete pretende?\n")
                    print(model.tabela_precos())
                    controlos = input()

                
                if controlos == "Normal":
                    print(model.palco_default())
                    print("Selecione o seu lugar")
                    controlos = input()
                    
                    #Tiago Sousa
                    lugar = controlos
                    variavel_teste = controller.criar_reservas_normal(dia, lugar)
                    while variavel_teste == "Não reservado":
                        print(f"Este lugar {lugar} já se encontra reservado. Por favor, selecione outro lugar.\n")
                        input("Pressione ENTER para continuar\n")
                        print(model.palco_default())
                        print("Selecione o seu lugar\n")
                        
                        lugar = input()
                        variavel_teste = controller.criar_reservas_normal(dia, lugar)
                        
                    valor_bilhete = 4
                    bilheteira_janeiro_2022.insert(variavel_dia, valor_bilhete)
                    print() #apenas para aparecer separado, é so estetica
                    print(f"O lugar {lugar} está reservado para si.\n")
                    
                    input("Pressione ENTER para continuar\n")
                    print('\n'.join(map(str, menu_sala_espetaculos)))
                    
                        


            #EVENTOS CIRCO
            if controlos == "Circo":
                print(f"Escolha o dia, que pretende assitir ao evento.\n{dias_circo}" )
                controlos = input()

                if controlos == "1": #and registado
                    dia = dias_circo[1]

                #elif registado and controlos != 1
                else:
                    print("Instrução não compreendida!")
            
                if dia != 0:
                    print("Que tipo de bilhete pretende?\n")
                    print(model.tabela_precos())
                    controlos = input()
            
                if controlos == "Normal":
                    print(model.palco_default())
                    print("Selecione o seu lugar")
                    controlos = input()
                
                  

                

            #EVENTOS MUSICAL
            if controlos == "Musical":
                print(f"Escolha o dia, que pretende assitir ao evento.\n{dias_musical}" )
                controlos = input()

                if controlos == "1": #and registado
                    dia = dias_musical[1]
                if controlos == "2": #and registado
                    dia = dias_musical[3]

                #elif registado and controlos != 1 and controlos != 2::
                else:
                    print("Instrução não compreendida!")
            
                if dia != 0:
                    print("Que tipo de bilhete pretende?\n")
                    print(model.tabela_precos())
                    controlos = input()
            
                if controlos == "Normal":
                    print(model.palco_default())
                    print("Selecione o seu lugar")
                    controlos = input()

            #EVENTOS OPERA
            if controlos == "Opera":
                print("De momento não existe registo de um espetaculo de Opera.")

        #Tiago Sousa
        elif controlos[0] == "Bilheteira":
            print() #apenas para aparecer separado, é so estetica
            print("Selecione uma opção.\n")
            print('\n'.join(map(str, bilheteira_menu_opcoes)))
            controlos = input()

            if controlos == "Dia":
                print("Ainda não está a funcionar")
            elif controlos == "Ano":
                print() #apenas para aparecer separado, é so estetica
                valor_ano = controller.contar_bilheteira_anual(bilheteira_anual_2022)
                print(f"Lucro bilheteira no Ano de 2022: {valor_ano}")

            elif controlos == "Mes":
                print() #apenas para aparecer separado, é so estetica
                print("Selecione o mês.\n")
                print('\n'.join(map(str, bilheteira_menu_meses)))
                controlos = input()

                if controlos == "Janeiro":
                    print() #apenas para aparecer separado, é so estetica
                    valor_mes = controller.contar_bilheteira_mes(bilheteira_janeiro_2022)
                    print(f"Lucro bilheteira em Janeiro: {valor_mes}")

                elif controlos == "Fevereiro":
                    print() #apenas para aparecer separado, é so estetica
                    valor_mes = controller.contar_bilheteira_mes(bilheteira_fevereiro_2022)
                    print(f"Lucro bilheteira em Fevereiro: {valor_mes}")

                elif controlos == "Março":
                    print() #apenas para aparecer separado, é so estetica
                    valor_mes = controller.contar_bilheteira_mes(bilheteira_março_2022)
                    print(f"Lucro bilheteira em Março: {valor_mes}")

                elif controlos == "Abril":
                    print() #apenas para aparecer separado, é so estetica
                    valor_mes= controller.contar_bilheteira_mes(bilheteira_abril_2022)
                    print(f"Lucro bilheteira em Abril: {valor_mes}")

                elif controlos == "Maio":
                    print() #apenas para aparecer separado, é so estetica
                    valor_mes = controller.contar_bilheteira_mes(bilheteira_maio_2022)
                    print(f"Lucro bilheteira em Maio: {valor_mes}")

                elif controlos == "Junho":
                    print() #apenas para aparecer separado, é so estetica
                    valor_mes = controller.contar_bilheteira_mes(bilheteira_junho_2022)
                    print(f"Lucro bilheteira em Junho: {valor_mes}")

                elif controlos == "Julho":
                    print() #apenas para aparecer separado, é so estetica
                    valor_mes = controller.contar_bilheteira_mes(bilheteira_julho_2022)
                    print(f"Lucro bilheteira em Julho: {valor_mes}")

                elif controlos == "Agosto":
                    print() #apenas para aparecer separado, é so estetica
                    valor_mes = controller.contar_bilheteira_mes(bilheteira_agosto_2022)
                    print(f"Lucro bilheteira em Agosto: {valor_mes}")

                elif controlos == "Setembro":
                    print() #apenas para aparecer separado, é so estetica
                    valor_mes = controller.contar_bilheteira_mes(bilheteira_setembro_2022)
                    print(f"Lucro bilheteira em Setembro: {valor_mes}")

                elif controlos == "Outubro":
                    print() #apenas para aparecer separado, é so estetica
                    valor_mes = controller.contar_bilheteira_mes(bilheteira_outubro_2022)
                    print(f"Lucro bilheteira em Outubro: {valor_mes}")

                elif controlos == "Novembro":
                    print() #apenas para aparecer separado, é so estetica
                    valor_mes = controller.contar_bilheteira_mes(bilheteira_novembro_2022)
                    print(f"Lucro bilheteira em Novembro: {valor_mes}")

                elif controlos == "Dezembro":
                    print() #apenas para aparecer separado, é so estetica
                    valor_mes = controller.contar_bilheteira_mes(bilheteira_dezembro_2022)
                    print(f"Lucro bilheteira em Dezembro: {valor_mes}")





        elif controlos[0] == "Reservas":
            print() #apenas para aparecer separado, é so estetica
            print("Selecione uma opção.")
            print() #apenas para aparecer separado, é so estetica
            print('\n'.join(map(str, reserva_opcoes)))


            
