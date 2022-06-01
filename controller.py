import view
import model
import colorama
from colorama import Fore


def criar_lista():
    lista = []
    return lista


def verificar_cliente(lista_clientes_registados, username):
    for x in lista_clientes_registados:
        if x[1] == username:
            return True
    return False


def registar_clientes(lista_clientes_registados, nome, username, password):
    cliente = [nome, username, password]
    lista_clientes_registados.append(cliente)


def verificacao_username(lista_clientes_registados, lista_usernames, username):
    x = username
    for x in lista_clientes_registados:
        if x[1] in lista_clientes_registados:
            lista_usernames.append(x)
            return username


def login_cliente(lista_username,username, password):
    for x in lista_username:
        if x in lista_username:
            login =[username, password]
            return login

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

#Tiago Sousa: funçao para guardar a data do dia escolhido, usar essa data para adicionar
#o valor a bilheteira 
def guardar_dia_1digito(controlos):
    return controlos[:1]

def guardar_dia_2digitos(controlos):
    return controlos[:2]
