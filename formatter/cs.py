import os
import subprocess

from format_failed_exception import FormattingFailedError
from . import IFormatter
from .formatter import format_common

PATH = os.getenv('DOTNET_PATH')

class CSharpFormatter(IFormatter):
    @staticmethod
    def format(source: str) -> str:
        def _process(dir_name):
            file_name = f'Program.cs'
            file_path = f'{dir_name}/{file_name}'
            with open(file_path, 'w') as f:
                f.write(source)

            cp = subprocess.run(
                [PATH, 'format', '--include', file_name, '--no-restore'],
                cwd=dir_name,
                stderr=subprocess.PIPE
            )
            if cp.returncode != 0:
                raise FormattingFailedError(cp.returncode, cp.stderr.decode('UTF-8'))

            return file_path

        return format_common('cs', _process)
