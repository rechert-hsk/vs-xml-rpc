# XML RPC Beispiel: Client

# Der Client enthält das Frontend des Antragsverfahrens.
# Business-Logik und Datenhaltung laufen im Server (xml-rpc-server.py).

import xmlrpc.client

# Verbindung zum Server herstellen
# Der ServerProxy ist der Client Stub: Aufrufe an remote werden als Nachricht an den Server gesendet
# Der Server muss bereits gestartet sein, sonst kommt es zu einem Fehler
remote = xmlrpc.client.ServerProxy('http://localhost:12345/endpunkt')

# Test der Verbindung und liste alle verfügbaren Funktionen
print(remote.system.listMethods())


# Frontend
def antrag_einreichen(eingaben):
   # sieht aus wie ein lokaler Aufruf, die Funktion läuft aber im Server
   ergebnis = remote.antrag_pruefen(eingaben)
   print(ergebnis)
   print(type(ergebnis))


antrag_einreichen({"name": "Erika Mustermann", "anliegen": "Wohnsitz ummelden"})
antrag_einreichen({"name": "Max Mustermann", "anliegen": ""})
