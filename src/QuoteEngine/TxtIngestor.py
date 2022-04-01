from typing import List
import pandas as pd

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TxtIngestor(IngestorInterface):
    """"ingest text files and append text to list of quotes as QuoteModel objects"""
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest')

        df = pd.read_csv(path, header = None)

        df = df[0].str.split(' - ', expand = True)
        quotes = []

        for index, row in df.iterrows():
            new_quote = QuoteModel(row[0], row[1])
            quotes.append(new_quote)

        return quotes
