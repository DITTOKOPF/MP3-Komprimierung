import wave

def read_wav_info(file_path):
    try:
        with wave.open(file_path, 'rb') as wav_file:
            # Extrahiere Informationen
            sample_rate = wav_file.getframerate()
            channels = wav_file.getnchannels()
            bytes_per_sample = wav_file.getsampwidth()

            # Gib die Informationen aus
            print(f'Sample Rate: {sample_rate} Hz')
            print(f'Channels: {channels}')
            print(f'Bytes per Sample: {bytes_per_sample}')

    except wave.Error as e:
        print(f"Fehler beim Öffnen der WAV-Datei: {e}")

# Beispielaufruf
wav_file_path = 'C:/Users/User/Desktop/IMP_10_2023_24/Jan Kappelmann/Projekte/Projekt1_MP3/files/Rosocha_Ausgabe.wav'  # Passe den Dateipfad entsprechend an
read_wav_info(wav_file_path)
