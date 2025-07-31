import json
import logging
import logging.config
from pathlib import Path


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "time": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        return json.dumps(log_record)


# ✅ backend/app/config から2階層上がって projectroot を取得
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
LOG_DIR = PROJECT_ROOT.parent / "logs"  # ← これで親ディレクトリに行く
LOG_DIR.mkdir(exist_ok=True)


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "json": {
            "()": JsonFormatter,
            "datefmt": "%Y-%m-%dT%H:%M:%S",
        },
        "simple": {
            "format": "[%(asctime)s] %(levelname)s - %(name)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",  # ここを変更
        },
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "json",
            "filename": str(LOG_DIR / "app.log"),
            "when": "midnight",
            "interval": 1,
            "backupCount": 7,
            "encoding": "utf-8",
        },
    },

    "root": {
        "level": "INFO",
        "handlers": ["console", "file"]
    },
}


def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)


def get_logger(name=None):
    return logging.getLogger(name)
