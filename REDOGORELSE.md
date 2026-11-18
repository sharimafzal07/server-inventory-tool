# Redogörelse

## Fråga 1: tre konstruktioner

* I `hitta_server` i `meny.py` använder jag `for server in servrar:` för att gå igenom listan med servrar en i taget. Syntaxen fungerar så att `server` får ett nytt värde ur listan vid varje varv, och raderna under är indragna för att visa vad som ligger inuti loopen och körs en gång per server.
* I `ta_bort_server` i `meny.py` kollar jag med `if server["miljo"] == "prod":` om servern ligger i miljön prod. Dubbla likhetstecken `==` jämför två värden och ger sant eller falskt, medan ett enda `=` skulle tilldela ett värde. Raden slutar på kolon `:` och raderna under är indragna för att visa vad som bara körs om villkoret stämmer.
* I `svarar_pa_ping` i `kontroller.py` skriver jag `return resultat.returncode == 0`, som ger tillbaka `True` om servern svarade på pingen och `False` om den inte gjorde det. Jämförelsen med `==` blir själv ett `True` eller `False`, och `return` skickar det värdet tillbaka till den som anropade funktionen.

## Fråga 2: lista med dictionaries

Jag lagrar servrarna i en lista, och varje server är en dictionary. Listan valde jag eftersom jag inte vet hur många servrar som kommer finnas, och den växer eller krymper med `append` och `remove` i `meny.py`. Dictionaryn gör att jag kan hämta en uppgift med namn, till exempel `server["adress"]`, i stället för att komma ihåg en plats. Allt är text: namn som `"web01"`, adress som `"127.0.0.1"`, miljö som `"prod"` och status som `"up"`. `senast_kontrollerad` börjar som en tom sträng och fylls i först när servern har pingats.

## Fråga 3: JSON och CSV

JSON använder jag när programmet ska komma ihåg sin data mellan körningarna. Det sparar listan med dictionaries precis som den är, så `las_servrar` i `lagring.py` får tillbaka samma struktur. CSV är mer som en vanlig tabell. Med `exportera_csv` får jag en fil som går att öppna i Excel, vilket passar när en människa ska läsa en rapport. Så JSON är för programmets eget minne och CSV är för att visa upp något.

## Fråga 4: moduler och ansvar

Jag har delat upp koden i fyra filer så att var och en har ett eget jobb:

* `main.py` startar programmet, läser flaggorna med `argparse` och avgör om menyn eller ett kommando ska köras.
* `meny.py` hanterar menyn samt att visa, lägga till, ta bort och hitta servrar.
* `lagring.py` tar hand om filerna: spara och läsa JSON, skriva CSV och lista ut var datafilen ligger.
* `kontroller.py` pingar servrarna och uppdaterar status. Menyn och kommandoraden använder samma funktioner därifrån.

## Fråga 5: standardbiblioteket

* `json` och `csv` för att spara servrarna och skriva rapporten.
* `os` för att läsa miljövariabeln `INVENTORY_DATAFIL`.
* `pathlib` för att se om datafilen finns och för att skapa mappen `rapporter/`.
* `datetime` för tidsstämplarna, både i filnamnet och i `senast_kontrollerad`.
* `subprocess` för att köra `ping`.
* `argparse` för flaggorna i `main.py`.
* `sys` för `sys.argv` och för att avsluta med rätt exit-kod.

## Fråga 6: tre exempel på god praxis

1. Ping-logiken ligger bara i `kontrollera_server` i `kontroller.py`. Både menyn och kommandoraden anropar den, så en ändring behöver göras på ett enda ställe.
2. Datafilens namn kommer från en miljövariabel med ett standardvärde (`hamta_datafil`). Då kan jag testa med en annan fil utan att röra koden eller min riktiga data.
3. Funktionerna är små och gör en sak var, som `ar_giltig_miljo` och `hitta_server`, och allt de behöver skickas in som parametrar. Det gör dem enkla att förstå och testa.

## Fråga 7: källor och hjälpmedel

* Kursens presentationer, med namn: introduktion, loopar, listor och dictionaries, funktioner, moduler, filer, JSON och CSV, standardbiblioteket, miljövariabler och CLI
* Lärarens uppgiftstext (gisten) med kraven G1-G20 och startdatan
* Kursprojektet Service Status Tool som läraren byggde, om du tittade på det som förebild
* Pythons dokumentation på docs.python.org, bara om du faktiskt slagit upp något där
* Git och GitHub, för versionshanteringen
* Terminalen i WSL och editorn nano, om du vill nämna verktygen
* Jag har även använt mig av Claude AI för att förstå begrepp och några små detaljer som jag inte förstod direkt från kursmaterialen och sedan lite hjälp med principer också.
