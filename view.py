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

lista_lugares_reservados = []

#Tiago e Rodrigo:
lista_todas_reservas = []

menu_sala_espetaculos = ["Eventos", "Bilheteira", "Reservas", "SignIn/SignUp"]

cartaz_espetaculos = [
    {"evento_1": "Brodway", "dia": 20, "mês": 1, "ano": 2022},
    {"evento_2": "Circo", "dia": 12, "mês": 2, "ano": 2022},
    {"evento_3": "Musical", "dia": 6, "mês": 3, "ano": 2022},
    {"evento_4": "Opera", "dia": 22, "mês": 4, "ano": 2022}
    ]
cartaz_espetaculos_user = [
    "Brodway", 
    "Circo", 
    "Musical", 
    "Opera"
    ]

dias_brodway = ["1", "Brodway_20/1/2022"]
dias_circo = ["1", "- 12/2/2022n\n"]
dias_musical = ["1", "- 6/3/2022\n", "2", "- 22/4/2022\n"]
dias_opera = []

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
                print(f"Escolha o dia, que pretende assitir ao evento.\n{dias_brodway}" )
                controlos = input()

                if controlos == "1": 
                    dia = dias_brodway[1]

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


        elif controlos[0] == "Reservas":
            print() #apenas para aparecer separado, é so estetica
            print("Selecione uma opção.")
            print() #apenas para aparecer separado, é so estetica
            print('\n'.join(map(str, reserva_opcoes)))


            
