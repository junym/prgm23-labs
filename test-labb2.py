"""Labb 2: 
Program som beräknar den aritmetiska och geometriska summan beroende på valda inputs."""

def beräkna_ari_summa(startvärde, differens, antal_tal):
    """Beräknar den aritmetiska summan beroende på startvärde, differens, antal tal och det n:te talet."""
    an = startvärde + differens * (antal_tal - 1)
    aritmetisk_summa = antal_tal * (startvärde + an) / 2 
    return aritmetisk_summa

def beräkna_geo_summa(startvärde, kvoten, antal_tal):
    """Beräknar den geometriska summan beroende på startvärde, kvoten och antal tal."""
    geometrisk_summa = startvärde*(((kvoten**antal_tal)-1) / (kvoten - 1))
    return geometrisk_summa


def huvudprogram():
    """Tar emot inputs från användaren om vilket startvärde, differens, kvot och antal tal, 
    och printar sen ut den aritmetiska respektive geometriska summan samt vilken av summorna som är störst."""
    try:
        startvärde = float(input("Vad väljer du för startvärde till den aritmetiska talföljden? "))
        differens = float(input("Vad är differensen? "))
        antal_tal = float(input("Hur många tal i talföljden? "))
        print()
        print(f"Då blir den aritmetiska summan: {beräkna_ari_summa(startvärde, differens, antal_tal)}")
    except ValueError:
        print("Oj det blev fel, det måste vara ett flyttal, starta om programmet och kör igen")    
    print()

    try:
        startvärde = float(input("Vad väljer du för startnummer till den geometriska talföljden? "))
        kvoten = float(input("Vad väljer du för kvot? "))
        antal_tal = float(input("Hur många tal vill du ha i din följd? "))
        print()
        print(f"Då blir den geometriska summan: {beräkna_geo_summa(startvärde, kvoten, antal_tal)}")
    except ValueError:
        print("Oj det blev fel, det måste vara ett flyttal, starta om programmet och kör igen")
    print()

    if beräkna_ari_summa(startvärde, differens, antal_tal) > beräkna_geo_summa(startvärde, kvoten, antal_tal):
        print("Den aritmetiska summan är större!")
    else:
        print("Den geometriska summan är större!") 
    print()

huvudprogram()