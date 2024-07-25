from models import Vectors, IEmbeddingProvider
from openai.embeddings_utils import get_embedding, cosine_similarity, get_embeddings
import openai


class OpenAIIEmbeddingProvider(IEmbeddingProvider):
    def __init__(self, token: str, engine: str = "text-embedding-ada-002"):
        self.engine = engine
        self.token = token
        openai.api_key = token

    def gen_embedding(self, value: str) -> Vectors:
        print(f"Generating embeddings for '{value}'")
        return get_embedding(value, engine=self.engine)

    def gen_embeddings(self, value: list[str]) -> list[Vectors]:
        print(f"Generating embeddings for {len(value)} items...")
        return get_embeddings(value, engine=self.engine)
