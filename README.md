# vs-xml-rpc
Beispiel für eine Client-Server RPC Kommunikation

Ein Antragsverfahren mit drei Bausteinen, aufgeteilt auf zwei Programme:

- `xml-rpc-client.py`: Frontend (`antrag_einreichen`)
- `xml-rpc-server.py`: Business-Logik (`antrag_pruefen`) und Datenhaltung (`antrag_speichern`)

Das Frontend ruft `antrag_pruefen` über XML-RPC im Server auf.

## Ablauf

1. Server in einem Terminal starten: `python xml-rpc-server.py`
2. Client in einem zweiten Terminal starten: `python xml-rpc-client.py`
3. Wireshark auf dem Loopback-Interface starten, Display Filter `tcp.port == 12345`, Client erneut starten. Eine Nachricht wählen und *Follow › TCP Stream* öffnen.
4. Server mit Strg+C beenden und mit Verzögerung neu starten: `python xml-rpc-server.py 8`. Den Client zweimal starten und die Ausgabe des Servers beobachten.

## Aufgaben

Die Kommentare im Code zeigen, welche Zeilen Client Stub und Server Stub bilden.

Nach Schritt 3:

1. Öffnen Sie eine Nachricht mit *Follow › TCP Stream*. Der Server Stub muss erkennen, welche Funktion gemeint ist, welcher Wert zu welchem Feld gehört und welchen Typ jeder Wert hat. Markieren Sie im Request die Stellen, an denen er das erkennt.

Nach Schritt 4:

Statt eines Ausfalls antwortet der Server zu spät: Er speichert den Antrag, sendet die Response aber erst nach der angegebenen Zahl von Sekunden. Der Client wartet höchstens 5 Sekunden.

2. Starten Sie den Client. Was geben Client und Server zum Antrag von Erika Mustermann aus?
3. Die Sachbearbeiterin sieht keine Bestätigung und sendet erneut: Starten Sie den Client noch einmal. Was gibt der Server jetzt aus?
4. Woran hätte der Client erkennen können, dass der Server nicht ausgefallen ist?
