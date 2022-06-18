import pickle
from sre_constants import JUMP
import view
import model
import colorama
from colorama import Fore


# Funçao para criar listas para o diferentes espetaculos com as diferentes salas
def criar_reservas_normal(x, y):  # x = evento_dia / y = lugar
    if len(view.lista_lugares_reservados) == 0:
        # lista normal
        temp = view.sala.copy()
        temp.insert(0, x)
        temp.remove(y)
        view.lista_lugares_reservados.append(temp)

        # lista para print
        temp = model.lugares_print.copy()
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
                    return "Não Reservado"

        #Lista normal
        temp = view.sala.copy()
        temp.insert(0, x)
        temp.remove(y)
        view.lista_lugares_reservados.append(temp)

        # lista para print
        temp = model.lugares_print.copy()
        temp.insert(0, x)
        reserva_print_lugares(temp, y)
        return "Reservado"


def criar_reservas_vip(x, y):
    if len(view.lista_lugares_reservados) == 0:
        # lista normal
        temp = view.sala.copy()
        temp.insert(0, x)
        temp[len(temp) - 1].remove(y)
        view.lista_lugares_reservados.append(temp)

        # lista para print
        temp = model.lugares_print.copy()
        temp.insert(0, x)
        reserva_print_lugares(temp, y)
        return "Reservado"

    else:
        for i in range(len(view.lista_lugares_reservados)):
            if view.lista_lugares_reservados[i][0] == x:
                if y in view.lista_lugares_reservados[i][len(view.lista_lugares_reservados[i]) - 1]:
                    view.lista_lugares_reservados[i][len(view.lista_lugares_reservados[i]) - 1].remove(y)
                    reserva_print_lugares(view.lista_todos_eventos_print[i], y)
                    return "Reservado"
                else:
                    return "Não Reservado"

        #Lista normal
        temp = view.sala.copy()
        temp.insert(0, x)
        temp[len(temp) - 1].remove(y)
        view.lista_lugares_reservados.append(temp)

        # lista para print
        temp = model.lugares_print.copy()
        temp.insert(0, x)
        reserva_print_lugares(temp, y)
        return "Reservado"


# Criar a lista com o lugar MARCADO quando reservado ou apenas colocar o lugar MARCADO
def reserva_print_lugares(x, y):  # x = evento_dia / y = lugar
    for i in range(len(model.sala_para_print)):
        if y == model.sala_para_print[i]:
            x.pop(i)
            x.insert(i, Fore.RED + model.lugares_print_copy[i - 1] + Fore.RESET)

    for i in range(len(view.lista_todos_eventos_print)):
        if x[0] in view.lista_todos_eventos_print[i][0]:
            return None
    view.lista_todos_eventos_print.append(x)
    return None


# Print do palco adequado ao evento selecionado
def print_palco_evento(evento):
    palco = "Não Existe"
    for i in range(len(view.lista_todos_eventos_print)):
        if evento == view.lista_todos_eventos_print[i][0]:
            model.palco_reserva_default(view.lista_todos_eventos_print[i])
            palco = "Existe"
    if palco == "Não Existe":
        model.palco_default()
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

def contar_bilheteira_anual_2023(x):
    valor = 0
    for i in x:
        sum = 0
        for j in i:
            sum += j
        valor += sum
    return valor

