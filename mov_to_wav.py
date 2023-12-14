from moviepy.editor import VideoFileClip # Nützlich für das Bearbeiten von Videos

def convert_mov_to_wav(mov_datei_video, wav_datei_audio):
    # Video laden
    video = VideoFileClip(mov_datei_video) # Das Video wird zum bearbeiten bereitgestellt

    
    audio_datei = video.audio # aus dem Video wird nur die Audio extrahiert


    audio_datei.write_audiofile(wav_datei_audio, codec='pcm_s16le', fps=audio_datei.fps) # die Audio (alle Klänge) werden in einer WAV Datei gespeichert

    print(f"Die Audio-Spur von {mov_datei_video} wurde erfolgreich in {wav_datei_audio} umgewandelt.")

#-------------------------Datei zum Umwandeln suchen in vorgegebenen Dateipfad----------------------------------------------------------

mov_datei_video = "C:/Users/User/Desktop/IMP_10_2023_24/Jan Kappelmann/Projekte/Projekt1_MP3/files/Rosocha.mov"
wav_datei_audio = "C:/Users/User/Desktop/IMP_10_2023_24/Jan Kappelmann/Projekte/Projekt1_MP3/files/Rosocha_Ausgabe.wav"

convert_mov_to_wav(mov_datei_video, wav_datei_audio)
