# test_inputs4

"""def testar_sträng(svar):
    while True:
        try:
            sträng = str(input(svar))
            return sträng
        except ValueError:
            print("Du måste råkat skriva en siffra, prova igen med bokstäver.")
"""
def testar_tal(svar):
    """Kontrollerar så att inputs är heltal och låter användaren försöka igen tills den ger ett heltal"""
    while True:
        try:
            heltal = int(input(svar))
            return heltal
        except ValueError:
            print("Personnumret får inte innehålla annat än siffror. Försök igen")