COIN_TO_BINANCE = {
    "bitcoin":        "BTCUSDT",
    "ethereum":       "ETHUSDT",
    "tether":         None,          # can't trade USDT against USDT
    "binancecoin":    "BNBUSDT",
    "solana":         "SOLUSDT",
    "ripple":         "XRPUSDT",
    "usd-coin":       "USDCUSDT",
    "cardano":        "ADAUSDT",
    "dogecoin":       "DOGEUSDT",
    "tron":           "TRXUSDT",
    "avalanche-2":    "AVAXUSDT",
    "polkadot":       "DOTUSDT",
    "chainlink":      "LINKUSDT",
    "matic-network":  "MATICUSDT",   # NOTE: if this one errors out when you run it,
                                      # don't panic - that IS a real lesson. Tokens get
                                      # relisted/renamed on exchanges over time. Check the
                                      # error in collection_log.txt, then look up the coin
                                      # on Binance's website to find its current symbol.
    "litecoin":       "LTCUSDT",
    "shiba-inu":      "SHIBUSDT",
    "bitcoin-cash":   "BCHUSDT",
    "uniswap":        "UNIUSDT",
    "stellar":        "XLMUSDT",
    "cosmos":         "ATOMUSDT",
}
 
ALL_COIN_IDS = list(COIN_TO_BINANCE.keys())
 