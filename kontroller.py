import subprocess
from datetime import datetime


def svarar_pa_ping(adress):
    resultat = subprocess.run(
        ["ping", "-c", "1", "-W", "2", adress],
        capture_output=True,
    )
    return resultat.returncode == 0


def kontrollera_server(server):
    if svarar_pa_ping(server["adress"]):
        server["status"] = "up"
    else:
        server["status"] = "down"
    server["senast_kontrollerad"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    return server["status"]
