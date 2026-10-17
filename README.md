# vs-xml-rpc
Beispiel für eine Client-Server RPC Kommunikation

Ein Antragsverfahren mit drei Bausteinen, aufgeteilt auf zwei Programme:

- `xml-rpc-client.py`: Frontend (`antrag_einreichen`)
- `xml-rpc-server.py`: Business-Logik (`antrag_pruefen`) und Datenhaltung (`antrag_speichern`)

Das Frontend ruft `antrag_pruefen` über XML-RPC im Server auf.

## Ablauf

1. Server in einem Terminal starten: `python3 xml-rpc-server.py`
2. Client in einem zweiten Terminal starten: `python3 xml-rpc-client.py`
3. Wireshark auf dem Loopback-Interface starten, Display Filter `tcp.port == 12345`, Client erneut starten. Eine Nachricht wählen und *Follow › TCP Stream* öffnen.
4. Server mit Strg+C beenden und den Client erneut starten.

## Aufgaben

1. Erklären Sie die Ausgabe des Clients: Welche Funktionen bietet der Server an, welches Ergebnis liefert `antrag_pruefen` für die beiden Anträge, und welchen Typ hat es?
2. Suchen Sie im TCP Stream den Funktionsnamen, die beiden Felder des Antrags und das Ergebnis. Notieren Sie, wie Name, Feldnamen, Werte und Typen in der Nachricht dargestellt werden.
3. Erklären Sie die Fehlermeldung aus Schritt 4. Warum kann dieser Fehler bei einem lokalen Funktionsaufruf nicht auftreten?
