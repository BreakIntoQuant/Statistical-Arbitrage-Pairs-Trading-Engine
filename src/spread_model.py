import numpy as np


def calculate_spread(
    series_1,
    series_2
):

    spread = series_1 - series_2

    return spread


def calculate_zscore(
    spread,
    window=30
):

    rolling_mean = (
        spread.rolling(window)
        .mean()
    )

    rolling_std = (
        spread.rolling(window)
        .std()
    )

    zscore = (
        spread - rolling_mean
    ) / rolling_std

    return zscore