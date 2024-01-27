from datetime import datetime
import logging
import pytest
from src.cookie_analyzer import CookieAnalytics
from main import parse_arguments
from pathlib import Path

# Constants for tests
VALID_DATE = '2018-12-09'
INVALID_DATE_FORMAT = '12-09-2018'
DATA_DIR = Path(__file__).parent / 'data'

def test_argument_parsing():
    """
    Test the correct parsing of command-line arguments.
    This ensures that the program correctly interprets input parameters.
    """
    test_args = ['-f', str(DATA_DIR / 'basic_functionality_test.csv'), '-d', VALID_DATE]
    args = parse_arguments(test_args)
    assert args.file == str(DATA_DIR / 'basic_functionality_test.csv')
    assert args.date == VALID_DATE

def test_cookie_analytics_creation():
    """
    Test the creation of the CookieAnalytics object with valid parameters.
    Verifies that the object is initialized correctly with the given file path and date.
    """
    analytics = CookieAnalytics(str(DATA_DIR / 'basic_functionality_test.csv'), VALID_DATE)
    assert analytics.file_path == (DATA_DIR / 'basic_functionality_test.csv')
    assert analytics.target_date == datetime.strptime(VALID_DATE, '%Y-%m-%d').date()

def test_analyze_valid_cookies(capsys):
    """
    Test the main functionality of analyzing and finding the most active cookie.
    Ensures the program correctly identifies and prints the most active cookies for a given date.
    """
    analytics = CookieAnalytics(str(DATA_DIR / 'basic_functionality_test.csv'), VALID_DATE)
    analytics.analyze()
    captured = capsys.readouterr()
    assert 'AtY0laUfhglK3lC7' in captured.out

def test_analyze_multiple_active_cookies(capsys):
    """
    Test the case where multiple cookies are equally active.
    Checks if the program correctly handles and outputs all cookies with the highest activity.
    """
    analytics = CookieAnalytics(str(DATA_DIR / 'multiple_active_cookies_test.csv'), VALID_DATE)
    analytics.analyze()
    captured = capsys.readouterr()
    assert 'cookieA' in captured.out
    assert 'cookieB' in captured.out

def test_analyze_empty_file(capsys):
    """
    Test the program's behavior with an empty log file.
    Verifies that no output is produced when there are no entries to analyze.
    """
    analytics = CookieAnalytics(str(DATA_DIR / 'empty_file_test.csv'), VALID_DATE)
    analytics.analyze()
    captured = capsys.readouterr()
    assert captured.out == ''

def test_file_not_found():
    """
    Test the program's response to a non-existent file.
    Ensures proper error handling and raising of FileNotFoundError in such cases.
    """
    with pytest.raises(FileNotFoundError):
        analytics = CookieAnalytics(str(DATA_DIR / 'nonexistent.csv'), VALID_DATE)
        analytics.analyze()

def test_invalid_date_format():
    """
    Test the program's handling of invalid date formats.
    Checks if ValueError is raised for incorrectly formatted date strings.
    """
    with pytest.raises(ValueError):
        CookieAnalytics(str(DATA_DIR / 'basic_functionality_test.csv'), INVALID_DATE_FORMAT)

def test_analyze_no_matching_date(capsys):
    """
    Test the scenario where no entries match the specified date.
    Ensures the program handles days with no data correctly and produces no output.
    """
    analytics = CookieAnalytics(str(DATA_DIR / 'no_matching_date_test.csv'), VALID_DATE)
    analytics.analyze()
    captured = capsys.readouterr()
    assert captured.out == ''

def test_analyze_single_entry(capsys):
    """
    Test the program's behavior with a log file containing only a single entry.
    This test verifies that the program can correctly handle and identify the most active cookie 
    when there's only one cookie logged for the specified date.
    """
    analytics = CookieAnalytics(str(DATA_DIR / 'single_entry_test.csv'), VALID_DATE)
    analytics.analyze()
    captured = capsys.readouterr()
    assert 'singleCookie' in captured.out

def test_analyze_invalid_format(capsys):
    """
    Test the program's ability to handle entries with invalid formats.
    Ensures that format errors are logged or handled appropriately without crashing the program.
    """
    analytics = CookieAnalytics(str(DATA_DIR / 'invalid_format_test.csv'), VALID_DATE)
    analytics.analyze()
    captured = capsys.readouterr()
    assert 'Invalid date format in row' in captured.err

def test_large_log_file(capsys):
    """
    Test handling of a large log file.
    """
    VALID_DATE = '2024-01-04' # Different as had to generate a large file with cookie_gen.py
    analytics = CookieAnalytics(str(DATA_DIR / 'large_file_test.csv'), VALID_DATE)
    analytics.analyze()
    captured = capsys.readouterr()
    assert len(captured.out.split('\n')) > 1


def test_boundary_date_condition(capsys):
    """
    Test handling of cookies at the boundary of the target date.
    """
    analytics = CookieAnalytics(str(DATA_DIR / 'boundary_date_test.csv'), VALID_DATE)
    analytics.analyze()
    captured = capsys.readouterr()
    assert 'cookieCorrect' in captured.out