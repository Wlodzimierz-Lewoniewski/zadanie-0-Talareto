from collections import deafultdict

def process_documents_and_queries(documents,queries):
  word_in_docs = deafultdict(lambda:deafultdict(int))

  for doc_index, document in enumerate(documents):
    for word in document.split():
      word_in_docs[word][doc_index] += 

  results = []

  for query in queries:
    if query in word_in_docs:
      occurrences = list(word_in_docs[query].items())
      sorted_occurances = sorted(occurrences, key = lambda x: (-x[1], x[0]))
      results.append([doc_index for doc_index, _ in sorted_occurences])
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
