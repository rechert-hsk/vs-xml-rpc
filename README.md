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

1. Welche Zeilen übernehmen die Aufgabe Ihres Pseudocodes aus der Vorlesung? Ordnen Sie zu: die Funktion `antrag_pruefen` am Arbeitsplatz und die Schleife im Rechenzentrum.

Nach Schritt 3:

2. Öffnen Sie eine Nachricht mit *Follow › TCP Stream*. Der Server Stub muss erkennen, welche Funktion gemeint ist, welcher Wert zu welchem Feld gehört und welchen Typ jeder Wert hat. Markieren Sie im Request die Stellen, an denen er das erkennt.

Nach Schritt 4:

Die Zahl beim Start des Servers legt fest, wie viele Sekunden er nach dem Speichern wartet, bevor er antwortet. Der Client wartet höchstens 5 Sekunden auf eine Response.

3. Starten Sie den Client zweimal. Notieren Sie, was Client und Server zum Antrag von Erika Mustermann ausgeben.
4. Vergleichen Sie mit Ihrer Vorhersage aus der Vorlesung: Was stimmt, was ist anders?
