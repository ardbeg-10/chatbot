import csv

# Reading data from csv file
data_to_embed = []
with open('embedding_raw.csv', mode='r', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        data_to_embed.append({"id": row["id"], "text": row["summary"]})

import openai
import csv

# generate embeddings
embeddings = []
for item in data_to_embed:
    try:
        response = openai.Embedding.create(input=item["text"], model="text-embedding-ada-002")
        embedding_vector = response['data'][0]['embedding']
        embeddings.append((item["id"], embedding_vector))
    except Exception as e:
        print(f"An error occurred for item {item['id']}: {e}")

# save embeddings to csv file
with open('embeddings.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["id", "embedding"])
    for id, embedding in embeddings:
        writer.writerow([id, embedding])
