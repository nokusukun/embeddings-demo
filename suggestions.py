import pathlib
from typing import Any

from openai.embeddings_utils import cosine_similarity

from models import Vectors, Providers, Document


class Suggestions:

    def __init__(self, providers: Providers):
        print("Loading Suggestions Engine")
        self.providers: Providers = providers

    def search(self, value: str, _type: str, n_items: int = 3) -> list[Any]:
        if _type == "brand":
            embeddings = self.providers.storage.brands
            value = value.lower()
        elif _type == "taxon":
            embeddings = self.providers.storage.taxons
            value = value.lower().split(">")
            value = [x.strip() for x in value]
            value = ", ".join(value)
        else:
            raise Exception(f"401, Unknown type: {_type}")

        # Transform search term into embeddings
        search = self.providers.embed.gen_embedding(value)

        # Calculate Cosine Similarity between vectors (This could be done in a vector database)
        calculated = [
            {
                "id": x.id,
                "source": x.raw_value,
                "value": x.value,
                "score": cosine_similarity(search, x.vectors)
            } for x in embeddings
        ]

        ranked = sorted(calculated, key=lambda x: x["score"], reverse=True)
        return ranked[:n_items]

    def store(self, value: str, _type: str):
        if _type == "brand":
            store = self.providers.storage.brands
            sanitized = value.lower()
            vectors = self.providers.embed.gen_embedding(sanitized)
        elif _type == "taxon":
            store = self.providers.storage.taxons
            sanitized = value.lower().replace(" > ", ", ")
            vectors = self.providers.embed.gen_embedding(sanitized)
        else:
            raise Exception(f"401, Unknown type: {_type}")

        doc = Document(
            id=len(store),
            value=sanitized,
            raw_value=value,
            vectors=vectors,
        )
        store.append(doc)
        self.providers.storage.save()
