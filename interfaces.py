from abc import abstractmethod
from typing import List

from pydantic import BaseModel

from classes import BaseDocument, BaseGeneratedResponse


class RetrieverInterface(BaseModel):
    @abstractmethod
    def retrieve(self, user_query: str):
        raise NotImplementedError


class GeneratorInterface(BaseModel):
    @abstractmethod
    def generate(self, user_query: str, documents: List[BaseDocument]):
        raise NotImplementedError
