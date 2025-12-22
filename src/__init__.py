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
from .core import classifier


launcher = Launcher(classifier)

__author__ = "Eric Santos <ericshantos13@gmail.com>"

__all__ = ["launcher"]

__version__ = "2.0.0"
