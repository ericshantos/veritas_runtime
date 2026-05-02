# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Module responsible for loading dependencies required for prediction.
"""

import logging
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from transformers import (AutoModelForSequenceClassification, AutoTokenizer,
                          PreTrainedModel, PreTrainedTokenizerBase)

T = TypeVar("T")

logger = logging.getLogger(__name__)


class Loader(ABC, Generic[T]):
    def __init__(self, repo_id: str) -> None:
        if not repo_id:
            raise ValueError("repo_id not provided")

        self._repo_id = repo_id

        self._resource: T | None = None

    @abstractmethod
    def _load(self) -> T:
        pass

    @property
    def instance(self) -> T:
        if self._resource is None:
            self._resource = self._load()
        return self._resource


class MyTokenizer(Loader[PreTrainedTokenizerBase]):
    def _load(self) -> PreTrainedTokenizerBase:
        try:
            logger.info("Loading tokenizer...")
            return AutoTokenizer.from_pretrained(self._repo_id)
        except Exception as e:
            logger.exception("Tokenizer load failed")
            raise RuntimeError("Failed to load tokenizer") from e


class MyModel(Loader[PreTrainedModel]):
    def _load(self) -> PreTrainedModel:
        try:
            logger.info("Loading model...")
            model = AutoModelForSequenceClassification.from_pretrained(
                self._repo_id, trust_remote_code=True, local_files_only=True
            )

            model.eval()
            return model

        except Exception as e:
            logger.exception("Model load failed")
            raise RuntimeError("Failed to load model") from e
