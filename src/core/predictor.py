# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Module responsible for making predictions using a trained deep learning model.
"""

from typing import Sequence, List
import logging
import threading

import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer


logger = logging.getLogger(__name__)


class Predictor:
    """
    Handles text classification predictions using a trained Keras model
    and tokenizer.
    """

    def __init__(
        self,
        model: Model,
        tokenizer: Tokenizer,
        max_len: int = 200,
    ) -> None:
        self._model = model
        self._tokenizer = tokenizer
        self._max_len = max_len

        self._lock = threading.Lock()

        self._validate_components()

    def _validate_components(self) -> None:
        if not hasattr(self._tokenizer, "texts_to_sequences"):
            raise TypeError("Tokenizer must implement texts_to_sequences().")

        if not hasattr(self._model, "predict"):
            raise TypeError("Model must implement predict().")

    def _prepare_input(self, texts: Sequence[str]) -> np.ndarray:
        sequences = self._tokenizer.texts_to_sequences(texts)
        return pad_sequences(sequences, maxlen=self._max_len)

    def __call__(self, text_cleaned: str) -> float:
        """
        Predict a probability score for a single cleaned text.
        """
        if not isinstance(text_cleaned, str) or not text_cleaned.strip():
            raise ValueError("Input text must be a non-empty string.")

        scores = self.predict_batch([text_cleaned])
        return scores[0]

    def predict_batch(self, texts: Sequence[str]) -> List[float]:
        """
        Predict probability scores for a batch of cleaned texts.
        """
        if not texts:
            return []

        logger.debug("Running prediction on batch of size %d", len(texts))

        padded = self._prepare_input(texts)

        with self._lock:
            raw_output = self._model.predict(padded, verbose=0)

        return self._normalize_output(raw_output)

    @staticmethod
    def _normalize_output(output: np.ndarray) -> List[float]:
        """
        Normalize model output to a list of floats.
        """
        output = np.asarray(output)

        if output.ndim == 2 and output.shape[1] == 1:
            return output[:, 0].astype(float).tolist()

        if output.ndim == 1:
            return output.astype(float).tolist()

        raise ValueError(
            f"Unsupported model output shape: {output.shape}"
        )
    