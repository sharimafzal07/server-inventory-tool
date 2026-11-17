import csv
import json
import os
from datetime import datetime
from pathlib import Path


def hamta_datafil():
    # Filnamnet kommer från miljövariabeln, annars används standardfilen
    return os.environ.get("INVENTORY_DATAFIL", "servrar.json")


def las_servrar(filnamn):
    # Finns filen inte börjar programmet med en tom lista
    sokvag = Path(filnamn)
    if not sokvag.exists():
        return []
    with open(filnamn, "r", encoding="utf-8") as fil:
        return json.load(fil)


def spara_servrar(servrar, filnamn):
    # ensure_ascii=False gör att å, ä och ö sparas som vanliga tecken
    with open(filnamn, "w", encoding="utf-8") as fil:
        json.dump(servrar, fil, indent=2, ensure_ascii=False)


def exportera_csv(servrar, katalog="rapporter"):
    # Katalogen skapas om den inte finns
    rapportkatalog = Path(katalog)
    rapportkatalog.mkdir(exist_ok=True)
    tidsstampel = datetime.now().strftime("%Y-%m-%d_%H%M")
    sokvag = rapportkatalog / f"inventering_{tidsstampel}.csv"
    faltnamn = ["namn", "adress", "miljo", "roll", "status", "senast_kontrollerad"]
    # newline="" behövs så att csv-modulen inte lägger till extra tomrader
    with open(sokvag, "w", newline="", encoding="utf-8") as fil:
        skrivare = csv.DictWriter(fil, fieldnames=faltnamn)
        skrivare.writeheader()
        skrivare.writerows(servrar)
    return sokvag
