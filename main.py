import sys

from generators.basic_openai_llm_generator import BasicOpenAILLMGenerator
from rag_system import RAGSystem
from retrievers.trivial_retriver import TrivialRetriever

rag_system = RAGSystem(
    retriever=TrivialRetriever(),
    generator=BasicOpenAILLMGenerator()
)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    response = rag_system.query("When he first read the book 'True Stories from Nature'?")
    for generated_response in response:
        sys.stdout.write(generated_response.content)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
