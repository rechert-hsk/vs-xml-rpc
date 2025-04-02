# XML RPC Beispiel

# Beispiel einer einfachen RPC Anwendung. Die Umsetzung erfolgt mittels der XML-RPC Bibliothek: 
# https://docs.python.org/3/library/xmlrpc.server.html

# Die Python Bibliothek xmlrpc liefert schon fertige Server-Komponenten
# Diese müssen mittels des import ins Program integriert werden
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Endpunkte: -> schema://host:port/<rpc_paths>
# wir definineren unter welcher URL der Server die RPC Anfragen entgegen nimmt
# Ein RequestHandler ist für die Verarbeitung der Anfragen zuständig
class RequestHandler(SimpleXMLRPCRequestHandler):
   rpc_paths = ('/endpunkt',)

# Der Server wird auf localhost Port 12345 gestartet und nutzt der o.g. RequestHandler
with SimpleXMLRPCServer(('localhost', 12345), requestHandler=RequestHandler) as server:
   
   # unser einfacher Server kann zwei Funktionen ausführen
   # addition und string_add   
   def remote_addition(a, b):
      return a + b
   
   def remote_string_add(input):
      return "foo" + input

   #  publizieren der funktion unter einem selbst gewählten namen
   server.register_function(remote_addition, 'addition')
   server.register_function(remote_string_add, "string_add")

   # wir registrieren zusätzliche Funntionen, die uns über Über die verfügbaren Funktionen des Servers informieren
   # system.listMethods, system.methodHelp and system.methodSignature
   server.register_introspection_functions()

   # der Server wird gestartet und wartet auf Anfragen
   server.serve_forever()