from fastapi import FastAPI
from langchain_core.documents import Document
from pydantic import BaseModel

from .store import get_store

app = FastAPI()


class QueryRequest(BaseModel):
    query: str
    k: int = 5


class Result(BaseModel):
    content: str
    score: float


class QueryResponse(BaseModel):
    query: str
    results: list[Result]


@app.post(
    "/",
    response_model=QueryResponse,
)
async def root(request: QueryRequest):
    with get_store() as db:
        _res: tuple[Document, float] = db.similarity_search_with_score(request.query, k=request.k)
        results = [
            {
                "content": doc.page_content,
                "score": score,
            }
            for doc, score in _res
        ]

    return {
        "query": request.query,
        "results": results,
    }
