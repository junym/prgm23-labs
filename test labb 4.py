# test labb 4

import test_inputs4

class Student:
    def __init__(self, förnamn, efternamn, personummer):
        self.förnamn = förnamn
        self.efternamn = efternamn
        self.personnummer = personummer

    def __str__(self):
        return "Namn: " + self.förnamn + " " + self.efternamn + ". Personnummer: " + str(self.personnummer)
    
def main():
    studentlista = []

    studentlista.append(Student(input("Vad heter studenten i förnamn? "), input("Vad heter studenten i efternamn? "), test_inputs4.testar_tal("Vad har studenten för personnummer? ")))
    print("\nObjektet skapat!\n")
    studentlista.append(Student(input("Vad heter studenten i förnamn? "), input("Vad heter studenten i efternamn? "), test_inputs4.testar_tal("Vad har studenten för personnummer? ")))
    print("\nObjektet skapat!\n")
    studentlista.append(Student(input("Vad heter studenten i förnamn? "), input("Vad heter studenten i efternamn? "), test_inputs4.testar_tal("Vad har studenten för personnummer? ")))
    print("\nObjektet skapat!\n")

    print("Här är en lista på alla sparade studenter:")
    for student in studentlista:
        print(student)

main()