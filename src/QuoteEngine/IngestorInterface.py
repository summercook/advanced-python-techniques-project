from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """"generic method for identifying whether a given file type can be ingested and
    abstract method to be used for parsing text in various formats
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        pass
