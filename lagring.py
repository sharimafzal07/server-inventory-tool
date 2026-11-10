import json
import os
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
