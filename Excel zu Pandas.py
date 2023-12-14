import os
import pandas as pd

def read_excel_from_folder(ausgangs_ordner, Datei_Name):

    file_path = os.path.join(ausgangs_ordner, Datei_Name) # Hier wird der vollständige datei Pfad angegeben (Durch Kombination von Name und Ordner)

    if not os.path.exists(file_path):
        print(f"Die Datei '{Datei_Name}' existiert nicht im angegebenen Ordner.") # Überprüfung, ob die Datei im angegebenen Ordner existiert
        return None

    excel_datei = pd.read_excel(file_path) # Pandas (hier pd) wird benutzt um aus der durch Data Frame gelesenen Datei, die im Terminal sichtbare Tabelle zu machen

    keine_Zahl = excel_datei.fillna('') # wenn es ein NaN geben würde (keine Zahl in der Zelle), wird es durch eine leere Zelle ersetzt

    keine_Zahl = keine_Zahl.applymap(lambda x: int(x) if pd.notna(x) and isinstance(x, (int, float)) else x) # Die Zahlen hinter dem Komma werden entfernt

    return excel_datei, keine_Zahl

#-------------------------------hier können Dateipfad und Dateiname angegeben werden-----------------------------------------------

ausgangs_ordner = r'C:\Users\User\Desktop\IMP_10_2023_24\Jan Kappelmann\Projekte\Projekt1_MP3\files'
excel_Datei_Name = 'Filtered_Rosocha_Signale.xlsx'

excel_data_original, excel_data_no_decimal = read_excel_from_folder(ausgangs_ordner, excel_Datei_Name) # Excel datei wird gelesen

if excel_data_original is not None and excel_data_no_decimal is not None: # überprüfung, ob die Datei gelesen wurde

    print("Original Excel-Datei:") # originale Zahlen werden angezeigt
    print(excel_data_original)

    print("\nExcel-Datei mit entfernten Dezimalstellen:") # alle Kommazahlen werden gelöscht und die Datei wird angezeigt
    print(excel_data_no_decimal)
