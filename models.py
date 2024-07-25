import dataclasses
from typing import Any

from pydantic import BaseModel

Vectors = list[Any]

class DocumentLite(BaseModel):
    id: str | int
    value: str
    raw_value: str

class Document(BaseModel):
    id: str | int
    value: str
    raw_value: str
    vectors: Vectors


class IStorageProvider:
    def taxon(self, value: str) -> Document:
        raise NotImplementedError()

    def brand(self, value: str) -> Document:
        raise NotImplementedError()

    def search(self, value: str, _type: str, n_items: int = 3) -> list[Any]:
        raise NotImplementedError()

    def load(self, embed_provider):
        print("Warning: Load called on base IStorageProvider")
        pass

    def save(self):
        raise NotImplementedError()

class IEmbeddingProvider:
    def gen_embedding(self, value: str) -> Vectors:
        raise NotImplementedError()

    def gen_embeddings(self, value: list[str]) -> list[Vectors]:
        raise NotImplementedError()


@dataclasses.dataclass
class Providers:
    embed: IEmbeddingProvider
    storage: IStorageProvider
