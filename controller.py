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

#Tiago Sousa
def verificar_lugar(sala, lugar):
    if sala.search_item(lugar) == True:
        return True
    else:
        return False

#Tiago Sousa
def eliminar_lugar(sala, lugar):
    if sala.search_item(lugar) == True:
        sala.delete_element_by_value(lugar)
        return True
    else:
        return False

    





