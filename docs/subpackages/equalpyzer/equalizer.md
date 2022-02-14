[Index](../../index.md) > equalpyzer > **Equalizer**

# Equalizer.py

> Equalizer that can be used to manipulate frequency bands from a wave file.

Die `Equalizer` Klasse ist im Grunde nur noch ein Überbleibsel von Umstrukturierungen während der Projektarbeit. Sie
enthält nur eine einzige Methode, welche mithilfe eines Bandpass-Rechteckfilters das Frequenzband eines beliebigen Signals
manipulieren kann.

## Klassenattribute

| Attribut | Typ | Beschreibung |
| ------ | ------ | ------ |
| `altered_signal` | `ndarray` | Eine Kopie des Ausgangssignal, welche vom Equalizer verändert werden kann. |
| `altered_amplitudes` | `ndarray` | Eine Kopie der Amplituden des Ausgangssignals, welche vom Equalizer verändert werden kann. |
| `altered_amplitudes_db` | `ndarray` | Eine Kopie der Frequenzen des Ausgangssignals, welche vom Equalizer verändert werden kann. |

## Klassenmethoden

| Methode | Parameter | Beschreibung |
| ------ | ------ | ------ |
| `boost` | `decibels` `low_cut` `high_cut` | Erlaubt, ein beliebiges Intervall in einem beliebigen Signal zu manipulieren. Der Boost wird in Dezibel angegeben. |

### boost

| Parameter | Typ | Beschreibung |
| ------ | ------ | ------ |
| `decibels` | `int` | Anzahl an Dezibel, um die das Intervall erhöht bzw. erniedrigt wird. |
| `low_cut` | `int`, optional | Die untere Grenzfrequenz des Intervalls. Default ist `0`. |
| `high_cut` | `Union[int, None]`, optional | Die obere Grenzfrequenz des Intervalls. Default ist die höchste im Signal vorkommende Frequenz. |

| Rückgabetyp | Beschreibung |
| ------ | ------ |
| `None` | - |
