import xmlrpc.client

# Verbindung zum Server herstellen
# Der Server muss bereits gestartet sein, sonst kommt es zu einem Fehler
remote = xmlrpc.client.ServerProxy('http://localhost:12345/endpunkt')

# Test der Verbindung und liste alle verfügbaren Funktionen
print(remote.system.listMethods())

addition_result = remote.addition(5, 7)
print(f"addition_result = {addition_result}")
print(type(addition_result))

string_add_result = remote.string_add("bar")
print(f"string_add_result = {string_add_result}")
print(type(string_add_result))


