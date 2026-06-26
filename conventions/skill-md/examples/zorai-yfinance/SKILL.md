<!-- source: zorai-yfinance — https://raw.githubusercontent.com/mkurman/zorai/main/skills/scientific-skills/yfinance/SKILL.md -->
---
name: yfinance
description: "Yahoo Finance market data downloader. Stock prices, options chains, fundamentals, dividends, splits, earnings, institutional holders, and financial statements. Quick data ingestion for quant research and backtesting."
tags: [yahoo-finance, market-data, stocks, etfs, financial-data, api, zorai]
---
## Overview

yfinance downloads Yahoo Finance market data: stock prices, options chains, fundamentals, dividends, splits, earnings, institutional holders, and financial statements. The fastest path from ticker symbol to pandas DataFrame for quant research and backtesting.

## Installation

```bash
uv pip install yfinance
```

## Price History

```python
import yfinance as yf

msft = yf.download("MSFT", start="2024-01-01", end="2024-12-31")
print(msft.head())
```

## Fundamentals & Financials

```python
ticker = yf.Ticker("AAPL")
info = ticker.info
print(f"Market cap: {info['marketCap']:,}")
print(f"PE ratio: {info['trailingPE']}")
print(f"Dividend yield: {info.get('dividendYield', 0)*100:.2f}%")
print(ticker.balance_sheet)
print(ticker.financials)
```

## Options

```python
opt = ticker.option_chain(ticker.options[0])
print(opt.calls[["strike", "lastPrice", "impliedVolatility", "volume"]].head())
print(opt.puts[["strike", "lastPrice", "impliedVolatility", "volume"]].head())
```

## References
- [yfinance GitHub](https://github.com/ranaroussi/yfinance)