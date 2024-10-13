import string
from collections import defaultdict

def wyczysc_tekst(tekst):
    return tekst.translate(str.maketrans('', '', string.punctuation)).lower().split()

liczba_dokumentow = int(input())
dokumenty = [input().strip() for _ in range(liczba_dokumentow)]
liczba_slow = int(input())
slowa = [input().strip().lower() for _ in range(liczba_slow)]

# Inicjalizacja słownika do przechowywania wyników
wyniki = defaultdict(list)

for index, dokument in enumerate(dokumenty):
    oczyszczony_dokument = wyczysc_tekst(dokument)
    zliczanie = defaultdict(int)

    for slowo in oczyszczony_dokument:
        if slowo in slowa:
            zliczanie[slowo] += 1

    for slowo in slowa:
        if zliczanie[slowo] > 0:
            wyniki[slowo].append(index + 1)  # Dodajemy 1, żeby indeks był od 1

# Wyświetlenie wyników
for slowo in slowa:
    print(" ".join(map(str, wyniki[slowo])))
