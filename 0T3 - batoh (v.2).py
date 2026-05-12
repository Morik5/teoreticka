import time
baliky = [
    ["A", 40, 900],
    ["B", 30, 700],
    ["C", 50, 1200],
    ["D", 20, 400],
    ["E", 10, 200],
    ["F", 25, 500],
    ["G", 35, 800]
#    ["H", 15, 300],
#    ["I", 45, 1000],
#    ["J", 5, 100],
#    ["K", 55, 1300],
#    ["L", 60, 1500],
#    ["M", 8, 150],
#    ["N", 22, 450],
#    ["O", 15, 300],
#    ["P", 45, 1000],
#    ["Q", 10, 200],
#    ["R", 25, 500],
#    ["S", 35, 800],
#    ["T", 15, 300],
]

maximalni_nosnost = 120
nejvyssi_hodnota = 0
nejlepsi_vyber = []


def najdi_nejlepsi(index, aktualni_vaha, aktualni_hodnota, vybrany_vyber):
    global nejvyssi_hodnota, nejlepsi_vyber

    # Kontroluje se při každém zavolání funkce, aby to zbytečně neprohledávalo kombinace, které už se nevejdou
    if aktualni_vaha > maximalni_nosnost:
        return

    # Na konci seznamu se porovná nalezená kombinace s dosavadním nejlepším výsledkem
    if index == len(baliky):
        if aktualni_hodnota > nejvyssi_hodnota:
            nejvyssi_hodnota = aktualni_hodnota
            nejlepsi_vyber = vybrany_vyber.copy()
        return

    balik = baliky[index]

    # Vyzkouší se možnost, že tento balík nevezmeme
    najdi_nejlepsi(index + 1, aktualni_vaha, aktualni_hodnota, vybrany_vyber)

    # Vyzkouší se druhá možnost, že se balík do batohu přidá, a pokud se nevejde, tak se to zkontroluje právě na začátku funkce a vrátí se zpět
    vybrany_vyber.append(balik)
    najdi_nejlepsi(
        index + 1,
        aktualni_vaha + balik[1],
        aktualni_hodnota + balik[2],
        vybrany_vyber,
    )
    # Pak se to jen smaže, aby se to mohlo znovu použít v další kombinaci
    vybrany_vyber.pop()

start_cas = time.time()
najdi_nejlepsi(0, 0, 0, [])

# Vypíše se vybraná kombinace, celková váha, hodnota a čas 
print("Čas výpočtu:", round((time.time() - start_cas) * 1000, 3), "ms")
print("OPTIMÁLNÍ NÁKLAD")
print("------------------------")
celkova_vaha_vysledku = 0

print("Vybrané balíky: ")
for balik in nejlepsi_vyber:
    print("Balík", balik[0])
    celkova_vaha_vysledku = celkova_vaha_vysledku + balik[1]

print("------------------------")
print("Celková váha:", celkova_vaha_vysledku, "kg")
print("Celková hodnota:", nejvyssi_hodnota, "Kč")

