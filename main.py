#!/usr/bin/env python3

import argparse
from typing import List, Optional
from src.cookie_analyzer import CookieAnalytics

def parse_arguments(args: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze the most active cookies in a log file.")
    parser.add_argument("-f", "--file", required=True, help="Path to the cookie log file")
    parser.add_argument("-d", "--date", required=True, help="Date for analyzing the most active cookie (YYYY-MM-DD format)")
    return parser.parse_args(args)

def main():
    args = parse_arguments()

    if not args.file.startswith('data/'):
        args.file = 'data/' + args.file

    analytics = CookieAnalytics(args.file, args.date)
    analytics.analyze()

if __name__ == "__main__":
    main()