"""Convenience imports and path helpers for the ACEBench codebase.

The repository is intended to be consumed directly (e.g. via a git
submodule) without requiring installation.  When this package is
imported we therefore expose a couple of useful path constants and make
sure the inner modules remain importable as top-level names such as
``model_eval`` or ``model_inference``.
"""

from pathlib import Path
import sys

PACKAGE_ROOT = Path(__file__).resolve().parent
REPO_ROOT = PACKAGE_ROOT.parent

# Ensure backwards-compatibility for modules that expect to import the
# original top-level packages (e.g. ``import model_eval``).
if str(PACKAGE_ROOT) not in sys.path:
    sys.path.insert(0, str(PACKAGE_ROOT))

__all__ = [
    "PACKAGE_ROOT",
    "REPO_ROOT",
    "model_eval",
    "model_inference",
    "category",
    "generate",
    "eval_main",
]
