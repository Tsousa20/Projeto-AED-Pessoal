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
        if username in lista_username:
            login =[username, password]
            return login







