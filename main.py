import re

docs = [input("Input document: ").strip() for _ in range(int(input("How many documents you want to add?: ")))]
queries = []
for _ in range(int(input("How many words you want to search?: "))):
    while True:
        term = input("Input the word: ").strip()
        if term not in queries:
            queries.append(term)
            break
        print("This word already exists")

def count_occurrences(term, text):
    words = re.sub(r'[^\w\s]', '', text.lower()).split()
    return words.count(term.lower())

for term in queries:
    counts = [(i, count_occurrences(term, doc)) for i, doc in enumerate(docs) if count_occurrences(term, doc) > 0]
    sorted_indices = [index for index, _ in sorted(counts, key=lambda x: (-x[1], x[0]))]
    print(sorted_indices)
