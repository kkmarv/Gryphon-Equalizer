[Index](../../index.md) > gryphonui > **MainWindow**

# MainWindow

Die Klasse `MainWindow` beschreibt das gesamte Fenster der Anwendung. In ihr werden die einzelnen Komponenten
initialisiert und verwaltet.

## Klassenattribute

| Attribut | Typ | Beschreibung |
| ------ | ------ | ------ |
| `_eq` | `Union[Equalizer, None]` | Der Equalizer. | 
| `_canvas_view_mode` | `str` | Der momentan angezeigte Plot. Mögliche Werte sind: <br> `'time'` - Zeitbereich <br> `'frequency'` - Frequenzbereich <br> `'frequency-db'` - Frequenzbereich in dbFS | 
| `_eq_control_buttons` | `EQControlButtons` | Das Widget, welches die unteren Buttons zur Bedienung des Equalizers enthält. | 
| `_eq_widget` | `EQWidget` | Das Widget, welches den Plot und die Drehregler enthält. |

## Klassenmethoden

| Methode | Parameter | Beschreibung |
| ------ | ------ | ------ |
| `__init_gui` | - | Initialisiert die GUI-Komponenten. | 
| `__init_gui` | - | Verknüpft die Menu-Bar-Buttons mit ihren dazugehörigen Funktionen. | 
| `__connect_buttons` | - | Verknüpft den Reset-Dials-Button mit der dazugehörigen Methode. | 
| `__on_open` | - | Öffnet ein Explorer-Fenster, in dem der Nutzer eine wav-Datei auswählen kann, welche dann geladen wird.| 
| `__on_save` | - |  Öffnet ein Explorer-Fenster, in dem der Nutzer auswählen kann, wo er das aktuelle Signal als Datei speichern will.|  
| `__on_dial_change` | `db_boost` `low_cut` `high_cut` | Aktualisiert das Signal und den Graphen mit den aktuellen Dial-Werten. | 
| `__on_dial_change` | - | Schließt das Programm. | 
| `__on_dial_change` | `view_mode` `normalize`, optional | Wechselt die Ansicht des Graphen zum ausgewählten `view_mode`. | 

### __init_gui

| Rückgabetyp | Beschreibung |
| ------ | ------ |
| `None` | - | 

### __init_gui

| Rückgabetyp | Beschreibung |
| ------ | ------ |
| `None` | - | 

### __connect_buttons

| Rückgabetyp | Beschreibung |
| ------ | ------ |
| `None` | - | 

### __on_open

| Rückgabetyp | Beschreibung |
| ------ | ------ |
| `None` | - | 

### __on_save

| Rückgabetyp | Beschreibung |
| ------ | ------ |
| `None` | - | 

### __on_dial_change

| Rückgabetyp | Beschreibung |
| ------ | ------ |
| `None` | - | 

### __on_dial_change

| Rückgabetyp | Beschreibung |
| ------ | ------ |
| `None` | - | 

### __on_dial_change

| Rückgabetyp | Beschreibung |
| ------ | ------ |
| `None` | - | 
