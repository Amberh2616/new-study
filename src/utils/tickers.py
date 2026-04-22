import re


TAIWAN_STOCK_EXCHANGE_SUFFIX = ".TW"
TAIWAN_OTC_SUFFIX = ".TWO"


def normalize_ticker(ticker: str) -> str:
    """Normalize ticker input with Taiwan stock shortcuts.

    Supported forms:
    - `2330` -> `2330.TW`
    - `2330.tw` -> `2330.TW`
    - `8069.two` -> `8069.TWO`
    - `TWSE:2330` / `TSE:2330` -> `2330.TW`
    - `TPEX:8069` / `OTC:8069` -> `8069.TWO`
    """
    normalized = ticker.strip().upper()
    if not normalized:
        return normalized

    if re.fullmatch(r"\d{4,6}", normalized):
        return f"{normalized}{TAIWAN_STOCK_EXCHANGE_SUFFIX}"

    exchange_match = re.fullmatch(r"(TWSE|TSE|TPEX|OTC):([0-9]{4,6})", normalized)
    if exchange_match:
        exchange, code = exchange_match.groups()
        suffix = TAIWAN_STOCK_EXCHANGE_SUFFIX if exchange in {"TWSE", "TSE"} else TAIWAN_OTC_SUFFIX
        return f"{code}{suffix}"

    if normalized.endswith(TAIWAN_STOCK_EXCHANGE_SUFFIX) or normalized.endswith(TAIWAN_OTC_SUFFIX):
        return normalized

    return normalized


def normalize_tickers(tickers: list[str]) -> list[str]:
    return [normalized for ticker in tickers if (normalized := normalize_ticker(ticker))]
