from typing import List
import pandas as pd

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CsvIngestor(IngestorInterface):
    """"ingest CSV files and append text to list of quotes as QuoteModel objects"""
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest')

        quotes = []

        df = pd.read_csv(path, header=0)
        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
