import os
import pandas as pd
import wave

def wav_zu_excel(datei_pfad, wav_datei_name, output_folder, output_excel_file):
    input_file_path = os.path.join(datei_pfad, wav_datei_name)

    if not os.path.exists(input_file_path):
        print(f"Die Eingabedatei '{wav_datei_name}' existiert nicht im angegebenen Ordner.") # falls die Datei (Audiodatei) nicht gefunden wird schreibt es das
        return

    with wave.open(input_file_path, 'rb') as wav_file:
        audio_data = wav_file.readframes(wav_file.getnframes()) # die Audiodatei wird geöffnet und gelesen
        audio_data = list(audio_data)

    df = pd.DataFrame({'AudioData': audio_data}) # ein DataFrame wird erstellt, dessen Spalte AudioData heißen wird

    filter_zeros = input("Möchten Sie alle Nullen in der Excel-Datei filtern? (Ja/Nein): ").lower() # hier wird gefragt, ob alle Nullen ausgefiltert werden sollen

    if filter_zeros == 'ja':
        df['FilteredData'] = df['AudioData'].apply(lambda x: x if x != 0 else pd.NA) # Nullen werden gefiltert

        if df['AudioData'].eq(0).all():
            df = df.drop(columns=['AudioData']) # wenn die Nullen entfernt werden, wird AudioData (also die Überschrift) auch gelöscht

        df['FilteredData'] = df['FilteredData'].dropna().reset_index(drop=True) # die AudioData spalte heißt jetzt FilteredData und alle Zahlen, die nicht 0 sind rücken auf

        filtered_output_file_path = os.path.join(output_folder, f"Filtered_{output_excel_file}") # eine gefilterte seperate Excel Datei wird erstellt
        df[['FilteredData']].to_excel(filtered_output_file_path, index=False)

        print(f"Erfolgreich: Gefilterte Zahlen wurden in der Excel-Datei '{filtered_output_file_path}' gespeichert :D.")
    else:
        output_file_path = os.path.join(output_folder, output_excel_file)
        df.to_excel(output_file_path, index=False)

        print(f"Erfolgreich: Die WAV-Datei wurde in die Excel-Datei '{output_excel_file}' konvertiert :D.")

# Setze die Pfade und Dateinamen entsprechend deiner Bedürfnisse
datei_pfad = r'C:\Users\User\Desktop\IMP_10_2023_24\Jan Kappelmann\Projekte\Projekt1_MP3\files'
wav_datei_name = 'Rosocha_Ausgabe.wav'
output_folder = r'C:\Users\User\Desktop\IMP_10_2023_24\Jan Kappelmann\Projekte\Projekt1_MP3\files'
output_excel_file = 'Rosocha_Signale.xlsx'

wav_zu_excel(datei_pfad, wav_datei_name, output_folder, output_excel_file)
