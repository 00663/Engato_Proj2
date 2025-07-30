"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Filip Hnilica
email: filip.hnilica@gmail.com
"""

import random
from time import sleep


def generuj_unikatni_cislo() -> int:

    """
    Generuje unikátní čtyřciferné číslo bez opakujících se číslic a nezačínající nulou.

    Tato funkce zajišťuje, že vygenerované číslo splňuje všechna kritéria pro hru:
    má přesně 4 číslice, první číslice není nula a všechny čtyři číslice jsou unikátní.

    Returns:
        int: Náhodně vygenerované čtyřciferné číslo splňující zadaná kritéria.
    """
    while True:
        cislice = random.sample(range(10), 4)
        # Zajistíme, že první číslice není 0
        if cislice[0] != 0:
            # Převedeme seznam číslic na řetězec a poté na celé číslo
            unikatni_cislo = ''.join(map(str, cislice))
            return int(unikatni_cislo)


def ziskej_uzivatelsky_vstup() -> int:

    """
    Vyzve uživatele k zadání čtyřciferného čísla a ověří platnost vstupu.

    Tato funkce opakovaně žádá uživatele o vstup, dokud není zadáno platné
    čtyřciferné číslo. Poskytuje specifickou zpětnou vazbu pro různé typy
    neplatných vstupů. Platný vstup musí mít přesně 4 číslice, skládat se
    pouze z číslic, nezačínat na '0' a nesmí mít opakující se číslice.

    Returns:
        int: Ověřené čtyřciferné číslo zadané uživatelem.
    """
    while True:
        uzivatelsky_vstup = input("Zadejte čtyřciferné číslo bez opakujících se číslic: ")

        if not uzivatelsky_vstup.isdigit():
            print("Neplatný vstup: Váš tip musí obsahovat pouze číslice (0-9). Zkuste to prosím znovu.")
        elif len(uzivatelsky_vstup) != 4:
            print(f"Neplatný vstup: Váš tip musí mít přesně 4 číslice. Zadali jste {len(uzivatelsky_vstup)} číslic. Zkuste to prosím znovu.")
        elif uzivatelsky_vstup[0] == '0':
            print("Neplatný vstup: Váš tip nemůže začínat nulou. Zkuste to prosím znovu.")
        elif len(set(uzivatelsky_vstup)) != 4:
            print("Neplatný vstup: Váš tip nesmí mít opakující se číslice. Zkuste to prosím znovu.")
        else:
            return int(uzivatelsky_vstup)


def porovnej_cisla(tajne_cislo: int, uzivatelsky_tip: int) -> tuple[int, int]:

    """
    Porovná tajné číslo s uživatelským tipem a vypočítá počet býků a krav.

    'Býci' jsou číslice, které jsou správné a na správné pozici.
    'Krávy' jsou číslice, které jsou správné, ale na špatné pozici.

    Args:
        tajne_cislo (int): Tajné čtyřciferné číslo k uhodnutí.
        uzivatelsky_tip (int): Uživatelský čtyřciferný tip.

    Returns:
        tuple[int, int]: Dvojice (tuple) obsahující dvě celá čísla:
                         - První prvek je počet býků.
                         - Druhý prvek je počet krav.
    """

    tajne_str = str(tajne_cislo)
    tip_str = str(uzivatelsky_tip)

    byci = sum(s == u for s, u in zip(tajne_str, tip_str))
    
    kravy = 0
    # Spočítáme celkový počet společných číslic a pak odečteme býky, abychom dostali jen krávy
    for cislice in set(tip_str): # Projdeme unikátní číslice v uživatelském tipu
        kravy += min(tajne_str.count(cislice), tip_str.count(cislice))
    kravy -= byci # Odečteme býky, protože jsou také "společnými číslicemi"

    return byci, kravy


def vypis_byky_a_kravy(byci: int, kravy: int) -> None:

    """
    Vypíše aktuální počet býků a krav, správně ošetřuje jednotné a množné číslo.

    Args:
        byci (int): Počet býků.
        kravy (int): Počet krav.
    """

    slovo_byk = "býk" if byci == 1 else "býci"
    slovo_krava = "kráva" if kravy == 1 else "krávy"

    print(f"Býci: {byci} {slovo_byk}, Krávy: {kravy} {slovo_krava}")


def vyhral_jsi(pokusy: int) -> None:

    """
    Vypíše gratulační zprávu uživateli po výhře ve hře.

    Zahrnuje celkový počet pokusů, které uživateli trvalo uhodnout tajné číslo.

    Args:
        pokusy (int): Počet pokusů, které uživatel provedl před výhrou.
    """

    print(f"\nGratuluji! Uhodl jsi číslo na {pokusy} pokusů. Vyhrál jsi!")
    sleep(2)
    print("Děkuji, že jsi hrál!")


def zobraz_pravidla() -> None:

    """
    Zobrazí uživateli pravidla hry Býci a Krávy.

    Poskytuje jasné vysvětlení, jak se hra hraje, včetně definice 'býků' a 'krav'
    a požadavků na tajné číslo.
    """

    print("--- Pravidla hry Býci a Krávy ---")
    print("Cílem je uhodnout tajné čtyřciferné číslo, které jsem si myslel.")
    print("Číslo nesmí začínat nulou a nesmí mít žádné opakující se číslice.")
    print("\nPo každém tvém tipu ti řeknu, kolik jsi získal/a 'býků' a 'krav':")
    print("- 'Býci' = správná číslice na správném místě.")
    print("- 'Krávy' = správná číslice, ale na špatném místě.")
    print("\nPojďme začít! Hodně štěstí!\n")
    sleep(1) # Krátká pauza pro lepší čitelnost


def hraj_hru() -> None:

    """
    Řídí hlavní herní smyčku hry Býci a Krávy.

    Tato funkce organizuje celý průběh hry, od zobrazení pravidel
    a generování tajného čísla, přes zpracování uživatelského vstupu,
    porovnávání tipů, až po vyhlášení vítěze.
    """

    print("Vítejte ve hře Býci a Krávy!")
    zobraz_pravidla()
    
    tajne_cislo = generuj_unikatni_cislo()
    # Ladící řádek: vypne se pro produkci
    # print(f"DEBUG: Tajné číslo je {tajne_cislo}") 

    byci, kravy = 0, 0
    pocet_pokusu = 0

    while byci != 4:
        uzivatelsky_tip = ziskej_uzivatelsky_vstup()
        byci, kravy = porovnej_cisla(tajne_cislo, uzivatelsky_tip)
        vypis_byky_a_kravy(byci, kravy)
        pocet_pokusu += 1

    vyhral_jsi(pocet_pokusu)


if __name__ == "__main__":
    hraj_hru()
