import re


text = """Today is sunny. She is a sunny girl. To be or not to be. She is in Berlin today. 
Sunny Berlin! Berlin is always exciting!"""

documents = re.split(r'[.!?]', text)

documents = [doc.strip() for doc in documents if doc.strip()]


for i, doc in enumerate(documents, start=1):
    print(f"D{i}: {doc}")

tokenized_documents = []

for doc in documents:
    tokens = re.split(r'[^a-zA-Z]+', doc)
    tokens = [token.lower() for token in tokens if token]
    tokenized_documents.append(tokens)

print(tokenized_documents)
