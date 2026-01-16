# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Main module for running the fake news prediction pipeline over network connections.
"""

from dotenv import load_dotenv


load_dotenv()


import logging
import warnings
from src import launcher, setup_logging
import asyncio
import os


if __name__ == "__main__":
    setup_logging(logging.DEBUG)

    # Silence TensorFlow and warnings
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
    os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

    logging.getLogger("tensorflow").setLevel(logging.ERROR)
    logging.getLogger("absl").setLevel(logging.ERROR)

    warnings.filterwarnings(
        "ignore",
        category=FutureWarning,
        module="keras.src.export.tf2onnx_lib"
    )
    
    asyncio.run(
        launcher.run(
            str(os.getenv("HOST")),
            int(os.getenv("PORT"))
        )
    )
