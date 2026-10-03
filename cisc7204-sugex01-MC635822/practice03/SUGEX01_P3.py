#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 21:00:44 2026

@author: Mewtwo
"""


# Practice 03
import os

env_name = os.environ.get("CONDA_DEFAULT_ENV", "Not in conda")
print(f"""Anaconda feels a bit heavy and laggy. May I use Miniconda for now, and install Anaconda again later if needed?
By the way, the current environment is "{env_name}" """)