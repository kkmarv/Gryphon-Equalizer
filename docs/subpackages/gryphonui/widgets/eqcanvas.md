[Index](../../../index.md) > gryphonui > widgets > **EQCanvas**

# EQCanvas

Die Klasse `EQCanvas` wird benutzt, um eine Matplotlib canvas als `QWidget` nutzbar zu machen.

## Klassenattribute

| Attribut | Typ | Beschreibung |
| ------ | ------ | ------ |
| `_figure` | `Figure` | Zeichenfläche, auf die der Plot geplottet wird. | 
| `_axes` | `Axes` | Plot, welcher auf die Zeichenfläche gezeichnet wird. | 

## Klassenmethoden

| Methode | Parameter | Beschreibung |
| ------ | ------ | ------ |
| `plot_time_domain` | `input_signal` `duration` `num_of_samples` `max_sample_value` `normalize` | Zeichnet den Zeitbereich des Signals auf die Zeichenfläche. | 
| `plot_freq_domain` | `frequencies` `amplitudes` `normalize` | Zeichnet den Frequenzbereich des Signals auf die Zeichenfläche. | 
| `plot_freq_domain_db` | `frequencies` `amplitudes_db` | Zeichnet den Frequenzbereich des Signals auf die Zeichenfläche, die Werte sind in Decibels relative to full scale angegeben. | 

### plot_time_domain

| Parameter | Typ | Beschreibung |
| ------ | ------ | ------ |
| `input_signal` | `ndarray` | Das Array des Signals, welches geplottet werden soll. | 
| `duration` | `float` | Länge des Signals in Sekunden. | 
| `num_of_samples` | `int` | Anzahl der Samples im Signal. | 
| `max_sample_value` | `int` | Beschreibt den höchste im Signal vorkommenden Wert. | 
| `normalize`, optional | `bool` | Angabe, ob das Signal normalisiert dargestellt werden soll. Default ist `True`. | 

| Rückgabetyp | Beschreibung |
| ------ | ------ |
| `None` | - | 

### plot_freq_domain

| Parameter | Typ | Beschreibung |
| ------ | ------ | ------ |
| `frequencies` | `ndarray` | Array mit allen im Signal vorkommenden Frequenzen. | 
| `amplitudes` | `ndarray` |  Array mit den dazugehörigen Amplituden der Frequenzen. | 
| `normalize`, optional | `bool` | Angabe, ob das Signal normalisiert dargestellt werden soll. Default ist `True`. | 

| Rückgabetyp | Beschreibung |
| ------ | ------ |
| `None` | - |

### plot_freq_domain_db

| Parameter | Typ | Beschreibung |
| ------ | ------ | ------ |
| `frequencies` | `ndarray` | Array mit allen im Signal vorkommenden Frequenzen. | 
| `amplitudes_db` | `ndarray` | Array mit den dazugehörigen Amplituden der Frequenzen, angegeben in Decibels relative to full scale. | 

| Rückgabetyp | Beschreibung |
| ------ | ------ |
| `None` | - |
