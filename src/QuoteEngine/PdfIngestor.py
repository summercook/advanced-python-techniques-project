import random
import os
import subprocess
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


# sudo apt-get install -y xpdf

class PdfIngestor(IngestorInterface):
    """ingest PDF files and append text to list of quotes as QuoteModel objects"""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path=path):
            raise Exception('Cannot ingest Exception')

        tmp = f'./tmp/{random.randint(0, 1000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])
        file_ref = open(tmp, 'r')

        quotes = []
        t_list = []

        for line in file_ref.readlines():
            line = line.strip('\n\r').replace('"', '')
            line = line.split('-')
            t_list.append(line)

        t_list = t_list[0:-2]
        for quote in t_list:
            quote = QuoteModel(quote[0], quote[1])
            quotes.append(quote)

        file_ref.close()
        os.remove(tmp)

        return quotes



    ........................
