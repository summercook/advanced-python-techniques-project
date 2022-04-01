from typing import List
import docx
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """"ingest docx files and append text to list of quotes as QuoteModel objects"""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest')

        quotes = []

        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                new_quote = QuoteModel(parse[0].strip('" '), parse[1].strip("'"))
                quotes.append(new_quote)

        return quotes
