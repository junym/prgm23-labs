'''
def beräkna_an(startvärde, differens, antal_tal):
    return(startvärde + differens * (antal_tal - 1))

startvärde = 1
differens = 2
antal_tal = 4

print(beräkna_an(startvärde, differens, antal_tal))

def beräkna_aritmetisk_summa(startvärde, differens, antal_tal):
    return(antal_tal * (startvärde + beräkna_an(startvärde, differens, antal_tal)) / 2)

print(beräkna_aritmetisk_summa(startvärde, differens, antal_tal))

startvärde = 1
kvoten = 2
antal_tal = 4
def beräkna_geometrisk_summa(startvärde, kvoten, antal_tal):
    return(startvärde*(((kvoten**antal_tal)-1) / (kvoten - 1)))

print(beräkna_geometrisk_summa(startvärde, kvoten, antal_tal)) '''

startvärde = int(input("Vad väljer du för startnummer? "))
differens = int(input("Vad väljer du för differens? "))
antal_tal = int(input("Hur många tal vill du ha i din följd? "))

def beräkna_an(startvärde, differens, antal_tal):
    """Funktionen beräknar an"""
    return(startvärde + differens * (antal_tal - 1))

def beräkna_aritmetisk_summa(startvärde, differens, antal_tal):
    """Funktionen beräknar den aritmetiska summan beroende på valda inputs"""
    return(antal_tal * (startvärde + beräkna_an(startvärde, differens, antal_tal)) / 2)

print (f"Den aritmetiska summan blir: {beräkna_aritmetisk_summa(startvärde, differens, antal_tal)}")

startvärde = int(input("Vad väljer du för startnummer? "))
kvoten = int(input("Vad väljer du för kvot? "))
antal_tal = int(input("Hur många tal vill du ha i din följd? "))

def beräkna_geometrisk_summa(startvärde, kvoten, antal_tal):
    """Funktionen beräknar den geometriska summan beroende på valda inputs"""
    return(startvärde*(((kvoten**antal_tal)-1) / (kvoten - 1)))

print(f"Den geometriska summan blir: {beräkna_geometrisk_summa(startvärde, kvoten, antal_tal)}")