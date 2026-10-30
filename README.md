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

Nach Schritt 2:

1. Welche Zeile im Client erzeugt den Client Stub? Welche Zeile im Server macht `antrag_pruefen()` von außen aufrufbar?
2. Erklären Sie die Ausgabe des Clients: Welche Funktionen bietet der Server an, welches Ergebnis liefert `antrag_pruefen()` für die beiden Anträge, und welchen Typ hat es?

Nach Schritt 3:

3. Suchen Sie den Funktionsnamen, die beiden Felder des Antrags und das Ergebnis. Wie sind Funktionsname, Feldnamen, Werte und Typen in der Nachricht dargestellt?

Nach Schritt 4:

4. Was weiß der Client nach dem ersten Lauf über den Antrag von Erika Mustermann?
5. Was ist durch den zweiten Lauf im Server entstanden?
