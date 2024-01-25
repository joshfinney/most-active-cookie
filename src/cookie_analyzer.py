import argparse
import logging
from datetime import datetime, date
from collections import Counter
from pathlib import Path
from typing import List, Optional
import csv

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CookieAnalytics:
    def __init__(self, file_path: str, date_str: str):
        self.file_path = Path(file_path)
        self.target_date = self._validate_date(date_str)

    @staticmethod
    def _validate_date(date_str: str) -> date:
        try:
            return datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            logging.error("Invalid date format. Please use YYYY-MM-DD.")
            raise

    def _read_log_file(self) -> List[str]:
        cookies = []

        with self.file_path.open(mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    cookie_date = datetime.fromisoformat(row['timestamp'].split('T')[0]).date()
                    if cookie_date == self.target_date:
                        cookies.append(row['cookie'])
                except ValueError as ve:
                    logging.warning(f"Invalid date format in row: {row}. Error: {ve}")

        return cookies

    @staticmethod
    def _find_most_active_cookies(cookies: List[str]) -> List[str]:
        counter = Counter(cookies)
        max_count = max(counter.values(), default=0)
        return [cookie for cookie, count in counter.items() if count == max_count]

    def analyze(self):
        try:
            cookies = self._read_log_file()
            most_active_cookies = self._find_most_active_cookies(cookies)
            for cookie in most_active_cookies:
                print(cookie)
        except FileNotFoundError:
            logging.error("Invalid file path")
            raise
        except Exception as e:
            logging.error(f"An error occurred: {e}")