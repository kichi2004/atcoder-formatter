import os

from . import IFormatter
from .formatter import format_common

PATH = os.getenv('CLANG_FORMAT_PATH')

class CppFormatter(IFormatter):
    @staticmethod
    def format(source: str) -> str:
        return format_common(
            'cpp',
            lambda file: [PATH, file, '-i'],
            [0],
            source
        )
