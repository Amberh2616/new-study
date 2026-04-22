from src.cli.input import parse_tickers
from src.utils.tickers import normalize_ticker, normalize_tickers


def test_normalize_ticker_supports_taiwan_stock_exchange_shortcut():
    assert normalize_ticker("2330") == "2330.TW"


def test_normalize_ticker_supports_explicit_taiwan_exchange_prefixes():
    assert normalize_ticker("TWSE:2330") == "2330.TW"
    assert normalize_ticker("TPEX:8069") == "8069.TWO"


def test_normalize_ticker_preserves_existing_suffixes_and_us_tickers():
    assert normalize_ticker("2330.tw") == "2330.TW"
    assert normalize_ticker("8069.two") == "8069.TWO"
    assert normalize_ticker("AAPL") == "AAPL"


def test_normalize_tickers_filters_empty_values():
    assert normalize_tickers(["2330", " ", "AAPL"]) == ["2330.TW", "AAPL"]


def test_parse_tickers_applies_normalization():
    assert parse_tickers("2330, TPEX:8069, AAPL") == ["2330.TW", "8069.TWO", "AAPL"]
