import controller
import model

k = ["k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8", "k9", "k10", "k11", "k12", "k13" "k14"]
j = ["j1", "j2", "j3", "j4", "j5", "j6", "j7", "j8", "j9", "j10", "j11", "j12", "j13", "j14"]
i = ["i1", "i2", "i3", "i4", "i5", "i6", "i7", "i8", "i9", "i10", "i11", "i12", "i13", "i14"]
h = ["h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "h11", "h12", "h13", "h14"]

showroom_options = ["Events", "Tickets", "Reservations"]
showroom_events = ["Brodway", "Circus", "Musical", "Opera"]
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
            print("Welcome to THE SHOWROOM\nPlease, choose an option.")
            print() #apenas para aparecer separado, é so estetica
            print('\n'.join(map(str, showroom_options)))

        elif controlos[0] == "Events":
            print() #apenas para aparecer separado, é so estetica
            print("Please, choose you event!")
            print() #apenas para aparecer separado, é so estetica
            print('\n'.join(map(str, showroom_events)))

            controlos = input().split(" ")

            if controlos[0] == "Brodway":
                Brodway()
        else:
            if controlos[0] not in showroom_options:
                print("That option does not exist.")


def Brodway():
    print("Please, choose you seat!")
    print() #apenas para aparecer separado, é so estetica
    print(model.palco())
