import os
import sys

from dotenv import load_dotenv
from generators.basic_openai_llm_generator import BasicOpenAILLMGenerator
from rag_system import RAGSystem
from retrievers.meilisearch_retriver import MeilisearchRetriever
from retrievers.trivial_retriver import TrivialRetriever

load_dotenv()

rag_system = RAGSystem(
    retriever=MeilisearchRetriever(host=os.getenv("MEILISEARCH_HOST"),
                                   password=os.getenv("MEILISEARCH_API_KEY"),
                                   index_name=os.getenv("MEILISEARCH_INDEX")),
    generator=BasicOpenAILLMGenerator()
)

if __name__ == '__main__':
    response = rag_system.query("the best tool to chat with pdf document files")
    for generated_response in response:
        sys.stdout.write(generated_response.content)
