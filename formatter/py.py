import os

from . import IFormatter
from .formatter import format_common

PATH = os.getenv('BLACK_PATH')

class PythonFormatter(IFormatter):
    @staticmethod
    def format(source: str) -> str:
        return format_common(
            'py',
            lambda file: [PATH, file, '-v', '--skip-string-normalization'],
            [0],
            source
        )
