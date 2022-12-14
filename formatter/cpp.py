import os
import subprocess

from format_failed_exception import FormattingFailedError
from . import IFormatter
from .formatter import format_common

PATH = os.getenv('CLANG_FORMAT_PATH')

class CppFormatter(IFormatter):
    @staticmethod
    def format(source: str) -> str:
        def _process(dir_name):
            file_name = f'main.cpp'
            file_path = f'{dir_name}/{file_name}'
            with open(file_path, 'w') as f:
                f.write(source)

            cp = subprocess.run(
                [PATH, file_name, '-i'],
                cwd=dir_name,
                stderr=subprocess.PIPE
            )
            if cp.returncode != 0:
                raise FormattingFailedError(cp.returncode, cp.stderr.decode('UTF-8'))

            return file_path

        return format_common('cpp', _process)
