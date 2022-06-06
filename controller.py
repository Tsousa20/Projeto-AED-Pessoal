from pickle import FALSE
import view
import model
import colorama
from colorama import Fore


#Tiago e Rodrigo: funçao para criar listas para o diferentes espetaculos com as diferentes salas
def criar_reservas_normal(x, y): #x = evento_dia / y = lugar
    if len(view.lista_lugares_reservados) == 0:
        #lista normal
        temp = view.sala
        temp.insert(0, x)
        temp.remove(y)
        view.lista_lugares_reservados.append(temp)

        #lista para print
        temp = model.lugares_print
        temp.insert(0, x)
        reserva_print_lugares(temp, y)
        return "Reservado"

    else:
        for i in range(len(view.lista_lugares_reservados)):
            if view.lista_lugares_reservados[i][0] == x:
                if y in view.lista_lugares_reservados[i]:
                    view.lista_lugares_reservados[i].remove(y)
                    reserva_print_lugares(view.lista_todos_eventos_print[i], y)
                    return "Reservado"
                else:
                    return "Não reservado"
            else:
                temp = view.sala
                temp.insert(0, x)
                temp.remove(y)
                view.lista_lugares_reservados.append(temp)

                #lista para print
                temp = model.lugares_print
                temp.insert(0, x)
                reserva_print_lugares(temp, y)
                return "Reservado"
                
#def criar_reservas_vip(x, y):

#Criar a lista com o lugar MARCADO quando reservado ou apenas colocar o lugar MARCADO 
def reserva_print_lugares(x, y): #x = evento_dia / y = lugar
    for i in range(len(view.sala_para_print)):
        if y == view.sala_para_print[i]:
            x.insert(i, Fore.RED + x.pop(i) + Fore.RESET)
    view.lista_todos_eventos_print.append(x)
    return None

#Print do palco adequado ao evento selecionado
def print_palco_evento(evento):
    for i in range(len(view.lista_todos_eventos_print)):
        if evento == view.lista_todos_eventos_print[i][0]:
            model.palco_reserva_default(view.lista_todos_eventos_print[i])
            return None
    

                   
def contar_bilheteira_mes(x):
    valor = 0
    for i in x:
        valor += i
    return valor

def contar_bilheteira_anual(x):
    valor = 0
    for i in x:
        sum = 0
        for j in i:
            sum += j
        valor += sum
    return valor

def contar_bilheteira_dia(x, y, bilheteira_janeiro_2022, bilheteira_fevereiro_2022, bilheteira_março_2022, bilheteira_abril_2022,
bilheteira_maio_2022, bilheteira_junho_2022, bilheteira_julho_2022, bilheteira_agosto_2022, bilheteira_setembro_2022,
bilheteira_outubro_2022, bilheteira_novembro_2022, bilheteira_dezembro_2022):
    if x == "Janeiro":
        i = y - 1
        valor = bilheteira_janeiro_2022[i]
        print(f"valor dia: {valor}")
        return valor
    elif x == "Fevereiro":
        i = y - 1
        valor = bilheteira_fevereiro_2022[i]
        print(f"valor dia: {valor}")
        return valor
    elif x == "Março":
        i = y - 1
        valor = bilheteira_março_2022[i]
        print(f"valor dia: {valor}")
        return valor
    elif x == "Abril":
        i = y - 1
        valor = bilheteira_abril_2022[i]
        print(f"valor dia: {valor}")
        return valor
    elif x == "Maio":
        i = y - 1
        valor = bilheteira_maio_2022[i]
        print(f"valor dia: {valor}")
        return valor
    elif x == "Junho":
        i = y - 1
        valor = bilheteira_junho_2022[i]
        print(f"valor dia: {valor}")
        return valor
    elif x == "Julho":
        i = y - 1
        valor = bilheteira_julho_2022[i]
        print(f"valor dia: {valor}")
        return valor
    elif x == "Agosto":
        i = y - 1
        valor = bilheteira_agosto_2022[i]
        print(f"valor dia: {valor}")
        return valor
    elif x == "Setembro":
        i = y - 1
        valor = bilheteira_setembro_2022[i]
        print(f"valor dia: {valor}")
        return valor
    elif x == "Outubro":
        i = y - 1
        valor = bilheteira_outubro_2022[i]
        print(f"valor dia: {valor}")
        return valor
    elif x == "Novembro":
        i = y - 1
        valor = bilheteira_novembro_2022[i]
        print(f"valor dia: {valor}")
        return valor
    elif x == "Dezembro":
        i = y - 1
        valor = bilheteira_dezembro_2022[i]
        print(f"valor dia: {valor}")
        return valor






#Tiago Sousa: funçao para guardar a data do dia escolhido, usar essa data para adicionar
#o valor a bilheteira 
def guardar_dia_1digito(controlos):
    return controlos[:1]

def guardar_dia_2digitos(controlos):
    print(type(controlos[:2]))
    return controlos[:2]
    
def funcao_menu(menu_sala_espetaculos):
    input("Pressione ENTER para continuar\n")
    print('\n'.join(map(str, menu_sala_espetaculos)))

#Tiago Lança

def verificar_cliente(lista_clientes_registados, lista_usernames, controlos):
    nome = controlos[0]
    username = controlos[1]
    password = controlos[2]
    cliente = {'Nome': nome, 'Username': username, 'Password': password}
    temp = False
    if username in lista_usernames:
        temp = True
    else:
        lista_usernames.append(username)
        lista_clientes_registados.append(cliente)
    return temp

def verificar_username(lista_clientes_registados, controlos):
    username = controlos[0]
    password = controlos[1]
    verificacao = False
    for cliente in lista_clientes_registados:
        if username == cliente.get('Username') and password == cliente.get('Password'):
            verificacao = True
    return verificacao

