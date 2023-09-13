"""Labb 2: 
Program som beräknar den aritmetiska och geometriska summan beroende på valda inputs.

Namn: Julia Nyman, Thea Nolgren, Milka Rasmussen
Datum: 2023-09-13
Kurskod: DD1310"""


def beräkna_ari_summa(startvärde_a1, differens, antal_tal):
    """Beräknar den aritmetiska summan beroende på startvärde, differens, antal tal och det n:te talet."""
    an = startvärde_a1 + differens * (antal_tal - 1)
    aritmetisk_summa = antal_tal * (startvärde_a1 + an) / 2 
    return aritmetisk_summa

def beräkna_geo_summa(startvärde_g1, kvoten, antal_tal):
    """Beräknar den geometriska summan beroende på startvärde, kvoten och antal tal."""
    geometrisk_summa = startvärde_g1*(((kvoten**antal_tal)-1) / (kvoten - 1))
    return geometrisk_summa


def huvudprogram():
    """Tar emot inputs från användaren om vilket startvärde, differens, kvot och antal tal, 
    och printar sen ut den aritmetiska respektive geometriska summan samt vilken av summorna som är störst eller om de är lika stora."""
    try:
        print("Vi börjar med startvärde och differens för den aritmetiska talföljden:")
        startvärde_a1 = float(input("Vad väljer du för startvärde (a1)? "))
        differens = float(input("Vad är differensen (d)? "))
        print()

        print("Vi fortsätter med startvärde och kvot för den geometriska talföljden:")
        startvärde_g1 = float(input("Vad väljer du för startvärde (g1)? "))
        kvoten = float(input("Vad väljer du för kvot (q)? "))
        print()
    except ValueError:
        print("Oj, det blev fel, det måste vara ett flyttal, starta om programmet och försök igen.")
        exit()

    try:
        print("Nu väljer vi antal tal för båda talföljderna:")
        antal_tal = int(input("Skriv in antal tal i följderna: "))
        print()
        
        print(f"Då blir den aritmetiska summan: {beräkna_ari_summa(startvärde_a1, differens, antal_tal)} och den geometriska summan: {beräkna_geo_summa(startvärde_g1, kvoten, antal_tal)}")
    except ValueError:
        print("Oj det blev fel, det måste vara ett heltal, starta om programmet och försök igen")  
        exit()
    
    print()
    if beräkna_ari_summa(startvärde_a1, differens, antal_tal) == beräkna_geo_summa(startvärde_g1, kvoten, antal_tal):
        print("Summorna är lika!")
    elif beräkna_ari_summa(startvärde_a1, differens, antal_tal) > beräkna_geo_summa(startvärde_g1, kvoten, antal_tal):
        print("Den aritmetiska summan är störst!")
    else:
        print("Den geometriska summan är störst!") 

    print() 

huvudprogram()