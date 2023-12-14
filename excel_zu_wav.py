import os
import pandas as pd
import wave
import struct

def excel_zu_wav(input_excel_path, output_folder, output_wav_file):
    # Lese die Excel-Datei in einen DataFrame ein
    df = pd.read_excel(input_excel_path)

    # Überprüfe, ob die Spalte 'FilteredData' in der Excel-Datei vorhanden ist
    if 'FilteredData' not in df.columns:
        print("Die Excel-Datei muss eine Spalte namens 'FilteredData' enthalten.")
        return

    # Extrahiere die Audiodaten aus der Spalte 'FilteredData'
    audio_data = df['FilteredData'].dropna().tolist()

    # Skaliere die Werte auf den Bereich von 16-Bit signed integers (-32768 bis 32767)
    scaled_audio_data = [int(max(min(x, 1.0), -1.0) * 32767) for x in audio_data]

    # Konvertiere die skalierten Zahlen in Bytes (16-Bit signed integers)
    byte_data = struct.pack('<' + 'h' * len(scaled_audio_data), *scaled_audio_data)

    # Kombiniere den Ausgabeordnerpfad und den Ausgabedateinamen
    output_file_path = os.path.join(output_folder, output_wav_file)

    # Erstelle eine WAV-Datei mit den extrahierten Audiodaten
    with wave.open(output_file_path, 'wb') as wav_file:
        wav_file.setnchannels(2)  # Ein Kanal (Mono)
        wav_file.setsampwidth(2)  # 2 Bytes pro Sample (16-Bit signed integers)

        # Setze die Beispielrate auf 44100 (kann angepasst werden)
        wav_file.setframerate(44100)

        # Berechne die Anzahl der Frames basierend auf der Beispielrate und der Dauer der Audiodaten
        wav_file.setnframes(int(len(audio_data) * wav_file.getsampwidth()))
        wav_file.writeframes(byte_data)

    print(f"Erfolgreich: Die Excel-Datei wurde in die WAV-Datei '{output_wav_file}' konvertiert :D.")

# Setze die Pfade und Dateinamen entsprechend deiner Bedürfnisse
input_excel_path = r'C:\Users\User\Desktop\IMP_10_2023_24\Jan Kappelmann\Projekte\Projekt1_MP3\files\Filtered_Rosocha_Signale.xlsx'
output_folder = r'C:\Users\User\Desktop\IMP_10_2023_24\Jan Kappelmann\Projekte\Projekt1_MP3\files'
output_wav_file = 'New_Rosocha_WAV.wav'

excel_zu_wav(input_excel_path, output_folder, output_wav_file)
