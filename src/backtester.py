import numpy as np


def backtest_strategy(
    spread,
    signals
):

    returns = spread.pct_change()

    strategy_returns = np.zeros(
        len(returns)
    )

    position = 0

    for i in range(1, len(returns)):

        if signals['Long'].iloc[i]:
            position = 1

        elif signals['Short'].iloc[i]:
            position = -1

        elif signals['Exit'].iloc[i]:
            position = 0

        strategy_returns[i] = (
            position
            * returns.iloc[i]
        )

    cumulative_returns = (
        1 + strategy_returns
    ).cumprod()

    sharpe_ratio = (
        np.mean(strategy_returns)
        / np.std(strategy_returns)
    ) * np.sqrt(252)

    max_drawdown = (
        cumulative_returns
        / np.maximum.accumulate(
            cumulative_returns
        ) - 1
    ).min()

    return (
        cumulative_returns,
        sharpe_ratio,
        max_drawdown
    )