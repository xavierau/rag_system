from pydantic import BaseModel

from classes import BaseGeneratedResponse
from interfaces import RetrieverInterface, GeneratorInterface


class RAGSystem(BaseModel):
    retriever: RetrieverInterface
    generator: GeneratorInterface

    def query(self, user_query):
        documents = self.retriever.retrieve(user_query)
        return self.generator.generate(user_query, documents)
