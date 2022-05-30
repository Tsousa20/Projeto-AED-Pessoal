import colorama
from colorama import Fore
colorama.init(autoreset=True)

#CHAMAR VARIAVEL QUANDO HOUVER UMA RESERVA
reservado = Fore.RED

def palco_default():
    print("| K1 || K2 |          | K3 || K4 || K5 || K6 || K7 || K8 || K9 || K10 || K11 || K12 |     | K13 || K14 |")
    print("| J1 || J2 |          | J3 || J4 || J5 || J6 || J7 || J8 || J9 || J10 || J11 || J12 |     | J13 || J14 |")
    print("| I1 || I2 |          | I3 || I4 || I5 || I6 || I7 || I8 || I9 || I10 || I11 || I12 |     | I13 || I14 |")
    print("| H1 || H2 |          | H3 || H4 || H5 || H6 || H7 || H8 || H9 || H10 || H11 || H12 |     | H13 || H14 |")
    print("| G1 || G2 |          | G3 || G4 || G5 || G6 || G7 || G8 || G9 || G10 || G11 || G12 |     | G13 || G14 |")
    print(f"| F1 || F2 |                            {Fore.YELLOW}| F6 || F7 || F8 || F9 |{Fore.RESET}                          | F13 || F14 |")
    print("\n")
    print("| E1 || E2 |          | E3 || E4 || E5 || E6 || E7 || E8 || E9 || E10 || E11 || E12 |     | E13 || E14 |")
    print("| D1 || D2 |          | D3 || D4 || D5 || D6 || D7 || D8 || D9 || D10 || D11 || D12 |     | D13 || D14 |")
    print("| C1 || C2 |          | C3 || C4 || C5 || C6 || C7 || C8 || C9 || C10 || C11 || C12 |     | C13 || C14 |")
    print("| B1 || B2 |          | B3 || B4 || B5 || B6 || B7 || B8 || B9 || B10 || B11 || B12 |     | B13 || B14 |")
    print("\n")
    print(f"| A1 || A2 |                            {Fore.YELLOW}| A6 || A7 || A8 || A9 |{Fore.RESET}                          | A13 || A14 |")
    print("\n")
    print("                ┌────────────────────────────────────────────────────────────────────────────────────────┐")
    print("                |                                                                                        |")
    print("                |                                          PALCO                                         |")
    print("                |                                                                                        |")
    print("                └────────────────────────────────────────────────────────────────────────────────────────┘")

def tabela_precos():
    print("┌────────────────────────┐")
    print("|         Preços         |")
    print("├────────────────────────┤")
    print("|        Normal 4€       |")
    print("|       (1 pessoa)       |")
    print("|                        |")
    print("|        VIP  12€        |")
    print("|       (1 pessoa)       |")
    print("└────────────────────────┘")

#IGNORAR
lugares_default = ["| K1 |","| K2 |","| K3 |","| K4 |","| K5 |","| K6 |","| K7 |","| K8 |","| K9 |","| K10 |","| K11 |","| K12 |","| K13 |","| K14 |",
"| J1 |","| J2 |","| J3 |","| J4 |","| J5 |","| J6 |","| J7 |","| J8 |","| J9 |","| J10 |","| J11 |","| J12 |","| J13 |","| J14 |",
"| I1 |","| I2 |","| I3 |","| I4 |","| I5 |","| I6 |","| I7 |","| I8 |","| I9 |","| I10 |","| I11 |","| I12 |","| I13 |","| I14 |",
"| H1 |","| H2 |","| H3 |","| H4 |","| H5 |","| H6 |","| H7 |","| H8 |","| H9 |","| H10 |","| H11 |","| H12 |","| H13 |","| H14 |",
"| G1 |","| G2 |","| G3 |","| G4 |","| G5 |","| G6 |","| G7 |","| G8 |","| G9 |","| G10 |","| G11 |","| G12 |","| G13 |","| G14 |",
"| F1 |","| F2 |","| F6 |","| F7 |","| F8 |","| F9 |","| F13 |","| F14 |",
"| E1 |","| E2 |","| E3 |","| E4 |","| E5 |","| E6 |","| E7 |","| E8 |","| E9 |","| E10 |","| E11 |","| E12 |","| E13 |","| E14 |",
"| D1 |","| D2 |","| D3 |","| D4 |","| D5 |","| D6 |","| D7 |","| D8 |","| D9 |","| D10 |","| D11 |","| D12 |","| D13 |","| D14 |",
"| C1 |","| C2 |","| C3 |","| C4 |","| C5 |","| C6 |","| C7 |","| C8 |","| C9 |","| C10 |","| C11 |","| C12 |","| C13 |","| C14 |",
"| B1 |","| B2 |","| B3 |","| B4 |","| B5 |","| B6 |","| B7 |","| B8 |","| B9 |","| B10 |","| B11 |","| B12 |","| B13 |","| B14 |",
"| A1 |","| A2 |","| A6 |","| A7 |","| A8 |","| A9 |","| A13 |","| A14 |"]

