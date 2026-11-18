# Server Inventory Tool

Det här är ett program i Python som håller reda på servrar. Man kan lägga till och ta bort servrar, kolla om de svarar och spara en rapport. Programmet är gjort som inlämningsuppgift i Python-kursen (MALM26).

Programmet kan användas på två sätt: med en meny där man väljer med siffror, eller direkt från kommandoraden med flaggor.

## Vad som krävs

- Python 3 (jag har testat med version 3.14)
- Linux eller WSL, eftersom programmet använder kommandot `ping`
- Inget extra behöver installeras. Programmet använder bara det som följer med Python.

## Så startar man programmet

Gå först till projektmappen i terminalen. Kör sedan kommandona därifrån.

### Menyn

```
python3 main.py
```

Då visas en meny:

```
1. Visa alla servrar
2. Visa servrar i en miljö
3. Lägg till en server
4. Ta bort en server
5. Kontrollera en server
6. Kontrollera alla servrar
7. Exportera rapport (CSV)
8. Avsluta
```

Man skriver en siffra och trycker Enter. Menyn visas igen efter varje val, tills man väljer 8.

### Kommandoraden

| Kommando | Vad som händer |
|----------|----------------|
| `python3 main.py --help` | Visar en hjälptext |
| `python3 main.py --lista` | Skriver ut alla servrar |
| `python3 main.py --lista --miljo prod` | Skriver bara ut servrar i miljön prod |
| `python3 main.py --kontrollera web01` | Kontrollerar servern web01 |
| `python3 main.py --kontrollera-alla` | Kontrollerar alla servrar |
| `python3 main.py --export` | Skapar en CSV-rapport |

### Exit-koder

När programmet körs med flaggor ger det tillbaka en kod som visar hur det gick:

- `0` betyder att allt gick bra
- `1` betyder att en server inte hittades, eller att minst en kontrollerad server är nere

Man ser koden genom att skriva `echo $?` direkt efter att programmet har körts.

## Datafilen

Servrarna sparas i filen `servrar.json`. Varje server har sex fält:

| Fält | Vad det är |
|------|------------|
| `namn` | Servens namn, till exempel `web01` |
| `adress` | IP-adress eller domännamn |
| `miljo` | Måste vara `dev`, `test` eller `prod` |
| `roll` | Vad servern används till |
| `status` | `up`, `down` eller `unknown` |
| `senast_kontrollerad` | När servern kontrollerades senast |

Programmet följer med fyra servrar från början. Om filen saknas startar programmet ändå, med en tom lista. Filen skapas när något sparas första gången.

### Välja en annan datafil

Namnet på datafilen kan ändras med miljövariabeln `INVENTORY_DATAFIL`. Om den inte är satt används `servrar.json`.

Så här kan man använda en testfil i stället:

```
export INVENTORY_DATAFIL=test.json
python3 main.py --lista
unset INVENTORY_DATAFIL
```

`unset` tar bort variabeln igen. Det är bra för att kunna testa utan att ändra de riktiga servrarna.

## Rapporter

När man väljer 7 i menyn, eller kör `--export`, skapas en CSV-fil i mappen `rapporter/`. Filnamnet innehåller datum och tid, till exempel `inventering_2026-11-17_2053.csv`. Mappen skapas av programmet om den inte finns. Den ligger i `.gitignore`, så rapporterna kommer inte med i Git.

## Hur projektet är uppbyggt

| Fil | Vad den gör |
|-----|-------------|
| `main.py` | Där programmet startar. Läser flaggor med `argparse`. Utan flaggor startas menyn. |
| `meny.py` | Menyn och funktionerna för att visa, lägga till och ta bort servrar |
| `lagring.py` | Läser och sparar JSON, skapar CSV-rapporter och hittar datafilen |
| `kontroller.py` | Kollar om en server svarar med `ping` och uppdaterar status |
| `servrar.json` | Startdata med fyra servrar |
| `.gitignore` | Gör att `__pycache__/` och `rapporter/` inte kommer med i Git |
| `REDOGORELSE.md` | Svar på frågorna om hur uppgiften är löst |

## Hur det fungerar

- När programmet startar läses servrarna från JSON-filen in i en lista. Varje server är en dictionary.
- Varje gång något ändras sparas listan till filen direkt.
- För att kontrollera en server körs `ping -c 1 -W 2 adress`. Om servern svarar blir statusen `up`, annars `down`. Samma funktion används av både menyn och kommandoraden.
- När man lägger till en server måste miljön vara dev, test eller prod. Annars frågar programmet igen.
- Man kan inte lägga till två servrar med samma namn.
- När man tar bort en server i miljön prod frågar programmet en extra gång: man måste skriva `ja`.
- Om man skriver ett menyval som inte finns, eller ett servernamn som inte finns, skriver programmet ett meddelande och fortsätter.

## Begränsningar

- Programmet fungerar bara där kommandot `ping` finns, till exempel Linux och WSL.
- Om en server inte svarar på ping räknas den som `down`, även om den kanske är igång. Vissa nätverk blockerar ping.
