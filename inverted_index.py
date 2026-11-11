import re


text = """Today is sunny. She is a sunny girl. To be or not to be. She is in Berlin today. 
Sunny Berlin! Berlin is always exciting!"""

documents = re.split(r'[.!?]', text)

documents = [doc.strip() for doc in documents if doc.strip()]


# for i, doc in enumerate(documents, start=1):
#     print(f"D{i}: {doc}")

tokenized_documents = []

for doc in documents:
    tokens = re.split(r'[^a-zA-Z]+', doc)
    tokens = [token.lower() for token in tokens if token]
    tokenized_documents.append(tokens)

# print(tokenized_documents)

inverted_index = {}


for doc_id, tokens in enumerate(tokenized_documents, start=1):
    for token in tokens:
        if token not in inverted_index:
            inverted_index[token] = []

        if doc_id not in inverted_index[token]:
            inverted_index[token].append(doc_id)

print("\nInverted Index:")

for term in sorted(inverted_index):
    print(f"{term}: {inverted_index[term]}")


# intersection algo

def intersect(postings1, postings2):
    result = []

    i = 0
    j = 0

    while i < len(postings1) and j < len(postings2):

        if postings1[i] == postings2[j]:
            result.append(postings1[i])
            i += 1
            j += 1

        elif postings1[i] < postings2[j]:
            i += 1

        else:
            j += 1

    return result


print("Intersection Algo:")


# Retrieve postings lists
sunny_postings = inverted_index["sunny"]
print("sunny :",sunny_postings)
exciting_postings = inverted_index["exciting"]
print("exciting :",sunny_postings)


# Find common documents
result = intersect(sunny_postings, exciting_postings)

print("Documents containing sunny AND exciting:", result)