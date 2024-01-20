import csv

import meilisearch

file_path = "docs/tastic-ai-opensource-ai-tools.csv"

index_name = "opensource-ai-tools-1"

client = meilisearch.Client('http://127.0.0.1:7700', 'aSampleMasterKey')

index = client.index(index_name)

myFile = open(file_path, 'r')

reader = csv.DictReader(myFile)
myList = list()

for dictionary in reader:
    myList.append(dictionary)
