[Index](../../index.md) > equalpyzer > **Wavefile**

# Wavefile.py

> A container for specific properties from a single wav file.  
> Contains properties which are important in order to manipulate the signal.

Die Klasse `Wavefile` ist die zentrale Datenstruktur aller Signalverarbeitung.  
Sie öffnet .wav Dateien, speichert diese in numpy Arrays ab, berechnet nominale Werte über die Signale und wandelt sie
auf Anfrage mittels reeller Fouriertransformation in den Frequenzbereich um. Weiterhin verfügt sie über Methoden, welche
Signalamplituden in eine dbFS Skalierung - und zurück - ermöglicht.

## Klassenattribute

| Attribut | Typ | Beschreibung |
| ------ | ------ | ------ |
| `sample_rate` | `Union[int, None]` | Die Samplerate des Signals. |
| `input_signal` | `Union[ndarray, None]` | Das Signal. | 
| `duration` | `Union[float, None]` | Die Länge des Signals in Sekunden. | 
| `num_of_samples` | `Union[int, None]` | Die Anzahl der Samples im Signal. | 
| `loudest_samp_value` | `Union[int, None]` | Der Wert des lautesten im Signal vorkommenden Samples. | 
| `max_possible_samp_value` | `Union[int, float, None]` | Der höchstmögliche Wert eines Samples für dieses spezielle Signal. Wird durch seinen Datentyp bestimmt. | 
| `amplitudes` | `Union[ndarray, None]` | Die Amplituden der Frequenzen Signals, welche aus der FFT resultieren. | 
| `frequencies` | `Union[ndarray, None]` | Die Frequenzen des Signals, welche aus der FFT resultieren. | 
| `amplitudes_db` | `Union[ndarray, None]` | Die Frequenzen des Signals, welche aus der FFT resultieren, aber in dbFS Skalierung. | 

## Klassenmethoden

| Methode | Parameter | Beschreibung |
| ------ | ------ | ------ |
| `load_signal` | `path` | Öffnet eine .wav Datei und liest alle relevanten Daten ein. |
| `save_signal` | `path` `output_signal` | Schreibt ein gegebenes Signal an den gegebenen Pfad als .wav Datei. |

### load_signal

> Opens the wave file from path and reads all relevant data.

| Parameter | Typ | Beschreibung |
| ------ | ------ | ------ |
| `path` | `str` | Der Pfad der zu öffnenden .wav Datei |

| Rückgabetyp | Beschreibung |
| ------ | ------ |
| `void` | - |

### save_signal

> Saves this or another wave file to path.

| Parameter | Typ | Beschreibung |
| ------ | ------ | ------ |
| `path` | `str` | Der Pfad, an den die .wav Datei geschrieben werden soll. Falls bereits existent, so wird die Datei überschrieben. |
| `output_signal` | `ndarray` | Das zu schreibende Signal. |

| Rückgabetyp | Beschreibung |
| ------ | ------ |
| `None` | - |
