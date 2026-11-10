import os

def hamta_datafil():
    return os.getenv("INVENTORY_DATAFIL", "servrar.json")
