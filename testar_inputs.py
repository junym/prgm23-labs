"""testar inputs"""

def kontrollerar_flyttal(svar):
    """Kontrollerar så att inputs är flyttal och låter användaren försöka igen tills den ger ett flyttal"""
    while True:
        try:
            flyttal = float(input(svar))
            return flyttal
        except ValueError:
            print("Oj, det du skrev var inte ett flyttal. Försök igen")

def kontrollerar_heltal(svar):
    """Kontrollerar så att inputs är heltal och låter användaren försöka igen tills den ger ett heltal"""
    while True:
        try:
            heltal = int(input(svar))
            return heltal
        except ValueError:
            print("Oj, det du skrev var inte ett heltal. Försök igen")


def flyt_inte_noll_eller_ett(svar):
    while True:
        try:
            flyttal = float(input(svar)) and flyttal <= 0 or flyttal == 1
            return flyttal
        except ValueError:
            print("Oj det blev fel, ditt tal måste vara ett flyttal, större än noll men skiljt från 1, prova igen!")

