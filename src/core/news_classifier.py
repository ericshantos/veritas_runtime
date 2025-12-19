# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Module for preprocessing and cleaning Portuguese text data using spaCy.
"""

import logging
import traceback
import sys
from typing import Union

from .cleaner import TextCleaner
from .predictor import Predictor


class NewsClassifier:
    def __init__(self, predictor: Predictor, cleaner: TextCleaner) -> None:
        self.cleaner = cleaner
        self.predictor = predictor

    def predict(self, text: str) -> Union[float, int]:
        """
        Predicts the likelihood or class of a news article being fake.

        Args:
            text (str): Raw news article text.

        Returns:
            float | int: Probability score or class label.
        """
        try:
            cleaned = self.cleaner(text)
            return self.predictor.predict(cleaned)
        except Exception as e:
            logging.error("Prediction error: %s", str(e))
            traceback.print_exc(file=sys.stderr)
            raise RuntimeError("Prediction failed.") from e
        