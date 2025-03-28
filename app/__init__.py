"""
ContentUp - A FastAPI-based dashboard for validating Amazon product listings
"""

from importlib import metadata

try:
    __version__ = metadata.version(__package__)
except metadata.PackageNotFoundError:
    __version__ = "unknown"
