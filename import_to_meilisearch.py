import csv
import os

import meilisearch

from dotenv import load_dotenv

load_dotenv()

file_path = "docs/tastic-ai-opensource-ai-tools.csv"

index_name = os.getenv('MEILISEARCH_INDEX')

client = meilisearch.Client(os.getenv('MEILISEARCH_HOST'), os.getenv("MEILISEARCH_API_KEY"))

index = client.index(index_name)

myFile = open(file_path, 'r')

reader = csv.DictReader(myFile)
myList = list()

for dictionary in reader:
    myList.append(dictionary)
