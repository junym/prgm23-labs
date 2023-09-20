"""Modul för felhantering till Labb 3
Namn: Julia Nyman, Thea Nolgren
Datum: 20 sep 2023
Kurskod: DD1310"""

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
