# Multi-Agent-Architektur für einen Musik-Lernassistenten

## Übersicht

Das System besteht aus mehreren spezialisierten Agenten, die gemeinsam einen personalisierten Musikunterricht ermöglichen.

```text
User
 │
 ▼
Orchestrator Agent
 │
 ├── Goal Agent
 ├── Curriculum Agent
 ├── Practice Agent
 ├── Theory Agent
 ├── Feedback Agent
 ├── Progress Agent
 └── Motivation Agent
```

## Komponenten

### Orchestrator Agent

Der zentrale Koordinator des Systems.

**Aufgaben**

- Nimmt Anfragen des Nutzers entgegen.
- Entscheidet, welche Agenten benötigt werden.
- Koordiniert den Informationsfluss.
- Fasst Ergebnisse zu einer Antwort zusammen.

---

### Goal Agent

Versteht die Lernziele des Nutzers.

**Verantwortlichkeiten**

- Lernziel analysieren
- Erfahrungsniveau bestimmen
- Verfügbare Lernzeit erfassen
- Instrument erkennen
- Prioritäten definieren

**Beispiel**

> "Ich möchte in drei Monaten Jazz-Piano lernen und täglich 30 Minuten üben."

---

### Curriculum Agent

Erstellt einen individuellen Lernplan.

**Verantwortlichkeiten**

- Lernmodule auswählen
- Reihenfolge festlegen
- Meilensteine definieren
- Lernfortschritt berücksichtigen

**Beispiel**

1. Noten lesen
2. Dur-Tonleitern
3. Dreiklänge
4. Akkordfolgen
5. Improvisation

---

### Practice Agent

Generiert tägliche Übungen.

**Verantwortlichkeiten**

- Technikübungen
- Rhythmusübungen
- Hörtraining
- Wiederholungen
- Hausaufgaben

**Beispiel**

- C-Dur Tonleiter
- Rhythmus klatschen
- Akkorde erkennen
- Melodie nachspielen

---

### Theory Agent

Erklärt musikalische Inhalte.

**Verantwortlichkeiten**

- Notenlehre
- Intervalle
- Akkorde
- Harmonielehre
- Rhythmus
- Tonleitern

**Beispiel**

> "Ein Dur-Akkord besteht aus Grundton, großer Terz und Quinte."

---

### Feedback Agent

Bewertet Antworten und Übungen.

**Verantwortlichkeiten**

- Fehler erkennen
- Lösungen erklären
- Verbesserungsvorschläge geben
- Hinweise statt nur Bewertungen liefern

**Beispiele**

- Rhythmus korrekt
- Akkord falsch gegriffen
- Tempo zu schnell
- Tonhöhe korrekt

---

### Progress Agent

Verwaltet den Lernfortschritt.

**Verantwortlichkeiten**

- absolvierte Lektionen speichern
- Statistiken führen
- Schwächen erkennen
- Wiederholungen planen

**Gespeicherte Daten**

- Übungen
- Punkte
- Erfolgsquote
- Übungszeit
- letzte Lektion

---

### Motivation Agent

Passt den Lernprozess an den Nutzer an.

**Verantwortlichkeiten**

- Motivation fördern
- Schwierigkeit anpassen
- Erfolge feiern
- Pausen empfehlen
- Ziele aktualisieren

**Beispiele**

> "Du hast bereits fünf Tage hintereinander geübt."

> "Die Übungen werden etwas schwieriger."

---

## Datenfluss

```text
User
   │
   ▼
Orchestrator Agent
   │
   ├────────► Goal Agent
   │
   ├────────► Curriculum Agent
   │
   ├────────► Practice Agent
   │
   ├────────► Theory Agent
   │
   ├────────► Feedback Agent
   │
   ├────────► Progress Agent
   │
   └────────► Motivation Agent
                     │
                     ▼
              Personalisierte Antwort
                     │
                     ▼
                    User
```


## Mögliche Erweiterungen

- Ear Training Agent
- Chord Recognition Agent
- Composition Agent
- Improvisation Coach
- Performance Evaluation Agent
- AI Piano Tutor
- Voice Training Agent
- MIDI Analysis Agent
- Audio Feedback Agent