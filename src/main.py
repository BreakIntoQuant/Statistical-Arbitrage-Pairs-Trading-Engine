from data_loader import (
    fetch_pair_data
)

from cointegration import (
    test_cointegration
)

from spread_model import (
    calculate_spread,
    calculate_zscore
)

from signals import (
    generate_trading_signals
)

from backtester import (
    backtest_strategy
)

from visualization import (
    plot_spread,
    plot_zscore,
    plot_equity_curve
)


def main():

    ticker_1 = "KO"
    ticker_2 = "PEP"

    print(
        "\nDownloading market data..."
    )

    data = fetch_pair_data(
        ticker_1,
        ticker_2,
        "2020-01-01",
        "2025-01-01"
    )

    series_1 = data[ticker_1]
    series_2 = data[ticker_2]

    print(
        "Testing cointegration..."
    )

    score, pvalue = (
        test_cointegration(
            series_1,
            series_2
        )
    )

    print("\n==========")
    print("COINTEGRATION TEST")
    print("==========")

    print(
        f"\nTest Statistic: {score:.4f}"
    )

    print(
        f"P-Value: {pvalue:.6f}"
    )

    spread = calculate_spread(
        series_1,
        series_2
    )

    zscore = calculate_zscore(
        spread
    )

    print(
        "\nGenerating trading signals..."
    )

    signals = (
        generate_trading_signals(
            zscore
        )
    )

    print(
        "Running backtest..."
    )

    (
        cumulative_returns,
        sharpe_ratio,
        max_drawdown
    ) = backtest_strategy(
        spread,
        signals
    )

    print("\n==========")
    print("STRATEGY PERFORMANCE")
    print("==========")

    print(
        f"\nSharpe Ratio: {sharpe_ratio:.2f}"
    )

    print(
        f"Max Drawdown: {max_drawdown:.2%}"
    )

    print(
        "\nGenerating visualizations..."
    )

    plot_spread(spread)

    plot_zscore(zscore)

    plot_equity_curve(
        cumulative_returns
    )

    print(
        "\nStatistical Arbitrage Analysis Complete."
    )


if __name__ == "__main__":
    main()