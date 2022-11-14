import abc
import os
import shutil
from abc import abstractmethod
from pathlib import Path
from typing import Callable
from uuid import uuid4


class IFormatter(metaclass=abc.ABCMeta):
    @staticmethod
    @abstractmethod
    def format(source: str) -> str:
        pass


def format_common(lang: str, process: Callable[[str], str]) -> str:
    uuid = str(uuid4())
    dir_name = f'./working/{uuid}'
    os.mkdir(dir_name)
    try:
        for file in Path(f'./working/_template_{lang}').glob('*'):
            shutil.copy(file, f"{dir_name}/{file.name.replace('DIRNAME', uuid)}")

        file_path = process(dir_name)

        with open(file_path, 'r') as f:
            result = f.read()
    finally:
        shutil.rmtree(dir_name)

    return result
