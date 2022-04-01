from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .CsvIngestor import CsvIngestor
from .PdfIngestor import PdfIngestor
from .TxtIngestor import TxtIngestor
from typing import List


class Ingestor(IngestorInterface):
    """"identify file type and apply to appropriate ingestor class"""
    ingestors = [DocxIngestor, CsvIngestor, TxtIngestor, PdfIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
            else:
                pass
