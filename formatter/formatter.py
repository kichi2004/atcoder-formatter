import abc
import os
import shutil
import subprocess
from abc import abstractmethod
from pathlib import Path
from typing import Callable
from uuid import uuid4

from format_failed_exception import FormattingFailedError


class IFormatter(metaclass=abc.ABCMeta):
    @staticmethod
    @abstractmethod
    def format(source: str) -> str:
        pass


def format_common(lang: str, process: Callable[[str], list[str]], ok_code: list[int], source: str) -> str:
    uuid = uuid4()
    dir_name = f'./working/{uuid}'
    os.mkdir(dir_name)
    for file in Path(f'./working/_template_{lang}').glob('*'):
        shutil.copy(file, dir_name)

    file_name = f'main.{lang}'
    file_path = f'{dir_name}/{file_name}'
    with open(file_path, 'w') as f:
        f.write(source)

    cp = subprocess.run(
        process(file_name),
        cwd=dir_name,
        stderr=subprocess.PIPE
    )
    if cp.returncode not in ok_code:
        raise FormattingFailedError(cp.returncode, cp.stderr.decode('UTF-8'))

    with open(file_path, 'r') as f:
        result = f.read()

    shutil.rmtree(dir_name)
    return result
