"""
=========================================================
LoveLens AI
Export Report
=========================================================
"""

import pandas as pd


def export_csv(history_df):

    """
    Convert DataFrame to CSV
    """

    return history_df.to_csv(index=False)


def export_filename():

    return "LoveLens_AI_History.csv"