import pandas as pd


def generate_trading_signals(
    zscore,
    entry_threshold=2,
    exit_threshold=0.5
):

    signals = pd.DataFrame(
        index=zscore.index
    )

    signals['Z-Score'] = zscore

    signals['Long'] = (
        zscore < -entry_threshold
    )

    signals['Short'] = (
        zscore > entry_threshold
    )

    signals['Exit'] = (
        abs(zscore)
        < exit_threshold
    )

    return signals