import subprocess
from datetime import datetime


def svarar_pa_ping(adress):
    # -c 1: skicka ett ping, -W 2: vänta högst 2 sekunder på svar
    resultat = subprocess.run(
        ["ping", "-c", "1", "-W", "2", adress],
        capture_output=True,
    )
    # Exitkod 0 betyder att servern svarade
    return resultat.returncode == 0


def kontrollera_server(server):
    # Kontrollen finns bara här, så menyn och kommandoraden använder samma kod
    if svarar_pa_ping(server["adress"]):
        server["status"] = "up"
    else:
        server["status"] = "down"
    server["senast_kontrollerad"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    return server["status"]


def kontrollera_alla_servrar(servrar):
    # Skriver ut resultatet per server och returnerar hur många som är nere
    antal_nere = 0
    for server in servrar:
        status = kontrollera_server(server)
        print(f"{server['namn']} är {status}.")
        if status == "down":
            antal_nere += 1
    return antal_nere
