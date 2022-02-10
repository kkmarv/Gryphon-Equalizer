# Gryphon Equalizer

Der Gryphon Equalizer (zusammengesetzt aus den Wörtern Python und Graphic Equalizer) ist ein 10-Band Equalizer, mit
dessen Hilfe beliebige mono Wave Dateien eingelesen und deren Frequenzbänder grafisch manipuliert werden können.

Er ist das Ergebnis des Moduls "Multimediale Signalverarbeitung" der Hochschule Anhalt in Köthen, in dem Studierende ein
Programm entwickeln und programmieren sollen. Die einzige Einschränkung dabei ist die thematische Gebundenheit an einen
multimedialen Anwendungsfall.

## Inhalt

1. [Motivation](#motivation)
2. [Ziel]()
3. [Konzept]()
4. [Umsetzung]()
5. [Fazit zum Projekt]()
6. [Future Work]()

## Motivation

## Ziel

(Was ist das Problem bzw. was wollen wir erreichen)

Im Folgenden sind die zu Beginn der Projektphase von uns selbst erstellten Anforderungen an das Endprodukt.  
Diese enthalten sowohl harte Anforderungen, also solche, die wir unbedingt zum Ende des Bearbeitungszeitraums vollendet
haben wollen, als auch nice-to-have Anforderungen, die dem Equalizer durchaus gerecht werden würden, aber von uns als
nicht allzu wichtig eingestuft werden.

### Harte Anforderungen

Der Equalizer soll:

- eine grafische Benutzeroberfläche für einen 10-Band Equalizer enthalten.
- (mono) Wave Dateien einlesen können und:
    - zehn Bänder im Frequenzbereich manipulieren können, sowie
    - abspeichern können.
- mindestens zur Benutzung unter Windows 10 funktionieren

### Nice-to-Haves

Der Equalizer könnte außerdem:

- stereo Wave Dateien einlesen
- eine Funktion zur Vorschau des (manipulierten) Signals enthalten.
- einen Mikrofon-Stream:
    - aufnehmen und abspeichern, sowie
    - live manipulieren und ausgeben.

## Konzept

(Wie wollen das Problem theoretisch, konzeptuell angehen)

Bilder und Zeugs aus den Issues hierhin.

## Umsetzung

(So wurde es praktisch umgesetzt)

Code Dokumentation hierhin.

Die verwendeten Pakete können der [requirements.txt](./requirements.txt) entnommen werden.

## Fazit zum Projekt

(Welche Schlussfolgerung ziehen wir aus dem Arbeitsprozess)

## Future work

Unserer Auffassung nach ist dieses Projekt nur bedingt und eher zur eigenen Übung in der Zukunft nutzbar, da es an sich
keinen Mehrwert bietet. Es gibt bereits einige gute Equalizer und DAWs auf dem Markt, die sogar als open-source Software
vertrieben werden und deutlich effizienter gestaltet sind, als dieses.  
Dennoch wollen wir hier einen kleinen Ausblick auf Optionen zur Weiterentwicklung des Equalizers geben.

Mögliche Einstiegspunkte zur weiteren Bearbeitung (ob nun durch uns oder durch ein anderes Team) wurden bereits im
Abschnitt [Nice-to-Haves](#nice-to-haves) genannt. Dazu kämen noch weitere Möglichkeiten zwecks Customization der GUI,
sowie die Erweiterung auf andere Dateiformate, wie z.B. mp3 oder ogg wären durchaus sinnvoll, um dem Nutzer ein größeres
Spektrum an Möglichkeiten zur Bearbeitung seiner Sounddateien zu geben.

Weiterhin wäre aber auch ein Fokus auf die Laufzeitoptimierung oder gar der Wechsel von Python hin zu einer low-level
Programmiersprache (C/C++) denkbar, um diverse Performance-Probleme mit Python loszuwerden und den Equalizer auch
Echtzeit-tauglich zu machen.