def contar_bilheteira_dia(x, y, bilheteira_janeiro_2022, bilheteira_fevereiro_2022, bilheteira_marco_2022,
                          bilheteira_abril_2022,
                          bilheteira_maio_2022, bilheteira_junho_2022, bilheteira_julho_2022, bilheteira_agosto_2022,
                          bilheteira_setembro_2022,
                          bilheteira_outubro_2022, bilheteira_novembro_2022, bilheteira_dezembro_2022):
    if x == "janeiro":
        i = y - 1
        valor = bilheteira_janeiro_2022[i]
        return valor
    elif x == "fevereiro":
        i = y - 1
        valor = bilheteira_fevereiro_2022[i]
        return valor
    elif x == "março":
        i = y - 1
        valor = bilheteira_marco_2022[i]
        return valor
    elif x == "abril":
        i = y - 1
        valor = bilheteira_abril_2022[i]
        return valor
    elif x == "maio":
        i = y - 1
        valor = bilheteira_maio_2022[i]
        return valor
    elif x == "junho":
        i = y - 1
        valor = bilheteira_junho_2022[i]
        return valor
    elif x == "julho":
        i = y - 1
        valor = bilheteira_julho_2022[i]
        return valor
    elif x == "agosto":
        i = y - 1
        valor = bilheteira_agosto_2022[i]
        return valor
    elif x == "setembro":
        i = y - 1
        valor = bilheteira_setembro_2022[i]
        return valor
    elif x == "outubro":
        i = y - 1
        valor = bilheteira_outubro_2022[i]
        return valor
    elif x == "novembro":
        i = y - 1
        valor = bilheteira_novembro_2022[i]
        return valor
    elif x == "dezembro":
        i = y - 1
        valor = bilheteira_dezembro_2022[i]
        return valor

def adicionar_valor_bilheteira(variavel_mes, variavel_dia, valor_bilhete, bilheteira_janeiro_2022, bilheteira_fevereiro_2022, bilheteira_marco_2022,
                          bilheteira_abril_2022,
                          bilheteira_maio_2022, bilheteira_junho_2022, bilheteira_julho_2022, bilheteira_agosto_2022,
                          bilheteira_setembro_2022,
                          bilheteira_outubro_2022, bilheteira_novembro_2022, bilheteira_dezembro_2022):
   if variavel_mes == 1:
        bilheteira_janeiro_2022.insert(variavel_dia - 1, valor_bilhete)
   elif variavel_mes == 2:
        bilheteira_fevereiro_2022.insert(variavel_dia - 1, valor_bilhete)
   elif variavel_mes == 3:
        bilheteira_marco_2022.insert(variavel_dia - 1, valor_bilhete)
   elif variavel_mes == 4:
        bilheteira_abril_2022.insert(variavel_dia - 1, valor_bilhete)
   elif variavel_mes == 5:
        bilheteira_maio_2022.insert(variavel_dia - 1, valor_bilhete)
   elif variavel_mes == 6:
        bilheteira_junho_2022.insert(variavel_dia - 1, valor_bilhete)
   elif variavel_mes == 7:
        bilheteira_julho_2022.insert(variavel_dia - 1, valor_bilhete)
   elif variavel_mes == 8:
        bilheteira_agosto_2022.insert(variavel_dia - 1, valor_bilhete)
   elif variavel_mes == 9:
        bilheteira_setembro_2022.insert(variavel_dia - 1, valor_bilhete)
   elif variavel_mes == 10:
        bilheteira_outubro_2022.insert(variavel_dia - 1, valor_bilhete)
   elif variavel_mes == 11:
        bilheteira_novembro_2022.insert(variavel_dia - 1, valor_bilhete)
   elif variavel_mes == 12:
        bilheteira_dezembro_2022.insert(variavel_dia - 1, valor_bilhete)


# Funçao para guardar a data do dia escolhido, usar essa data para adicionar
# Valor da bilheteira
def guardar_dia_1digito(controlos):
    return controlos[:1]

def guardar_dia_2digitos(controlos):
    return controlos[:2]

def guardar_mes_1digito(controlos):
    return controlos[2:3]

def guardar_mes_2digitos(controlos):
    return controlos[3:5]

def guardar_mes_9elementos_1digito(controlos):
    return controlos[1:2]

def guardar_mes_9elementos_2digitos(controlos):
    return controlos[2:4]

def guardar_mes_9elementos(controlos):
    return controlos[3:4]
    
def funcao_menu():
    input("Pressione ENTER para continuar\n")
    model.menu()


