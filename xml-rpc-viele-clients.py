# XML RPC Beispiel: viele Clients gleichzeitig

# Vorführung für Sitzung 3: python xml-rpc-viele-clients.py 5
# Startet die angegebene Zahl von Clients gleichzeitig. Jeder hat einen eigenen
# Client Stub und wartet höchstens 5 Sekunden auf die Response (wie xml-rpc-client.py).
# Der Server muss vor jedem Lauf neu gestartet werden: Er bearbeitet auch die
# Requests noch, auf die kein Client mehr wartet.

import socket
import sys
import threading
import time
import xmlrpc.client

socket.setdefaulttimeout(5)

anzahl = int(sys.argv[1]) if len(sys.argv) > 1 else 5
start = time.monotonic()

def client(nummer):
   remote = xmlrpc.client.ServerProxy('http://127.0.0.1:12345/endpunkt')
   antrag = {"name": f"Client {nummer}", "anliegen": "Wohnsitz ummelden"}
   try:
      ergebnis = remote.antrag_pruefen(antrag)
   except socket.timeout:
      ergebnis = "keine Response nach 5 Sekunden"
   print(f"Client {nummer}: {ergebnis} (nach {time.monotonic() - start:.1f} s)\n", end="")

clients = [threading.Thread(target=client, args=(n,)) for n in range(1, anzahl + 1)]
for c in clients:
   c.start()
for c in clients:
   c.join()
