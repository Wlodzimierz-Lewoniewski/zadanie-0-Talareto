from collections import defaultdict

def process_documents_and_queries(documents, queries):
    word_in_docs = defaultdict(lambda: defaultdict(int))

    for doc_index, document in enumerate(documents):
        for word in document.lower().split():
            word_in_docs[word][doc_index] += 1

    results = []
    for query in queries:
        query = query.lower()
        if query in word_in_docs:
            occurrences = list(word_in_docs[query].items())
            sorted_occurrences = sorted(occurrences, key=lambda x: (-x[1], x[0]))
            results.append([doc_index for doc_index, _ in sorted_occurrences])
        else:
            results.append([])

    return results

n = int(input())
documents = [input() for _ in range(n)]

m = int(input())
queries = [input() for _ in range(m)]

results = process_documents_and_queries(documents, queries)

for result in results:
    print(" ".join(map(str, result)))