def verificar_cliente(lista_clientes_registados, lista_usernames, controlos):
    
    nome = controlos[0]
    username = controlos[1]
    password = controlos[2]
    cliente_registar = {}
    temp = False
    if username in lista_usernames:
        temp = True
    else:
        cliente_registar['Username'] = username
        cliente_registar['Password'] = password
        lista_usernames.append(username)
        lista_clientes_registados.append(cliente_registar)
    return temp


def verificar_username(lista_clientes_registados, controlos):
    username = controlos[0]
    password = controlos[1]
    verificacao = False
    for cliente_registar in lista_clientes_registados:
        if username == cliente_registar.get('Username') and  password == cliente_registar.get('Password'):
            verificacao = True
    if username == "admin" and password == "admin":
        model.admin_logado = True
    else:
        model.admin_logado = False
    return verificacao

def verificar_sessao_iniciada():
    verificacao = False
    if model.sessao_iniciada == True:
        verificacao = True
    return verificacao

#adicionar reservas a uma lista temporaria que depois adiciona essa reserva a uma 
#lista que contem todas as reservas do programa.
def adicionar_dict(username, evento, reserva_dia, tipo_bilhete, lugar):
    cliente = {}
    cliente['Username'] = username
    cliente['Eventos'] = evento
    cliente['Dia do evento'] = reserva_dia
    cliente['Bilhete'] = tipo_bilhete
    cliente['Lugar'] = lugar
    view.lista_reservas_total.append(cliente)

#Função para consultar as reservas
def consultar_reserva(controlos):
    username_reserva = controlos[0]
    for i in view.lista_reservas_total:
        if i.get('Username') == username_reserva:
            for key in i:
                print(key, ":", i[key])
            print() #print para separar as varias reservas

       
def alterar_eliminar_reserva(controlos):
    lista_reservas_utilizador = []
    username_reserva = controlos[0]
    numero = 1
    for i in view.lista_reservas_total:
        if i.get('Username') == username_reserva:
            print(f"{numero}.")
            numero = 1 + numero
            for key in i:
                print(key, ":", i[key])
            print()
            lista_reservas_utilizador.append(i)
    return lista_reservas_utilizador

def eliminar_antiga_adicionar_nova_reserva(x, y, z): # x = Reserva_Antiga / y = Lugar_Novo / z = Tipo_Bilhete_Novo
    reserva_nova = x.copy()
    reserva_nova['Bilhete'] = z
    reserva_nova['Lugar'] = y
    if x in view.lista_reservas_total:
        view.lista_reservas_total.remove(x)
    view.lista_reservas_total.append(reserva_nova)

def eliminar_reserva(x): # x = Reserva
    if x in view.lista_reservas_total:
        view.lista_reservas_total.remove(x)

def alterar_reservas_normal_normal(x, y, z):  # x = evento_dia / y = lugar_Novo / z = Lugar_Antigo
    for i in range(len(view.lista_lugares_reservados)):
        if view.lista_lugares_reservados[i][0] == x:
            if y in view.lista_lugares_reservados[i]:
                view.lista_lugares_reservados[i].remove(y)
                view.lista_lugares_reservados[i].append(z)
                alterar_reserva_print_lugares_normal(view.lista_todos_eventos_print[i], y, z)
                return "Reservado"
            else:
                return "Não Reservado"

def alterar_reservas_vip_vip(x, y, z):  # x = evento_dia / y = lugar_Novo / z = Lugar_Antigo
    for i in range(len(view.lista_lugares_reservados)):
            if view.lista_lugares_reservados[i][0] == x:
                if y in view.lista_lugares_reservados[i][len(view.lista_lugares_reservados[i]) - 1]:
                    view.lista_lugares_reservados[i][len(view.lista_lugares_reservados[i]) - 1].remove(y)
                    view.lista_lugares_reservados[i][len(view.lista_lugares_reservados[i]) - 1].append(z)
                    alterar_reserva_print_lugares_vip(view.lista_todos_eventos_print[i], y, z)
                    return "Reservado"
                else:
                    return "Não Reservado"

