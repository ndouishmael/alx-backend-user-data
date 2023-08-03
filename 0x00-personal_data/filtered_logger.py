#!/usr/bin/env python3

import logging
import re
from typing import List
import csv
import os

# Define the sensitive fields from user_data.csv
PII_FIELDS = ("name", "email", "ssn", "password", "credit_card")

class RedactingFormatter(logging.Formatter):
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        log_message = super().format(record)
        return self._filter_datum(self.fields, self.REDACTION, log_message, self.SEPARATOR)

    def _filter_datum(self, fields: List[str], redaction: str, message: str, separator: str) -> str:
        """Returns regex obfuscated log messages"""
        for field in fields:
            message = re.sub(f'{field}=(.*?){separator}', f'{field}={redaction}{separator}', message)
        return message

def get_db() -> None:
    """Connection to MySQL environment"""
    # This function is just a placeholder since the database connection is not used in this task.
    pass

def get_logger() -> logging.Logger:
    """Returns a logging.Logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    target_handler = logging.StreamHandler()
    target_handler.setLevel(logging.INFO)

    formatter = RedactingFormatter(list(PII_FIELDS))
    target_handler.setFormatter(formatter)

    logger.addHandler(target_handler)
    return logger

def main() -> None:
    """Obtain database connection using get_db,
    retrieve all role in the users table and display
    each row under a filtered format"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")

    headers = [field[0] for field in cursor.description]
    logger = get_logger()

    for row in cursor:
        info_answer = ''
        for f, p in zip(row, headers):
            info_answer += f'{p}={(f)}; '
        logger.info(info_answer)

    cursor.close()
    db.close()

if __name__ == '__main__':
    main()