#IGNORAR
lugar_reservar_default = ["K1","K2","K3","K4","K5","K6","K7","K8","K9","K10","K11","K12","K13","K14",
"J1","J2","J3","J4","J5","J6","J7","J8","J9","J10","J11","J12","J13","J14",
"I1","I2","I3","I4","I5","I6","I7","I8","I9","I10","I11","I12","I13","I14",
"H1","H2","H3","H4","H5","H6","H7","H8","H9","H10","H11","H12","H13","H14",
"G1","G2","G3","G4","G5","G6","G7","G8","G9","G10","G11","G12","G13","G14",
"F1","F2","F6","F7","F8","F9","F13","F14",
"E1","E2","E3","E4","E5","E6","E7","E8","E9","E10","E11","E12","E13","E14 ",
"D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","D11","D12","D13","D14",
"C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","C11","C12","C13","C14",
"B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","B11","B12","B13","B14",
"A1","A2","A6","A7","A8","A9","A13","A14"]

#IGNORAR
def palco_reserva_default():
    print(f"{lugares_default[0]}{lugares_default[1]}          {lugares_default[2]}{lugares_default[3]}{lugares_default[4]}{lugares_default[5]}{lugares_default[6]}{lugares_default[7]}{lugares_default[8]}{lugares_default[9]}{lugares_default[10]}{lugares_default[11]}     {lugares_default[12]}{lugares_default[13]}")
    print(f"{lugares_default[14]}{lugares_default[15]}          {lugares_default[16]}{lugares_default[17]}{lugares_default[18]}{lugares_default[19]}{lugares_default[20]}{lugares_default[21]}{lugares_default[22]}{lugares_default[23]}{lugares_default[24]}{lugares_default[25]}     {lugares_default[26]}{lugares_default[27]}")
    print(f"{lugares_default[28]}{lugares_default[29]}          {lugares_default[30]}{lugares_default[31]}{lugares_default[32]}{lugares_default[33]}{lugares_default[34]}{lugares_default[35]}{lugares_default[36]}{lugares_default[37]}{lugares_default[38]}{lugares_default[39]}     {lugares_default[40]}{lugares_default[41]}")
    print(f"{lugares_default[42]}{lugares_default[43]}          {lugares_default[44]}{lugares_default[45]}{lugares_default[46]}{lugares_default[47]}{lugares_default[48]}{lugares_default[49]}{lugares_default[50]}{lugares_default[51]}{lugares_default[52]}{lugares_default[53]}     {lugares_default[54]}{lugares_default[55]}")
    print(f"{lugares_default[56]}{lugares_default[57]}          {lugares_default[58]}{lugares_default[59]}{lugares_default[60]}{lugares_default[61]}{lugares_default[62]}{lugares_default[63]}{lugares_default[64]}{lugares_default[65]}{lugares_default[66]}{lugares_default[67]}     {lugares_default[68]}{lugares_default[69]}")
    print(f"{lugares_default[70]}{lugares_default[71]}                            {lugares_default[72]}{lugares_default[73]}{lugares_default[74]}{lugares_default[75]}                          {lugares_default[76]}{lugares_default[77]}")
    print("\n")
    print(f"{lugares_default[78]}{lugares_default[79]}          {lugares_default[80]}{lugares_default[81]}{lugares_default[82]}{lugares_default[83]}{lugares_default[84]}{lugares_default[85]}{lugares_default[86]}{lugares_default[87]}{lugares_default[88]}{lugares_default[89]}     {lugares_default[90]}{lugares_default[91]}")
    print(f"{lugares_default[92]}{lugares_default[93]}          {lugares_default[94]}{lugares_default[95]}{lugares_default[96]}{lugares_default[97]}{lugares_default[98]}{lugares_default[99]}{lugares_default[100]}{lugares_default[101]}{lugares_default[102]}{lugares_default[103]}     {lugares_default[104]}{lugares_default[105]}")
    print(f"{lugares_default[106]}{lugares_default[107]}          {lugares_default[108]}{lugares_default[109]}{lugares_default[110]}{lugares_default[111]}{lugares_default[112]}{lugares_default[113]}{lugares_default[114]}{lugares_default[115]}{lugares_default[116]}{lugares_default[117]}     {lugares_default[118]}{lugares_default[119]}")
    print(f"{lugares_default[120]}{lugares_default[121]}          {lugares_default[122]}{lugares_default[123]}{lugares_default[124]}{lugares_default[125]}{lugares_default[126]}{lugares_default[127]}{lugares_default[128]}{lugares_default[129]}{lugares_default[130]}{lugares_default[131]}     {lugares_default[132]}{lugares_default[133]}")
    print("\n")
    print(f"{lugares_default[134]}{lugares_default[135]}                            {lugares_default[136]}{lugares_default[137]}{lugares_default[138]}{lugares_default[139]}                          {lugares_default[140]}{lugares_default[141]}")
    print("\n")
    print("                ┌──────────────────────────────────────────────────────────────────────────────────────┐")
    print("                |                                                                                      |")
    print("                |                                          PALCO                                       |")
    print("                |                                                                                      |")
    print("                └──────────────────────────────────────────────────────────────────────────────────────┘")
