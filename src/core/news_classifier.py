# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Module for preprocessing and cleaning Portuguese text data using spaCy.
"""


from typing import Final
import logging

from .cleaner import TextCleaner
from .predictor import Predictor


logger = logging.getLogger(__name__)


class NewsClassifier:
    """
    Orchestrates text cleaning and prediction for fake news classification.
    """

    def __init__(self, predictor: Predictor, cleaner: TextCleaner) -> None:
        self._predictor: Final = predictor
        self._cleaner: Final = cleaner

        self._validate_dependencies()

    def _validate_dependencies(self) -> None:
        if not callable(self._cleaner):
            raise TypeError("Cleaner must be callable")

        if not callable(self._predictor):
            raise TypeError("Predictor must be callable")

    def predict(self, text: str) -> float:
        """
        Predicts the probability of a news article being fake.

        Args:
            text (str): Raw news article text.

        Returns:
            float: Probability score between 0 and 1.
        """
        if not isinstance(text, str) or not text.strip():
            raise ValueError("Input text must be a non-empty string")

        logger.debug("Starting prediction")

        try:
            cleaned_text = self._cleaner(text)

            if not cleaned_text:
                raise ValueError("Text cleaning resulted in empty output")

            score = self._predictor(cleaned_text)

            logger.debug("Prediction completed successfully")
            return score

        except Exception:
            logger.exception("Prediction pipeline failed")
            raise
