import argparse
import sys

import kontroller
import lagring
import meny


def skapa_tolk():
    tolk = argparse.ArgumentParser(
        description="Server Inventory Tool - håll koll på dina servrar"
    )
    tolk.add_argument("--lista", action="store_true", help="visa alla servrar")
    tolk.add_argument(
        "--miljo", default="alla", help="filtrera listan på miljö (dev/test/prod)"
    )
    tolk.add_argument(
        "--kontrollera", metavar="NAMN", help="kontrollera en server med ping"
    )
    tolk.add_argument(
        "--kontrollera-alla", action="store_true", help="kontrollera alla servrar"
    )
    tolk.add_argument(
        "--export", action="store_true", help="exportera en CSV-rapport"
    )
    return tolk


def main():
    # Utan flaggor startar den interaktiva menyn
    if len(sys.argv) == 1:
        meny.kor_meny()
        return

    args = skapa_tolk().parse_args()
    filnamn = lagring.hamta_datafil()
    servrar = lagring.las_servrar(filnamn)
    utgangskod = 0

    if args.lista:
        meny.visa_servrar(servrar, args.miljo)

    if args.kontrollera:
        server = meny.hitta_server(servrar, args.kontrollera)
        if server is None:
            print(f"Hittade ingen server med namnet {args.kontrollera}.")
            utgangskod = 1
        else:
            status = kontroller.kontrollera_server(server)
            print(f"{server['namn']} är {status}.")
            if status == "down":
                utgangskod = 1
            lagring.spara_servrar(servrar, filnamn)

    if args.kontrollera_alla:
        for server in servrar:
            status = kontroller.kontrollera_server(server)
            print(f"{server['namn']} är {status}.")
            if status == "down":
                utgangskod = 1
        lagring.spara_servrar(servrar, filnamn)

    if args.export:
        sokvag = lagring.exportera_csv(servrar)
        print(f"Rapporten sparades i {sokvag}")

    sys.exit(utgangskod)


if __name__ == "__main__":
    main()
