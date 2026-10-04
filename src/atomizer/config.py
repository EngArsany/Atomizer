import logging, sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def configure_logging() -> None:
    """
    Configure console and file logging.
    """

    logs_directory = PROJECT_ROOT / "logs"

    logs_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    root_logger = logging.getLogger()

    root_logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | " "%(name)s | %(message)s"
    )

    # Avoid adding duplicate handlers
    if root_logger.handlers:
        return

    console_handler = logging.StreamHandler(sys.stdout)

    console_handler.setLevel(logging.INFO)

    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(
        logs_directory / "app.log",
        encoding="utf-8",
    )

    file_handler.setLevel(logging.DEBUG)

    file_handler.setFormatter(formatter)

    root_logger.addHandler(console_handler)

    root_logger.addHandler(file_handler)
