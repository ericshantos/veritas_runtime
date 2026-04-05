import logging
import os
from typing import Union

from .core import Factory
from .server import Launcher


def setup_logging(level: Union[int, str]) -> None:
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


setup_logging(logging.DEBUG)

model_repo = os.getenv("MODEL_REPOSITORY")
tokenizer_repo = os.getenv("TOKENIZER_REPOSITORY")

if model_repo is None or tokenizer_repo is None:
    raise ValueError("Model and tokenizer must be provided")

classifier = Factory.create_classifier(model_repo, tokenizer_repo)

launcher = Launcher(classifier)


__author__ = "Eric Santos <ericshantos13@gmail.com>"

__all__ = ["launcher"]

__version__ = "3.0.0"