def alterar_reservas_vip_normal(x, y, z):  # x = evento_dia / y = lugar_Novo / z = Lugar_Antigo
    for i in range(len(view.lista_lugares_reservados)):
        if view.lista_lugares_reservados[i][0] == x:
            if y in view.lista_lugares_reservados[i]:
                view.lista_lugares_reservados[i].remove(y)
                view.lista_lugares_reservados[i][len(view.lista_lugares_reservados[i]) - 1].append(z)
                alterar_reserva_print_lugares_vip(view.lista_todos_eventos_print[i], y, z)
                return "Reservado"
            else:
                return "Não Reservado"

def alterar_reservas_normal_vip(x, y, z):  # x = evento_dia / y = lugar_Novo / z = Lugar_Antigo
    for i in range(len(view.lista_lugares_reservados)):
        if view.lista_lugares_reservados[i][0] == x:
            if y in view.lista_lugares_reservados[i][len(view.lista_lugares_reservados[i]) - 1]:
                view.lista_lugares_reservados[i][len(view.lista_lugares_reservados[i]) - 1].remove(y)
                view.lista_lugares_reservados[i].append(z)
                alterar_reserva_print_lugares_normal(view.lista_todos_eventos_print[i], y, z)
                return "Reservado"
            else:
                return "Não Reservado"

def alterar_reserva_print_lugares_normal(x, y, z):  # x = evento_dia / y = lugar_Novo / z = Lugar_Antigo APENAS QUANDO normal_normal e normal_vip
    for i in range(len(model.sala_para_print)): # Colocar a vermelho o novo lugar reservado
        if y == model.sala_para_print[i]:
            x.pop(i)
            x.insert(i, Fore.RED + model.lugares_print_copy[i - 1] + Fore.RESET)

    for i in range(len(model.sala_para_print)): # Colocar a branco o antigo lugar
        if z == model.sala_para_print[i]:
            x.pop(i)
            x.insert(i, Fore.WHITE + model.lugares_print_copy[i - 1] + Fore.RESET)

def alterar_reserva_print_lugares_vip(x, y, z):  # x = evento_dia / y = lugar_Novo / z = Lugar_Antigo APENAS QUANDO vip_vip e vip_normal
    for i in range(len(model.sala_para_print)): # Colocar a vermelho o novo lugar reservado
        if y == model.sala_para_print[i]:
            x.pop(i)
            x.insert(i, Fore.RED + model.lugares_print_copy[i - 1] + Fore.RESET)

    for i in range(len(model.sala_para_print)): # Colocar a amarelo o antigo lugar
        if z == model.sala_para_print[i]:
            x.pop(i)
            x.insert(i, Fore.YELLOW + model.lugares_print_copy[i - 1] + Fore.RESET)

def eliminar_reserva_normal(x, y): # x = evento_dia / y = lugar
    for i in range(len(view.lista_lugares_reservados)):
            if view.lista_lugares_reservados[i][0] == x:
                view.lista_lugares_reservados[i].append(y)
                eliminar_reserva_palco_normal(view.lista_todos_eventos_print[i], y)

def eliminar_reserva_palco_normal(x, y):  # x = evento_dia / y = lugar
    for i in range(len(model.sala_para_print)): # Colocar a branco o antigo lugar
        if y == model.sala_para_print[i]:
            x.pop(i)
            x.insert(i, Fore.WHITE + model.lugares_print_copy[i - 1] + Fore.RESET)

def eliminar_reserva_vip(x, y): # x = evento_dia / y = lugar
    for i in range(len(view.lista_lugares_reservados)):
            if view.lista_lugares_reservados[i][0] == x:
                view.lista_lugares_reservados[i][len(view.lista_lugares_reservados[i]) - 1].append(y)
                eliminar_reserva_palco_vip(view.lista_todos_eventos_print[i], y)

def eliminar_reserva_palco_vip(x, y):  # x = evento_dia / y = lugar
    for i in range(len(model.sala_para_print)): # Colocar a branco o antigo lugar
        if y == model.sala_para_print[i]:
            x.pop(i)
            x.insert(i, Fore.YELLOW + model.lugares_print_copy[i - 1] + Fore.RESET)
