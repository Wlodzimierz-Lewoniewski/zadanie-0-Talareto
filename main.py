import re
from collections import defaultdict

def wyczysc_tekst(tekst):
    return re.findall(r'\b\w+\b', tekst.lower())

liczba_dokumentow = int(input())
dokumenty = [input().strip() for _ in range(liczba_dokumentow)]
liczba_slow = int(input())
slowa = [input().strip().lower() for _ in range(liczba_slow)]

# Inicjalizacja słownika do przechowywania wystąpień słów w dokumentach
word_occurrences = defaultdict(lambda: defaultdict(int))

# Zliczanie wystąpień słów w dokumentach
for index, dokument in enumerate(dokumenty):
    oczyszczony_dokument = wyczysc_tekst(dokument)
    for slowo in oczyszczony_dokument:
        word_occurrences[slowo][index + 1] += 1  # Indeks dokumentu od 1

# Przygotowanie wyników
wyniki_listy = []

for slowo in slowa:
    if slowo in word_occurrences:
        occurrences = sorted(word_occurrences[slowo].items(), key=lambda x: (-x[1], x[0]))
        wyniki_listy.append([doc_id for doc_id, count in occurrences])
    else:
        wyniki_listy.append([])

# Wyświetlenie wyników
for lista in wyniki_listy:
    print(" ".join(map(str, lista)))
