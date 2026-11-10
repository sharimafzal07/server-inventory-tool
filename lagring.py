import csv
import json
import os
from datetime import datetime
from pathlib import Path


def hamta_datafil():
    return os.getenv("INVENTORY_DATAFIL", "servrar.json")


def las_servrar(filnamn):
    sokvag = Path(filnamn)
    if not sokvag.exists():
        return []
    with open(filnamn, "r", encoding="utf-8") as fil:
        return json.load(fil)


def spara_servrar(servrar, filnamn):
    with open(filnamn, "w", encoding="utf-8") as fil:
        json.dump(servrar, fil, indent=2, ensure_ascii=False)


def exportera_csv(servrar, katalog="rapporter"):
    rapportkatalog = Path(katalog)
    rapportkatalog.mkdir(exist_ok=True)
    tidsstampel = datetime.now().strftime("%Y-%m-%d_%H%M")
    sokvag = rapportkatalog / f"inventering_{tidsstampel}.csv"
    faltnamn = ["namn", "adress", "miljo", "roll", "status", "senast_kontrollerad"]
    with open(sokvag, "w", newline="", encoding="utf-8") as fil:
        skrivare = csv.DictWriter(fil, fieldnames=faltnamn)
        skrivare.writeheader()
        skrivare.writerows(servrar)
    return sokvag
