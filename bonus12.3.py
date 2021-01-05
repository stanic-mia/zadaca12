import json

drzava = ["Hrvatske", "Slovenije", "Bosne i Hercegovine", "Srbije", "Italije", "Njemačke", "Mađarske", "Francuske", "Portugala", "Španjolske", "Nizozemske", "Rusije", "Grčke", "Ujedinjenog kraljevstva"]
grad = ["Zagreb", "Ljubljana", "Sarajevo", "Beograd", "Rim", "Berlin", "Budimpešta", "Pariz", "Lisabon", "Madrid", "Amsterdam", "Moskva", "Atena", "London"]

name = input("Ime: ")
print("Bok " + name.capitalize() + "! Ovo je kviz iz geografije - pogodi glavni grad države.")

# pokretanje igre
def pokreni_igru():
    tocno = 0
    bonus_list = get_bonus_list()

    while True:

        for x in drzava:
            odgovor = input("Koji je glavni grad " + x + "? ")
            for y in grad:
                if odgovor.capitalize() == y:
                    tocno += 1
                    print("Bravo.")
                    grad.pop(0)
                    break
                else:
                    print("Krivi odgovor.")
                    grad.pop(0)
                    break

        bonus_list.append({"ime_igraca": name, "tocni_odgovori": str(tocno)})

        with open("bonus_lista.txt", "w") as bonus_file:
            bonus_file.write(json.dumps(bonus_list))

        break
    print("Imate " + str(tocno) + "/15 točnih odgovora.")

# čitanje score liste
def get_bonus_list():
    with open("bonus_lista.txt", "r") as bonus_file:
        bonus_list = json.loads(bonus_file.read())
    return bonus_list

# najbolji rezultati
def get_top_scores():
    bonus_list = get_bonus_list()
    top_list = sorted(bonus_list, key=lambda k: k['tocni_odgovori'], reverse=True)
    return top_list

# izbornik
while True:
    selection = input("Izaberi: A) Pokreni igru  B) Najbolji rezultati ili  C) izlaz: ")

    if selection.upper() == "A":
        pokreni_igru()
    elif selection.upper() == "B":
        for bonus_dict in get_top_scores():
            print("Igrač: " + bonus_dict.get("ime_igraca") + " Točni odgovori: " + str(bonus_dict["tocni_odgovori"]) +"/15")
    elif selection.upper() == "C":
        break
    else:
        print("Ne prepoznajem odabir. Molim te ponovi.")