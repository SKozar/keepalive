"""Logging — rotating 5 × 1 MB, stored in ~/Library/Logs/keepalive/."""

import logging
import sys
from logging.handlers import RotatingFileHandler

from keepalive.config import LOG_DIR, LOG_FILE


def setup_logging() -> logging.Logger:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("keepalive")
    logger.setLevel(logging.INFO)

    fmt = logging.Formatter("%(asctime)s  %(message)s", datefmt="%H:%M:%S")

    fh = RotatingFileHandler(str(LOG_FILE), maxBytes=1_000_000, backupCount=5)
    fh.setFormatter(fmt)
    logger.addHandler(fh)

    ch = logging.StreamHandler(sys.stderr)
    ch.setFormatter(fmt)
    logger.addHandler(ch)

    return logger


log = setup_logging()
