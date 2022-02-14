[Index](../../../../index.md) > gryphonui > widgets > designer > **EQDials**

# EQDials

Die Klasse `EQDials` verwaltet die Drehregler, mit deren Hilfe die Dezibel-Werte der Frequenzbänder angepasst werden
können. Ihr Layout wurde mit dem QT Designer definiert.

## Klassenattribute

| Attribut | Typ | Beschreibung |
| ------ | ------ | ------ |
| `` | `` | | 

## Klassenmethoden

| Methode | Typ | Beschreibung |
| ------ | ------ | ------ |
| `__connect_dials` | `` | Ordnet die Frequenzbänder den entsprechenden Drehreglern zu.|
| `__woof` | `` | Ordnet die Funktion des Drehreglers eines Frequenzbands einem entsprechenden Drehregler zu.  |
| `__reset_dials` | `` | Setzt alle Drehregler auf 0 dbFS zurück. |

### __connect_dials

| Rückgabetyp | Beschreibung |
| ------ | ------ |
| `None` | - |

### __woof

| Parameter | Typ | Beschreibung |
| ------ | ------ | ------ |
| `dial` | `QDial` | Der Drehregler, dessen Funktion eingestellt werden soll. |
| `freq_band_label` | `QLabel` | Das Label des Drehreglers, welcher das Frequenzband angibt. |
| `db_label` | `QLabel` | Das Label des Drehreglers, welcher die Veränderung in dbFS angibt. |

| Rückgabetyp | Beschreibung |
| ------ | ------ |
| `None` | - |

### __reset_dials

| Rückgabetyp | Beschreibung |
| ------ | ------ |
| `None` | - |