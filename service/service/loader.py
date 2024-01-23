from pathlib import Path

from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import JSONLoader
from langchain_community.vectorstores import Neo4jVector
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings

from .conf import settings

BASE_PATH = Path(__file__).parent

if __name__ == "__main__":
    print("Loading documents...")

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

    loader = JSONLoader(
        str(BASE_PATH / "wikipedia_pages.json"),
        jq_schema='.[]',
        content_key="content",
    )
    documents = loader.load()

    text_splitter = CharacterTextSplitter(separator='\n', chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    db: Neo4jVector = Neo4jVector.from_documents(
        docs,
        embeddings,
        url=settings.NEO4J_URI,
        username=settings.NEO4J_USERNAME,
        password=settings.NEO4J_PASSWORD,
        index_name=settings.index_name
    )

    query = "What place should I visit in Tokyo?"
    docs_with_score = db.similarity_search_with_score(query, k=2)
    for doc, score in docs_with_score:
        print("-" * 80)
        print("Score: ", score)
        print(doc.page_content)
        print("-" * 80)

    db._driver.close()
