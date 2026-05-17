"""Pytest configuration shared across all modules.

This file lets each module's tests import from its sibling ``solutions/``
and ``reference.py`` files without needing ``__init__.py`` in every folder.
"""
import sys
from pathlib import Path

# Add the repo root so ``import common.bench`` works from any test.
sys.path.insert(0, str(Path(__file__).parent))
