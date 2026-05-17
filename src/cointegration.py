from statsmodels.tsa.stattools import coint


def test_cointegration(
    series_1,
    series_2
):

    score, pvalue, _ = coint(
        series_1,
        series_2
    )

    return score, pvalue