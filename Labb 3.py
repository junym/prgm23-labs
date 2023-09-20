"""Labb 3
Namn: Julia Nyman, Thea Nolgren
Datum: 20 sep 2023
Kurskod: DD1310"""

import skrivna_input

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
    och printar sen ut den aritmetiska respektive geometriska summan samt vilken av summorna
    som är störst eller om de är lika stora. Felhanteringen är i en importerad modul."""
    
    print("Vi börjar med startvärde och differens för den aritmetiska talföljden:")
    startvärde_a1 = skrivna_input.kontrollerar_flyttal("Vad väljer du för startvärde (a1)? ")
    differens = skrivna_input.kontrollerar_flyttal(("Vad är differensen (d)? ")) 

    print("Vi fortsätter med startvärde och kvot för den geometriska talföljden:")
    startvärde_g1 = skrivna_input.kontrollerar_flyttal("Vad väljer du för startvärde (g1)? ")
    kvoten = skrivna_input.kontrollerar_flyttal("Vad väljer du för kvot (q)? ")

    while kvoten <= 0 or kvoten == 1:
        """Kontrollerar om kvoten är mindre än noll eller ett, och låter en försöka igen."""
        kvoten = skrivna_input.kontrollerar_flyttal("Vad väljer du för kvot (q)? ")

    print("Nu väljer vi antal tal för båda talföljderna:")
    
    antal_tal = skrivna_input.kontrollerar_heltal("Skriv in antal tal i följderna: ")

    while antal_tal <= 0:
        """Kontrollerar om antal tal är 0 och låter en prova igen om det är fallet."""
        antal_tal = skrivna_input.kontrollerar_heltal("Skriv in antal tal i följderna: ")
       
           
    print(f"Då blir den aritmetiska summan: {beräkna_ari_summa(startvärde_a1, differens, antal_tal)} och den geometriska summan: {beräkna_geo_summa(startvärde_g1, kvoten, antal_tal)}")
     
    if beräkna_ari_summa(startvärde_a1, differens, antal_tal) == beräkna_geo_summa(startvärde_g1, kvoten, antal_tal):
     print("Summorna är lika!")
    elif beräkna_ari_summa(startvärde_a1, differens, antal_tal) > beräkna_geo_summa(startvärde_g1, kvoten, antal_tal):
        print("Den aritmetiska summan är störst!")
    else:
        print("Den geometriska summan är störst!") 

if __name__ == "__main__":
    huvudprogram()