# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Module responsible for loading dependencies required for prediction.
"""

import pickle
import logging
from huggingface_hub import hf_hub_download
from tensorflow.keras.models import load_model


logger = logging.getLogger(__name__)

class ModelLoader:
    def __init__(self, repo_id: str, model_filename: str, tokenizer_filename: str) -> None:
        self.repo_id = repo_id
        self.model_filename = model_filename
        self.tokenizer_filename = tokenizer_filename

        self.model = self._load_model()
        self.tokenizer = self._load_tokenizer()

    def _load_model(self):
        try:
            logging.info("Downloading model from Hugging Face Hub...")

            model_path = hf_hub_download(
                repo_id=self.repo_id,
                filename=self.model_filename
            )

            logging.info("Loading TensorFlow model.")
            model = load_model(model_path)
            return model

        except Exception as e:
            logger.error(f"Error loading model: {e}")
            raise RuntimeError("Failed to load model") from e
    
    def _load_tokenizer(self):
        try:
            logger.info("Downloading tokenizer from Hugging Face Hub")
            tokenizer_path = hf_hub_download(
                repo_id=self.repo_id,
                filename=self.tokenizer_filename
            )

            logger.info("Loading tokenizer")
            with open(tokenizer_path, "rb") as f:
                tokenizer = pickle.load(f)

            if not hasattr(tokenizer, "texts_to_sequences"):
                raise TypeError("Loaded object is not a valid tokenizer")

            return tokenizer

        except Exception as e:
            logger.exception("Failed to load tokenizer")
            raise RuntimeError("Tokenizer loading failed") from e
        