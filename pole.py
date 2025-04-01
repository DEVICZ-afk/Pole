predmety = ["Český jazyk", "Matematika", "Anglický jazyk", "Fyzika", "Chemie", "Biologie"]
print(len(predmety))
for i in predmety:
    print(i)

dalsi_predmet = input("Zadejte další předmět: ")
predmety.append(dalsi_predmet)
predmety.pop(1)
predmety.sort()
predmety.reverse()
print(predmety)