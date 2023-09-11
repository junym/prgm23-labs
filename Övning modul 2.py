""" Övning modul 2, 11 september 2023 """

def totalPris(antal_barn, antal_vuxen):
    """ Funktionen räknar ut det totala priset för biljetterna. Inparametrar:
    antal_barn, antal_vuxen. Returvärden total_pris."""
    BARN_PRIS = 10
    VUXEN_PRIS = 20
    total_pris = antal_barn*BARN_PRIS + antal_vuxen*VUXEN_PRIS
    return total_pris

def huvudprogram():
    """ Huvudprogrammet skickar ut frågor till användaren
    där den får skriva hur många biljetter och hur många av de som är 
    vuxna som inputs. Det printar till slut det totala priset."""
    try:
        antal_biljetter = int(input("Hur många biljetter vill du köpa? "))

        antal_vuxen = int(input("Hur många av de biljetterna är för en vuxen? "))

        antal_barn = antal_biljetter - antal_vuxen

        total_pris = totalPris(antal_barn, antal_vuxen)

        print(f"Du ska betala: {total_pris}")

    except ValueError:
        print("Något blev fel, svaret måste vara ett heltal")

huvudprogram()