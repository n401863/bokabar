import csv
import os
import tkinter as tk
from tkinter import filedialog

def laad_tabel_van_csv(bestandspad):
    try:
        with open(bestandspad, mode='r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            inhoud = list(csv_reader)  # Laad de inhoud van de CSV in een lijst
            return inhoud
    except FileNotFoundError:
        print("Bestand niet gevonden. Controleer het pad en probeer het opnieuw.")
        return None
    except Exception as e:
        print(f"Er is een fout opgetreden: {e}")
        return None

def vergelijk_tabel(tabel1, tabel2):
    # Vergelijk de twee tabellen
    verschillen = []
    max_len = max(len(tabel1), len(tabel2))
    
    for i in range(max_len):
        if i < len(tabel1) and i < len(tabel2):
            if tabel1[i] != tabel2[i]:
                verschillen.append((i, tabel1[i], tabel2[i]))
        elif i < len(tabel1):
            verschillen.append((i, tabel1[i], None))  # Alleen in tabel1
        elif i < len(tabel2):
            verschillen.append((i, None, tabel2[i]))  # Alleen in tabel2

    return verschillen

def bereken_verschillen(tabel1, tabel2):
    resultaten = []
    max_len = max(len(tabel1), len(tabel2))
    
    for i in range(max_len):
        if i < len(tabel1) and i < len(tabel2):
            rij_resultaat = []
            for j in range(max(len(tabel1[i]), len(tabel2[i]))):
                waarde1 = float(tabel1[i][j]) if j < len(tabel1[i]) else 0
                waarde2 = float(tabel2[i][j]) if j < len(tabel2[i]) else 0
                rij_resultaat.append(waarde1 - waarde2)
            resultaten.append(rij_resultaat)
        elif i < len(tabel1):
            resultaten.append([float(val) for val in tabel1[i]])  # Alleen in tabel1
        elif i < len(tabel2):
            resultaten.append([-float(val) for val in tabel2[i]])  # Alleen in tabel2

    return resultaten

def schrijf_naar_csv(bestandspad, data):
    try:
        with open(bestandspad, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(data)
        print(f"Resultaten zijn opgeslagen in: {bestandspad}")
    except Exception as e:
        print(f"Er is een fout opgetreden bij het schrijven naar het bestand: {e}")

def selecteer_bestand(titel):
    root = tk.Tk()
    root.withdraw()  # Verberg het hoofdvenster
    bestandspad = filedialog.askopenfilename(title=titel, filetypes=[("CSV bestanden", "*.csv")])
    return bestandspad

def main():
    # Vraag de gebruiker om het pad van het eerste CSV-bestand in te voeren
    bestandspad1 = selecteer_bestand("Selecteer het eerste CSV-bestand")
    
    # Controleer of het eerste bestand bestaat
    if os.path.isfile(bestandspad1):
        tabel1 = laad_tabel_van_csv(bestandspad1)
    else:
        print("Het opgegeven pad is geen geldig bestand. Controleer het pad en probeer het opnieuw.")
        return

    # Vraag de gebruiker om het pad van het tweede CSV-bestand in te voeren
    bestandspad2 = selecteer_bestand("Selecteer het tweede CSV-bestand")
    
    # Controleer of het tweede bestand bestaat
    if os.path.isfile(bestandspad2):
        tabel2 = laad_tabel_van_csv(bestandspad2)
    else:
        print("Het opgegeven pad is geen geldig bestand. Controleer het pad en probeer het opnieuw.")
        return

    # Vergelijk de twee tabellen
    verschillen = vergelijk_tabel(tabel1, tabel2)

    # Toon de verschillen
    if verschillen:
        print("\nVerschillen gevonden:")
        for index, rij1, rij2 in verschillen:
            print(f"Rij {index}: Tabel 1: {rij1} | Tabel 2: {rij2}")

    # Bereken de verschillen en schrijf ze naar een nieuw CSV-bestand
    resultaten = bereken_verschillen
