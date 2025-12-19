# -*- coding: utf-8 -*-
"""
@Author: Eric Santos <ericshantos13@gmail.com>

This module provides the EnvLoader class, which simplifies the access
to specific environment variables defined in the system.

It allows retrieving selected environment variables with optional default values,
and caches them internally for controlled access and testing.
"""

import os
from typing import Any, Optional, Union


class EnvLoader:
    """
    A lightweight utility class for loading and accessing environment variables.

    This class caches selected environment variables at initialization and
    provides a simple interface to retrieve their values.
    """

    def __init__(self, *vars: str):
        """
        Initializes the EnvLoader with a list of environment variable names to track.

        Args:
            *vars (str): One or more names of environment variables to load and cache.
        """
        self._env = {var: os.environ.get(var) for var in vars}

    def get(
        self, var_name: str, default: Optional[Any] = None
    ) -> Optional[Union[str, int]]:
        """
        Retrieves the value of a previously loaded environment variable.

        Args:
            var_name (str): The name of the environment variable to fetch.
            default (Optional[Any]): The default value to return if the variable is not found.

        Returns:
            Optional[Union[str, int]]: The value of the environment variable, or the default.
        """
        value = self._env.get(var_name)
        return value if value is not None else default