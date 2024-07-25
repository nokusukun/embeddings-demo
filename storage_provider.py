import pathlib
import pickle
from typing import Any

from openai.embeddings_utils import cosine_similarity

from models import IStorageProvider, Document, IEmbeddingProvider


def load_from_raw(filename: str, preprocess: callable = lambda x: x.strip()) -> list[str]:
    p = pathlib.Path('raw').joinpath(f"{filename}.txt")
    with open(p) as f:
        lines = f.readlines()

    if preprocess:
        lines = [preprocess(x) for x in lines]

    return lines


class MemStorageProvider(IStorageProvider):
    def __init__(self, embed_provider: IEmbeddingProvider):
        self.embed_provider = embed_provider
        self.brands: list[Document] = []
        self.taxons: list[Document] = []

    def load(self):
        try:
            with open(".cache.brands", "rb") as f:
                self.brands = pickle.load(f)
                print("brands loaded from cache")
        except:
            # load brands
            brands = load_from_raw("brands")
            brand_vectors = self.embed_provider.gen_embeddings([x.lower() for x in brands])
            for i, brand in enumerate(brands):
                doc = Document(
                    id=i,
                    value=brand.lower(),
                    raw_value=brand,
                    vectors=brand_vectors[i],
                )
                self.brands.append(doc)

        try:
            with open(".cache.taxons", "rb") as f:
                self.taxons = pickle.load(f)
                print("taxons loaded from cache")
        except:
            # load taxons
            taxons = load_from_raw("taxons")
            taxon_vectors = self.embed_provider.gen_embeddings([x.lower().replace(" > ", ", ") for x in taxons])
            for i, taxon in enumerate(taxons):
                doc = Document(
                    id=i,
                    value=taxon.lower().replace(" > ", ", "),
                    raw_value=taxon,
                    vectors=taxon_vectors[i],
                )
                self.taxons.append(doc)

        self.save()

    def save(self):
        with open(".cache.taxons", "wb") as f:
            pickle.dump(self.taxons, f)

        with open(".cache.brands", "wb") as f:
            pickle.dump(self.brands, f)

    def taxon(self, value: str) -> Document:
        val = [x for x in self.taxons if str(x.id) == value or str(x.value) == value or str(x.raw_value) == value]
        if val:
            return val[0]

        raise Exception("404, Taxon not found")

    def brand(self, value: str) -> Document:
        val = [x for x in self.brands if str(x.id) == value or str(x.value) == value or str(x.raw_value) == value]
        if val:
            return val[0]

        raise Exception("404, Brand not found")
