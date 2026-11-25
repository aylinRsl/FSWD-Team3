[← Design Decisions](README.md)

# 01: Kategorien statt Suchleiste und umfangreicher Filtermaske
| Property | Value |
|--:|:--|
| **Status** | 🟢 Decided |
| **Updated** | 16.11.2026 |
| **Lead** | [Miriam Kouweider] (docs/contributors/miriam-kouweider.md)

## Problem Statement

Bei der Gestaltung der Beitragsübersicht stellte sich die Frage, wie Nutzer\*innen passende Anfragen und Angebote möglichst einfach finden können. Dabei wollten wir sowohl das gezielte Finden bestimmter Themen als auch das offene Durchstöbern der Beiträge unterstützen. Die Oberfläche sollte übersichtlich bleiben und ohne viele Eingaben bedienbar sein.

## Decision

Wir entschieden uns für wenige, direkt sichtbare Kategorien, der den Großteil der erwarteten Anfragen abdecken sollen. Beim Erstellen eines Beitrags wählen Nutzer\*innen eine passende Kategorie aus. Für Beiträge, die sich keiner der vorgegebenen Kategorien zuordnen lassen, steht "Sonstiges“ zur Verfügung.

In der Übersicht können Nutzer\*innen mit einem Klick die Beiträge einer Kategorie anzeigen lassen. Über "Alle“ gelangen sie zurück zur vollständigen Übersicht.

Diese Lösung benötigt wenige Bedienschritte und vermeidet eine umfangreiche Filtermaske mit mehreren Auswahlmöglichkeiten. Die vorgegebenen Kategorien sorgen außerdem für eine einheitliche Zuordnung der Beiträge und erleichtern die Orientierung.

Im ursprünglichen UI-Entwurf war eine Suchleiste vorgesehen. Wir entschieden uns dagegen, da wir davon ausgehen, dass Nutzer\*innen die Plattform auch ohne konkreten Suchbegriff besuchen, um aktuelle Beiträge anzusehen und mögliche Unterstützung anzubieten. Kategorien ermöglichen ihnen einen Einstieg, ohne vorher genau wissen zu müssen, wonach sie suchen.

Außerdem können ähnliche Anfragen unterschiedlich beschrieben werden, beispielsweise als "Mathehilfe" oder "Nachhilfe in Mathematik“. Eine einfache Textsuche könnte dadurch relevante Beiträge übersehen. Eine gemeinsame Kategorie "Lernen & Nachhilfe“ bündelt diese Beiträge unabhängig von ihrer Formulierung.

*Decision was taken by:* Miriam Kouweider

## Regarded options

We considered the following options:

+ Suchleiste
+ Umfangreicher Filtermaske

| Criterion | Umfangreiche Filtermaske | Suchleiste | Kategorien |
| --- | --- | --- | --- |
| **UI-Design** | ❌ Mehrere Auswahlfelder oder separater Filterbereich erforderlich | ❌ Zusätzliches Eingabefeld und gegebenenfalls Suchbutton | ✔️ Direkt sichtbare Themenauswahl |
| **Implementation** | ❌ Mehrere Filter und deren Kombinationen verarbeiten und testen | ❌ Zusätzliche Verarbeitung von Suchbegriffen erforderlich | ✔️ Abfrage anhand einer vorgegebenen Kategorie |
| **Search interaction** | ✔️ Präzise Eingrenzung | ✔️ Konkrete Suche möglich (passender Suchbegriff nötig) | ❌ Themenauswahl mit einem Klick, aber nur grobe Eingrenzung |