from contextlib import contextmanager

from langchain_community.vectorstores import Neo4jVector
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings

from .conf import settings

embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')


@contextmanager
def get_store():
    store = Neo4jVector.from_existing_index(
        embeddings,
        url=settings.NEO4J_URI,
        username=settings.NEO4J_USERNAME,
        password=settings.NEO4J_PASSWORD,
        index_name=settings.index_name,
    )
    yield store
    store._driver.close()


if __name__ == "__main__":
    with get_store() as db:
        for doc, score in db.similarity_search_with_score("What place should I visit in Tokyo?", k=2):
            print("-" * 80)
            print("Score: ", score)
            print(doc.page_content)
            print("-" * 80)
