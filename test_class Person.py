class Person:
    def __init__(self, förnamn, efternamn, födelseår):
        self.förnamn = förnamn
        self.efternamn = efternamn
        self.födelseår = födelseår

    def __lt__(self, other):
        if self.förnamn < other.förnamn:
            return True
        else:
            return False

    def __repr__(self):
        return self.förnamn + ": " + str(self.födelseår)


def huvudprogram():
    personlista = []
    personlista.append(Person("Selim", "Farin", 1999))
    personlista.append(Person("Felicia", "Gröngöling", 2002))
    personlista.append(Person("Ebru", "Hansson", 2004))

    for person in personlista:
        print(person)

    print("\nNu sorterad efter förnamn:")
    personlista.sort()
    for person in personlista:
        print(person)


huvudprogram()