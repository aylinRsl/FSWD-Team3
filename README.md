# StudyNet

>Eine Plattform für gegenseitige Unterstützung, Vernetzung und Gemeinschaft in Studierendenwohnheimen.

>Bewohner\*Innen können Hilfe suchen oder anbieten, verlorene und gefundene Gegenstände melden sowie Tools und Skills teilen. 

>Mehr dazu in der [Dokumentation](docs/README.md) sowie in der  [Value Proposition](docs/01-value-proposition.md).

> Projekt im Rahmen des Moduls Full-Stack Web Development (HWR Berlin), Team 4 "StudyNet".

## Team

* [Aylin Rasul C.](docs/contributors/aylin-rasulcervino.md)
* [Miriam Kouweider](docs/contributors/miriam-kouweider.md)
* [Nastasya Bernadette](docs/contributors/nastasya-bernadette.md)
* [Narin Edebali](docs/contributors/narin-edebali.md)

## Features

* Registrierung und Login
* Identitätsprüfung für Wohnheim-Bewohner\*Innen
* Beiträge erstellen und kategorisieren
* Beiträge Suchen
* Privatnachrichten verschicken
* Statusverwaltung (offen / erledigt)

> TODO: Liste mit dem tatsächlich umgesetzten Stand abgleichen/laufend aktualisieren.

## Tech Stack

* Python, Flask
* SQLite
* HTML, CSS

> TODO: Anpassen

## Setup

**Voraussetzungen:** Python 3.x, Git

1. Repository klonen:
   ```
   git clone https://github.com/aylinRsl/FSWD-Team4.git
   cd FSWD-Team4
   ```
2. Virtuelle Umgebung erstellen und aktivieren:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
3. Abhängigkeiten installieren:
   ```
   pip install -r requirements.txt
   ```
4. App starten:
   ```
   flask run --reload
   ```
5. Im Browser öffnen: http://127.0.0.1:5000/

> TODO: wenn fertig nochmal überprüfen

## Usage

> TODO: Kurz beschreiben, wie man die App nutzt, z. B.:
> 1. Registrieren und einloggen
> 2. Beitrag erstellen
> 3. Beiträge suchen und filtern
> 4. Per Privatnachricht Kontakt aufnehmen
> 5. Beitrag als erledigt markieren
>
> Optional: Screenshots unter `docs/assets/`.

## Projektstruktur

```
FSWD-Team4/
├── app.py
├── requirements.txt
├── docs/
└── README.md
```

> TODO: ergänzen

## Dokumentation

Die komplette Projektdokumentation liegt im Ordner [`docs/`](docs/README.md).

## Lizenz

Siehe [LICENSE](LICENSE).