import meilisearch

from classes import BaseDocument
from interfaces import RetrieverInterface


class MeilisearchRetriever(RetrieverInterface):
    host: str
    password: str
    index_name: str

    def retrieve(self, user_query: str):
        client = meilisearch.Client(self.host, self.password)

        index = client.index(self.index_name)

        results = index.search(user_query)

        return [BaseDocument(content=d.get('desc', ""), meta={
            key: d[key] for key in d.keys()
                                   & {'title', 'features', 'cat', 'url', 'vote'}}) for d in
                results.get("hits", [])]
