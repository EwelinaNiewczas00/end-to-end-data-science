import pandas as pd
import os

# 1. TWOJA BAZA WIEDZY (Dane do tabeli)
dane = {
    "Zastosowanie": [
        "Miejsca po przecinku", 
        "Procenty", 
        "Separator tysięcy", 
        "Wyśrodkowanie tekstu", 
        "Wyrównanie do prawej", 
        "Wypełnienie wolnego miejsca",
        "Szybki podgląd (Debug)"
    ],
    "Kod (f-string)": [
        ":.2f", 
        ":.1%", 
        ":,", 
        ":^N", 
        ":>N", 
        ":znak^N",
        "{zmienna=}"
    ],
    "Przykład zapisu": [
        "f'{x:.2f}'", 
        "f'{x:.1%}'", 
        "f'{x:,}'", 
        "f'{x:^20}'", 
        "f'{x:>20}'", 
        "f'{x:=^20}'",
        "f'{x=}'"
    ],
    "Opis działania": [
        "Zaokrągla do 2 miejsc (np. 10.50)", 
        "Mnoży x100 i dodaje % (np. 88.0%)", 
        "Dodaje przecinek co 3 cyfry (np. 1,000,000)", 
        "Środkuje tekst w polu o szerokości N", 
        "Przesuwa tekst do prawej krawędzi", 
        "Zamiast spacji daje wybrany znak (np. ===)",
        "Wypisuje nazwę i wartość (np. x=10.5)"
    ]
}

# 2. TWORZENIE TABELI
df = pd.DataFrame(dane)

# 3. USTALANIE ŚCIEŻKI DO FOLDERU 'Bootcamp2'
nazwa_pliku = "Instrukcja_Python_Formatowanie.xlsx"
sciezka_obecna = os.getcwd()

# Sprawdzamy, czy folder Bootcamp2 jest pod nami, czy już w nim jesteśmy
if "Bootcamp2" in sciezka_obecna:
    # Jesteśmy już w środku Bootcamp2
    pelna_sciezka = nazwa_pliku
else:
    # Jesteśmy w folderze nadrzędnym (Bootcamp), więc celujemy w podfolder
    pelna_sciezka = os.path.join("Bootcamp2", nazwa_pliku)

# 4. EXPORT DO EXCELA
try:
    # Sprawdzenie czy folder Bootcamp2 w ogóle istnieje, żeby nie było błędu
    if "Bootcamp2" not in sciezka_obecna and not os.path.exists("Bootcamp2"):
        print("⚠️ Folder 'Bootcamp2' nie został znaleziony! Tworzę plik w obecnym miejscu.")
        df.to_excel(nazwa_pliku, index=False)
    else:
        df.to_excel(pelna_sciezka, index=False)
        print("--- STATYSTYKI OPERACJI ---")
        print(f"✅ Plik został zapisany dla: Bootcamp2")
        print(f"📍 Dokładna ścieżka: {os.path.abspath(pelna_sciezka)}")
        print("---------------------------")
except Exception as e:
    print(f"❌ Wystąpił błąd przy zapisie: {e}")