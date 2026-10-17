# XML RPC Beispiel: Server

# Beispiel einer einfachen RPC Anwendung. Die Umsetzung erfolgt mittels der XML-RPC Bibliothek:
# https://docs.python.org/3/library/xmlrpc.server.html

# Der Server enthält Business-Logik und Datenhaltung des Antragsverfahrens.
# Das Frontend läuft im Client (xml-rpc-client.py).

# Die Python Bibliothek xmlrpc liefert schon fertige Server-Komponenten
# Diese müssen mittels des import ins Program integriert werden
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Endpunkte: -> schema://host:port/<rpc_paths>
# wir definieren unter welcher URL der Server die RPC Anfragen entgegen nimmt
# Ein RequestHandler ist für die Verarbeitung der Anfragen zuständig
class RequestHandler(SimpleXMLRPCRequestHandler):
   rpc_paths = ('/endpunkt',)


# Datenhaltung
# Die Anträge liegen nur im Speicher des Servers und gehen beim Beenden verloren
antraege = {}

def antrag_speichern(antrag):
   nummer = f"A-{len(antraege) + 1:04d}"
   antraege[nummer] = antrag
   return nummer


# Business-Logik
# Ein Antrag ist vollständig, wenn Name und Anliegen ausgefüllt sind
def vollstaendig(antrag):
   return bool(antrag.get("name")) and bool(antrag.get("anliegen"))

def antrag_pruefen(antrag):
   if not vollstaendig(antrag):
      return "unvollständig"
   nummer = antrag_speichern(antrag)
   return "eingegangen: " + nummer


# Der Server wird auf localhost Port 12345 gestartet und nutzt der o.g. RequestHandler
with SimpleXMLRPCServer(('localhost', 12345), requestHandler=RequestHandler) as server:

   # publizieren der Funktion unter einem selbst gewählten Namen
   # nur antrag_pruefen ist von außen aufrufbar, antrag_speichern bleibt intern
   server.register_function(antrag_pruefen, 'antrag_pruefen')

   # wir registrieren zusätzliche Funktionen, die uns über die verfügbaren Funktionen des Servers informieren
   # system.listMethods, system.methodHelp and system.methodSignature
   server.register_introspection_functions()

   # der Server wird gestartet und wartet auf Anfragen
   print("Server läuft auf http://localhost:12345/endpunkt (Beenden mit Strg+C)")
   server.serve_forever()
