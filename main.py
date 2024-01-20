import sys

from generators.basic_openai_llm_generator import BasicOpenAILLMGenerator
from rag_system import RAGSystem
from retrievers.meilisearch_retriver import MeilisearchRetriever
from retrievers.trivial_retriver import TrivialRetriever

rag_system = RAGSystem(
    retriever=MeilisearchRetriever(host='http://127.0.0.1:7700',
                                   password='aSampleMasterKey',
                                   index_name="opensource-ai-tools-1"),
    generator=BasicOpenAILLMGenerator()
)

if __name__ == '__main__':
    response = rag_system.query("the best tool to chat with pdf document files")
    for generated_response in response:
        sys.stdout.write(generated_response.content)
