"""Labb 5"""

import skrivna_inputs_labb5

class Skola():
    def __init__(self, namn, studenter):
        self.namn = namn
        self.studenter = studenter

class Student():
    def __init__(self, namn, efternamn, personnummer):
        self.namn = namn
        self.efternamn = efternamn
        self.personnummmer = personnummer

    def __str__(self):
        return "Namn: " + self.namn + " " + self.efternamn + " Personnummer: " + str(self.personnummmer)
    
def huvudprogram():

    studenter = {}

    i = 0
    while i < 3:
        namn = input("\nVad heter studenten i förnamn? ")
        efternamn = input("\nVad heter studenten i efternamn? ")
        personnummer = skrivna_inputs_labb5.kontrollerar_heltal("\nVad är studentens personnummer? ")

        student = Student(namn, efternamn, personnummer)
        studenter[personnummer] = student
        i += 1
        print("\nObjekt skapats!")
    
    skola = Skola("KTH", studenter)

    print("\nHär kommer en lista på alla sparade studenter på KTH:")

    for studenter in skola.studenter.values():
        print(studenter)

huvudprogram()    
