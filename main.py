import win32clipboard
import time
import pandas as pd


def get_clipboard_text():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
    return data


def main():
    clipboard_history = []  # Liste zur Speicherung des Clipboard-Verlaufs

    while True:
        clipboard_data = get_clipboard_text()

        if clipboard_data:
            clipboard_history.append(clipboard_data)
            df = pd.DataFrame({"Clipboard Content": clipboard_history})
            df.to_csv("clipboard_history.csv", index=False)  # Speichern in CSV-Datei

        time.sleep(1)  # Warte 1 Sekunde vor der nächsten Überprüfung


if __name__ == "__main__":
    main()
