import os
import logging
from typing import Union


def setup_logging(level: Union[int, str]) -> None:
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

setup_logging(logging.DEBUG)

from .server import Launcher
from .core import Factory


launcher = Launcher(
    Factory.create_classifier(
    os.getenv("MODEL_REPO_ID"),
    os.getenv("MODEL_FILENAME"),
    os.getenv("TOKENIZER_FILENAME")
))

__author__ = "Eric Santos <ericshantos13@gmail.com>"

__all__ = ["launcher"]

__version__ = "2.2.0"
