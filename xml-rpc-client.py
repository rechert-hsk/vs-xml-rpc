# XML RPC Beispiel: Client

# Der Client enthält das Frontend des Antragsverfahrens.
# Business-Logik und Datenhaltung laufen im Server (xml-rpc-server.py).

import socket
import xmlrpc.client

# der Client wartet höchstens 5 Sekunden auf eine Response (Timeout)
socket.setdefaulttimeout(5)

# Verbindung zum Server herstellen
# Der ServerProxy ist der Client Stub. Er ersetzt die selbst geschriebene
# Funktion antrag_pruefen() am Arbeitsplatz: Er schreibt Funktionsname und
# Parameter in eine Nachricht (Marshalling), sendet sie als Request und
# wartet auf die Response.
# Der Server muss bereits gestartet sein, sonst kommt es zu einem Fehler
remote = xmlrpc.client.ServerProxy('http://localhost:12345/endpunkt')

# Test der Verbindung und liste alle verfügbaren Funktionen
print(remote.system.listMethods())


# Frontend
def antrag_einreichen(eingaben):
   try:
      # sieht aus wie ein lokaler Aufruf; die Funktion läuft aber im Server
      ergebnis = remote.antrag_pruefen(eingaben)
      print(ergebnis)
      print(type(ergebnis))
   except TimeoutError:
      print("keine Response nach 5 Sekunden:", eingaben)


antrag_einreichen({"name": "Erika Mustermann", "anliegen": "Wohnsitz ummelden"})
antrag_einreichen({"name": "Max Mustermann", "anliegen": ""})
