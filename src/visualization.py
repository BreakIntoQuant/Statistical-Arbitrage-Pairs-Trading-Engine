import matplotlib.pyplot as plt


def plot_spread(
    spread
):

    plt.figure(figsize=(14, 6))

    plt.plot(spread)

    plt.title(
        'Pairs Trading Spread'
    )

    plt.grid(True)

    plt.savefig(
        'charts/spread_chart.png'
    )

    print("Spread chart saved.")


def plot_zscore(
    zscore
):

    plt.figure(figsize=(14, 6))

    plt.plot(zscore)

    plt.axhline(
        2,
        color='red',
        linestyle='--'
    )

    plt.axhline(
        -2,
        color='green',
        linestyle='--'
    )

    plt.axhline(
        0,
        color='black'
    )

    plt.title(
        'Z-Score Mean Reversion Signals'
    )

    plt.grid(True)

    plt.savefig(
        'charts/zscore_chart.png'
    )

    print("Z-score chart saved.")


def plot_equity_curve(
    cumulative_returns
):

    plt.figure(figsize=(14, 6))

    plt.plot(cumulative_returns)

    plt.title(
        'Statistical Arbitrage Equity Curve'
    )

    plt.grid(True)

    plt.savefig(
        'charts/equity_curve.png'
    )

    print("Equity curve saved.")