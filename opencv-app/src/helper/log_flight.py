import logging
from logging.handlers import RotatingFileHandler


class LogFlight:
    def initialize():
        # Create a logger
        logger = logging.getLogger()

        # Set the logging level
        logger.setLevel(logging.DEBUG)

        # Create a rotating file handler
        handler = RotatingFileHandler(
            "app.log",
            maxBytes=5 * 1024 * 1024,
            backupCount=2,  # 5 MB max size, keep 2 backups
        )

        # Set the log format
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)

        # Add the handler to the logger
        logger.addHandler(handler)

        # # Enable logging to see connection details
        # logging.basicConfig(
        #     filename="app.log",
        #     level=logging.INFO,
        #     format="%(asctime)s - %(levelname)s - %(message)s",
        # )

    def info(msg):
        logging.info(msg)
        print(msg)

    def error(msg):
        logging.error(msg)
        print(msg)

    def debug(msg):
        logging.debug(msg)
        print(msg)

    def critical(msg):
        logging.critical(msg)
        print(msg)

    def warning(msg):
        logging.warning(msg)
        print(msg)

    def get_log():
        # Open the log file and read all lines
        with open("app.log", "r") as f:
            lines = f.readlines()

        # Reverse the order of the lines
        reversed_lines = lines[::-1]

        # Join the reversed lines back into a string and return
        return "".join(reversed_lines)
