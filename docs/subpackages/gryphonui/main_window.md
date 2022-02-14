[Index](../../index.md) > gryphonui > **MainWindow**

# MainWindow
Die Klasse `MainWindow` beschreibt das gesamte Fenster der Anwendung. In ihr werden die einzelnen Komponenten
initialisiert.

## Klassenattribute

| Attribut | Typ | Beschreibung |
| ------ | ------ | ------ |
| `_eq` | `Union[Equalizer,  None]` | | 
| `_canvas_view_mode` | `str` | | 
| `_eq_control_buttons` | `EQControlButtons` | | 
| `_eq_widget` | `EQWidget` | | 

## Klassenmethoden

| Methode | Parameter | Beschreibung |
| ------ | ------ | ------ |
| `init_gui` | - | Initialisiert die GUI-Komponenten. | 
| `connect_menu_bar_methods` | - | Verknüpft die Menu-Bar-Buttons mit ihren dazugehörigen Funktionen. | 
| `connect_buttons` | - | Verknüpft den Reset-Dials-Button mit der dazugehörigen Methode. | 
| `on_open` | - | Öffnet ein Explorer-Fenster, in dem der Nutzer eine wav-Datei auswählen kann, welche dann geladen wird.| 
| `on_save` | - |  Öffnet ein Explorer-Fenster, in dem der Nutzer auswählen kann, wo er das aktuelle Signal als Datei speichern will.|  
| `on_dial_change` | `db_boost` `low_cut` `high_cut` | Aktualisiert das Signal und den Graphen mit den aktuellen Dial-Werten. | 
| `on_exit` | - | Schließt das Programm. | 
| `update_plot` | `view_mode` `normalize`, optional | Wechselt die Ansicht des Graphen zum ausgewählten `view_mode`. | 

### init_gui
| Rückgabetyp | Beschreibung |
| ------ | ------ |
| `None` | - | 

### connect_menu_bar_methods
| Rückgabetyp | Beschreibung |
| ------ | ------ |
| `None` | - | 

### connect_buttons
| Rückgabetyp | Beschreibung |
| ------ | ------ |
| `None` | - | 

### on_open
| Rückgabetyp | Beschreibung |
| ------ | ------ |
| `None` | - | 

### on_save
| Rückgabetyp | Beschreibung |
| ------ | ------ |
| `None` | - | 

### on_dial_change
| Rückgabetyp | Beschreibung |
| ------ | ------ |
| `None` | - | 

### on_exit
| Rückgabetyp | Beschreibung |
| ------ | ------ |
| `None` | - | 

### update_plot
| Rückgabetyp | Beschreibung |
| ------ | ------ |
| `None` | - | 
