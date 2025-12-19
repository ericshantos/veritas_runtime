# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Module responsible for making predictions using a trained deep learning model.
"""

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.text import Tokenizer


class Predictor:
    """
    A class to handle text classification predictions using a trained model 
    and tokenizer.
    """

    def __init__(self, model: Model, tokenizer: Tokenizer, max_len: int = 200) -> None:
        """
        Initializes the Predictor with a model, tokenizer, and maximum sequence length.

        Args:
            model: A trained Keras model for prediction.
            tokenizer: A fitted Keras tokenizer used to preprocess input text.
            max_len (int, optional): Maximum length of the padded sequences. Defaults to 200.
        """
        self._model = model
        self._tokenizer = tokenizer
        self.max_len = max_len

    def predict(self, text_cleaned: str) -> float:
        """
        Predicts the probability score for the given cleaned input text.

        Args:
            text_cleaned (str): A preprocessed (cleaned) input string.

        Returns:
            float: The model's prediction score as a float between 0 and 1.
        """
        sequences = self._tokenizer.texts_to_sequences([text_cleaned])
        padded = pad_sequences(sequences, maxlen=self.max_len)
        predict = self._model.predict(padded, verbose=0)
        return float(predict[0][0])
    