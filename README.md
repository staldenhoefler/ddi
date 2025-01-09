# Datenbankdesign und Implementierung

Dieses Projekt wurde im Rahmen des Moduls **Datenbankdesign und Implementierung (DDI)** entwickelt 
und umfasst die Umsetzung einer Problemstellung mit sowohl relationalen als auch nicht-relationalen Datenbanken. 
Der Fokus liegt auf dem Vergleich beider Ansätze hinsichtlich Flexibilität und Speicherbedarf.

## Zielsetzung

Die Aufgabe besteht darin:
- Eine reale Problemstellung, z. B. die Datenverwaltung eines Online-Shops, zu modellieren.
- Diese Daten sowohl in einer SQL- als auch einer NoSQL-Datenbank zu implementieren.
- Beide Datenbanken mit denselben Datensätzen zu füllen und anschließend zu vergleichen.
- Die Ergebnisse in einem Bericht zu dokumentieren.

## Features

- Modellierung eines Online-Shops mit Entitäten wie Produkten, Kunden, Bestellungen und Bewertungen.
- Nutzung einer relationalen Datenbank (Hier PostgreSQL).
- Nutzung einer NoSQL-Datenbank (Hier MongoDB).
- Vergleich beider Ansätze anhand der Flexibilität und des Speicherbedarfs.


## Projektstruktur
TODO: Update project structure
- `models/`: Enthält die konzeptionellen Datenmodelle für SQL und NoSQL.
- `scripts/`: Skripte zur Erstellung und Befüllung der Datenbanken.
- `results/`: Messresultate und Vergleiche der Datenbanken.
- `report/`: Bericht, der die Problemstellung, die Implementierung und die Ergebnisse dokumentiert.

## Einrichtung

### Einrichtung der NoSQL-Datenbank
Ich verwende eine lokal laufende MongoDB Datenbank [MongoDB Community Edition](https://www.mongodb.com/try/download/community).
Mit dem Programm MongoDB Compass greife ich auf diese zu. 
Die Datenbank startet automatisch beim Hochfahren des Computers und ist unter 'mongodb://localhost:27017/' erreichbar.

Die Struktur sowie die Daten werden im Script `src/generate_all.py` erstellt und befüllt.

### Einrichtung der SQL-Datenbank
Ich verwende eine lokal laufende PostgreSQL Datenbank [Postgresql](https://www.postgresql.org/download/).
Ich greife mit PyCharm auf die Datenbank zu.
Die Datenbank startet automatisch beim Hochfahren des Computers und ist unter 'localhost:5432' 
mit Nutzernamen und Passwort erreichbar.

Für das Erstellen der Datenbankstruktur werden die beiden Scripte `src/CREATE_DATABASE.sql` und `src/CREATE_TABLES.sql` verwendet.
Die Daten werden im Script `src/Upload_data_postgres.py` umstrukturiert und in die Datenbank gefüllt.

## Autoren

- Denis Schatzmann
