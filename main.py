from fastapi import FastAPI

from suggestions import Suggestions
from exception_middleware import ExceptionHandlerMiddleware
from openai_provider import OpenAIIEmbeddingProvider
from models import Providers, IStorageProvider, DocumentLite
from storage_provider import MemStorageProvider
from openai.embeddings_utils import cosine_similarity


embed_provider = OpenAIIEmbeddingProvider("sk-proj-yourAPIKeyHere")
storage_provider = MemStorageProvider(embed_provider)

providers = Providers(
    embed=embed_provider,
    storage=storage_provider
)

providers.storage.load()
suggestions = Suggestions(providers)

def get_score(a: str, b: str):
    a = suggestions.providers.embed.gen_embedding(a)
    b = suggestions.providers.embed.gen_embedding(b)
    score = cosine_similarity(a, b)
    print(f"Score: {score}")

app = FastAPI()
app.add_middleware(ExceptionHandlerMiddleware)


@app.get("/brands")
async def get_all_brand() -> list[DocumentLite]:
    return suggestions.providers.storage.brands


@app.get("/taxons")
async def get_all_taxon() -> list[DocumentLite]:
    return suggestions.providers.storage.taxons


@app.put("/brands")
async def put_brand(value: str):
    suggestions.store(value, "brand")
    return "OK"


@app.put("/taxons")
async def put_taxon(value: str):
    suggestions.store(value, "taxon")
    return "OK"


@app.get("/brands/{i}")
async def get_brand(i: str) -> DocumentLite:
    return suggestions.providers.storage.brand(i)


@app.get("/taxons/{i}")
async def get_taxon(i: str) -> DocumentLite:
    return suggestions.providers.storage.taxon(i)


@app.get("/search/{query}")
async def query(query: str, type: str, n_result: int = 3):
    return suggestions.search(query, type, n_result)


@app.post("/generate_embedding")
async def generate_embedding(value: str):
    return suggestions.providers.embed.gen_embedding(value)
