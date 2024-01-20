import os
from typing import List
from openai import OpenAI
from pydantic import Field

from classes import BaseDocument, BaseGeneratedResponse
from interfaces import GeneratorInterface

from dotenv import load_dotenv

import yaml

load_dotenv()


class BasicOpenAILLMGenerator(GeneratorInterface):
    SYSTEM_PROMPT: str = """You are a helpful AI assistant. Base on the given context to answer user's query."""
    messages: List[BaseDocument] = []
    client: OpenAI = Field(default_factory=lambda: OpenAI())

    def generate(self, user_query: str, documents: List[BaseDocument]) -> BaseGeneratedResponse:

        self.construct_messages(user_query, documents)
        print(self.messages)
        response = self.client.chat.completions.create(
            model=os.getenv("OPENAI_LLM_MODEL", "gpt-3.5-turbo-1106"),
            messages=self.messages,
            stream=True
        )

        for chunk in response:
            choice = chunk.choices[0]
            if choice.finish_reason == "stop":
                break
            yield BaseGeneratedResponse(
                content=choice.delta.content,
                meta={}
            )

    def construct_messages(self, user_query, documents):
        system_message = {
            "role": "system",
            "content": self.SYSTEM_PROMPT
        }

        parsed_documents = self._parse_documents(documents)

        user_message = {
            "role": "user",
            "content": f"""Base on the context below, please generate a response to the user query:
            
            User Query:
            {user_query}
            `````
            
            Context (in yaml format):
            {parsed_documents}
            `````
            """
        }

        self.messages = [
            system_message,
            user_message
        ]

    def _parse_documents(self, documents: List[BaseDocument]) -> str:
        return "\n".join([f"{yaml.dump(document.__dict__)}" for document in documents])

    class Config:
        arbitrary_types_allowed = True
