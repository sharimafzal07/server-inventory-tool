import lagring
import kontroller

def visa_servrar(servrar, miljo="alla"):
    print("NAMN      ADRESS          MILJO  ROLL                STATUS   SENAST KONTROLLERAD")
    print("--------------------------------------------------------------------------------")
    for server in servrar:
        if miljo != "alla" and server["miljo"] != miljo:
            continue
        print(f"{server['namn']:<10}{server['adress']:<16}{server['miljo']:<7}{server['roll']:<20}{server['status']:<9}{server['senast_kontrollerad']}")

def ar_giltig_miljo(miljo):
    if miljo == "dev" or miljo == "test" or miljo == "prod":
        return True
    else:
        return False

def namn_finns(servrar, namn):
    for server in servrar:
        if server["namn"] == namn:
            return True
    return False

def hitta_server(servrar, namn):
    for server in servrar:
        if server["namn"] == namn:
            return server
    return None

def lagg_till_server(servrar):
    namn = input("Namn: ")
    if namn_finns(servrar, namn):
        print("Det finns redan en server med det namnet.")
        return
    adress = input("Adress: ")
    miljo = input("Miljö (dev/test/prod): ")
    while not ar_giltig_miljo(miljo):
        print("Ogiltig miljö. Ange dev, test eller prod.")
        miljo = input("Miljö (dev/test/prod): ")
    roll = input("Roll: ")
    server = {
        "namn": namn,
        "adress": adress,
        "miljo": miljo,
        "roll": roll,
        "status": "unknown",
        "senast_kontrollerad": "",
    }
    servrar.append(server)
    print(f"Servern {namn} lades till.")

def ta_bort_server(servrar):
    namn = input("Namn på servern som ska tas bort: ")
    server = hitta_server(servrar, namn)
    if server is None:
        print("Hittade ingen server med det namnet.")
        return
    if server["miljo"] == "prod":
        svar = input("Det här är en prod-server. Skriv ja för att bekräfta: ")
        if svar != "ja":
            print("Avbröt. Ingenting togs bort.")
            return
    servrar.remove(server)
    print(f"Servern {namn} togs bort.")

def visa_meny():
    print()
    print("=== Server Inventory Tool ===")
    print("1. Visa alla servrar")
    print("2. Visa servrar i en miljö")
    print("3. Lägg till en server")
    print("4. Ta bort en server")
    print("5. Kontrollera en server")
    print("6. Kontrollera alla servrar")
    print("7. Exportera rapport (CSV)")
    print("8. Avsluta")

def kor_meny():
    filnamn = lagring.hamta_datafil()
    servrar = lagring.las_servrar(filnamn)
    while True:
        visa_meny()
        val = input("Välj ett alternativ: ")
        if val == "1":
            visa_servrar(servrar)
        elif val == "2":
            miljo = input("Miljö (dev/test/prod): ")
            visa_servrar(servrar, miljo)
        elif val == "3":
            lagg_till_server(servrar)
            lagring.spara_servrar(servrar, filnamn)
        elif val == "4":
            ta_bort_server(servrar)
            lagring.spara_servrar(servrar, filnamn)
        elif val == "8":
            print("Hej då!")
            break
        else:
            print("Ogiltigt val, försök igen.")
