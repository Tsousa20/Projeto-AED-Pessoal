import controller
import model

k = ["k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8", "k9", "k10", "k11", "k12", "k13" "k14"]
j = ["j1", "j2", "j3", "j4", "j5", "j6", "j7", "j8", "j9", "j10", "j11", "j12", "j13", "j14"]
i = ["i1", "i2", "i3", "i4", "i5", "i6", "i7", "i8", "i9", "i10", "i11", "i12", "i13", "i14"]
h = ["h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "h11", "h12", "h13", "h14"]
g = ["g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9", "g10", "g11", "g12", "g13", "g14"]
f = ["f1", "f2", None, None, None, "f6", "f7", "f8", "f9", None, None, None, "f13", "f14"] #vip
e = ["e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "e9","e10", "e11", "e12", "e13", "e14"]
d = ["d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "d11", "d12", "d13", "d14"]
c = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13", "c14"]
b = ["b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9", "b10", "b11","b12", "b13", "b14"]
a = ["a1", "a2", None, None, None, "a6", "a7", "a8", "a9", None, None, None, "a13", "a14"] #vip




showroom_options = ["Eventos", "Bilhetes", "Reservas"]
showroom_events = ["Brodway", "Circo", "Musical", "Opera"]
def main():
    while True:
        try:
            controlos = input().split(" ")
        except EOFError:
            return

        #Fazer Reserva
        if controlos[0] == "FR":
            ##print("Indique a data da reserva")
            ##input()
            print(model.palco())

        elif controlos[0] == "START":
            print() #apenas para aparecer separado, é so estetica
            print("Bem vindo à sala de espetaculos!\nEscolha uma opção!")
            print() #apenas para aparecer separado, é so estetica
            print('\n'.join(map(str, showroom_options)))

        elif controlos[0] == "Events":
            print() #apenas para aparecer separado, é so estetica
            print("Escolha o evento!")
            print() #apenas para aparecer separado, é so estetica
            print('\n'.join(map(str, showroom_events)))

            controlos = input().split(" ")

            if controlos[0] == "Brodway":
                Brodway()
                if controlos[0] not in showroom_options:
                    print("Opção inexistente.")


def Brodway():
    print("Selecione o seu lugar!")
    print() #apenas para aparecer separado, é so estetica
    print(model.palco())
