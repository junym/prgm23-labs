# skrivna_inputs_labb5

def kontrollerar_heltal(svar):
    """Kontrollerar så att inputs är heltal och låter användaren försöka igen tills den ger ett heltal"""
    while True:
        try:
            heltal = int(input(svar))
            return heltal
        except ValueError:
            print("Personnumret måste bara innehålla siffror. Försök igen")