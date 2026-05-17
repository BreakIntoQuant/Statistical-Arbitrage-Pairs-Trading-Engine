import yfinance as yf


def fetch_pair_data(
    ticker_1,
    ticker_2,
    start_date,
    end_date
):

    data = yf.download(
        [ticker_1, ticker_2],
        start=start_date,
        end=end_date
    )['Close']

    data = data.dropna()

    return data