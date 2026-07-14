"""
=========================================================
LoveLens AI
History Engine
=========================================================
"""

import pandas as pd


def get_history(history_df):
    """
    Returns complete history.
    """

    return history_df


def search_history(history_df, username):

    if history_df.empty:
        return history_df

    if username == "":
        return history_df

    return history_df[
        history_df["username"].str.contains(
            username,
            case=False,
            na=False
        )
    ]


def filter_prediction(history_df, prediction):

    if prediction == "All":
        return history_df

    return history_df[
        history_df["prediction"] == prediction
    ]


def latest_predictions(history_df, limit=10):

    return history_df.head(limit)


def total_history(history_df):

    return len(history_df)


def highest_score(history_df):

    if history_df.empty:
        return 0

    return history_df["love_score"].max()


def average_score(history_df):

    if history_df.empty:
        return 0

    return round(history_df["love_score"].mean(), 2)