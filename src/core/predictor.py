# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Module responsible for making predictions using a trained deep learning model.
"""

import logging

import torch
from transformers import PreTrainedModel, PreTrainedTokenizerBase

logger = logging.getLogger(__name__)


class Predictor:
    """
    Handles text classification predictions using a trained Keras model
    and tokenizer.
    """

    def __init__(
        self,
        model: PreTrainedModel,
        tokenizer: PreTrainedTokenizerBase,
    ) -> None:
        self._model = model
        self._tokenizer = tokenizer

    def __call__(self, text: str) -> float:
        inputs = self._tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=512,
        )

        inputs.pop("token_type_ids", None)

        with torch.no_grad():
            outputs = self._model(**inputs)
            logits = outputs.logits
            probs = torch.softmax(logits, dim=1)

        return round(probs[0][1].item(), 2)
