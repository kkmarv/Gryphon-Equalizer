[Index](./index.md) > **How to get started**

# How to get started

## Mit Benutzung einer virtuellen Python Umgebung

Zuerst wollen wir eine virtuelle Python Umgebung aufsetzen, um alle erforderlichen Pakete zu installieren:

```shell
python -m venv .venv  
```

Diese virtuelle Umgebung muss dann aktiviert werden.  
Dieser Schritt muss jedes Mal ausgeführt werden, bevor die `main.py` ausgeführt werden kann.

```shell
.\.venv\Scripts\activate
```

Falls der Befehl erfolgreich war, so sollte jetzt `(.venv)` an vorderster Stelle in der Konsoleneingabe stehen.

Dann müssen noch einmalig die erforderlichen Pakete installiert werden:

```shell
pip install requirements.txt
```

Letztlich kann das Programm über `main.py` gestartet werden:

```shell
python main.py
```

Die genauen Versionen der verwendeten Pakete können der [requirements.txt](../requirements.txt) entnommen werden.
