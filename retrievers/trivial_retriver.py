from typing import List

from classes import BaseDocument
from interfaces import RetrieverInterface


class TrivialRetriever(RetrieverInterface):
    def retrieve(self, user_query: str) -> List[BaseDocument]:
        return [
            BaseDocument(
                content="""Once when I was six years old I saw a magnificent picture in a book, called True Stories from Nature,
            about the primeval forest. It was a picture of a boa constrictor in the act of swallowing an animal. Here is a
            copy of the drawing.""",
                meta={
                    "title": "The Little Prince",
                    "page": 4,
                    "chapter": 1,
                    "pdf_url": "https://blogs.ubc.ca/edcp508/files/2016/02/TheLittlePrince.pdf"
                }
            )
        ]
