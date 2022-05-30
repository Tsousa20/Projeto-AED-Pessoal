import view
import model

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

#funçao para criar listas para o diferentes espetaculos com as diferentes salas
def criar_reservas_normal(x, y):
    
    if len(view.lista_lugares_reservados) == 0:
        print(f"teste")
        temp = view.sala
        temp.insert(0, x)
        temp.remove(y)
        view.lista_lugares_reservados.append(temp)
        return "Reservado"
        
    else:
        for i in range(len(view.lista_lugares_reservados)):
            if view.lista_lugares_reservados[i][0] == x:
                if y in view.lista_lugares_reservados[i]:
                    view.lista_lugares_reservados[i].remove(y)

                    return "Reservado"
                else:
                    return "Não reservado"
            else:
                temp = view.sala
                temp.insert(0, x)
                temp.remove(y)
                view.lista_lugares_reservados.append(temp)
                return "Reservado"
                

                   

    

