import logging
from .high_level import translate, translate_stream

log = logging.getLogger(__name__)

__version__ = "1.8.8"
__author__ = "Byaidu"
__all__ = ["translate", "translate_stream"]
